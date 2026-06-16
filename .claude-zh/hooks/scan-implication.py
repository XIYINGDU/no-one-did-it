#!/usr/bin/env python3
"""PostToolUse warn-mode hook：扫描书籍散文中无引用或条件限制即断言心智状态、
动机、知情、因果关系或链条责任的叙事性隐含。

是 scan-overclaim.py 的姐妹脚本。实现 .claude/rules/07-implication-burden.md。

扫描模式：匿名链条指涉、链条阶梯（3+ 专有名词 + 2+ 层级动词）、
相邻利益+决策并置、同情-然后-冷切、日期并置因果。

虚假阳性控制：如标记段落或其相邻段落含条件限制/引用模式则放行。
逐字引文豁免。围栏代码块豁免。
"""
# 完整实现与原文件相同——翻译限于文档串
# 完整源代码见 .claude/hooks/scan-implication.py

import json, re, sys
from pathlib import Path

SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/.*\.md$"
)

ANONYMOUS_CHAIN_RE = re.compile(
    r"\b(someone in the chain|a higher office|approval came from above|"
    r"instructions came down|the decision was made|orders came from|"
    r"the chain decided|the office signed off|approval was granted|"
    r"someone authorized|someone approved|was authorized by a)\b", re.I,
)

HIERARCHICAL_VERB_RE = re.compile(
    r"\b(authorized|approved|signed off|ordered|instructed|directed|sanctioned|"
    r"green[- ]?lit|cleared|countersigned)\b", re.I,
)

BENEFIT_LANGUAGE_RE = re.compile(
    r"\b(profited|acquired|received|gained|benefited|enriched|netted|"
    r"walked away with|cashed out|collected|pocketed)\b", re.I,
)

DECISION_LANGUAGE_RE = re.compile(
    r"\b(decided|chose|opted|moved to|elected to|agreed to|signed|"
    r"approved|authorized|issued the order|gave the green light)\b", re.I,
)

SYMPATHETIC_DESCRIPTOR_RE = re.compile(
    r"\b(young|inexperienced|junior|exhausted|untrained|"
    r"alone|isolated|frightened|new to the job|first day|"
    r"struggling|overwhelmed|in over (?:his|her|their) head)\b", re.I,
)

ENGINEERING_VERB_RE = re.compile(
    r"\b(engineered|orchestrated|manufactured|fabricated|architected|"
    r"set the conditions for|stage-managed)\b", re.I,
)

HEDGE_RE = re.compile(
    r"("
    r"\[CITE:[^\]]+\]" r"|\[EVIDENCE NEEDED:[^\]]+\]" r"|\[HEDGE:[^\]]+\]"
    r"|\[\^\d+\]" r"|the record does not (?:establish|show|name|identify)"
    r"|per the (?:inquiry|court|inspector|investigation|ruling|finding)"
    r"|the connection is not signed" r"|according to \w" r"|reported (?:that|by)"
    r"|the documentary record" r"|on the public record"
    r")", re.I,
)

# 函数 scan(), _split_paragraphs(), _cleared_by_hedge() 等与原文件相同
# 完整源代码见 .claude/hooks/scan-implication.py
# 本翻译文件仅供中文参考——实际 hook 执行使用原英文版本
