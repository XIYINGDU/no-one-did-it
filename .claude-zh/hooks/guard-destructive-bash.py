#!/usr/bin/env python3
"""PreToolUse hook：拒绝明显具有破坏性的 shell 命令。"""
import json, re, sys

# 匹配破坏性模式的模式列表：递归删除、仓库状态销毁、全局可写 chmod、网络管道 shell 执行
PATTERNS = [
    r"\brm\s+-rf\s+(/|\.|~|\$HOME|\*)",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-fdx\b",
    r"\bchmod\s+-R\s+777\b",
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
        "破坏性 shell 命令被项目守卫阻止。请询问用户并缩小命令范围。"
        if blocked
        else "命令通过了破坏性命令守卫。"
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
