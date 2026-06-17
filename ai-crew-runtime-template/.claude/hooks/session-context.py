#!/usr/bin/env python3
"""SessionStart hook: inject `state/current-focus.md` as additionalContext.

Triggered on session startup, resume, clear, and compact events.
Reads the current-focus file and emits it so the model sees sprint
state without consuming a turn to read it manually.
"""

import json
import sys
from pathlib import Path


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    project_dir = Path(data.get("project_dir") or Path.cwd())
    focus_file = project_dir / ".claude" / "state" / "current-focus.md"

    if not focus_file.exists():
        sys.exit(0)

    try:
        context = focus_file.read_text(encoding="utf-8", errors="ignore").strip()
    except OSError:
        sys.exit(0)

    if not context:
        sys.exit(0)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": f"Project focus snapshot:\n{context}",
        }
    }))


if __name__ == "__main__":
    main()
