#!/usr/bin/env python3
"""Verify URLs in source-ledger cards (primary + Wayback archive).

Reads every card in book/evidence/source-ledger/cards/*.md, extracts the
source.url and source.archive.wayback_url fields, runs HTTP HEAD
checks against each unique URL (concurrent), classifies status,
and writes:

  1. A verification report:    process/audits/url-verification-<DATE>.md
  2. A per-card metadata patch: appends a `verification.url_check`
     block recording verified_on date + per-URL status. Cards are
     updated in place.

Status taxonomy:
  ok               — 2xx response
  redirect         — 3xx (final URL recorded if available)
  not-found        — 404
  server-error     — 5xx
  unreachable      — timeout / connection refused / SSL error (could
                     be checkpoint-specific; flagged for re-check
                     from a different network)
  invalid          — malformed URL or unsupported scheme

GFW caveat: this script runs from the principal author's checkpoint
in China. Unreachable status may mean "blocked from here" rather than
"globally broken." The report distinguishes the two by checking if
the URL belongs to a known-GFW-blocked domain (Google, Twitter/X,
Facebook, NYT, etc.); for blocked domains a single failure is treated
as "pending-other-checkpoint" rather than "broken."

Usage::

    python3 scripts/verify_card_urls.py [--limit N] [--no-update]
                                        [--cards-dir <path>]
                                        [--report <path>]
                                        [--concurrency N]

Exit code is 0 on completion regardless of how many URLs failed; the
report itself is the authoritative result. Non-zero only on script
error (missing cards directory, etc.).
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]


# Domains commonly blocked or rate-limited from China; treat single
# failures as "pending other checkpoint" rather than "broken."
GFW_SUSPECT_DOMAINS = {
    "twitter.com", "x.com", "t.co",
    "facebook.com", "fb.com",
    "google.com", "googleusercontent.com",
    "youtube.com", "youtu.be",
    "instagram.com",
    "medium.com",
    "nytimes.com", "washingtonpost.com",
    "bbc.com", "bbc.co.uk",
    "reuters.com",
    "theguardian.com",
    "wsj.com",
    "ft.com",
}

# Real browser UA — many sites (CourtListener, DOJ, news outlets,
# Twitter/X) 403 any UA containing "bot" / "compatible" / "verifier".
# Using a current Chrome string reduces false-403 noise dramatically;
# the verification is for citation freshness, not for scraping content.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)

# Browser-like headers — Accept + Accept-Language are sometimes
# enforced by WAFs (Cloudflare etc.) as additional bot signals.
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

TIMEOUT_SECONDS = 15


@dataclass
class UrlCheck:
    url: str
    status: str  # ok | redirect | not-found | server-error | unreachable | invalid | pending-other-checkpoint
    http_code: int | None = None
    final_url: str | None = None
    error: str | None = None


@dataclass
class CardResult:
    card_id: str
    path: Path
    primary: UrlCheck | None = None
    archive: UrlCheck | None = None


def _is_gfw_suspect(url: str) -> bool:
    try:
        host = urllib.parse.urlparse(url).netloc.lower()
    except ValueError:
        return False
    if not host:
        return False
    # Strip leading www.
    if host.startswith("www."):
        host = host[4:]
    return any(host == d or host.endswith("." + d) for d in GFW_SUSPECT_DOMAINS)


def _check_one(url: str) -> UrlCheck:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return UrlCheck(url=url, status="invalid", error=f"unsupported scheme {parsed.scheme!r}")

    # Try HEAD first (fast, no body transfer). If HEAD returns 4xx, fall
    # back to GET — many WAFs (Cloudflare, CourtListener, DOJ archive)
    # 403 HEAD-only requests but allow GET with browser headers.
    last_error: str | None = None
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers=dict(DEFAULT_HEADERS))
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
                code = resp.getcode()
                final = resp.geturl()
                if code is None:
                    continue
                if 200 <= code < 300:
                    status = "ok" if final == url else "redirect"
                    return UrlCheck(url=url, status=status, http_code=code,
                                    final_url=final if final != url else None)
                if 300 <= code < 400:
                    return UrlCheck(url=url, status="redirect", http_code=code, final_url=final)
                if code == 404:
                    return UrlCheck(url=url, status="not-found", http_code=code)
                if 500 <= code < 600:
                    return UrlCheck(url=url, status="server-error", http_code=code)
                if code == 403 and method == "HEAD":
                    # Anti-bot likely; try GET.
                    last_error = f"HEAD HTTP {code}"
                    continue
                return UrlCheck(url=url, status="not-found", http_code=code,
                                error=f"HTTP {code}")
        except urllib.error.HTTPError as e:
            code = e.code
            if code in (403, 405) and method == "HEAD":
                # Method not allowed or HEAD-forbidden — retry with GET.
                last_error = f"HEAD HTTP {code} {e.reason}"
                continue
            if code == 403:
                # Bot wall even on GET; treat as forbidden but distinct
                # from genuine not-found. Mark as 'forbidden' so downstream
                # can decide whether the archive should win.
                return UrlCheck(url=url, status="forbidden", http_code=code,
                                error=f"HTTP {code} {e.reason}")
            if code == 404:
                return UrlCheck(url=url, status="not-found", http_code=code)
            if 500 <= code < 600:
                return UrlCheck(url=url, status="server-error", http_code=code)
            if 300 <= code < 400:
                return UrlCheck(url=url, status="redirect", http_code=code)
            return UrlCheck(url=url, status="not-found", http_code=code,
                            error=f"HTTP {code} {e.reason}")
        except urllib.error.URLError as e:
            reason = str(e.reason)
            # Network-level failure on HEAD — some servers (justice.gov,
            # archive.gov) have slow TLS handshakes or reject HEAD outright.
            # Fall back to GET before declaring unreachable.
            if method == "HEAD":
                last_error = f"HEAD URLError: {reason}"
                continue
            status = "pending-other-checkpoint" if _is_gfw_suspect(url) else "unreachable"
            return UrlCheck(url=url, status=status, error=reason)
        except (TimeoutError, OSError) as e:
            if method == "HEAD":
                last_error = f"HEAD {type(e).__name__}: {e}"
                continue
            status = "pending-other-checkpoint" if _is_gfw_suspect(url) else "unreachable"
            return UrlCheck(url=url, status=status, error=str(e))
        except Exception as e:  # noqa: BLE001
            if method == "HEAD":
                last_error = f"HEAD {type(e).__name__}: {e}"
                continue
            return UrlCheck(url=url, status="unreachable", error=f"{type(e).__name__}: {e}")
    return UrlCheck(url=url, status="unreachable",
                    error=last_error or "no method succeeded")


def _extract_card_urls(card_path: Path) -> tuple[str, str | None, str | None, dict[str, Any] | None]:
    """Return (card_id, primary_url, archive_url, parsed_frontmatter)."""
    text = card_path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 4)
        if end >= 0:
            front = text[4:end]
            try:
                data = yaml.safe_load(front)
            except yaml.YAMLError:
                data = None
        else:
            data = None
    else:
        # Whole file is YAML.
        try:
            data = yaml.safe_load(text)
        except yaml.YAMLError:
            data = None

    if not isinstance(data, dict):
        return (card_path.stem, None, None, None)

    card_id = str(data.get("id") or card_path.stem)
    source = data.get("source") or {}
    primary = source.get("url") if isinstance(source, dict) else None
    archive_url = None
    if isinstance(source, dict):
        archive_block = source.get("archive")
        if isinstance(archive_block, dict):
            archive_url = archive_block.get("wayback_url") or archive_block.get("url")
        elif isinstance(archive_block, str):
            archive_url = archive_block
    return (card_id, primary if isinstance(primary, str) else None,
            archive_url if isinstance(archive_url, str) else None, data)


def _check_card(card_path: Path) -> tuple[CardResult, dict[str, Any] | None]:
    card_id, primary_url, archive_url, data = _extract_card_urls(card_path)
    result = CardResult(card_id=card_id, path=card_path)
    if primary_url:
        result.primary = _check_one(primary_url)
    if archive_url:
        result.archive = _check_one(archive_url)
    return result, data


def _format_check(check: UrlCheck | None) -> str:
    if check is None:
        return "—"
    parts = [check.status]
    if check.http_code is not None:
        parts.append(f"HTTP {check.http_code}")
    if check.final_url:
        parts.append(f"→ {check.final_url}")
    if check.error:
        parts.append(check.error[:80])
    return " · ".join(parts)


def _patch_card_metadata(card_path: Path, data: dict[str, Any], result: CardResult,
                        verified_on: str) -> bool:
    """Insert verification.url_check block; return True if file modified."""
    if data is None:
        return False
    verification = data.get("verification")
    if not isinstance(verification, dict):
        verification = {}
        data["verification"] = verification
    url_check_block: dict[str, Any] = {
        "verified_on": verified_on,
        "verifier_checkpoint": "principal-author-cn",
    }
    if result.primary is not None:
        primary_block: dict[str, Any] = {
            "url": result.primary.url,
            "status": result.primary.status,
        }
        if result.primary.http_code is not None:
            primary_block["http_code"] = result.primary.http_code
        if result.primary.final_url:
            primary_block["final_url"] = result.primary.final_url
        if result.primary.error:
            primary_block["error"] = result.primary.error
        url_check_block["primary"] = primary_block
    if result.archive is not None:
        archive_block: dict[str, Any] = {
            "url": result.archive.url,
            "status": result.archive.status,
        }
        if result.archive.http_code is not None:
            archive_block["http_code"] = result.archive.http_code
        if result.archive.final_url:
            archive_block["final_url"] = result.archive.final_url
        if result.archive.error:
            archive_block["error"] = result.archive.error
        url_check_block["archive"] = archive_block
    verification["url_check"] = url_check_block

    # Re-emit the frontmatter.
    text = card_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 4)
    if end < 0:
        return False
    body = text[end + 4:]
    new_front = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10_000)
    card_path.write_text(f"---\n{new_front}---{body}", encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__ or "")
    p.add_argument("--cards-dir", type=Path, default=Path("book/evidence/source-ledger/cards"))
    p.add_argument("--report", type=Path, default=None,
                   help="Report path (default: process/audits/url-verification-<YYYY-MM-DD>.md)")
    p.add_argument("--limit", type=int, default=None, help="Only check first N cards (debug)")
    p.add_argument("--concurrency", type=int, default=10)
    p.add_argument("--no-update", action="store_true",
                   help="Skip writing verification.url_check back into cards")
    args = p.parse_args(argv)

    cards_dir: Path = args.cards_dir
    if not cards_dir.is_dir():
        print(f"error: cards directory not found: {cards_dir}", file=sys.stderr)
        return 1

    today = dt.date.today().isoformat()
    report_path: Path = args.report or Path("process/audits") / f"url-verification-{today}.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    card_paths = sorted(cards_dir.glob("*.md"))
    if args.limit:
        card_paths = card_paths[: args.limit]

    print(f"Checking {len(card_paths)} cards "
          f"(concurrency={args.concurrency})...", file=sys.stderr)

    results: list[tuple[CardResult, dict[str, Any] | None]] = []
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(_check_card, p): p for p in card_paths}
        for i, fut in enumerate(cf.as_completed(futures), start=1):
            results.append(fut.result())
            if i % 20 == 0:
                print(f"  {i}/{len(card_paths)} done", file=sys.stderr)

    # Sort results by card_id for stable report output.
    results.sort(key=lambda r: r[0].card_id)

    # Tally statuses.
    primary_tally: Counter[str] = Counter()
    archive_tally: Counter[str] = Counter()
    cards_no_url: list[str] = []
    cards_primary_broken: list[CardResult] = []
    cards_primary_broken_archive_ok: list[CardResult] = []
    cards_both_broken: list[CardResult] = []
    cards_gfw_pending: list[CardResult] = []

    for cr, _ in results:
        if cr.primary is None and cr.archive is None:
            cards_no_url.append(cr.card_id)
            continue
        if cr.primary:
            primary_tally[cr.primary.status] += 1
        if cr.archive:
            archive_tally[cr.archive.status] += 1
        primary_bad = (cr.primary is not None and
                       cr.primary.status in ("not-found", "server-error"))
        archive_ok = (cr.archive is not None and cr.archive.status in ("ok", "redirect"))
        primary_pending = (cr.primary is not None and
                           cr.primary.status == "pending-other-checkpoint")
        if primary_bad and archive_ok:
            cards_primary_broken_archive_ok.append(cr)
        elif primary_bad and not archive_ok:
            cards_both_broken.append(cr)
        elif primary_bad:
            cards_primary_broken.append(cr)
        if primary_pending or (cr.archive is not None and
                               cr.archive.status == "pending-other-checkpoint"):
            cards_gfw_pending.append(cr)

    # Update cards in place unless asked not to.
    updated = 0
    if not args.no_update:
        for cr, data in results:
            if data is None:
                continue
            if _patch_card_metadata(cr.path, data, cr, today):
                updated += 1

    # Write report.
    lines: list[str] = []
    lines.append(f"# URL Verification Report — {today}")
    lines.append("")
    lines.append("Owner: scripts/verify_card_urls.py (run by jerry-crew-chief)")
    lines.append(f"Task: Verify primary + Wayback URLs in {len(card_paths)} source-ledger cards.")
    lines.append(f"Inputs reviewed: `{cards_dir}/*.md` ({len(card_paths)} files)")
    lines.append(f"Output: this report; cards updated with `verification.url_check` block "
                 f"(updated_in_place={updated})")
    lines.append("Evidence grade: N/A (operational check)")
    lines.append(f"Assumptions: checkpoint is principal-author-cn (subject to GFW). URLs on "
                 f"known-blocked domains are reported as `pending-other-checkpoint` rather "
                 f"than `unreachable` on a single failure.")
    lines.append("Open questions: any URL marked `pending-other-checkpoint` should be re-run "
                 "from an unblocked checkpoint; any `not-found` whose archive is also broken "
                 "should be re-sourced or re-archived via Wayback's Save Page Now.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Cards checked: **{len(card_paths)}**")
    lines.append(f"- Cards with no URL fields: **{len(cards_no_url)}**")
    lines.append(f"- Cards updated in place: **{updated}**")
    lines.append("")
    lines.append("### Primary URL status")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for status, count in sorted(primary_tally.items(), key=lambda x: -x[1]):
        lines.append(f"| `{status}` | {count} |")
    lines.append(f"| **total** | **{sum(primary_tally.values())}** |")
    lines.append("")
    lines.append("### Archive URL status")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for status, count in sorted(archive_tally.items(), key=lambda x: -x[1]):
        lines.append(f"| `{status}` | {count} |")
    lines.append(f"| **total** | **{sum(archive_tally.values())}** |")
    lines.append("")
    lines.append("## Action items")
    lines.append("")
    lines.append(f"### Primary URL broken AND archive missing / also broken — re-source ({len(cards_both_broken)})")
    if cards_both_broken:
        lines.append("")
        for cr in cards_both_broken:
            lines.append(f"- `{cr.card_id}`")
            lines.append(f"    - primary: {_format_check(cr.primary)}")
            lines.append(f"    - archive: {_format_check(cr.archive)}")
    else:
        lines.append("")
        lines.append("None.")
    lines.append("")
    lines.append(f"### Primary URL broken but archive OK — demote primary, keep archive ({len(cards_primary_broken_archive_ok)})")
    if cards_primary_broken_archive_ok:
        lines.append("")
        for cr in cards_primary_broken_archive_ok:
            lines.append(f"- `{cr.card_id}`")
            lines.append(f"    - primary: {_format_check(cr.primary)}")
            lines.append(f"    - archive: {_format_check(cr.archive)}")
    else:
        lines.append("")
        lines.append("None.")
    lines.append("")
    lines.append(f"### Pending other-checkpoint re-verification ({len(cards_gfw_pending)})")
    if cards_gfw_pending:
        lines.append("")
        lines.append("These URLs returned timeout/connection error from the principal-author-cn checkpoint; the domain is on the GFW-suspect list. Re-run `scripts/verify_card_urls.py` from a different network (or rely on the archive URL which generally remains reachable).")
        lines.append("")
        for cr in cards_gfw_pending:
            lines.append(f"- `{cr.card_id}`")
            if cr.primary and cr.primary.status == "pending-other-checkpoint":
                lines.append(f"    - primary: {_format_check(cr.primary)}")
            if cr.archive and cr.archive.status == "pending-other-checkpoint":
                lines.append(f"    - archive: {_format_check(cr.archive)}")
    else:
        lines.append("")
        lines.append("None.")
    lines.append("")
    lines.append("## Cards with no URL fields")
    lines.append("")
    if cards_no_url:
        for cid in cards_no_url:
            lines.append(f"- `{cid}`")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("## Handoff")
    lines.append("")
    lines.append("- stephen-fact-check-director — re-source any `Primary URL broken AND archive missing / also broken` items; trigger Wayback Save-Page-Now for any `Primary broken / archive OK` items where the primary is genuinely gone (so the archive captures the current state before further drift).")
    lines.append("- principal-author or any non-CN checkpoint — re-run `scripts/verify_card_urls.py` to close the `Pending other-checkpoint` list.")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nReport written: {report_path}", file=sys.stderr)
    print(f"Cards updated:  {updated}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
