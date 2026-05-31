from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / ".claude" / "agents"
RATIONALS_DOC = ROOT / ".claude" / "docs" / "agent-tool-grants.md"
DIAGRAM_VALIDATOR = ROOT / "scripts" / "validate_diagram_artifact.py"

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)
TOOLS_RE = re.compile(r"^tools:\s*(.+?)\s*$", re.MULTILINE)


def _extract_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return ""
    return parts[0].removeprefix("---\n")


class TestAgentToolMinimums(unittest.TestCase):
    def _agent_fields(self, path: Path) -> tuple[str, str]:
        text = path.read_text(encoding="utf-8")
        frontmatter = _extract_frontmatter(text)
        name_match = NAME_RE.search(frontmatter)
        tools_match = TOOLS_RE.search(frontmatter)
        self.assertIsNotNone(name_match, f"Missing name in {path.name}")
        self.assertIsNotNone(tools_match, f"Missing tools in {path.name}")
        return name_match.group(1).strip(), tools_match.group(1).strip()

    def test_laura_has_required_web_tools(self) -> None:
        """The red-team editor must source adversarial evidence in real time."""
        _, tools = self._agent_fields(AGENTS_DIR / "laura-red-team-editor.md")
        self.assertIn("WebSearch", tools)
        self.assertIn("WebFetch", tools)

    def test_researchers_have_web_tools(self) -> None:
        for researcher in (
            "shirley-historical-case-researcher.md",
            "selina-war-statecraft-researcher.md",
            "warren-ai-technology-researcher.md",
            "loki-public-law-politics-researcher.md",
        ):
            _, tools = self._agent_fields(AGENTS_DIR / researcher)
            self.assertIn("WebSearch", tools, researcher)
            self.assertIn("WebFetch", tools, researcher)

    def test_alan_has_web_tools_for_authority_lookups(self) -> None:
        _, tools = self._agent_fields(AGENTS_DIR / "alan-expert-reviewer.md")
        self.assertIn("WebSearch", tools)
        self.assertIn("WebFetch", tools)

    def test_diagram_validator_exists(self) -> None:
        """Jade is gone (consolidated out) but the deterministic
        diagram-validation script remains usable from any agent that needs
        to validate a Mermaid responsibility-chain map."""
        self.assertTrue(DIAGRAM_VALIDATOR.exists())

    def test_no_agents_have_bash_or_todowrite(self) -> None:
        for path in sorted(AGENTS_DIR.glob("*.md")):
            _, tools = self._agent_fields(path)
            self.assertNotIn("Bash", tools, f"{path.name} unexpectedly has Bash")
            self.assertNotIn("TodoWrite", tools, f"{path.name} unexpectedly has TodoWrite")

    def test_no_bash_todowrite_rationale_lists_all_agents(self) -> None:
        text = RATIONALS_DOC.read_text(encoding="utf-8")
        for path in sorted(AGENTS_DIR.glob("*.md")):
            agent_id, _ = self._agent_fields(path)
            self.assertIn(f"`{agent_id}`", text, f"Missing rationale row for {agent_id}")


if __name__ == "__main__":
    unittest.main()
