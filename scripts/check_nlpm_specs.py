#!/usr/bin/env python3
"""Static checker for NLPM test specs under ``.nlpm-test/``.

Validates:

1. Every spec lives at ``.nlpm-test/<name>.spec.md`` (the location
   ``/nlpm:test`` reads from — see ``skills/nlpm/testing/SKILL.md`` in the
   nlpm plugin).
2. Each spec has frontmatter with ``artifact:``, ``type:``, ``min_score:``.
3. The ``artifact:`` path resolves to an existing file in the repo.
4. The ``type:`` matches the artifact's location (agent / skill / command /
   rule / hook / prompt).
5. Each cell lead agent has a spec under ``.nlpm-test/``.

This is a static check — it does not invoke any agent. The runtime runner
is the ``/nlpm:test`` plugin command. Static check catches malformed,
mis-located, or unmapped specs before they ever reach the runner.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SPEC_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
FRONTMATTER_FIELD_RE = re.compile(r"^([a-z_]+):\s*(.+?)\s*$", re.MULTILINE)
AGENT_PATH_RE = re.compile(r"^\.claude/agents/[a-z0-9-]+\.md$")
SKILL_PATH_RE = re.compile(r"^\.claude/skills/[a-z0-9-]+/SKILL\.md$")
RULE_PATH_RE = re.compile(r"^\.claude/rules/[0-9]{2}-[a-z0-9-]+\.md$")
COMMAND_PATH_RE = re.compile(r"^\.claude/commands/[a-z0-9-]+\.md$")
HOOK_PATH_RE = re.compile(r"^\.claude/hooks/[a-z0-9-_]+\.py$")

TYPE_BY_PATH = (
    (AGENT_PATH_RE, "agent"),
    (SKILL_PATH_RE, "skill"),
    (RULE_PATH_RE, "rule"),
    (COMMAND_PATH_RE, "command"),
    (HOOK_PATH_RE, "hook"),
)

REQUIRED_FIELDS = ("artifact", "type", "min_score")

# Cell leads that must each have a spec (the operating-competence
# acceptance bar for /nlpm:test coverage).
REQUIRED_LEAD_SPECS = (
    "jerry-crew-chief",
    "bonnie-book-architect",
    "wayne-narrative-lead",
    "delon-research-director",
    "stephen-fact-check-director",
    "laura-red-team-editor",
    "nancy-legal-risk-counsel",
    "blair-market-strategist",
    "alan-expert-reviewer",
)


@dataclass
class SpecReport:
    path: str
    issues: list[str]

    @property
    def passed(self) -> bool:
        return not self.issues


def _parse_frontmatter(text: str) -> dict[str, str] | None:
    match = SPEC_FRONTMATTER_RE.match(text)
    if not match:
        return None
    return {
        field.group(1): field.group(2).strip()
        for field in FRONTMATTER_FIELD_RE.finditer(match.group(1))
    }


def _classify_artifact(artifact_path: str) -> str | None:
    for pattern, label in TYPE_BY_PATH:
        if pattern.match(artifact_path):
            return label
    return None


def validate_spec(spec_path: Path, repo_root: Path) -> SpecReport:
    issues: list[str] = []
    text = spec_path.read_text(encoding="utf-8")
    fm = _parse_frontmatter(text)
    if fm is None:
        return SpecReport(spec_path.as_posix(), ["spec is missing frontmatter (`---` block)"])

    for field in REQUIRED_FIELDS:
        if field not in fm:
            issues.append(f"frontmatter is missing required field `{field}:`")

    artifact_value = fm.get("artifact", "").strip()
    if artifact_value:
        artifact_resolved = repo_root / artifact_value
        if not artifact_resolved.exists():
            issues.append(
                f"frontmatter `artifact: {artifact_value}` does not exist on disk"
            )

        inferred = _classify_artifact(artifact_value)
        declared = fm.get("type", "").strip().lower()
        if inferred and declared and inferred != declared:
            issues.append(
                f"frontmatter `type: {declared}` does not match inferred type "
                f"`{inferred}` from path `{artifact_value}`"
            )

    if "min_score" in fm:
        try:
            score_int = int(fm["min_score"])
            if not 0 <= score_int <= 100:
                issues.append(
                    f"frontmatter `min_score: {fm['min_score']}` must be 0-100"
                )
        except ValueError:
            issues.append(
                f"frontmatter `min_score: {fm['min_score']}` must be an integer"
            )

    # Path must live under .nlpm-test/
    rel = spec_path.relative_to(repo_root).as_posix()
    if not rel.startswith(".nlpm-test/"):
        issues.append(
            f"spec lives at `{rel}`; nlpm:test reads from `.nlpm-test/` only"
        )
    if not rel.endswith(".spec.md"):
        issues.append(f"spec filename `{rel}` must end with `.spec.md`")

    return SpecReport(spec_path.as_posix(), issues)


def check_coverage(spec_dir: Path) -> list[str]:
    found_stems = {p.stem.replace(".spec", "") for p in spec_dir.glob("*.spec.md")}
    missing: list[str] = []
    for lead in REQUIRED_LEAD_SPECS:
        if lead not in found_stems:
            missing.append(f"missing required spec: .nlpm-test/{lead}.spec.md")
    return missing


def check_repo(spec_dir: Path, repo_root: Path) -> tuple[bool, list[SpecReport], list[str]]:
    spec_dir = spec_dir if spec_dir.is_absolute() else (repo_root / spec_dir)
    reports = [validate_spec(p, repo_root) for p in sorted(spec_dir.glob("*.spec.md"))]
    coverage_gaps = check_coverage(spec_dir)
    passed = all(r.passed for r in reports) and not coverage_gaps
    return passed, reports, coverage_gaps


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Static check for nlpm:test specs.")
    parser.add_argument(
        "--spec-dir", type=Path, default=Path(".nlpm-test"),
        help="Directory containing *.spec.md files",
    )
    parser.add_argument(
        "--repo-root", type=Path, default=Path("."),
        help="Repo root for resolving `artifact:` paths",
    )
    args = parser.parse_args(argv)

    repo_root = args.repo_root.resolve()
    passed, reports, coverage_gaps = check_repo(args.spec_dir, repo_root)

    for report in reports:
        status = "PASS" if report.passed else "FAIL"
        print(f"{status}: {report.path}")
        for issue in report.issues:
            print(f"  - {issue}")

    if coverage_gaps:
        print()
        print("FAIL: coverage gaps")
        for gap in coverage_gaps:
            print(f"  - {gap}")

    if passed:
        print(f"\nPASS: all {len(reports)} specs valid; all required lead specs present.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(_cli())
