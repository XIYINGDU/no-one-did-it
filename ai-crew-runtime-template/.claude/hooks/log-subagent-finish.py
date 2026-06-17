#!/usr/bin/env python3
"""SubagentStop hook: log subagent completions for workflow visibility.

Triggered when any subagent finishes. Logs the agent name, tool calls made,
and turn count. Provides workflow transparency without requiring the
Orchestrator to poll.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    agent_name = data.get("agent_name") or "unknown"
    tool_calls = data.get("tool_calls") or 0
    turns = data.get("turns") or 0

    # Log to project-level subagent log
    project_dir = Path(data.get("project_dir") or Path.cwd())
    log_dir = project_dir / ".claude" / "state"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "subagent-finish.log"

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"{timestamp} | {agent_name:40s} | tools: {tool_calls:3d} | turns: {turns:3d}\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry)
    except OSError:
        sys.exit(0)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SubagentStop",
            "additionalContext": (
                f"Subagent {agent_name} finished — "
                f"{tool_calls} tool calls, {turns} turns."
            ),
        }
    }))


if __name__ == "__main__":
    main()
