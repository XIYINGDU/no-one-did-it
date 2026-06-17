#!/usr/bin/env python3
"""PostToolUse warn-mode hook: generic deliverable quality scanner.

Triggered on writes/edits to the project's deliverable paths (configured
in DELIVERABLE_SCOPE below). Implements the quality-standards rule by
scanning for common quality issues:

1. Missing required schema fields (Owner, Evidence grade, Handoff)
2. Unresolved placeholder markers (TODO, FIXME without owner)
3. Banned hedge-replacement words that signal weak claims

The hook is **warn-only**. It never returns ``permissionDecision: deny`` —
the promotion gate in the Orchestrator's quality-gate pass is the only
deny path. This hook is the cheap pattern-level scan; the quality-gate
skill is the deep read.

Customize PATTERNS and SCOPE_RE for your project's domain.
"""

import json
import re
import sys
from pathlib import Path


# ============================================================
# CONFIGURABLE — adjust to your project
# ============================================================

# Which files to scan (project-relative regex)
SCOPE_RE = re.compile(
    r"^(outputs|deliverables|chapters|src)/.*\.(md|py|js|ts|rs|go)$"
)

# Required schema fields every deliverable should carry
REQUIRED_FIELDS = [
    "Owner:",
    "Handoff:",
]

# Placeholder patterns that should not survive to ready
PLACEHOLDER_PATTERNS = [
    (re.compile(r"\[TODO\]", re.IGNORECASE), "TODO — unresolved"),
    (re.compile(r"\[FIXME\]", re.IGNORECASE), "FIXME — unresolved"),
    (re.compile(r"\[PLACEHOLDER\]", re.IGNORECASE), "PLACEHOLDER — unresolved"),
]

# Banned hedge-replacement words (project-agnostic)
BANNED_ADVERBS = [
    (re.compile(r"\b(clearly|obviously|undeniably)\b", re.IGNORECASE),
     "clearly/obviously/undeniably",
     "Cite the source that makes it clear; let the reader judge."),
    (re.compile(r"\b(must have|would have)\b", re.IGNORECASE),
     "must have / would have",
     "Use only documented facts, not speculation about what must have happened."),
]


def _project_relative(path: Path) -> str | None:
    """Return path relative to project root, or None if outside project."""
    project_root = Path(__file__).resolve().parents[2]
    try:
        return path.resolve().relative_to(project_root).as_posix()
    except ValueError:
        return None


def scan(text: str) -> list[str]:
    """Return a list of warning messages for the given file content."""
    warnings: list[str] = []

    # Check for required schema fields
    for field in REQUIRED_FIELDS:
        if field not in text:
            warnings.append(f"Missing required schema field: '{field}'")

    # Check for placeholder markers
    for pattern, label in PLACEHOLDER_PATTERNS:
        matches = pattern.findall(text)
        if matches:
            warnings.append(f"Found {len(matches)} unresolved {label} marker(s)")

    # Check for banned adverbs
    for pattern, word, suggestion in BANNED_ADVERBS:
        if pattern.search(text):
            warnings.append(f"Banned hedge-replacement: '{word}' — {suggestion}")

    return warnings


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    inp = data.get("tool_input") or {}

    # Extract file path from tool input
    path_str = ""
    for key in ("file_path", "path"):
        value = inp.get(key)
        if isinstance(value, str) and value:
            path_str = value
            break
    if not path_str:
        sys.exit(0)

    path = Path(path_str)
    if not path.is_absolute():
        path = Path(data.get("cwd") or ".") / path

    if not path.exists():
        sys.exit(0)

    rel = _project_relative(path)
    if not rel:
        sys.exit(0)

    if not SCOPE_RE.match(rel):
        sys.exit(0)

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        sys.exit(0)

    warnings = scan(text)

    if not warnings:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Warn mode: check-deliverable passed for {rel}.",
            }
        }))
        return

    lines = [f"Warn mode: check-deliverable flagged {len(warnings)} issue(s) in {rel}:"]
    for w in warnings:
        lines.append(f"  • {w}")

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": " ".join(lines),
        }
    }))


if __name__ == "__main__":
    main()
