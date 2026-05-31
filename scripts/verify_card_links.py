#!/usr/bin/env python3
"""
verify_card_links.py — Link-integrity verification for research cards.

For each card under book/evidence/source-ledger/cards/ that has a source.url:
  1. HEAD-request the URL (10s timeout) — record status.
  2. GET the body (20s timeout) — compute sha256 — store in verification.body_sha256.
  3. Query Wayback Availability API for an existing snapshot:
     https://archive.org/wayback/available?url=<url>
     If a snapshot exists, capture its timestamped URL + date.
  4. If no snapshot exists, call Wayback Save API:
     https://web.archive.org/save/<url>
     (slower; rate-limited by archive.org).
  5. Update the card's source.archive.wayback_url and wayback_captured fields
     with the REAL snapshot URL (replacing template placeholders).
  6. Log every action to book/evidence/source-ledger/.verify-log.json (idempotent state).

Idempotent: re-runs skip cards already verified (body_sha256 present AND
wayback_url contains a real timestamp, not '*').

Usage:
  python3 scripts/verify_card_links.py [--dry-run] [--limit N] [--only <slug>]
                                       [--no-save] [--retry-dead]

Exit codes:
  0 — completed; per-card outcomes in log
  1 — script error
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
import time
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / "cards"
LOG_PATH = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / ".verify-log.json"
SECRETS_PATH = PROJECT_ROOT / ".secrets.env"


def load_secrets() -> dict[str, str]:
    """Load API keys from .secrets.env (gitignored). Returns {} if absent.

    Values are never logged or printed. Only their presence/absence is reported.
    """
    secrets: dict[str, str] = {}
    if not SECRETS_PATH.exists():
        return secrets
    for line in SECRETS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        v = v.strip().strip('"').strip("'")
        if v:
            secrets[k.strip()] = v
    return secrets


SECRETS = load_secrets()
COURTLISTENER_TOKEN = SECRETS.get("COURTLISTENER_TOKEN", "")
ARCHIVE_ORG_ACCESS_KEY = SECRETS.get("ARCHIVE_ORG_ACCESS_KEY", "")
ARCHIVE_ORG_SECRET_KEY = SECRETS.get("ARCHIVE_ORG_SECRET_KEY", "")
# Accept either spelling of the api.data.gov key.
API_DATA_GOV_KEY = SECRETS.get("DATA_GOV_API_KEY", "") or SECRETS.get("API_DATA_GOV_KEY", "")

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36"
)
HEAD_TIMEOUT = 10
GET_TIMEOUT = 25
SAVE_TIMEOUT = 60
AVAIL_API = "https://archive.org/wayback/available"
SAVE_API_BASE = "https://web.archive.org/save/"

# Pacing: be polite to archive.org. The free Wayback Save API throttles at
# ~15 req/min. We aim for ~5 req/min to leave headroom.
SAVE_DELAY_SECONDS = 12
AVAIL_DELAY_SECONDS = 1
HEAD_DELAY_SECONDS = 0.3
# Authenticated SPN2 allows a higher save rate; reduce pacing when keys are present.
SAVE_DELAY_SECONDS_AUTH = 5


def load_log() -> dict:
    if LOG_PATH.exists():
        try:
            return json.loads(LOG_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def save_log(log: dict) -> None:
    LOG_PATH.write_text(json.dumps(log, indent=2, sort_keys=True), encoding="utf-8")


def parse_frontmatter_text(card_text: str) -> tuple[str, str, str]:
    """Return (prefix '---\n', frontmatter_text, suffix starting with '\n---\n...')."""
    if not card_text.startswith("---\n"):
        return "", "", card_text
    end = card_text.find("\n---\n", 4)
    if end == -1:
        return "", "", card_text
    return "---\n", card_text[4:end], card_text[end:]


URL_RE = re.compile(r'^\s*url:\s*"?([^"\s]+)"?\s*$', re.MULTILINE)
WAYBACK_URL_RE = re.compile(r'^(\s*)wayback_url:\s*.*$', re.MULTILINE)
WAYBACK_CAPTURED_RE = re.compile(r'^(\s*)wayback_captured:\s*.*$', re.MULTILINE)
BODY_SHA_RE = re.compile(r'^(\s*)body_sha256:\s*.*$', re.MULTILINE)


def extract_url(fm: str) -> str | None:
    m = URL_RE.search(fm)
    if not m:
        return None
    url = m.group(1).strip().strip('"').strip("'")
    # ignore non-http urls
    if not url.startswith(("http://", "https://")):
        return None
    return url


def extract_wayback_url(fm: str) -> str | None:
    for line in fm.splitlines():
        m = re.match(r'\s*wayback_url:\s*(.*)\s*$', line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def extract_body_sha256(fm: str) -> str | None:
    for line in fm.splitlines():
        m = re.match(r'\s*body_sha256:\s*(.*)\s*$', line)
        if m:
            v = m.group(1).strip().strip('"').strip("'")
            if re.fullmatch(r'[a-f0-9]{64}', v):
                return v
    return None


def is_template_wayback(url: str | None) -> bool:
    if not url:
        return True
    return "/web/*/" in url or url == "https://web.archive.org/"


_BROWSER_HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "identity",  # avoid gzip — we want hashable raw bytes
    "Connection": "close",
}


def _auth_headers_for(url: str) -> dict[str, str]:
    """Per-host auth headers. CourtListener token; api.data.gov key passed via query, not header."""
    headers = dict(_BROWSER_HEADERS)
    host = urllib.parse.urlparse(url).netloc.lower()
    if "courtlistener.com" in host and COURTLISTENER_TOKEN:
        headers["Authorization"] = f"Token {COURTLISTENER_TOKEN}"
    return headers


def http_head(url: str) -> tuple[int | None, str | None]:
    """Return (status_code, error_str). Falls back to GET-with-Range if HEAD is blocked."""
    base = _auth_headers_for(url)
    try:
        req = urllib.request.Request(url, method="HEAD", headers=base)
        with urllib.request.urlopen(req, timeout=HEAD_TIMEOUT) as resp:
            return resp.status, None
    except urllib.error.HTTPError as e:
        # Many CDNs (Cloudfront, Cloudflare) block HEAD entirely. Retry as a Range GET.
        if e.code in (403, 405, 501):
            try:
                hdrs = dict(base, **{"Range": "bytes=0-1023"})
                req = urllib.request.Request(url, headers=hdrs)
                with urllib.request.urlopen(req, timeout=HEAD_TIMEOUT) as resp:
                    return resp.status, None
            except urllib.error.HTTPError as e2:
                return e2.code, str(e2)
            except urllib.error.URLError as e2:
                return None, str(e2.reason)
            except Exception as e2:
                return None, str(e2)
        return e.code, str(e)
    except urllib.error.URLError as e:
        return None, str(e.reason)
    except Exception as e:
        return None, str(e)


def http_get_sha256(url: str) -> tuple[str | None, int | None, str | None]:
    """Fetch URL, return (sha256_hex, status_code, error_str). 5 MB max."""
    try:
        req = urllib.request.Request(url, headers=_auth_headers_for(url))
        with urllib.request.urlopen(req, timeout=GET_TIMEOUT) as resp:
            data = resp.read(5 * 1024 * 1024)
            return hashlib.sha256(data).hexdigest(), resp.status, None
    except urllib.error.HTTPError as e:
        return None, e.code, str(e)
    except urllib.error.URLError as e:
        return None, None, str(e.reason)
    except Exception as e:
        return None, None, str(e)


def wayback_check_available(url: str) -> tuple[str | None, str | None]:
    """Query Wayback Availability API. Returns (snapshot_url, snapshot_date_YYYY-MM-DD) or (None, None)."""
    try:
        q = urllib.parse.urlencode({"url": url})
        api = f"{AVAIL_API}?{q}"
        req = urllib.request.Request(api, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        snap = (data.get("archived_snapshots") or {}).get("closest") or {}
        if snap.get("available") and snap.get("status") == "200":
            ts = snap.get("timestamp", "")  # YYYYMMDDhhmmss
            snap_url = snap.get("url")
            if snap_url and ts and len(ts) >= 8:
                iso_date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}"
                return snap_url, iso_date
    except Exception:
        pass
    return None, None


def _wayback_save_authenticated(url: str) -> tuple[str | None, str | None]:
    """SPN2 authenticated flow: POST to /save → job_id → poll /save/status/<job_id>.

    Succeeds on many bot-blocked origins (justice.gov, congress.gov, courts) that the
    anonymous endpoint refuses. Returns (snapshot_url, iso_date) or (None, None).
    """
    auth = f"LOW {ARCHIVE_ORG_ACCESS_KEY}:{ARCHIVE_ORG_SECRET_KEY}"
    headers = {"Accept": "application/json", "Authorization": auth, "User-Agent": UA}
    try:
        data = urllib.parse.urlencode({"url": url}).encode()
        req = urllib.request.Request("https://web.archive.org/save", data=data, method="POST", headers=headers)
        with urllib.request.urlopen(req, timeout=SAVE_TIMEOUT) as resp:
            j = json.loads(resp.read().decode("utf-8", errors="replace"))
        job = j.get("job_id")
        # If the same snapshot was just made, the message says so; poll availability instead.
        if not job:
            return None, None
        # Poll status up to ~8 times (≈40s) for the capture to complete.
        for _ in range(8):
            time.sleep(5)
            try:
                s = urllib.request.Request(
                    f"https://web.archive.org/save/status/{job}",
                    headers=headers,
                )
                with urllib.request.urlopen(s, timeout=30) as sr:
                    st = json.loads(sr.read().decode("utf-8", errors="replace"))
            except Exception:
                continue
            status = st.get("status")
            if status == "success":
                ts = st.get("timestamp", "")
                orig = st.get("original_url", url)
                if ts and len(ts) >= 8:
                    iso_date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}"
                    return f"https://web.archive.org/web/{ts}/{orig}", iso_date
                return None, None
            if status == "error":
                return None, None
    except Exception:
        pass
    return None, None


def wayback_save(url: str) -> tuple[str | None, str | None]:
    """Capture a Wayback snapshot. Authenticated SPN2 when keys present; else anonymous GET.

    Returns (snapshot_url, iso_date) or (None, None).
    """
    if ARCHIVE_ORG_ACCESS_KEY and ARCHIVE_ORG_SECRET_KEY:
        snap_url, iso_date = _wayback_save_authenticated(url)
        if snap_url:
            return snap_url, iso_date
        # Fall through to availability poll — the capture may have completed server-side.

    save_url = SAVE_API_BASE + url
    try:
        req = urllib.request.Request(save_url, method="GET", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=SAVE_TIMEOUT) as resp:
            content_location = resp.headers.get("Content-Location") or resp.headers.get("Location") or ""
            final_url = resp.url
            for candidate in (final_url, content_location):
                if not candidate:
                    continue
                m = re.search(r'/web/(\d{14})/', candidate)
                if m:
                    ts = m.group(1)
                    iso_date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}"
                    if candidate.startswith("/web/"):
                        candidate = "https://web.archive.org" + candidate
                    return candidate, iso_date
            try:
                resp.read(1024)
            except Exception:
                pass
    except urllib.error.HTTPError:
        pass
    except urllib.error.URLError:
        pass
    except Exception:
        pass

    # Final fallback: poll Availability API (catches server-side completion).
    for _ in range(3):
        time.sleep(3)
        snap_url, iso_date = wayback_check_available(url)
        if snap_url:
            return snap_url, iso_date
    return None, None


def _patch_body_sha(fm: str, body_sha256: str | None) -> str:
    """Inject or replace verification.body_sha256."""
    if body_sha256 is None:
        return fm
    m = BODY_SHA_RE.search(fm)
    if m:
        indent = m.group(1)
        return BODY_SHA_RE.sub(f'{indent}body_sha256: "{body_sha256}"', fm, count=1)
    verified_on_re = re.compile(r'(^(\s*)verified_on:\s*.*$)', re.MULTILINE)
    m2 = verified_on_re.search(fm)
    if m2:
        indent = m2.group(2)
        inject = f'\n{indent}body_sha256: "{body_sha256}"'
        return fm[:m2.end(1)] + inject + fm[m2.end(1):]
    return fm


def patch_card_frontmatter(fm: str, *, body_sha256: str | None,
                            wayback_url: str | None, wayback_captured: str | None) -> str:
    """In-place YAML patch using regex; preserves surrounding lines."""

    def patch_line(text: str, line_re: re.Pattern, key: str, value: str | None) -> str:
        if value is None:
            return text
        m = line_re.search(text)
        if m:
            indent = m.group(1) if m.lastindex else "    "
            replacement = f'{indent}{key}: "{value}"'
            return line_re.sub(replacement, text, count=1)
        return text

    # Ensure the archive: block can hold wayback fields. Handle three states:
    #   (a) "archive: {}"  (empty map)   → expand to a block
    #   (b) "archive:" with no children  (null)        → expand to a block
    #   (c) "archive:" with children                   → leave; patch_line injects
    # Only do this when we actually have a wayback_url to write.
    if wayback_url is not None and not WAYBACK_URL_RE.search(fm):
        cap = f'\n    wayback_captured: "{wayback_captured}"' if wayback_captured else ""
        block = f'  archive:\n    wayback_url: "{wayback_url}"{cap}'
        if re.search(r'^\s*archive:\s*\{\}\s*$', fm, re.MULTILINE):
            fm = re.sub(r'^\s*archive:\s*\{\}\s*$', block, fm, count=1, flags=re.MULTILINE)
            return _patch_body_sha(fm, body_sha256)
        # bare "archive:" followed by a non-indented line (null map)
        if re.search(r'^\s*archive:\s*$\n(?!\s+\S)', fm, re.MULTILINE):
            fm = re.sub(r'^\s*archive:\s*$', block, fm, count=1, flags=re.MULTILINE)
            return _patch_body_sha(fm, body_sha256)
        # no archive key at all → inject before access_constraint
        if not re.search(r'^\s*archive:', fm, re.MULTILINE) and re.search(r'^\s*access_constraint:', fm, re.MULTILINE):
            fm = re.sub(r'^(\s*access_constraint:.*)$', f'{block}\n\\1', fm, count=1, flags=re.MULTILINE)
            return _patch_body_sha(fm, body_sha256)

    fm = patch_line(fm, WAYBACK_URL_RE, "wayback_url", wayback_url)
    fm = patch_line(fm, WAYBACK_CAPTURED_RE, "wayback_captured", wayback_captured)
    return _patch_body_sha(fm, body_sha256)


def verify_card(card_path: Path, log: dict, args) -> dict:
    """Verify one card. Return per-card outcome dict."""
    slug = card_path.stem
    raw = card_path.read_text(encoding="utf-8")
    prefix, fm, suffix = parse_frontmatter_text(raw)
    if not fm:
        return {"slug": slug, "skipped": "no frontmatter"}

    url = extract_url(fm)
    if not url:
        return {"slug": slug, "skipped": "no source.url"}

    prior = log.get(slug, {})
    existing_sha = extract_body_sha256(fm)
    existing_wb = extract_wayback_url(fm)
    if existing_sha and existing_wb and not is_template_wayback(existing_wb) and not args.retry_dead:
        return {"slug": slug, "skipped": "already verified", "url": url, "sha256": existing_sha,
                "wayback_url": existing_wb}

    outcome: dict = {"slug": slug, "url": url, "timestamp": datetime.datetime.utcnow().isoformat()}

    # Step 1: HEAD
    head_status, head_err = http_head(url)
    outcome["head_status"] = head_status
    if head_err:
        outcome["head_error"] = head_err

    # Step 2: GET + sha256 (only if HEAD looks live or HEAD failed but we want a body for paywall pages)
    body_sha = None
    if head_status is None or 200 <= (head_status or 0) < 500:
        sha, get_status, get_err = http_get_sha256(url)
        outcome["get_status"] = get_status
        if get_err:
            outcome["get_error"] = get_err
        if sha:
            body_sha = sha
            outcome["body_sha256"] = sha

    # Step 3 + 4: Wayback availability, fall back to Save
    wb_url, wb_date = wayback_check_available(url)
    if wb_url:
        outcome["wayback_existing"] = True
        outcome["wayback_url"] = wb_url
        outcome["wayback_captured"] = wb_date
    elif not args.no_save:
        outcome["wayback_existing"] = False
        wb_url, wb_date = wayback_save(url)
        if wb_url:
            outcome["wayback_url"] = wb_url
            outcome["wayback_captured"] = wb_date
            outcome["wayback_saved"] = True
            _auth = bool(ARCHIVE_ORG_ACCESS_KEY and ARCHIVE_ORG_SECRET_KEY)
            time.sleep(SAVE_DELAY_SECONDS_AUTH if _auth else SAVE_DELAY_SECONDS)  # pacing
        else:
            outcome["wayback_save_failed"] = True

    # Step 5: write back to card
    if args.dry_run:
        return outcome

    new_fm = patch_card_frontmatter(
        fm,
        body_sha256=body_sha,
        wayback_url=outcome.get("wayback_url"),
        wayback_captured=outcome.get("wayback_captured"),
    )
    if new_fm != fm:
        card_path.write_text(prefix + new_fm + suffix, encoding="utf-8")
        outcome["card_updated"] = True

    return outcome


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify research-card link integrity.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None, help="Process at most N cards")
    parser.add_argument("--only", type=str, default=None, help="Process only this card slug")
    parser.add_argument("--no-save", action="store_true", help="Skip Wayback Save API (use only existing snapshots)")
    parser.add_argument("--retry-dead", action="store_true", help="Re-verify even cards already verified")
    parser.add_argument("--skip", type=int, default=0, help="Skip the first N cards (for batch resume)")
    args = parser.parse_args()

    log = load_log()
    cards = sorted(CARDS_DIR.glob("*.md"))
    if args.only:
        cards = [c for c in cards if c.stem == args.only]
    if args.skip:
        cards = cards[args.skip:]
    if args.limit:
        cards = cards[: args.limit]

    print(f"Verifying {len(cards)} cards (limit={args.limit}, dry_run={args.dry_run}, no_save={args.no_save})")
    print()

    processed = 0
    updated = 0
    skipped = 0
    head_failures: list[str] = []
    save_failures: list[str] = []

    for i, c in enumerate(cards):
        try:
            outcome = verify_card(c, log, args)
        except KeyboardInterrupt:
            print(f"\nInterrupted at {c.stem}", file=sys.stderr)
            break
        except Exception as e:
            outcome = {"slug": c.stem, "error": str(e)}

        log[c.stem] = outcome
        # save log every 5 cards
        if i % 5 == 0:
            save_log(log)

        if outcome.get("skipped"):
            skipped += 1
            tag = "SKIP"
        elif outcome.get("card_updated"):
            updated += 1
            tag = "UPDT"
        else:
            tag = "----"

        head_status = outcome.get("head_status")
        if head_status and head_status >= 400:
            head_failures.append(f"{c.stem} ({head_status})")
        if outcome.get("head_error"):
            head_failures.append(f"{c.stem} (HEAD: {outcome['head_error'][:60]})")
        if outcome.get("wayback_save_failed"):
            save_failures.append(c.stem)

        sha_short = (outcome.get("body_sha256") or "")[:8]
        wb_existing = "wb-old" if outcome.get("wayback_existing") else ("wb-new" if outcome.get("wayback_saved") else "wb-???")
        print(f"[{i+1:3d}/{len(cards)}] {tag} {c.stem[:60]:60s}  head={head_status}  sha={sha_short}  {wb_existing}")
        processed += 1

    save_log(log)

    print()
    print(f"Processed: {processed}")
    print(f"Updated  : {updated}")
    print(f"Skipped  : {skipped}")
    print(f"HEAD failures ({len(head_failures)}):")
    for f in head_failures[:20]:
        print(f"  {f}")
    if len(head_failures) > 20:
        print(f"  ... and {len(head_failures) - 20} more")
    print(f"Wayback Save failures ({len(save_failures)}):")
    for f in save_failures[:20]:
        print(f"  {f}")
    print()
    print(f"Log: {LOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
