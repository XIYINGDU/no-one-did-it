#!/usr/bin/env python3
"""
triage_content_audit.py — bucket the content-audit.json into actionable repair queues.

Reads book/evidence/source-ledger/.content-audit.json (output of audit_card_content.py) and
writes book/evidence/source-ledger/.content-audit-triage.md — a sorted, grouped action list.

Buckets:
  1. CONFIRMED MISMATCH (sim == 0)            — URL serves an entirely different document.
  2. STRONG MISMATCH    (0 < sim < 0.20)      — major divergence; almost certainly wrong document.
  3. WEAK MISMATCH      (0.20 ≤ sim < 0.40)   — partial overlap; needs eyes.
  4. LANDING-PAGE SUSPECT                     — URL host is amazon/books.google/sciencedirect
                                                  but card claims fine-grained content (entry/page).
  5. FETCH FAILED                             — both live and Wayback failed; needs new URL.

Each bucket lists slug, card_title (truncated), card_url, extracted_title.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AUDIT_PATH = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / ".content-audit.json"
OUT_PATH = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / ".content-audit-triage.md"

LANDING_HOSTS = {
    "amazon.com", "www.amazon.com", "smile.amazon.com",
    "books.google.com", "books.google.co.uk",
    "sciencedirect.com", "www.sciencedirect.com",
    "jstor.org", "www.jstor.org",
    "springer.com", "link.springer.com",
    "muse.jhu.edu", "wiley.com", "onlinelibrary.wiley.com",
    "play.google.com",
}

# Card-title fragments that indicate fine-grained content within a larger work
FINE_GRAINED = re.compile(
    r"\b(entry|chapter|section|page|table|figure|appendix|article|essay|vol\.?\s*\d|volume\s*\d)\b",
    re.I,
)


def host_of(url: str) -> str:
    try:
        return urllib.parse.urlparse(url).hostname or ""
    except Exception:
        return ""


def is_landing_page_suspect(rec: dict) -> bool:
    host = host_of(rec.get("card_url", "")).lower()
    if host not in LANDING_HOSTS:
        return False
    title = rec.get("card_title", "")
    return bool(FINE_GRAINED.search(title))


def main() -> int:
    if not AUDIT_PATH.exists():
        print(f"missing: {AUDIT_PATH}", file=sys.stderr)
        return 1
    records = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))

    buckets: dict[str, list[dict]] = {
        "confirmed_mismatch": [],
        "strong_mismatch": [],
        "weak_mismatch": [],
        "landing_page_suspect": [],
        "fetch_failed": [],
    }
    ok_count = 0
    skipped_count = 0

    for r in records:
        if r.get("error") or r.get("skipped"):
            skipped_count += 1
            continue
        flag = r.get("flag", "")
        sim = r.get("similarity", 0.0)
        if flag == "fetch-failed":
            buckets["fetch_failed"].append(r)
        elif flag == "MISMATCH-strong":
            if sim == 0.0:
                buckets["confirmed_mismatch"].append(r)
            else:
                buckets["strong_mismatch"].append(r)
        elif flag == "MISMATCH-weak":
            buckets["weak_mismatch"].append(r)
        elif flag == "ok" and is_landing_page_suspect(r):
            buckets["landing_page_suspect"].append(r)
        elif flag == "ok":
            ok_count += 1
        elif flag == "unknown-content":
            buckets["fetch_failed"].append(r)

    def emit_bucket(name: str, label: str, recs: list[dict]) -> list[str]:
        lines = [f"## {label} ({len(recs)})", ""]
        if not recs:
            lines.append("_None._\n")
            return lines
        # Sort by ascending similarity, then slug
        recs_sorted = sorted(recs, key=lambda r: (r.get("similarity", 0.0), r.get("slug", "")))
        for r in recs_sorted:
            slug = r.get("slug", "")
            sim = r.get("similarity", "-")
            via = r.get("used", "?")
            url = r.get("card_url", "")
            page = r.get("extracted_title") or r.get("extracted_first") or "(empty)"
            card = r.get("card_title", "")
            lines.append(f"### `{slug}`")
            lines.append(f"- **sim={sim}** via {via}")
            lines.append(f"- **card claim:** {card[:160]}")
            lines.append(f"- **card URL:** `{url}`")
            lines.append(f"- **page identity:** {page[:160]}")
            if r.get("fetch_error"):
                lines.append(f"- **fetch error:** {r['fetch_error']}")
            lines.append("")
        return lines

    out = [
        "# Content-Audit Triage",
        "",
        f"Total records analyzed: **{len(records)}**",
        f"- OK (no defect surfaced): {ok_count}",
        f"- Skipped (no URL or template URL): {skipped_count}",
        f"- Confirmed mismatch (sim=0): **{len(buckets['confirmed_mismatch'])}**",
        f"- Strong mismatch (0<sim<0.20): **{len(buckets['strong_mismatch'])}**",
        f"- Weak mismatch (0.20≤sim<0.40): **{len(buckets['weak_mismatch'])}**",
        f"- Landing-page suspect (host=amazon/jstor/books.google + fine-grained claim): **{len(buckets['landing_page_suspect'])}**",
        f"- Fetch failed (live + Wayback unreachable): **{len(buckets['fetch_failed'])}**",
        "",
        "## Repair priority",
        "1. CONFIRMED + STRONG MISMATCH — re-research correct URL or downgrade card.",
        "2. FETCH FAILED — find a reachable mirror or downgrade.",
        "3. LANDING-PAGE SUSPECT — replace landing-page URL with the specific entry/page/section, or downgrade.",
        "4. WEAK MISMATCH — manual review; some are real near-matches (e.g. partial title overlap).",
        "",
    ]
    out += emit_bucket("confirmed", "Confirmed mismatch (sim=0)", buckets["confirmed_mismatch"])
    out += emit_bucket("strong", "Strong mismatch (0 < sim < 0.20)", buckets["strong_mismatch"])
    out += emit_bucket("fetch", "Fetch failed", buckets["fetch_failed"])
    out += emit_bucket("landing", "Landing-page suspect", buckets["landing_page_suspect"])
    out += emit_bucket("weak", "Weak mismatch (0.20 ≤ sim < 0.40)", buckets["weak_mismatch"])

    OUT_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")
    print()
    print(f"Confirmed:  {len(buckets['confirmed_mismatch']):>3}")
    print(f"Strong:     {len(buckets['strong_mismatch']):>3}")
    print(f"Fetch fail: {len(buckets['fetch_failed']):>3}")
    print(f"Landing:    {len(buckets['landing_page_suspect']):>3}")
    print(f"Weak:       {len(buckets['weak_mismatch']):>3}")
    print(f"OK:         {ok_count:>3}")
    print(f"Skipped:    {skipped_count:>3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
