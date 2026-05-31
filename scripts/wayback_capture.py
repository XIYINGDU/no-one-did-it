#!/usr/bin/env python3
"""Trigger Wayback Machine Save-Page-Now for cards with broken/missing
archives, then update the card metadata with the new archive URL.

Workflow per card:
  1. Read card.source.url (primary URL).
  2. Read card.verification.url_check.primary.status (if present).
  3. Skip card if primary status is ok/redirect AND archive exists.
  4. Otherwise: trigger https://web.archive.org/save/<url> (GET).
  5. Wayback responds with `Content-Location: /web/<TIMESTAMP>/<URL>`
     when capture starts; we poll up to N seconds for the capture to
     finish and then construct the final wayback URL.
  6. Update card.source.archive with new wayback_url + wayback_captured
     date.

Selection modes:
  --all              — every card whose primary is not ok/redirect
                       and whose archive is missing/broken
  --cards SLUG ...   — explicit card slugs (comma-separated or repeated)
  --dry-run          — print what would be captured, don't call Wayback

Wayback Save-Page-Now is rate-limited. The script throttles to 1
request per 5 seconds by default; --interval overrides.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)


def _parse_card(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    try:
        return yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None


def _write_card(path: Path, data: dict[str, Any]) -> None:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---", 4)
    body = text[end + 4:]
    new_front = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10_000)
    path.write_text(f"---\n{new_front}---{body}", encoding="utf-8")


def _needs_capture(data: dict[str, Any]) -> tuple[bool, str | None]:
    """Return (needs_capture, primary_url)."""
    source = data.get("source") or {}
    if not isinstance(source, dict):
        return False, None
    primary_url = source.get("url")
    if not isinstance(primary_url, str) or not primary_url:
        return False, None
    archive_block = source.get("archive") or {}
    has_archive = bool(isinstance(archive_block, dict)
                       and archive_block.get("wayback_url"))
    # Read the verification.url_check primary status.
    v = data.get("verification") or {}
    uc = v.get("url_check") or {} if isinstance(v, dict) else {}
    primary = uc.get("primary") or {} if isinstance(uc, dict) else {}
    p_status = primary.get("status", "") if isinstance(primary, dict) else ""
    archive = uc.get("archive") or {} if isinstance(uc, dict) else {}
    a_status = archive.get("status", "") if isinstance(archive, dict) else ""

    primary_ok = p_status in ("ok", "redirect")
    archive_ok = a_status in ("ok", "redirect") and has_archive

    # Capture iff (primary is broken or unverified) AND (archive is
    # missing or broken). Cards where both are ok don't need a re-capture.
    if not has_archive and not primary_ok:
        return True, primary_url
    if has_archive and not archive_ok and not primary_ok:
        return True, primary_url
    return False, primary_url


def _check_availability(url: str) -> tuple[str | None, str | None]:
    """Query the Wayback Availability API for an existing snapshot.

    Returns (wayback_url, capture_yyyymmdd) or (None, None) if no
    snapshot exists or the API is unreachable.
    """
    import json
    api = f"https://archive.org/wayback/available?url={url}"
    req = urllib.request.Request(api, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
    except Exception:  # noqa: BLE001
        return None, None
    closest = (data.get("archived_snapshots") or {}).get("closest") or {}
    if not closest.get("available"):
        return None, None
    wb_url = closest.get("url")
    ts = closest.get("timestamp") or ""
    # ts is YYYYMMDDhhmmss; expose YYYY-MM-DD for human reading.
    capture_date = f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}" if len(ts) >= 8 else None
    return wb_url, capture_date


def _save_via_wayback(url: str) -> tuple[str | None, str, str | None]:
    """Hit Wayback Save-Page-Now; fall back to Availability API on
    failure (returns the most-recent existing capture if any).

    Returns (archive_url_or_none, status_msg, capture_yyyy_mm_dd).
    """
    save_url = f"https://web.archive.org/save/{url}"
    req = urllib.request.Request(save_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            code = resp.getcode()
            final = resp.geturl()
            m = re.search(r"web\.archive\.org/web/(\d{14})/(.*)$", final)
            if m:
                ts = m.group(1)
                captured_url = m.group(2)
                if not captured_url.startswith(("http://", "https://")):
                    captured_url = "https://" + captured_url
                wayback_url = f"http://web.archive.org/web/{ts}/{captured_url}"
                return wayback_url, f"captured (HTTP {code})", dt.date.today().isoformat()
            # Fall back to availability lookup.
            wb_url, capture_date = _check_availability(url)
            if wb_url:
                return wb_url, f"save-now ambiguous (HTTP {code}); existing capture from {capture_date}", capture_date
            return None, f"no capture URL in response (HTTP {code}); final={final}", None
    except urllib.error.HTTPError as e:
        # Save-Now refused (520/429/etc); look for an existing snapshot.
        wb_url, capture_date = _check_availability(url)
        if wb_url:
            return wb_url, f"save-now HTTP {e.code}; existing capture from {capture_date}", capture_date
        return None, f"HTTP {e.code} {e.reason}; no existing capture", None
    except urllib.error.URLError as e:
        wb_url, capture_date = _check_availability(url)
        if wb_url:
            return wb_url, f"save-now URLError ({e.reason}); existing capture from {capture_date}", capture_date
        return None, f"URLError: {e.reason}; no existing capture", None
    except (TimeoutError, OSError) as e:
        wb_url, capture_date = _check_availability(url)
        if wb_url:
            return wb_url, f"save-now timeout; existing capture from {capture_date}", capture_date
        return None, f"{type(e).__name__}: {e}; no existing capture", None


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__ or "")
    p.add_argument("--cards-dir", type=Path, default=Path("book/evidence/source-ledger/cards"))
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true",
                   help="Process every card that needs capture per the rule above")
    g.add_argument("--cards", type=str, nargs="+",
                   help="Explicit list of card slugs")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--interval", type=float, default=5.0,
                   help="Seconds between Wayback requests (rate-limit)")
    args = p.parse_args(argv)

    cards_dir: Path = args.cards_dir
    if not cards_dir.is_dir():
        print(f"error: cards directory not found: {cards_dir}", file=sys.stderr)
        return 1

    if args.cards:
        # User specified explicit slugs.
        slugs = []
        for s in args.cards:
            slugs.extend(s.split(","))
        slugs = [s.strip() for s in slugs if s.strip()]
        targets: list[tuple[Path, dict[str, Any], str]] = []
        for slug in slugs:
            path = cards_dir / f"{slug}.md"
            if not path.exists():
                print(f"  SKIP {slug}: card not found", file=sys.stderr)
                continue
            data = _parse_card(path)
            if not data:
                print(f"  SKIP {slug}: card unparseable", file=sys.stderr)
                continue
            source = data.get("source") or {}
            url = source.get("url") if isinstance(source, dict) else None
            if not isinstance(url, str) or not url:
                print(f"  SKIP {slug}: no primary URL", file=sys.stderr)
                continue
            targets.append((path, data, url))
    else:
        # --all: scan every card.
        targets = []
        for path in sorted(cards_dir.glob("*.md")):
            data = _parse_card(path)
            if not data:
                continue
            needs, url = _needs_capture(data)
            if needs and url:
                targets.append((path, data, url))

    print(f"Targets: {len(targets)}", file=sys.stderr)
    for path, _, url in targets[:5]:
        print(f"  - {path.stem}  →  {url[:80]}", file=sys.stderr)
    if len(targets) > 5:
        print(f"  ... +{len(targets) - 5} more", file=sys.stderr)

    if args.dry_run:
        print("(dry-run; nothing captured)", file=sys.stderr)
        return 0

    successes = 0
    failures: list[tuple[str, str]] = []

    for i, (path, data, url) in enumerate(targets):
        if i > 0:
            time.sleep(args.interval)
        print(f"[{i+1}/{len(targets)}] {path.stem}", file=sys.stderr)
        wayback_url, msg, capture_date = _save_via_wayback(url)
        if wayback_url:
            print(f"  OK: {wayback_url}", file=sys.stderr)
            source = data.setdefault("source", {})
            archive = source.setdefault("archive", {})
            archive["wayback_url"] = wayback_url
            archive["wayback_captured"] = capture_date or dt.date.today().isoformat()
            archive["wayback_capture_source"] = "scripts/wayback_capture.py"
            _write_card(path, data)
            successes += 1
        else:
            print(f"  FAIL: {msg}", file=sys.stderr)
            failures.append((path.stem, msg))

    print(f"\nDone. Captured: {successes}/{len(targets)}", file=sys.stderr)
    if failures:
        print(f"\nFailures:", file=sys.stderr)
        for slug, msg in failures:
            print(f"  {slug}: {msg}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
