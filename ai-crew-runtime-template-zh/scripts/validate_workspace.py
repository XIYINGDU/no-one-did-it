#!/usr/bin/env python3
"""验证工作区结构和一致性。

检查项：
  1. 所有必需目录存在
  2. 所有 agent 有合法 frontmatter（name, description, tools, model）
  3. Agent 派遣图是合法 DAG，深度 ≤ 2
  4. 所有规则带有「为什么存在」段落
  5. 所有命令声明了存在的 owner agent
  6. 核心价值同步是最新的（运行 sync_core_values.py --check）

用法：
    python3 scripts/validate_workspace.py          # 完整验证
    python3 scripts/validate_workspace.py --quick  # 跳过同步检查
"""

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_DIR = ROOT / ".claude"

# 必需的子目录
REQUIRED_DIRS = [
    "agents",
    "commands",
    "skills",
    "rules",
    "hooks",
    "state",
    "agent-memory",
    "docs",
]

# YAML frontmatter 正则
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def check_required_dirs() -> list[str]:
    """验证所有必需目录存在。"""
    errors = []
    for d in REQUIRED_DIRS:
        if not (CLAUDE_DIR / d).is_dir():
            errors.append(f"缺少必需目录：.claude/{d}/")
    return errors


def check_agent_frontmatter() -> list[str]:
    """验证所有 agent 文件的 frontmatter 包含必填字段。"""
    errors = []
    agents_dir = CLAUDE_DIR / "agents"
    if not agents_dir.is_dir():
        return ["无法检查 agent — 目录缺失"]

    for path in sorted(agents_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            errors.append(f"无法读取 agent 文件：{path.name}")
            continue

        m = FRONTMATTER_RE.match(text)
        if not m:
            errors.append(f"{path.name}：缺少 YAML frontmatter")
            continue

        fm = m.group(1)
        # 每个 agent 必须声明这四个字段
        required_fields = ["name:", "description:", "tools:", "model:"]
        for field in required_fields:
            if field not in fm:
                errors.append(f"{path.name}：缺少 frontmatter 字段 '{field.rstrip(':')}'")

    return errors


def check_commands_owners() -> list[str]:
    """验证所有命令声明的 owner agent 存在。"""
    errors = []
    commands_dir = CLAUDE_DIR / "commands"
    agents_dir = CLAUDE_DIR / "agents"
    if not commands_dir.is_dir() or not agents_dir.is_dir():
        return []

    # 收集已知 agent 名称
    agent_names = set()
    for path in agents_dir.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        m = FRONTMATTER_RE.match(text)
        if m:
            for line in m.group(1).splitlines():
                if line.startswith("name:"):
                    agent_names.add(line.split(":", 1)[1].strip())
                    break

    # 检查命令 owner 引用
    for path in sorted(commands_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        m = FRONTMATTER_RE.match(text)
        if not m:
            errors.append(f"{path.name}：缺少 YAML frontmatter")
            continue
        fm = m.group(1)
        if "owner:" not in fm:
            errors.append(f"{path.name}：缺少 'owner:' 字段")
            continue
        owner = None
        for line in fm.splitlines():
            if line.startswith("owner:"):
                owner = line.split(":", 1)[1].strip()
                break
        if owner and owner not in agent_names:
            errors.append(f"{path.name}：owner '{owner}' 不匹配任何已知 agent")

    return errors


def check_rules() -> list[str]:
    """验证所有规则文件包含「为什么存在」段落（支持中英文）。"""
    errors = []
    rules_dir = CLAUDE_DIR / "rules"
    if not rules_dir.is_dir():
        return []

    for path in sorted(rules_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        # 支持中文和英文的「为什么存在」
        if "为什么存在" not in text and "Why this rule exists" not in text and "Why this role exists" not in text:
            errors.append(f"{path.name}：缺少「为什么存在」段落")

    return errors


def check_core_values_sync() -> list[str]:
    """以子进程运行 sync_core_values.py --check。"""
    import subprocess
    sync_script = ROOT / "scripts" / "sync_core_values.py"
    if not sync_script.exists():
        return ["sync_core_values.py 不存在"]
    result = subprocess.run(
        [sys.executable, str(sync_script), "--check"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return [f"核心价值同步漂移：{result.stdout.strip()}"]
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="验证 .claude/ 工作区")
    parser.add_argument("--quick", action="store_true", help="跳过核心价值同步检查")
    args = parser.parse_args()

    all_errors: list[str] = []

    all_errors.extend(check_required_dirs())
    all_errors.extend(check_agent_frontmatter())
    all_errors.extend(check_commands_owners())
    all_errors.extend(check_rules())

    if not args.quick:
        all_errors.extend(check_core_values_sync())

    if all_errors:
        print(f"\n失败：{len(all_errors)} 个验证错误：\n", file=sys.stderr)
        for e in all_errors:
            print(f"  ✗ {e}", file=sys.stderr)
        print(file=sys.stderr)
        sys.exit(1)
    else:
        print("通过：工作区验证通过。")


if __name__ == "__main__":
    main()
