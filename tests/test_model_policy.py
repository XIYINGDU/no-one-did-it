"""Enforce the all-opus model policy for crew agents.

Principal Author directive: every agent in `.claude/agents/` runs on
`opus`. Logic-laden tasks require the larger model; the crew does no
purely-mechanical work. Any agent that drifts to `sonnet` (or anything
else) must fail this test.
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / ".claude" / "agents"
MODEL_RE = re.compile(r"^model:\s*(\S+)\s*$", re.MULTILINE)
REQUIRED_MODEL = "opus"


class TestModelPolicy(unittest.TestCase):
    def test_every_crew_agent_runs_on_opus(self) -> None:
        offenders: list[tuple[str, str]] = []
        for path in sorted(AGENTS_DIR.glob("*.md")):
            match = MODEL_RE.search(path.read_text(encoding="utf-8"))
            self.assertIsNotNone(
                match, f"{path.name} has no `model:` frontmatter field"
            )
            actual = match.group(1)
            if actual != REQUIRED_MODEL:
                offenders.append((path.name, actual))
        self.assertEqual(
            offenders,
            [],
            msg=(
                "Crew agents must run on opus (logic-laden work). "
                f"Drifted: {offenders}"
            ),
        )


if __name__ == "__main__":
    unittest.main()
