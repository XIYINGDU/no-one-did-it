#!/usr/bin/env python3
"""PostToolUse hook: frontmatter + operating-contract validation.

Default mode is warn-only. A narrow deny path exists for chapter promotion:
deny whenever a chapter file persists with ``status: ready`` AND any chapter
rhythm section is missing. The deny is evaluated against the **final state of
the file on disk after the tool call**, not by diffing Edit/MultiEdit text —
that means Write-tool replacements, MultiEdit, and Edit are all covered
uniformly. The previous diff-based check was bypassable with the Write tool.
"""

import json
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.operating_validators import (  # noqa: E402
    extract_chapter_status,
    validate_file,
)


REQUIRED_FIELDS = ("name:", "description:")
SLUG_RE = re.compile(r"^[a-z0-9-]+$")
VALIDATION_TARGET_RE = re.compile(
    r"^(book/(case-files|chapters-v\d+|review-memos)/(?!README\.md$)|\.claude/agents/|\.claude/skills/)"
)
CHAPTER_PATH_RE = re.compile(r"^book/chapters-v\d+/(?!README\.md$)")


def _frontmatter_issues(path: str, text: str) -> list[str]:
    issues: list[str] = []
    if not text.startswith("---\n"):
        issues.append("missing YAML frontmatter opening line")
        fm = ""
    else:
        parts = text.split("---", 2)
        if len(parts) < 3:
            issues.append("missing YAML frontmatter closing line")
            fm = ""
        else:
            fm = parts[1]

    for field in REQUIRED_FIELDS:
        if field not in fm:
            issues.append(f"missing {field}")

    name_match = re.search(r"^name:\s*([^\n]+)", fm, re.M)
    if name_match and not SLUG_RE.match(name_match.group(1).strip()):
        issues.append("name must use lowercase letters, digits, and hyphens only")
    return issues


def _extract_path(tool_input: dict) -> str:
    for key in ("file_path", "path"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def _deny(reason: str, warn_context: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                    "additionalContext": "Warn mode: " + warn_context if warn_context else reason,
                }
            }
        )
    )


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    inp = data.get("tool_input") or {}
    raw_path = _extract_path(inp)
    if not raw_path:
        sys.exit(0)

    path = Path(raw_path)
    if not path.is_absolute():
        path = Path(data.get("cwd") or ".") / path

    if not path.exists():
        sys.exit(0)

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": (
                            f"Warn mode: could not read edited file {path.as_posix()}: {exc}"
                        ),
                    }
                }
            )
        )
        sys.exit(0)

    messages: list[str] = []
    resolved = path.resolve()
    try:
        rel_path = resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        rel_path = resolved.as_posix()

    if rel_path.startswith(".claude/agents/") and rel_path.endswith(".md"):
        fm_issues = _frontmatter_issues(rel_path, text)
        if fm_issues:
            messages.append(
                f"Agent frontmatter issue in {rel_path}: {'; '.join(fm_issues)}"
            )

    is_chapter_file = bool(CHAPTER_PATH_RE.match(rel_path))
    if VALIDATION_TARGET_RE.match(rel_path):
        report = validate_file(path)
        if report.passed:
            messages.append(f"Operating validator passed for {rel_path}.")
        else:
            issues = "; ".join(issue.message for issue in report.issues)
            messages.append(f"Operating validator warnings for {rel_path}: {issues}")
            if is_chapter_file:
                has_rhythm_gap = any(
                    issue.code == "chapter.rhythm.missing_section"
                    for issue in report.issues
                )
                # Deny by *final state*: a chapter that persists with
                # `status: ready` and missing rhythm sections is invalid no
                # matter how it got there (Edit, MultiEdit, or Write).
                if has_rhythm_gap and extract_chapter_status(text) == "ready":
                    reason = (
                        "Chapter promotion gate: a chapter with `status: ready` "
                        "must contain all 8 rhythm sections as `## Heading` or "
                        "`<section name>:` markers at the start of a line. "
                        "Either restore the missing sections or move `status:` "
                        "back to `draft`."
                    )
                    _deny(reason, " ".join(messages))
                    sys.exit(0)

    if not messages:
        sys.exit(0)

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": "Warn mode: " + " ".join(messages),
                }
            }
        )
    )


if __name__ == "__main__":
    main()
