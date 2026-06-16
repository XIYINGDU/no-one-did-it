#!/usr/bin/env python3
"""Warn-mode hook：在编辑时标记 EPUB 样式表中 KDP/Kindle 不支持的 CSS。

受 .claude/rules/16-kdp-epub.md 管辖。范围：book/design/epub/*.css。
捕获 Kindle 无声"修复"的可重排 EPUB 陷阱：position:、类型/盒模型上的固定 pt/px、
强制黑白背景以及（可能）文本元素上的 height。
"""
# 完整实现与原文件相同——翻译限于文档串
# 完整源代码见 .claude/hooks/scan-kdp-epub-css.py

from __future__ import annotations
import json, re, sys
from pathlib import Path

SCOPE_RE = re.compile(r"^book/design/epub/.*\.css$")

FIXED_UNIT = re.compile(
    r"(?<![\w-])(font|font-size|line-height|text-indent|margin|margin-\w+|padding|padding-\w+|width)\s*:"
    r"[^;{}]*\b\d*\.?\d+(px|pt)\b", re.I)
POSITION = re.compile(r"(?<![\w-])position\s*:\s*(absolute|relative|fixed|sticky)", re.I)
BW_BG = re.compile(
    r"(?<![\w-])background(?:-color)?\s*:[^;{}]*(#fff(?:fff)?\b|#000(?:000)?\b|\bwhite\b|\bblack\b)", re.I)
HEIGHT = re.compile(r"(?<![\w-])height\s*:[^;{}]*\b\d*\.?\d+(px|pt)\b", re.I)

CHECKS = [
    (POSITION, "position", "移除 `position:`——仅单列；Kindle 忽略它（rule 16）"),
    (FIXED_UNIT, "fixed-unit", "使用 em/% 而非 px/pt 用于类型/边距（rule 16）"),
    (BW_BG, "bw-background", "不强制黑白背景——让读者主题胜出（rule 16）"),
    (HEIGHT, "text-height", "仅在图像上设置 `height`，绝不在文本容器上（rule 16）"),
]

# 函数 scan(), _extract_path(), _emit(), main() 与原文件相同
# 完整源代码见 .claude/hooks/scan-kdp-epub-css.py
# 本翻译文件仅供中文参考——实际 hook 执行使用原英文版本
