#!/usr/bin/env python3
"""PreToolUse warn-mode hook: guard destructive bash commands.

Triggered before every Bash invocation. Warns when the command contains
destructive patterns (rm -rf, git push --force, etc.) so the human can
confirm before execution.
"""

import json
import re
import sys


DESTRUCTIVE_PATTERNS = [
    (re.compile(r"\brm\s+-rf\b"), "rm -rf"),
    (re.compile(r"\bgit\s+push\s+.*--force"), "git push --force"),
    (re.compile(r"\bgit\s+push\s+.*--delete"), "git push --delete"),
    (re.compile(r"\bgit\s+reset\s+--hard\b"), "git reset --hard"),
    (re.compile(r"\bgit\s+clean\s+-[a-z]*f"), "git clean -f"),
    (re.compile(r"\bdrop\s+table\b", re.IGNORECASE), "DROP TABLE — destructive SQL"),
    (re.compile(r"\bdelete\s+from\b", re.IGNORECASE), "DELETE FROM — destructive SQL"),
    (re.compile(r"\bshutdown\b", re.IGNORECASE), "shutdown"),
    (re.compile(r"\breboot\b", re.IGNORECASE), "reboot"),
    (re.compile(r"\bchmod\s+777\b"), "chmod 777 — world-writable permissions"),
    (re.compile(r">\s*/dev/[a-z]+"), "redirect to device file"),
]


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    tool_input = data.get("tool_input") or {}
    command = tool_input.get("command") or ""
    if not command:
        sys.exit(0)

    # Only guard bare commands; sandbox mode doesn't need this guard.
    if tool_input.get("dangerouslyDisableSandbox"):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": (
                    "⚠️  sandbox DISABLED for this command. "
                    "The destructive-bash guard is advisory in no-sandbox mode."
                ),
            }
        }))
        sys.exit(0)

    matches = []
    for pattern, label in DESTRUCTIVE_PATTERNS:
        if pattern.search(command):
            matches.append(label)

    if matches:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": (
                    f"⚠️  Destructive-bash guard: command matched {matches}. "
                    "Confirm intent before executing."
                ),
            }
        }))


if __name__ == "__main__":
    main()
