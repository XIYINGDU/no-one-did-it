#!/usr/bin/env python3
"""Reader-report gate: verify v3 chapters have current cold-reads with no
unresolved HARD findings.

Per rule 15-reader-experience-authority.md, a v3 chapter's publication
form is not promotion-ready while it carries an unresolved HARD finding
from `the-reader`. This script is the deterministic enforcement.

For each chapter in book/chapters-v6/:
  - Find the most recent reader-report in process/reader-reports/ matching
    `<n>-<slug>-*.md` (or `<n>-<slug>.md`).
  - Parse its `## Verdict` line:
      CLEAN              → chapter clear
      BLOCKED — N HARD   → chapter blocked (unresolved HARD findings)
  - No report           → cold-read owed (advisory by default).

Modes:
  default (advisory) — print status; exit 0 even if reports are missing.
                       Used in routine CI / build: v3 can build and tests
                       can pass before the reader has run.
  --gate             — exit 1 if any chapter is BLOCKED or has no report.
                       Used at publication-readiness, not routine build.

The split matches the workflow: building v3 and passing tests does not
require the cold-read; declaring v3 *publication-ready* does.

Usage:
  python3 scripts/check_reader_reports.py             # advisory
  python3 scripts/check_reader_reports.py --gate       # publication gate
  python3 scripts/check_reader_reports.py --sweep      # also require a
                                                       # current book-level sweep
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERDICT_RE = re.compile(r"^##\s*Verdict\s*$", re.MULTILINE | re.IGNORECASE)
# Match a CLEAN or BLOCKED token in the verdict block (next non-blank line).
CLEAN_RE = re.compile(r"\bCLEAN\b", re.IGNORECASE)
BLOCKED_RE = re.compile(r"\bBLOCKED\b", re.IGNORECASE)
# A recorded override per rule 15: the literal token OVERRIDE plus an
# attribution to the sole override authority (xaiolai / xiaolai — both
# spellings appear in the corpus). A BLOCKED chapter carrying a recorded
# override does not block the gate, but is reported distinctly from CLEAN
# so its retirement condition stays visible. Requiring the attribution
# keeps the override from being a casual bypass.
OVERRIDE_RE = re.compile(r"\bOVERRIDE\b", re.IGNORECASE)
OVERRIDE_AUTH_RE = re.compile(r"\bx(?:ai|ia)olai\b", re.IGNORECASE)


def chapter_slug(path: Path) -> str:
    """`07-the-record-is-the-battlefield.md` → `07-the-record-is-the-battlefield`."""
    return path.stem


def find_latest_report(reports_dir: Path, slug: str) -> Path | None:
    """Most recent `<slug>-<date>.md` or `<slug>.md` report for a chapter."""
    candidates = sorted(reports_dir.glob(f"{slug}-*.md"))
    candidates += sorted(reports_dir.glob(f"{slug}.md"))
    if not candidates:
        return None
    # Sort by filename (date suffix sorts lexicographically) then mtime.
    candidates.sort(key=lambda p: (p.name, p.stat().st_mtime))
    return candidates[-1]


def read_verdict(report_path: Path) -> str:
    """Return 'CLEAN' | 'OVERRIDE' | 'BLOCKED' | 'UNKNOWN' from the Verdict block.

    A recorded xaiolai override on a BLOCKED chapter wins over the BLOCKED
    token: the HARD finding stands (the reader is never wrong about its own
    experience), but xaiolai has recorded a decision to proceed past the gate.
    The override must carry both the OVERRIDE token and the xaiolai attribution.
    """
    text = report_path.read_text(encoding="utf-8")
    m = VERDICT_RE.search(text)
    if not m:
        # Fallback: scan the whole document for a clear signal.
        body = text
    else:
        body = text[m.end():m.end() + 300]
    if OVERRIDE_RE.search(body) and OVERRIDE_AUTH_RE.search(body):
        return "OVERRIDE"
    if BLOCKED_RE.search(body):
        return "BLOCKED"
    if CLEAN_RE.search(body):
        return "CLEAN"
    return "UNKNOWN"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__ or "")
    p.add_argument("--project-root", type=Path, default=Path("."))
    p.add_argument("--gate", action="store_true",
                   help="Fail (exit 1) if any chapter is BLOCKED or unread")
    p.add_argument("--sweep", action="store_true",
                   help="Also require a current book-level sweep report")
    args = p.parse_args(argv)

    root: Path = args.project_root
    chapters_dir = root / "book" / "chapters-v6"
    reports_dir = root / "process" / "reader-reports"

    if not chapters_dir.is_dir():
        print(f"note: {chapters_dir} not built; nothing to check.")
        return 0
    reports_dir.mkdir(parents=True, exist_ok=True)

    chapters = sorted(p for p in chapters_dir.glob("[0-9]*.md")
                      if not p.name.endswith(".meta.yml"))

    clean: list[str] = []
    overridden: list[str] = []
    blocked: list[str] = []
    unread: list[str] = []
    unknown: list[str] = []

    for chap in chapters:
        slug = chapter_slug(chap)
        report = find_latest_report(reports_dir, slug)
        if report is None:
            unread.append(slug)
            continue
        verdict = read_verdict(report)
        if verdict == "CLEAN":
            clean.append(slug)
        elif verdict == "OVERRIDE":
            overridden.append(f"{slug}  (report: {report.name})")
        elif verdict == "BLOCKED":
            blocked.append(f"{slug}  (report: {report.name})")
        else:
            unknown.append(f"{slug}  (report: {report.name})")

    # Book-level sweep.
    sweep_reports = sorted(reports_dir.glob("sweep-*.md"))
    sweep_verdict = read_verdict(sweep_reports[-1]) if sweep_reports else None

    print("\n=== reader-report gate ===")
    print(f"Chapters:              {len(chapters)}")
    print(f"  CLEAN cold-read:     {len(clean)}")
    print(f"  OVERRIDE (xaiolai):  {len(overridden)}")
    print(f"  BLOCKED (HARD):      {len(blocked)}")
    print(f"  not yet cold-read:   {len(unread)}")
    print(f"  verdict unknown:     {len(unknown)}")
    if args.sweep or sweep_reports:
        print(f"Book sweep:            {sweep_verdict or 'none yet'}")

    if overridden:
        print(f"\n--- OVERRIDDEN chapters (xaiolai-recorded; non-blocking, retirement owed) ---")
        for o in overridden:
            print(f"  {o}")
    if blocked:
        print(f"\n--- BLOCKED chapters (unresolved HARD findings) ---")
        for b in blocked:
            print(f"  {b}")
    if unread:
        print(f"\n--- chapters owed a cold-read ---")
        for u in unread:
            print(f"  {u}")
    if unknown:
        print(f"\n--- reports with unparseable verdict ---")
        for u in unknown:
            print(f"  {u}")

    if not args.gate:
        print("\n(advisory mode — exit 0 regardless; use --gate at publication-readiness)")
        return 0

    # Gate mode.
    fail = bool(blocked) or bool(unread) or bool(unknown)
    if args.sweep and sweep_verdict != "CLEAN":
        print(f"\nGATE FAIL: book-level sweep is {sweep_verdict or 'missing'}, not CLEAN")
        fail = True
    if fail:
        print("\nGATE FAIL: v3 is not publication-ready — resolve blocked/unread chapters "
              "(fix in v2, rebuild, re-read) or record an xaiolai override.")
        return 1
    if overridden:
        print("\nGATE PASS: every v3 chapter is CLEAN or carries a recorded xaiolai override.")
        print(f"  note: {len(overridden)} override(s) still owe retirement "
              "(fix in v2, rebuild, re-read to true CLEAN before final publication).")
        return 0
    print("\nGATE PASS: every v3 chapter has a CLEAN cold-read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
