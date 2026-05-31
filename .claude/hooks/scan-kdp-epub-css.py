#!/usr/bin/env python3
"""Warn-mode hook: flag KDP/Kindle-unsupported CSS in the EPUB stylesheet at edit time.

Governed by .claude/rules/16-kdp-epub.md. Scope: book/design/epub/*.css. Mirrors the
project's other warn-mode scanners (stdin JSON tool payload, SCOPE_RE gate, never
blocks — surfaces guidance). Catches the reflowable-EPUB pitfalls Kindle silently
"fixes": position:, fixed pt/px on type/box, forced black/white backgrounds, and
height on (likely) text elements.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCOPE_RE = re.compile(r"^book/design/epub/.*\.css$")

# value-bearing declarations that must use em/% not px/pt
# font-size / the `font` shorthand / box props with a fixed pt|px length
FIXED_UNIT = re.compile(
    r"(?<![\w-])(font|font-size|line-height|text-indent|margin|margin-\w+|padding|padding-\w+|width)\s*:"
    r"[^;{}]*\b\d*\.?\d+(px|pt)\b", re.I)
POSITION = re.compile(r"(?<![\w-])position\s*:\s*(absolute|relative|fixed|sticky)", re.I)
BW_BG = re.compile(
    r"(?<![\w-])background(?:-color)?\s*:[^;{}]*(#fff(?:fff)?\b|#000(?:000)?\b|\bwhite\b|\bblack\b)",
    re.I)
# fixed pt|px height on a text element (auto / % / em / max-/min- are exempt)
HEIGHT = re.compile(r"(?<![\w-])height\s*:[^;{}]*\b\d*\.?\d+(px|pt)\b", re.I)

CHECKS = [
    (POSITION, "position", "remove `position:` — single column only; Kindle ignores it (rule 16)"),
    (FIXED_UNIT, "fixed-unit", "use em/% not px/pt for type/margins so text reflows (rule 16)"),
    (BW_BG, "bw-background", "no forced black/white background — let the reader's theme win (rule 16)"),
    (HEIGHT, "text-height", "set `height` only on images, never on text containers (rule 16)"),
]


def scan(text: str) -> list[tuple[int, str, str, str]]:
    findings: list[tuple[int, str, str, str]] = []
    in_comment = False
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw
        # crude /* */ comment stripping (line-level) to cut false positives
        if in_comment:
            if "*/" in line:
                line = line.split("*/", 1)[1]
                in_comment = False
            else:
                continue
        if "/*" in line:
            before, _, after = line.partition("/*")
            if "*/" in after:
                line = before + after.split("*/", 1)[1]
            else:
                line = before
                in_comment = True
        if not line.strip():
            continue
        for rx, name, fix in CHECKS:
            if rx.search(line):
                findings.append((i, name, raw.strip()[:90], fix))
    return findings


def _extract_path(inp: dict) -> str | None:
    return inp.get("file_path") or inp.get("path") or inp.get("notebook_path")


def _emit(msg: str) -> None:
    print(msg)


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
    project_root = Path(__file__).resolve().parents[2]
    try:
        rel = path.resolve().relative_to(project_root).as_posix()
    except ValueError:
        sys.exit(0)
    if not SCOPE_RE.match(rel):
        sys.exit(0)
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        sys.exit(0)

    findings = scan(text)
    if not findings:
        _emit(f"Warn mode: scan-kdp-epub-css passed for {rel}.")
        return
    lines = [f"Warn mode: scan-kdp-epub-css flagged {len(findings)} KDP-CSS issue(s) in {rel}:"]
    for lineno, name, snippet, fix in findings[:10]:
        lines.append(f"  L{lineno} [{name}] {snippet}")
        lines.append(f"     -> {fix}")
    if len(findings) > 10:
        lines.append(f"  ... and {len(findings) - 10} more.")
    _emit(" ".join(lines))


if __name__ == "__main__":
    main()
