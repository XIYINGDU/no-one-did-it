#!/usr/bin/env python3
"""将全局五条核心原则从单一源同步到所有目标文件。

读取 ``rules/00-core-values.md`` 作为规范源。提取
``<!-- GENERATED:five-over-rules:manifest start -->`` 和
``<!-- GENERATED:five-over-rules:manifest end -->`` 之间的五条核心原则块。
查找 ``.claude/`` 下所有携带 ``<!-- GENERATED:five-over-rules:start -->``
标记的文件，替换标记之间的内容。

用法：
    python3 scripts/sync_core_values.py          # 同步所有目标
    python3 scripts/sync_core_values.py --check  # 验证一致性，有漂移则非零退出
"""

import argparse
import re
import sys
from pathlib import Path


# manifest 源文件中的标记
MANIFEST_START = "<!-- GENERATED:five-over-rules:manifest start -->"
MANIFEST_END = "<!-- GENERATED:five-over-rules:manifest end -->"
# 目标文件中的标记
TARGET_START = "<!-- GENERATED:five-over-rules:start -->"
TARGET_END = "<!-- GENERATED:five-over-rules:end -->"


def extract_source_block(text: str) -> str:
    """从 manifest 源中提取五条核心原则块。"""
    m = re.search(
        re.escape(MANIFEST_START) + r"\n(.*?)\n" + re.escape(MANIFEST_END),
        text,
        re.DOTALL,
    )
    if not m:
        print("错误：在 rules/00-core-values.md 中找不到 manifest 块", file=sys.stderr)
        sys.exit(1)
    return m.group(1)


def find_target_files(root: Path) -> list[Path]:
    """查找 .claude/ 下所有携带目标起始标记的文件。"""
    targets = []
    claude_dir = root / ".claude"
    if not claude_dir.is_dir():
        print(f"错误：在 {root} 找不到 .claude/ 目录", file=sys.stderr)
        sys.exit(1)

    for path in claude_dir.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if TARGET_START in text:
            targets.append(path)
    return targets


def sync_target(path: Path, new_block: str, check_only: bool = False) -> bool:
    """替换目标文件中的五条核心原则块。如有变更返回 True。"""
    text = path.read_text(encoding="utf-8")
    pattern = re.escape(TARGET_START) + r"\n.*?\n" + re.escape(TARGET_END)
    new_text = TARGET_START + "\n" + new_block + "\n" + TARGET_END
    updated = re.sub(pattern, new_text, text, flags=re.DOTALL)

    if updated == text:
        return False

    if check_only:
        return True  # 检测到漂移

    path.write_text(updated, encoding="utf-8")
    print(f"  已同步：{path.relative_to(path.parents[2])}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="将五条核心原则同步到所有目标文件")
    parser.add_argument("--check", action="store_true", help="验证一致性；有漂移则非零退出")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    source_path = root / ".claude" / "rules" / "00-core-values.md"
    if not source_path.exists():
        print(f"错误：源文件不存在：{source_path}", file=sys.stderr)
        sys.exit(1)

    source_text = source_path.read_text(encoding="utf-8")
    block = extract_source_block(source_text)
    targets = find_target_files(root)

    if not targets:
        print("找不到带有五条核心原则标记的目标文件。")
        sys.exit(0)

    drift_count = 0
    for path in sorted(targets):
        changed = sync_target(path, block, check_only=args.check)
        if changed:
            drift_count += 1

    if args.check:
        if drift_count > 0:
            print(f"\n失败：{drift_count} 个目标与源文件漂移。运行不带 --check 以同步。", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"通过：所有 {len(targets)} 个目标与源文件一致。")
    else:
        if drift_count > 0:
            print(f"\n已同步 {drift_count} 个目标。{len(targets) - drift_count} 个已是最新。")
        else:
            print(f"所有 {len(targets)} 个目标已是最新。")


if __name__ == "__main__":
    main()
