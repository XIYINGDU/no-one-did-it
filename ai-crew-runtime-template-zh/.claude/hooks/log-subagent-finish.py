#!/usr/bin/env python3
"""SubagentStop hook：记录子 agent 完成情况以提供工作流可见性。

当任何子 agent 完成时触发。记录 agent 名称、工具调用次数和回合数。
提供工作流透明度，编排者无需轮询。
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

    agent_name = data.get("agent_name") or "未知"
    tool_calls = data.get("tool_calls") or 0
    turns = data.get("turns") or 0

    # 记录到项目级子 agent 日志
    project_dir = Path(data.get("project_dir") or Path.cwd())
    log_dir = project_dir / ".claude" / "state"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "subagent-finish.log"

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"{timestamp} | {agent_name:40s} | 工具: {tool_calls:3d} | 回合: {turns:3d}\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry)
    except OSError:
        sys.exit(0)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SubagentStop",
            "additionalContext": (
                f"子 agent {agent_name} 已完成 — "
                f"{tool_calls} 次工具调用，{turns} 回合。"
            ),
        }
    }))


if __name__ == "__main__":
    main()
