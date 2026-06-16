#!/usr/bin/env python3
"""PostToolUse warn-mode hook：扫描书籍散文中违反 rule-13 slug-only 不变量的冗长内联 [CITE:] 标记。

实现 .claude/rules/13-citation-form.md 第 2 层纪律：内联 [CITE:] 括号仅携带以 ; 分隔的卡片 slug。
无逗号、无嵌入引用元数据、无"see also"、无存档说明、无 tier-1 佐证列表。

允许形式：[CITE: card-slug]、[CITE: slug; slug]、[CITE: slug — pending-stephen-lock]
禁止形式：完整引用、佐证装置、存档元数据、超 80 字符（可疑隐藏元数据）
"""
# 完整实现与原文件相同——翻译限于文档串
# 完整源代码见 .claude/hooks/scan-cite-density.py

import json, re, sys
from pathlib import Path

SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/.*\.md$"
)

CITE_RE = re.compile(r"\[CITE:\s*([^\]]*?)\s*\]")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")
PENDING_SUFFIX_RE = re.compile(
    r"^\s*(?P<slug>[a-z0-9]+(?:[-_][a-z0-9]+)*)\s*[—-]\s*pending-stephen-lock\s*$"
)
MAX_BRACKET_LENGTH = 80

# 函数 _classify(), scan(), _extract_path(), _emit(), main() 与原文件相同
# 完整源代码见 .claude/hooks/scan-cite-density.py
# 本翻译文件仅供中文参考——实际 hook 执行使用原英文版本
