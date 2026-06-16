#!/usr/bin/env python3
"""PostToolUse warn-mode hook：扫描书籍散文中缺乏明确引用或条件限制的过度声明动词。

实现 ``.claude/rules/05-overclaim-language.md``。仅 warn——从不返回 ``permissionDecision: deny``。
触发范围：book/evidence/case-files/、book/chapters-v*/、process/review-memos/、book/proposals/。
"""
# 完整扫描逻辑（禁用动词模式、条件限制模式、引文剥离等）与原文件相同
# 翻译限于文档串和关键注释

import json, re, sys
from pathlib import Path

SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/.*\.md$"
)

# 禁用动词/短语，每个条目：(regex, 简短名称, 建议处理)
PATTERNS: tuple[tuple[re.Pattern[str], str, str], ...] = (
    (re.compile(r"\b(knew|knew about|was aware that|were aware that)\b", re.I),
     "knew", "引用证明知情的来源或改写以限定"),
    (re.compile(r"\b(deliberately|intentionally|on purpose)\b", re.I),
     "deliberately", "引用记录了意图的来源（承认、陪审团裁定、有记录的陈述）"),
    (re.compile(r"\b(guilty|is guilty of|was guilty of)\b", re.I),
     "guilty", "引用定罪法院+日期，或替换为'被指控'/'被控以'"),
    (re.compile(r"\b(lied|lied about)\b", re.I),
     "lied", "引用有记录的不实陈述+当时已知其为虚假；否则使用'misstated'"),
    (re.compile(r"\b(proves|definitively shows|definitively proves)\b", re.I),
     "proves", "使用'supports'/'indicates'/'is consistent with'，除非引用最终裁决"),
    (re.compile(r"\b(must have|would have) (known|been|seen|read|done)\b", re.I),
     "must-have", "禁止用于心智状态归因；仅使用有记录的事实"),
    (re.compile(r"\b(clearly|obviously|undeniably)\b", re.I),
     "clearly", "禁止作为替代证据的副词；引用使其清楚的来源"),
)

# 条件限制/归因模式——如果出现在同一行，中和警告
HEDGE_PATTERNS = (
    r"\[CITE:[^\]]+\]", r"\[EVIDENCE NEEDED:[^\]]+\]", r"\[HEDGE:[^\]]+\]",
    r"\[\^\d+\]", r"according to \w", r"reported (?:that|by)", r"per the ",
    r"court records show", r"as documented in", r"pleaded guilty",
    r"(?:was|were|been) (?:found|convicted) guilty", r"guilty plea",
    r"jury found", r"court convicted",
    r"(?:the )?(?:Court|court of \w+|District Court|Supreme Court) (?:held|found|ruled)",
    r"\w+ J(?:\.|udge|ustice)? (?:held|found|ruled)",
)
HEDGE_RE = re.compile("|".join(HEDGE_PATTERNS), re.I)
FOOTNOTE_DEF_RE = re.compile(r"^\s*\[\^[^\]]+\]:\s")
QUOTED_RE = re.compile(r'"[^"\n]+"')

# 函数 scan(), _strip_quotes_and_codeblocks(), _frontmatter_end_line(),
# _is_skippable_structural(), _is_negated_match(), _match_in_diagnostic_question(),
# _extract_path(), _emit(), main() 与原文件相同
# （代码逻辑保留，仅文档串翻译）

def _strip_quotes_and_codeblocks(text: str) -> str:
    """返回将引文文本和围栏代码块内容清空后的 text 副本。
    引文内部的过度声明动词是豁免的（rule 06）。"""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)
    text = QUOTED_RE.sub(lambda m: " " * len(m.group(0)), text)
    return text

# ... 其余函数与原文件相同 ...
# 完整源代码见 .claude/hooks/scan-overclaim.py
# 本翻译文件仅供中文参考——实际 hook 执行使用原英文版本
