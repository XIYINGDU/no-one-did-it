#!/usr/bin/env python3
"""PreToolUse hook: deny obviously destructive shell commands."""
import json
import re
import sys


PATTERNS = [
    # destructive recursive deletes targeting volatile roots
    r"\brm\s+-rf\s+(/|\.|~|\$HOME|\*)",
    # repository-state destruction
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-fdx\b",
    # over-permissive recursive perms
    r"\bchmod\s+-R\s+777\b",
    # network-piped shell execution
    r"\bcurl\b.*\|\s*(sh|bash)\b",
    r"\bwget\b.*\|\s*(sh|bash)\b",
]


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        data = {}
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    blocked = any(re.search(p, cmd) for p in PATTERNS)
    decision = "deny" if blocked else "allow"
    reason = (
        "Destructive shell command blocked by project guard. Ask the user and narrow the command."
        if blocked
        else "Command passed destructive-command guard."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }))


if __name__ == "__main__":
    main()
