#!/usr/bin/env python3
"""Deterministic validator for diagram artifacts used by Jade."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

MERMAID_START_RE = re.compile(r"^\s*(graph|flowchart|sequenceDiagram|classDiagram|stateDiagram|erDiagram|journey|gantt|mindmap|timeline)\b", re.MULTILINE)
EDGE_RE = re.compile(r"-->|---|==>|\.\.>")


@dataclass(frozen=True)
class ValidationResult:
    passed: bool
    messages: tuple[str, ...]


def _extract_mermaid_payload(text: str) -> str:
    if "```mermaid" not in text:
        return text
    block_re = re.compile(r"```mermaid\s*(.*?)```", re.DOTALL | re.IGNORECASE)
    match = block_re.search(text)
    return match.group(1) if match else ""


def validate_diagram_text(text: str) -> ValidationResult:
    payload = _extract_mermaid_payload(text)
    messages: list[str] = []

    if not payload.strip():
        messages.append("No Mermaid payload found.")
        return ValidationResult(False, tuple(messages))

    if not MERMAID_START_RE.search(payload):
        messages.append("Missing recognized Mermaid diagram declaration.")

    if not EDGE_RE.search(payload):
        messages.append("Missing relationship edges (e.g., '-->').")

    return ValidationResult(len(messages) == 0, tuple(messages))


def validate_diagram_file(path: Path) -> ValidationResult:
    if not path.exists():
        return ValidationResult(False, (f"File not found: {path}",))

    text = path.read_text(encoding="utf-8", errors="ignore")
    result = validate_diagram_text(text)
    return result


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Mermaid diagram artifacts deterministically")
    parser.add_argument("path", type=Path, help="Path to diagram artifact (.md/.mmd/.mermaid)")
    args = parser.parse_args(argv)

    result = validate_diagram_file(args.path)
    if result.passed:
        print(f"PASS: diagram artifact validated: {args.path}")
        return 0

    print(f"FAIL: diagram artifact validation failed: {args.path}")
    for message in result.messages:
        print(f"  - {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(_cli())
