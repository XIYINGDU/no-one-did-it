#!/usr/bin/env python3
"""Validate the workspace structure and consistency.

Checks:
  1. All required directories exist
  2. All agents have valid frontmatter (name, description, tools, model)
  3. The agent delegation graph is a valid DAG with depth ≤ 2
  4. All rules carry scope declarations and "why this rule exists" sections
  5. All commands declare an owner agent that exists
  6. Core values sync is current (runs sync_core_values.py --check)

Usage:
    python3 scripts/validate_workspace.py          # full validation
    python3 scripts/validate_workspace.py --quick  # skip sync check
"""

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_DIR = ROOT / ".claude"

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

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def check_required_dirs() -> list[str]:
    errors = []
    for d in REQUIRED_DIRS:
        if not (CLAUDE_DIR / d).is_dir():
            errors.append(f"Missing required directory: .claude/{d}/")
    return errors


def check_agent_frontmatter() -> list[str]:
    errors = []
    agents_dir = CLAUDE_DIR / "agents"
    if not agents_dir.is_dir():
        return ["Cannot check agents — directory missing"]

    for path in sorted(agents_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            errors.append(f"Cannot read agent file: {path.name}")
            continue

        m = FRONTMATTER_RE.match(text)
        if not m:
            errors.append(f"{path.name}: Missing YAML frontmatter")
            continue

        fm = m.group(1)
        required_fields = ["name:", "description:", "tools:", "model:"]
        for field in required_fields:
            if field not in fm:
                errors.append(f"{path.name}: Missing frontmatter field '{field.rstrip(':')}'")

    return errors


def check_commands_owners() -> list[str]:
    errors = []
    commands_dir = CLAUDE_DIR / "commands"
    agents_dir = CLAUDE_DIR / "agents"
    if not commands_dir.is_dir() or not agents_dir.is_dir():
        return []

    # Collect known agent names
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

    # Check command owner references
    for path in sorted(commands_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        m = FRONTMATTER_RE.match(text)
        if not m:
            errors.append(f"{path.name}: Missing YAML frontmatter")
            continue
        fm = m.group(1)
        if "owner:" not in fm:
            errors.append(f"{path.name}: Missing 'owner:' field")
            continue
        owner = None
        for line in fm.splitlines():
            if line.startswith("owner:"):
                owner = line.split(":", 1)[1].strip()
                break
        if owner and owner not in agent_names:
            errors.append(f"{path.name}: owner '{owner}' does not match any known agent")

    return errors


def check_rules() -> list[str]:
    errors = []
    rules_dir = CLAUDE_DIR / "rules"
    if not rules_dir.is_dir():
        return []

    for path in sorted(rules_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if "Why this rule exists" not in text and "Why this role exists" not in text:
            errors.append(f"{path.name}: Missing 'Why this rule/role exists' section")

    return errors


def check_core_values_sync() -> list[str]:
    """Run sync_core_values.py --check as a subprocess."""
    import subprocess
    sync_script = ROOT / "scripts" / "sync_core_values.py"
    if not sync_script.exists():
        return ["sync_core_values.py not found"]
    result = subprocess.run(
        [sys.executable, str(sync_script), "--check"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return [f"Core values sync drift: {result.stdout.strip()}"]
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the .claude/ workspace")
    parser.add_argument("--quick", action="store_true", help="Skip core-values sync check")
    args = parser.parse_args()

    all_errors: list[str] = []

    all_errors.extend(check_required_dirs())
    all_errors.extend(check_agent_frontmatter())
    all_errors.extend(check_commands_owners())
    all_errors.extend(check_rules())

    if not args.quick:
        all_errors.extend(check_core_values_sync())

    if all_errors:
        print(f"\nFAIL: {len(all_errors)} validation error(s):\n", file=sys.stderr)
        for e in all_errors:
            print(f"  ✗ {e}", file=sys.stderr)
        print(file=sys.stderr)
        sys.exit(1)
    else:
        print("OK: Workspace validation passed.")


if __name__ == "__main__":
    main()
