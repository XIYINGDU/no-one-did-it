#!/usr/bin/env python3
"""Sync the Global Five Over-Rules from the single source to all targets.

Reads ``rules/00-core-values.md`` as the canonical source. Extracts the
five-over-rules block between ``<!-- GENERATED:five-over-rules:manifest start -->``
and ``<!-- GENERATED:five-over-rules:manifest end -->``. Finds every file
under ``.claude/`` carrying ``<!-- GENERATED:five-over-rules:start -->``
markers and replaces the content between the markers.

Usage:
    python3 scripts/sync_core_values.py          # sync all targets
    python3 scripts/sync_core_values.py --check  # verify consistency, exit non-zero on drift
"""

import argparse
import re
import sys
from pathlib import Path


MANIFEST_START = "<!-- GENERATED:five-over-rules:manifest start -->"
MANIFEST_END = "<!-- GENERATED:five-over-rules:manifest end -->"
TARGET_START = "<!-- GENERATED:five-over-rules:start -->"
TARGET_END = "<!-- GENERATED:five-over-rules:end -->"


def extract_source_block(text: str) -> str:
    """Extract the five-over-rules block from the manifest source."""
    m = re.search(
        re.escape(MANIFEST_START) + r"\n(.*?)\n" + re.escape(MANIFEST_END),
        text,
        re.DOTALL,
    )
    if not m:
        print("ERROR: Could not find manifest block in rules/00-core-values.md", file=sys.stderr)
        sys.exit(1)
    return m.group(1)


def find_target_files(root: Path) -> list[Path]:
    """Find all files under .claude/ carrying the target start marker."""
    targets = []
    claude_dir = root / ".claude"
    if not claude_dir.is_dir():
        print(f"ERROR: .claude/ directory not found at {root}", file=sys.stderr)
        sys.exit(1)

    for path in claude_dir.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if TARGET_START in text:
            targets.append(path)
    return targets


def sync_target(path: Path, new_block: str, check_only: bool = False) -> bool:
    """Replace the five-over-rules block in a target file. Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    pattern = re.escape(TARGET_START) + r"\n.*?\n" + re.escape(TARGET_END)
    new_text = TARGET_START + "\n" + new_block + "\n" + TARGET_END
    updated = re.sub(pattern, new_text, text, flags=re.DOTALL)

    if updated == text:
        return False

    if check_only:
        return True  # drift detected

    path.write_text(updated, encoding="utf-8")
    print(f"  Synced: {path.relative_to(path.parents[2])}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync five over-rules across all targets")
    parser.add_argument("--check", action="store_true", help="Verify consistency; exit non-zero on drift")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    source_path = root / ".claude" / "rules" / "00-core-values.md"
    if not source_path.exists():
        print(f"ERROR: Source file not found at {source_path}", file=sys.stderr)
        sys.exit(1)

    source_text = source_path.read_text(encoding="utf-8")
    block = extract_source_block(source_text)
    targets = find_target_files(root)

    if not targets:
        print("No target files found with five-over-rules markers.")
        sys.exit(0)

    drift_count = 0
    for path in sorted(targets):
        changed = sync_target(path, block, check_only=args.check)
        if changed:
            drift_count += 1

    if args.check:
        if drift_count > 0:
            print(f"\nFAIL: {drift_count} target(s) drifted from the source. Run without --check to sync.", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"OK: All {len(targets)} target(s) match the source.")
    else:
        if drift_count > 0:
            print(f"\nSynced {drift_count} target(s). {len(targets) - drift_count} were already current.")
        else:
            print(f"All {len(targets)} target(s) already current.")


if __name__ == "__main__":
    main()
