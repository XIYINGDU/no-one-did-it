#!/usr/bin/env python3
"""Static check that agent ``tools:`` frontmatter matches the documented
policy in ``.claude/docs/agent-tool-grants.md``.

The doc declares two things:

1. **Targeted additions** — specific agents that are granted high-impact
   tools (e.g. ``laura-red-team-editor: WebSearch + WebFetch``).
2. **No Bash/TodoWrite policy** — a table listing every agent and asserting
   ``Bash = no`` and ``TodoWrite = no``.

Both must match the agents' ``tools:`` frontmatter. Drift either way (an
agent gains Bash without doc update; an agent loses WebSearch without doc
update) is a policy violation.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


AGENT_FRONTMATTER_NAME_RE = re.compile(r"^\s*name:\s*(.+?)\s*$", re.MULTILINE)
AGENT_FRONTMATTER_TOOLS_RE = re.compile(r"^\s*tools:\s*(.+?)\s*$", re.MULTILINE)
TARGETED_ADDITION_RE = re.compile(
    r"^- `([a-z0-9-]+)`:\s+(.+?)$", re.MULTILINE
)
NO_BASH_TODO_ROW_RE = re.compile(
    r"^\|\s*`([a-z0-9-]+)`\s*\|\s*(no|yes)\s*\|\s*(no|yes)\s*\|", re.MULTILINE
)


@dataclass
class GrantPolicy:
    agent_id: str
    targeted_additions: tuple[str, ...]
    bash: str  # "yes" | "no"
    todowrite: str  # "yes" | "no"


def parse_targeted_additions(doc_text: str) -> dict[str, tuple[str, ...]]:
    """Extract ``- `agent-id`: granted X and Y for …`` entries.

    Looks at the ``## Targeted additions`` section only — entries elsewhere
    are ignored.
    """
    section_match = re.search(
        r"^##\s+Targeted additions\s*\n(.*?)(?=^##\s|\Z)",
        doc_text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return {}
    section = section_match.group(1)
    additions: dict[str, tuple[str, ...]] = {}
    for match in TARGETED_ADDITION_RE.finditer(section):
        agent_id = match.group(1)
        body = match.group(2)
        granted = tuple(
            sorted(
                token
                for token in re.findall(
                    r"`(WebSearch|WebFetch|Bash|TodoWrite|Edit|Read|Write|Grep|Glob)`",
                    body,
                )
            )
        )
        if not granted:
            granted = tuple(
                sorted(
                    re.findall(
                        r"\b(WebSearch|WebFetch|Bash|TodoWrite|Edit|Read|Write|Grep|Glob)\b",
                        body,
                    )
                )
            )
        additions[agent_id] = granted
    return additions


def parse_no_bash_table(doc_text: str) -> dict[str, tuple[str, str]]:
    """Extract per-agent ``Bash``/``TodoWrite`` declarations from the
    ``## No Bash/TodoWrite policy`` table."""
    section_match = re.search(
        r"^##\s+No Bash/TodoWrite policy\s*\n(.*?)(?=^##\s|\Z)",
        doc_text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return {}
    section = section_match.group(1)
    rows: dict[str, tuple[str, str]] = {}
    for match in NO_BASH_TODO_ROW_RE.finditer(section):
        rows[match.group(1)] = (match.group(2).lower(), match.group(3).lower())
    return rows


def load_policy(doc_path: Path) -> dict[str, GrantPolicy]:
    text = doc_path.read_text(encoding="utf-8")
    additions = parse_targeted_additions(text)
    bash_rows = parse_no_bash_table(text)
    all_ids = set(additions) | set(bash_rows)
    policies: dict[str, GrantPolicy] = {}
    for agent_id in sorted(all_ids):
        bash, todo = bash_rows.get(agent_id, ("no", "no"))
        policies[agent_id] = GrantPolicy(
            agent_id=agent_id,
            targeted_additions=additions.get(agent_id, ()),
            bash=bash,
            todowrite=todo,
        )
    return policies


def parse_agent_tools(agent_path: Path) -> tuple[str, set[str]]:
    text = agent_path.read_text(encoding="utf-8")
    name_match = AGENT_FRONTMATTER_NAME_RE.search(text)
    tools_match = AGENT_FRONTMATTER_TOOLS_RE.search(text)
    if not name_match or not tools_match:
        return ("", set())
    name = name_match.group(1).strip()
    raw_tools = tools_match.group(1).strip()
    # Strip Agent(...) calls and split on commas
    raw_tools = re.sub(r"Agent\([^)]*\)", "Agent", raw_tools)
    tokens = {token.strip() for token in raw_tools.split(",") if token.strip()}
    return name, tokens


def check_repo(
    agents_dir: Path, doc_path: Path
) -> tuple[bool, list[str]]:
    policies = load_policy(doc_path)
    errors: list[str] = []
    seen_agents: set[str] = set()

    for agent_path in sorted(agents_dir.glob("*.md")):
        name, tools = parse_agent_tools(agent_path)
        if not name:
            continue
        seen_agents.add(name)

        policy = policies.get(name)
        if policy is None:
            errors.append(
                f"`{name}`: defined under `.claude/agents/` but not listed in "
                "`agent-tool-grants.md` (add a row to the No Bash/TodoWrite "
                "policy table even if Bash/TodoWrite stay no)."
            )
            continue

        # Bash policy enforcement
        has_bash = "Bash" in tools
        if has_bash and policy.bash == "no":
            errors.append(
                f"`{name}` has `Bash` in frontmatter but policy says Bash=no. "
                "Either remove the tool or update agent-tool-grants.md."
            )
        if not has_bash and policy.bash == "yes":
            errors.append(
                f"`{name}` policy says Bash=yes but tool is absent from frontmatter."
            )

        # TodoWrite policy enforcement
        has_todo = "TodoWrite" in tools
        if has_todo and policy.todowrite == "no":
            errors.append(
                f"`{name}` has `TodoWrite` in frontmatter but policy says "
                "TodoWrite=no. Update one of them."
            )
        if not has_todo and policy.todowrite == "yes":
            errors.append(
                f"`{name}` policy says TodoWrite=yes but tool is absent from "
                "frontmatter."
            )

        # Targeted additions: every promised tool must be present
        for required_tool in policy.targeted_additions:
            if required_tool not in tools:
                errors.append(
                    f"`{name}` is documented as granted `{required_tool}` "
                    "but the tool is absent from its frontmatter."
                )

    # Any policy row that names an agent we never saw?
    for declared in sorted(set(policies) - seen_agents):
        errors.append(
            f"`{declared}` appears in agent-tool-grants.md but no agent file "
            "of that name exists under .claude/agents/."
        )

    return not errors, errors


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate agent tools: frontmatter against agent-tool-grants.md policy."
    )
    parser.add_argument(
        "--agents-dir",
        type=Path,
        default=Path(".claude/agents"),
        help="Directory containing agent markdown files",
    )
    parser.add_argument(
        "--doc",
        type=Path,
        default=Path(".claude/docs/agent-tool-grants.md"),
        help="Tool grants policy document",
    )
    args = parser.parse_args(argv)

    passed, errors = check_repo(args.agents_dir, args.doc)
    if passed:
        print("PASS: agent tool grants match agent-tool-grants.md policy.")
        return 0
    print("FAIL: agent tool grants drifted from agent-tool-grants.md policy.")
    for err in errors:
        print(f"  - {err}")
    return 1


if __name__ == "__main__":
    raise SystemExit(_cli())
