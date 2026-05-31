#!/usr/bin/env python3
"""SessionStart hook: inject the project's focus snapshot as additional context."""
import json
import sys
from pathlib import Path


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        data = {}
    cwd = Path(data.get("cwd") or ".")
    focus = cwd / ".claude" / "state" / "current-focus.md"
    try:
        text = focus.read_text(errors="ignore")[:4000] if focus.exists() else (
            "No current focus file exists. Use /crew-briefing to create one if needed."
        )
    except OSError as exc:
        text = f"(session-context: could not read {focus}: {exc})"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "Project focus snapshot:\n" + text,
        }
    }))


if __name__ == "__main__":
    main()
