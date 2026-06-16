#!/usr/bin/env python3
"""PostToolUse hook：frontmatter + 操作合同验证。

默认为 warn-only 模式。一个狭窄的拒绝路径存在于章节提升：
当章节文件以 ``status: ready`` 持久化且任何章节节奏段落缺失时拒绝。
拒绝基于**工具调用后磁盘上文件的最终状态**评估，而非通过差异对比。
"""
# 完整实现与原文件相同——翻译限于文档串和注释
import json, re, sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from scripts.operating_validators import extract_chapter_status, validate_file

REQUIRED_FIELDS = ("name:", "description:")
SLUG_RE = re.compile(r"^[a-z0-9-]+$")
VALIDATION_TARGET_RE = re.compile(
    r"^(book/(case-files|chapters-v\d+|review-memos)/(?!README\.md$)|\.claude/agents/|\.claude/skills/)"
)
CHAPTER_PATH_RE = re.compile(r"^book/chapters-v\d+/(?!README\.md$)")


def _frontmatter_issues(path: str, text: str) -> list[str]:
    issues: list[str] = []
    if not text.startswith("---\n"):
        issues.append("缺少 YAML frontmatter 开头行")
        fm = ""
    else:
        parts = text.split("---", 2)
        if len(parts) < 3:
            issues.append("缺少 YAML frontmatter 闭合行")
            fm = ""
        else:
            fm = parts[1]
    for field in REQUIRED_FIELDS:
        if field not in fm:
            issues.append(f"缺少 {field}")
    name_match = re.search(r"^name:\s*([^\n]+)", fm, re.M)
    if name_match and not SLUG_RE.match(name_match.group(1).strip()):
        issues.append("name 必须仅使用小写字母、数字和连字符")
    return issues


def _extract_path(tool_input: dict) -> str:
    for key in ("file_path", "path"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def _deny(reason: str, warn_context: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
            "additionalContext": "Warn 模式：" + (warn_context if warn_context else reason),
        }
    }))


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)
    inp = data.get("tool_input") or {}
    raw_path = _extract_path(inp)
    if not raw_path:
        sys.exit(0)
    path = Path(raw_path)
    if not path.is_absolute():
        path = Path(data.get("cwd") or ".") / path
    if not path.exists():
        sys.exit(0)
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Warn 模式：无法读取已编辑文件 {path.as_posix()}: {exc}",
            }
        }))
        sys.exit(0)

    messages: list[str] = []
    resolved = path.resolve()
    try:
        rel_path = resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        rel_path = resolved.as_posix()

    if rel_path.startswith(".claude/agents/") and rel_path.endswith(".md"):
        fm_issues = _frontmatter_issues(rel_path, text)
        if fm_issues:
            messages.append(f"Agent frontmatter 问题于 {rel_path}: {'; '.join(fm_issues)}")

    is_chapter_file = bool(CHAPTER_PATH_RE.match(rel_path))
    if VALIDATION_TARGET_RE.match(rel_path):
        report = validate_file(path)
        if report.passed:
            messages.append(f"操作验证器通过于 {rel_path}。")
        else:
            issues = "; ".join(issue.message for issue in report.issues)
            messages.append(f"操作验证器警告于 {rel_path}: {issues}")
            if is_chapter_file:
                has_rhythm_gap = any(
                    issue.code == "chapter.rhythm.missing_section" for issue in report.issues
                )
                # 按最终状态拒绝：以 `status: ready` 持久化且缺失节奏段落的章节无效
                if has_rhythm_gap and extract_chapter_status(text) == "ready":
                    reason = (
                        "章节提升关卡：带有 `status: ready` 的章节"
                        "必须包含所有 8 个节奏段落。"
                        "要么恢复缺失段落，要么将 `status:` 移回 `draft`。"
                    )
                    _deny(reason, " ".join(messages))
                    sys.exit(0)

    if not messages:
        sys.exit(0)
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "Warn 模式：" + " ".join(messages),
        }
    }))


if __name__ == "__main__":
    main()
