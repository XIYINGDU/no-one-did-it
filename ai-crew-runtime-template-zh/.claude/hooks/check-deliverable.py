#!/usr/bin/env python3
"""PostToolUse warn-mode hook：通用交付物质量扫描器。

在对项目交付物路径（在下方 SCOPE_RE 中配置）的写入/编辑时触发。
实现质量标准规则，扫描常见质量问题：

1. 缺失必需 schema 字段（Owner、Evidence grade、Handoff）
2. 未解决的占位符标记（TODO、FIXME 无负责人）
3. 禁用替代性副词——表明弱断言

此 hook 为 **warn-only**。它从不返回 ``permissionDecision: deny`` ——
编排者 quality-gate pass 中的提升关卡是唯一的 deny 路径。
此 hook 是廉价模式级扫描；quality-gate skill 是深层读取。

按你的项目领域自定义 PATTERNS 和 SCOPE_RE。
"""

import json
import re
import sys
from pathlib import Path


# ============================================================
# 可配置 —— 按你的项目调整
# ============================================================

# 要扫描的文件（项目相对路径正则）
SCOPE_RE = re.compile(
    r"^(outputs|deliverables|chapters|src)/.*\.(md|py|js|ts|rs|go)$"
)

# 每个交付物应携带的必需 schema 字段
REQUIRED_FIELDS = [
    "Owner:",
    "Handoff:",
]

# 不应存活到 ready 的占位符模式
PLACEHOLDER_PATTERNS = [
    (re.compile(r"\[TODO\]", re.IGNORECASE), "TODO — 未解决"),
    (re.compile(r"\[FIXME\]", re.IGNORECASE), "FIXME — 未解决"),
    (re.compile(r"\[PLACEHOLDER\]", re.IGNORECASE), "PLACEHOLDER — 未解决"),
]

# 禁用替代性副词（项目无关）
BANNED_ADVERBS = [
    (re.compile(r"\b(clearly|obviously|undeniably)\b", re.IGNORECASE),
     "clearly/obviously/undeniably（显然/无疑）",
     "引用使其明确的来源；让读者判断。"),
    (re.compile(r"\b(must have|would have)\b", re.IGNORECASE),
     "must have / would have（一定/本该）",
     "仅使用有文档记录的事实，不对必定发生之事进行推测。"),
]


def _project_relative(path: Path) -> str | None:
    """返回项目根目录的相对路径，或 None（如果不在项目内）。"""
    project_root = Path(__file__).resolve().parents[2]
    try:
        return path.resolve().relative_to(project_root).as_posix()
    except ValueError:
        return None


def scan(text: str) -> list[str]:
    """返回给定文件内容的警告消息列表。"""
    warnings: list[str] = []

    # 检查必需 schema 字段
    for field in REQUIRED_FIELDS:
        if field not in text:
            warnings.append(f"缺失必需 schema 字段：'{field}'")

    # 检查占位符标记
    for pattern, label in PLACEHOLDER_PATTERNS:
        matches = pattern.findall(text)
        if matches:
            warnings.append(f"发现 {len(matches)} 个未解决的 {label} 标记")

    # 检查禁用副词
    for pattern, word, suggestion in BANNED_ADVERBS:
        if pattern.search(text):
            warnings.append(f"禁用替代性副词：'{word}' — {suggestion}")

    return warnings


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    inp = data.get("tool_input") or {}

    # 从工具输入中提取文件路径
    path_str = ""
    for key in ("file_path", "path"):
        value = inp.get(key)
        if isinstance(value, str) and value:
            path_str = value
            break
    if not path_str:
        sys.exit(0)

    path = Path(path_str)
    if not path.is_absolute():
        path = Path(data.get("cwd") or ".") / path

    if not path.exists():
        sys.exit(0)

    rel = _project_relative(path)
    if not rel:
        sys.exit(0)

    if not SCOPE_RE.match(rel):
        sys.exit(0)

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        sys.exit(0)

    warnings = scan(text)

    if not warnings:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Warn 模式：check-deliverable 对 {rel} 通过。",
            }
        }))
        return

    lines = [f"Warn 模式：check-deliverable 在 {rel} 中标记了 {len(warnings)} 个问题："]
    for w in warnings:
        lines.append(f"  • {w}")

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": " ".join(lines),
        }
    }))


if __name__ == "__main__":
    main()
