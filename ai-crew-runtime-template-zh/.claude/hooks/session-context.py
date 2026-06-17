#!/usr/bin/env python3
"""SessionStart hook：将 state/current-focus.md 注入为 additionalContext。

在会话启动、恢复、清除和压缩事件时触发。
读取当前焦点文件并发出，使模型看到 sprint 状态而不消耗一个回合手动读取。
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
            "additionalContext": f"项目焦点快照：\n{context}",
        }
    }))


if __name__ == "__main__":
    main()
