#!/usr/bin/env python3
"""Validate agent delegation graph constraints for .claude/agents."""

from __future__ import annotations

import argparse
import re
from collections import deque
from dataclasses import dataclass
from pathlib import Path

NAME_RE = re.compile(r"^\s*name:\s*(.+?)\s*$")
TOOLS_RE = re.compile(r"^\s*tools:\s*(.+?)\s*$")
AGENT_CALL_RE = re.compile(r"Agent\(([^)]*)\)")
CREW_EXEMPT_RE = re.compile(r"^\s*crew_exempt:\s*(true|false)\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class AgentSpec:
    name: str
    delegates: tuple[str, ...]
    path: Path
    crew_exempt: bool = False


def _extract_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return "\n".join(lines[1:idx])
    return ""


def _extract_name(frontmatter: str) -> str | None:
    for line in frontmatter.splitlines():
        match = NAME_RE.match(line)
        if match:
            return match.group(1).strip()
    return None


def _extract_tools(frontmatter: str) -> str:
    for line in frontmatter.splitlines():
        match = TOOLS_RE.match(line)
        if match:
            return match.group(1).strip()
    return ""


def _extract_delegates(tools: str) -> tuple[str, ...]:
    delegates: list[str] = []
    for call in AGENT_CALL_RE.findall(tools):
        delegates.extend(part.strip() for part in call.split(",") if part.strip())
    return tuple(delegates)


def _extract_crew_exempt(frontmatter: str) -> bool:
    for line in frontmatter.splitlines():
        match = CREW_EXEMPT_RE.match(line)
        if match:
            return match.group(1).lower() == "true"
    return False


def load_agents(agents_dir: Path) -> dict[str, AgentSpec]:
    agents: dict[str, AgentSpec] = {}
    for path in sorted(agents_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        frontmatter = _extract_frontmatter(text)
        name = _extract_name(frontmatter)
        if not name:
            continue
        agents[name] = AgentSpec(
            name=name,
            delegates=_extract_delegates(_extract_tools(frontmatter)),
            path=path,
            crew_exempt=_extract_crew_exempt(frontmatter),
        )
    return agents


def _find_cycles(graph: dict[str, tuple[str, ...]]) -> list[list[str]]:
    state: dict[str, int] = {node: 0 for node in graph}
    stack: list[str] = []
    cycles: list[list[str]] = []

    def dfs(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for nxt in graph[node]:
            if nxt not in graph:
                continue
            if state[nxt] == 0:
                dfs(nxt)
            elif state[nxt] == 1:
                idx = stack.index(nxt)
                cycles.append(stack[idx:] + [nxt])
        stack.pop()
        state[node] = 2

    for node in graph:
        if state[node] == 0:
            dfs(node)
    return cycles


def check_graph(
    agents_dir: Path, root_agent: str = "jerry-crew-chief", max_depth: int = 2
) -> tuple[bool, list[str]]:
    agents = load_agents(agents_dir)
    errors: list[str] = []
    if root_agent not in agents:
        return False, [f"Missing required root agent `{root_agent}` in {agents_dir}."]

    graph = {name: spec.delegates for name, spec in agents.items()}
    for name, delegates in graph.items():
        for child in delegates:
            if child not in graph:
                errors.append(f"`{name}` delegates to unknown agent `{child}`.")

    for cycle in _find_cycles(graph):
        errors.append(f"Cycle detected: {' -> '.join(cycle)}")

    depth: dict[str, int] = {root_agent: 0}
    queue: deque[str] = deque([root_agent])
    while queue:
        node = queue.popleft()
        for child in graph.get(node, ()):
            if child in depth:
                continue
            depth[child] = depth[node] + 1
            queue.append(child)

    too_deep = sorted((node, d) for node, d in depth.items() if d > max_depth)
    if too_deep:
        errors.append(
            "Depth limit exceeded from "
            f"`{root_agent}` (max {max_depth}): "
            + ", ".join(f"{node}={d}" for node, d in too_deep)
        )

    for parent, children in graph.items():
        if parent not in depth:
            continue
        for child in children:
            if child not in depth:
                continue
            if depth[child] <= depth[parent]:
                errors.append(
                    f"Back-edge/cross-layer edge disallowed: `{parent}` -> `{child}` "
                    f"(depth {depth[parent]} -> {depth[child]})."
                )

    exempt = {name for name, spec in agents.items() if spec.crew_exempt}
    leaves = {name for name, children in graph.items() if not children}
    unreachable_leaves = sorted(
        leaf for leaf in leaves if leaf not in depth and leaf not in exempt
    )
    if unreachable_leaves:
        errors.append(
            "Leaf agents unreachable from "
            f"`{root_agent}`: {', '.join(unreachable_leaves)}"
        )

    return not errors, errors


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate delegation graph for agent frontmatter.")
    parser.add_argument(
        "--agents-dir",
        type=Path,
        default=Path(".claude/agents"),
        help="Directory containing agent markdown files",
    )
    parser.add_argument(
        "--root-agent",
        default="jerry-crew-chief",
        help="Root orchestration agent for depth and reachability checks",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=2,
        help="Maximum delegation depth from root agent",
    )
    args = parser.parse_args(argv)

    passed, errors = check_graph(
        agents_dir=args.agents_dir,
        root_agent=args.root_agent,
        max_depth=args.max_depth,
    )
    if passed:
        print("PASS: agent delegation graph is acyclic and depth-bounded.")
        return 0

    print("FAIL: agent delegation graph constraints violated.")
    for error in errors:
        print(f"  - {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(_cli())
