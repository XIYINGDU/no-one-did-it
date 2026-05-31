"""Tests for ``scripts/check_tool_grants.py`` — the static check that
``.claude/agents/*.md`` ``tools:`` frontmatter matches the policy declared
in ``.claude/docs/agent-tool-grants.md``."""

from pathlib import Path
import tempfile
import textwrap
import unittest

from scripts.check_tool_grants import check_repo, load_policy, parse_agent_tools


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / ".claude" / "agents"
POLICY_DOC = ROOT / ".claude" / "docs" / "agent-tool-grants.md"


class TestToolGrantsParsing(unittest.TestCase):
    def test_policy_doc_parses(self) -> None:
        policies = load_policy(POLICY_DOC)
        self.assertIn("laura-red-team-editor", policies)
        laura = policies["laura-red-team-editor"]
        self.assertIn("WebSearch", laura.targeted_additions)
        self.assertIn("WebFetch", laura.targeted_additions)
        self.assertEqual(laura.bash, "no")
        self.assertEqual(laura.todowrite, "no")

    def test_agent_frontmatter_parses(self) -> None:
        name, tools = parse_agent_tools(AGENTS_DIR / "laura-red-team-editor.md")
        self.assertEqual(name, "laura-red-team-editor")
        self.assertIn("WebSearch", tools)
        self.assertIn("WebFetch", tools)
        self.assertNotIn("Bash", tools)


class TestRepoPolicyMatches(unittest.TestCase):
    def test_live_repo_passes(self) -> None:
        passed, errors = check_repo(AGENTS_DIR, POLICY_DOC)
        self.assertTrue(passed, msg=f"Tool-grants policy drift:\n  - " + "\n  - ".join(errors))


class TestDriftDetection(unittest.TestCase):
    """Construct a fake agents dir + policy doc that *should* trigger drift,
    and assert each kind of drift is reported. Uses tempdirs so the live
    repo is untouched."""

    def _make_repo(
        self, agent_md: str, policy_md: str
    ) -> tuple[Path, Path, tempfile.TemporaryDirectory[str]]:
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        agents_dir = root / "agents"
        agents_dir.mkdir()
        (agents_dir / "test-agent.md").write_text(agent_md, encoding="utf-8")
        doc = root / "agent-tool-grants.md"
        doc.write_text(policy_md, encoding="utf-8")
        return agents_dir, doc, tmp

    def test_unexpected_bash_grant_is_flagged(self) -> None:
        agent_md = textwrap.dedent(
            """\
            ---
            name: test-agent
            description: stub
            tools: Read, Write, Bash
            model: sonnet
            ---
            body
            """
        )
        policy_md = textwrap.dedent(
            """\
            # Agent Tool Grants

            ## Targeted additions

            ## No Bash/TodoWrite policy

            | Agent ID | Bash | TodoWrite | Rationale |
            |---|---|---|---|
            | `test-agent` | no | no | stub |
            """
        )
        agents_dir, doc, tmp = self._make_repo(agent_md, policy_md)
        try:
            passed, errors = check_repo(agents_dir, doc)
            self.assertFalse(passed)
            self.assertTrue(any("Bash" in err and "policy says Bash=no" in err for err in errors))
        finally:
            tmp.cleanup()

    def test_promised_websearch_missing_is_flagged(self) -> None:
        agent_md = textwrap.dedent(
            """\
            ---
            name: test-agent
            description: stub
            tools: Read, Write
            model: sonnet
            ---
            body
            """
        )
        policy_md = textwrap.dedent(
            """\
            # Agent Tool Grants

            ## Targeted additions

            - `test-agent`: granted `WebSearch` and `WebFetch` for testing.

            ## No Bash/TodoWrite policy

            | Agent ID | Bash | TodoWrite | Rationale |
            |---|---|---|---|
            | `test-agent` | no | no | stub |
            """
        )
        agents_dir, doc, tmp = self._make_repo(agent_md, policy_md)
        try:
            passed, errors = check_repo(agents_dir, doc)
            self.assertFalse(passed)
            self.assertTrue(any("WebSearch" in err and "absent from its frontmatter" in err for err in errors))
            self.assertTrue(any("WebFetch" in err for err in errors))
        finally:
            tmp.cleanup()

    def test_agent_missing_from_policy_doc_is_flagged(self) -> None:
        agent_md = textwrap.dedent(
            """\
            ---
            name: test-agent
            description: stub
            tools: Read
            model: sonnet
            ---
            body
            """
        )
        policy_md = textwrap.dedent(
            """\
            # Agent Tool Grants

            ## Targeted additions

            ## No Bash/TodoWrite policy

            | Agent ID | Bash | TodoWrite | Rationale |
            |---|---|---|---|
            """
        )
        agents_dir, doc, tmp = self._make_repo(agent_md, policy_md)
        try:
            passed, errors = check_repo(agents_dir, doc)
            self.assertFalse(passed)
            self.assertTrue(any("not listed in" in err for err in errors))
        finally:
            tmp.cleanup()

    def test_policy_lists_unknown_agent_is_flagged(self) -> None:
        agent_md = textwrap.dedent(
            """\
            ---
            name: test-agent
            description: stub
            tools: Read
            model: sonnet
            ---
            body
            """
        )
        policy_md = textwrap.dedent(
            """\
            # Agent Tool Grants

            ## Targeted additions

            ## No Bash/TodoWrite policy

            | Agent ID | Bash | TodoWrite | Rationale |
            |---|---|---|---|
            | `test-agent` | no | no | stub |
            | `ghost-agent` | no | no | doesn't exist |
            """
        )
        agents_dir, doc, tmp = self._make_repo(agent_md, policy_md)
        try:
            passed, errors = check_repo(agents_dir, doc)
            self.assertFalse(passed)
            self.assertTrue(any("ghost-agent" in err for err in errors))
        finally:
            tmp.cleanup()


if __name__ == "__main__":
    unittest.main()
