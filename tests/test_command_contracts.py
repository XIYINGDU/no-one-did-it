from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / ".claude" / "commands"
AGENTS_DIR = ROOT / ".claude" / "agents"

NAME_RE = re.compile(r"^\s*name:\s*(.+?)\s*$", re.MULTILINE)
OWNER_RE = re.compile(r"^\s*owner:\s*(.+?)\s*$", re.MULTILINE)


def _extract_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return "", text
    frontmatter = parts[0].removeprefix("---\n")
    body = parts[1]
    return frontmatter, body


def _agent_ids() -> set[str]:
    ids: set[str] = set()
    for path in AGENTS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        frontmatter, _ = _extract_frontmatter(text)
        match = NAME_RE.search(frontmatter)
        if match:
            ids.add(match.group(1).strip())
    return ids


class TestCommandContracts(unittest.TestCase):
    def test_commands_declare_valid_owner_and_dispatch_owner(self) -> None:
        agents = _agent_ids()
        self.assertTrue(agents, "No agents discovered for owner validation.")

        for path in sorted(COMMANDS_DIR.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            frontmatter, body = _extract_frontmatter(text)
            owner_match = OWNER_RE.search(frontmatter)
            self.assertIsNotNone(owner_match, f"{path.name} missing `owner:` in frontmatter")

            owner = owner_match.group(1).strip()
            self.assertIn(owner, agents, f"{path.name} owner `{owner}` not found in .claude/agents")
            self.assertIn(
                f"Dispatch the `{owner}` agent",
                body,
                f"{path.name} must dispatch declared owner agent",
            )


if __name__ == "__main__":
    unittest.main()
