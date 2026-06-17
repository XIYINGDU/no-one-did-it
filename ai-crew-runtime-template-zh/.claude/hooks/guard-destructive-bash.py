#!/usr/bin/env python3
"""PreToolUse warn-mode hook：守卫破坏性 bash 命令。

在每次 Bash 调用前触发。当命令包含破坏性模式
（rm -rf、git push --force 等）时发出警告，以便人类在执行前确认。
"""

import json
import re
import sys


# 破坏性命令模式列表
DESTRUCTIVE_PATTERNS = [
    (re.compile(r"\brm\s+-rf\b"), "rm -rf"),
    (re.compile(r"\bgit\s+push\s+.*--force"), "git push --force"),
    (re.compile(r"\bgit\s+push\s+.*--delete"), "git push --delete"),
    (re.compile(r"\bgit\s+reset\s+--hard\b"), "git reset --hard"),
    (re.compile(r"\bgit\s+clean\s+-[a-z]*f"), "git clean -f"),
    (re.compile(r"\bdrop\s+table\b", re.IGNORECASE), "DROP TABLE — 破坏性 SQL"),
    (re.compile(r"\bdelete\s+from\b", re.IGNORECASE), "DELETE FROM — 破坏性 SQL"),
    (re.compile(r"\bshutdown\b", re.IGNORECASE), "shutdown — 关机"),
    (re.compile(r"\breboot\b", re.IGNORECASE), "reboot — 重启"),
    (re.compile(r"\bchmod\s+777\b"), "chmod 777 — 全局可写权限"),
    (re.compile(r">\s*/dev/[a-z]+"), "重定向到设备文件"),
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

    # 仅在裸命令时守卫；沙盒模式不需要此守卫
    if tool_input.get("dangerouslyDisableSandbox"):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": (
                    "⚠️  此命令已禁用沙盒。"
                    "破坏性命令守卫在无沙盒模式下仅供参考。"
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
                    f"⚠️  破坏性命令守卫：命令匹配 {matches}。"
                    "执行前请确认意图。"
                ),
            }
        }))


if __name__ == "__main__":
    main()
