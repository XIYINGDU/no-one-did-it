#!/usr/bin/env python3
"""
triage_verify_log.py — Analyze verify_card_links.py output to identify what needs follow-up.

Reads book/evidence/source-ledger/.verify-log.json and reports:
  - Overall HEAD status distribution
  - Wayback coverage: existing snapshots vs newly saved vs blocked
  - sha256 fingerprint count
  - Dead-link list grouped by domain
  - Cards that need re-research (4xx/5xx with no Wayback fallback)
  - Cards Wayback can't archive (blocked by origin)

Usage:
  python3 scripts/triage_verify_log.py [--by-domain] [--dead-only]
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / ".verify-log.json"


def load_log() -> dict:
    if not LOG_PATH.exists():
        print(f"FATAL: verify log not found at {LOG_PATH}", file=sys.stderr)
        sys.exit(1)
    return json.loads(LOG_PATH.read_text(encoding="utf-8"))


def domain_of(url: str) -> str:
    try:
        return urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
    except Exception:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--by-domain", action="store_true", help="Group results by source domain.")
    parser.add_argument("--dead-only", action="store_true", help="Show only dead URLs (HEAD 4xx/5xx, no Wayback).")
    args = parser.parse_args()

    log = load_log()

    head_status = defaultdict(int)
    sha256_count = 0
    wb_existing = 0
    wb_saved = 0
    wb_blocked = 0
    wb_missing = 0
    skipped = 0

    dead_links = []  # cards with HEAD 4xx/5xx AND no Wayback fallback
    wayback_blocked = []  # cards Wayback can't archive
    needs_save_retry = []  # cards we couldn't save but could later
    domain_stats = defaultdict(lambda: {"total": 0, "alive": 0, "dead": 0, "wb_existing": 0, "wb_saved": 0})

    for slug, entry in log.items():
        if entry.get("skipped"):
            skipped += 1
            continue

        url = entry.get("url", "")
        domain = domain_of(url)

        # HEAD status
        hs = entry.get("head_status")
        if hs is None:
            head_status["network_error"] += 1
        else:
            bucket = f"{hs // 100}xx"
            head_status[bucket] += 1
            head_status[str(hs)] += 1

        domain_stats[domain]["total"] += 1
        alive = hs is not None and 200 <= hs < 400
        if alive:
            domain_stats[domain]["alive"] += 1
        else:
            domain_stats[domain]["dead"] += 1

        # sha256
        if entry.get("body_sha256"):
            sha256_count += 1

        # Wayback
        has_wb = bool(entry.get("wayback_url"))
        if has_wb:
            if entry.get("wayback_existing"):
                wb_existing += 1
                domain_stats[domain]["wb_existing"] += 1
            elif entry.get("wayback_saved"):
                wb_saved += 1
                domain_stats[domain]["wb_saved"] += 1
        else:
            if entry.get("wayback_save_failed"):
                wb_blocked += 1
                wayback_blocked.append((slug, url, domain, hs))
            else:
                wb_missing += 1
                needs_save_retry.append((slug, url, domain))

        # Dead link = HEAD 4xx/5xx AND no Wayback
        if not alive and not has_wb:
            dead_links.append((slug, url, domain, hs))

    total = len(log) - skipped

    print("=" * 70)
    print("VERIFY LOG TRIAGE")
    print("=" * 70)
    print(f"Total cards in log : {len(log)}")
    print(f"Skipped (no URL)   : {skipped}")
    print(f"Processed          : {total}")
    print()
    print("HEAD status distribution:")
    for k in sorted(head_status.keys()):
        print(f"  {k:20s} {head_status[k]}")
    print()
    print(f"sha256 fingerprints captured: {sha256_count} / {total} ({100*sha256_count//max(1,total)}%)")
    print()
    print("Wayback coverage:")
    print(f"  existing snapshot : {wb_existing} ({100*wb_existing//max(1,total)}%)")
    print(f"  newly saved       : {wb_saved} ({100*wb_saved//max(1,total)}%)")
    print(f"  blocked by origin : {wb_blocked} ({100*wb_blocked//max(1,total)}%)")
    print(f"  no save attempted : {wb_missing}")
    total_wb = wb_existing + wb_saved
    print(f"  TOTAL WITH REAL SNAPSHOT: {total_wb} / {total} ({100*total_wb//max(1,total)}%)")
    print()
    print(f"Dead links (HEAD 4xx/5xx + no Wayback): {len(dead_links)}")
    if dead_links and not args.dead_only:
        print("  Sample (up to 10):")
        for slug, url, dom, hs in dead_links[:10]:
            print(f"    [{hs}] {slug} → {url}")
    elif args.dead_only:
        for slug, url, dom, hs in dead_links:
            print(f"  [{hs}] {slug} → {url}")
    print()
    print(f"Wayback-blocked cards (origin refused crawler): {len(wayback_blocked)}")
    if wayback_blocked and not args.dead_only:
        wb_by_domain = defaultdict(int)
        for slug, url, dom, hs in wayback_blocked:
            wb_by_domain[dom] += 1
        for dom, n in sorted(wb_by_domain.items(), key=lambda x: -x[1])[:10]:
            print(f"  {n:3d}  {dom}")

    if args.by_domain:
        print()
        print("Per-domain stats (top 30 by total):")
        rows = sorted(domain_stats.items(), key=lambda kv: -kv[1]["total"])[:30]
        print(f"  {'domain':40s} {'total':>6s} {'alive':>6s} {'dead':>6s} {'wb_old':>7s} {'wb_new':>7s}")
        for dom, st in rows:
            print(f"  {dom[:40]:40s} {st['total']:>6d} {st['alive']:>6d} {st['dead']:>6d} {st['wb_existing']:>7d} {st['wb_saved']:>7d}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
