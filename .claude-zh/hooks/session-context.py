#!/usr/bin/env python3
"""SessionStart hook：将项目的焦点快照注入为附加上下文。"""
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
            "无当前焦点文件。如需创建，使用 /crew-briefing。"
        )
    except OSError as exc:
        text = f"(session-context: 无法读取 {focus}: {exc})"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "项目焦点快照：\n" + text,
        }
    }))


if __name__ == "__main__":
    main()
