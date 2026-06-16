#!/usr/bin/env python3
"""PostToolUse warn-mode hook：扫描书籍散文中 rule-14 违规。

实现 .claude/rules/14-authorial-stance.md：拒绝元框架语言（"本章""本书""读者"等）、
拒绝作者声音中的"你"、拒绝模态-规定性形式（"你应该""我们必须记住"）、
拒绝回避性集体形式（"人们倾向于""许多读者会"）。

豁免：围栏代码块、逐字双引号跨度、块引用、frontmatter、intra-crew 段落、
标题及审查备忘录（本质上是元框架的）。
"""
# 完整实现与原文件相同——翻译限于文档串
# 完整源代码见 .claude/hooks/scan-pronoun-discipline.py

import json, re, sys
from pathlib import Path

# 简报（*-brief.md）豁免——它们是合法讨论"章节"/"读者"/"本书"作为架构设计对象的架构产物
SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/(?!.*-brief\.md$).*\.md$"
)

META_FRAME_PATTERNS = (
    (re.compile(r"\bthis chapter\b", re.I), "meta-frame:this-chapter",
     "删除'本章'——指涉结构（'我们''现在''早先'）而非对象"),
    (re.compile(r"\bthe chapter('s|s)?\b", re.I), "meta-frame:the-chapter",
     "删除'the chapter'——让散文承载要点而不指涉容器"),
    (re.compile(r"\bthe book\b", re.I), "meta-frame:the-book",
     "删除'the book'——使用'我们'（共同调查者）或'the pattern'（诊断）"),
    (re.compile(r"\bthe reader(?:'s|s)?\b", re.I), "meta-frame:the-reader",
     "删除'the reader'——使用'我们'（共同调查者站位）"),
    (re.compile(r"\breaders\b", re.I), "meta-frame:readers",
     "删除'readers'——使用'我们'或指明具体群体"),
    (re.compile(r"\bthe author(?:'s|s)?\b", re.I), "meta-frame:the-author",
     "删除'the author'——作者立场使用'I'，集体使用'we'"),
    (re.compile(r"\bin this (chapter|section|book)\b", re.I), "meta-frame:in-this-x",
     "删除——使用'earlier'/'now'/'we saw'代替"),
)

YOU_PATTERNS = (
    (re.compile(r"\byou (?:will|may|might|should|must|need|ought|can|are|have)\b", re.I),
     "you:address", "将'you ...'重述为'we ...'或祈使句"),
    (re.compile(r"\byour\b", re.I), "you:your", "将'your X'重述为'our X'或删除物主代词"),
    (re.compile(r"\bif you (?:are|find|see|have|encounter)\b", re.I),
     "you:if-you", "将'if you X'重述为'if we X'"),
)

MODAL_PRESCRIPTIVE_PATTERNS = (
    (re.compile(r"\byou (?:should|must|ought|need to)\b", re.I), "modal:you-should",
     "重述为祈使句"),
    (re.compile(r"\bwe (?:should|must) (?:remember|never|always|note)\b", re.I),
     "modal:we-should-remember", "重述为祈使句——说教节奏即使在'we'形式下也被禁止"),
)

EVASIVE_COLLECTIVE_PATTERNS = (
    (re.compile(r"\b(?:people|anyone|many readers|most readers|one) "
                r"(?:tend|tends|may|might|will)\b", re.I),
     "evasive:people-tend-to", "指明具体群体或使用'we'"),
)

# 函数 _strip_exempt_regions(), scan(), _extract_path(), _emit(), main() 与原文件相同
# 完整源代码见 .claude/hooks/scan-pronoun-discipline.py
# 本翻译文件仅供中文参考——实际 hook 执行使用原英文版本
