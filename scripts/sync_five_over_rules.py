#!/usr/bin/env python3
"""Generate and sync Global Five Over-Rules blocks across project files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = PROJECT_ROOT / ".claude" / "rules" / "00-five-values.md"
START_MARKER = "<!-- GENERATED:five-over-rules:start -->"
END_MARKER = "<!-- GENERATED:five-over-rules:end -->"
HEADING = "## Global Five Over-Rules"
RULE_LINE_RE = re.compile(r"^\d+\.\s")


def extract_canonical_rules(source_path: Path) -> list[str]:
    lines = source_path.read_text(encoding="utf-8").splitlines()
    rule_lines = [line for line in lines if RULE_LINE_RE.match(line)]
    if len(rule_lines) != 5:
        raise ValueError(f"Expected 5 rules in {source_path}, found {len(rule_lines)}")
    return rule_lines


def _iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    explicit = [root / "AGENTS.md", root / "README.md"]
    for path in explicit:
        if path.exists():
            files.append(path)

    for base in (root / ".claude" / "agents", root / ".claude" / "skills", root / ".claude" / "docs"):
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            files.append(path)
    return files


def find_targets(root: Path) -> list[Path]:
    targets: list[Path] = []
    for path in _iter_markdown_files(root):
        rel = path.relative_to(root).as_posix()
        if rel == ".claude/rules/00-five-values.md":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if f"\n{HEADING}\n" in f"\n{text}\n":
            targets.append(path)
    return sorted(targets)


def sync_one(path: Path, canonical_rules: list[str]) -> tuple[str, bool]:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    try:
        heading_idx = lines.index(HEADING)
    except ValueError as exc:
        raise ValueError(f"Heading not found in {path}") from exc

    start = heading_idx + 1
    while start < len(lines) and lines[start].strip() == "":
        start += 1

    end = start
    while end < len(lines):
        stripped = lines[end].strip()
        if stripped in {START_MARKER, END_MARKER} or RULE_LINE_RE.match(stripped) or stripped == "":
            end += 1
            continue
        break

    replacement = ["", START_MARKER, *canonical_rules, END_MARKER, ""]
    new_lines = lines[: heading_idx + 1] + replacement + lines[end:]
    updated = "\n".join(new_lines)
    if original.endswith("\n"):
        updated += "\n"

    return updated, updated != original


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Global Five Over-Rules blocks")
    parser.add_argument("--check", action="store_true", help="Check for drift without writing")
    args = parser.parse_args()

    canonical_rules = extract_canonical_rules(SOURCE_FILE)
    targets = find_targets(PROJECT_ROOT)

    changed: list[str] = []
    for path in targets:
        updated, is_changed = sync_one(path, canonical_rules)
        if is_changed:
            changed.append(path.relative_to(PROJECT_ROOT).as_posix())
            if not args.check:
                path.write_text(updated, encoding="utf-8")

    if args.check and changed:
        print("Five Over-Rules drift detected:")
        for rel in changed:
            print(f"- {rel}")
        return 1

    if args.check:
        print(f"Five Over-Rules sync check passed ({len(targets)} targets).")
    else:
        print(f"Five Over-Rules synced: {len(changed)} changed / {len(targets)} targets.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
