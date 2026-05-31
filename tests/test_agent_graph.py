from pathlib import Path
import tempfile
import unittest

from scripts.check_agent_graph import check_graph


def _write_agent(path: Path, name: str, tools: str) -> None:
    path.write_text(
        "\n".join(
            [
                "---",
                f"name: {name}",
                "description: test agent",
                f"tools: {tools}",
                "model: sonnet",
                "---",
                "",
                f"# {name}",
                "",
            ]
        ),
        encoding="utf-8",
    )


class TestAgentGraph(unittest.TestCase):
    def test_repo_graph_passes(self) -> None:
        passed, errors = check_graph(Path(".claude/agents"))
        self.assertTrue(passed, "\n".join(errors))

    def test_cycle_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            agents = Path(tmpdir)
            _write_agent(agents / "joe.md", "jerry-crew-chief", "Agent(alpha), Read")
            _write_agent(agents / "alpha.md", "alpha", "Agent(jerry-crew-chief), Read")
            passed, errors = check_graph(agents)
            self.assertFalse(passed)
            self.assertTrue(any("Cycle detected" in issue for issue in errors))

    def test_depth_overflow_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            agents = Path(tmpdir)
            _write_agent(agents / "joe.md", "jerry-crew-chief", "Agent(a), Read")
            _write_agent(agents / "a.md", "a", "Agent(b), Read")
            _write_agent(agents / "b.md", "b", "Agent(c), Read")
            _write_agent(agents / "c.md", "c", "Read")
            passed, errors = check_graph(agents, max_depth=2)
            self.assertFalse(passed)
            self.assertTrue(any("Depth limit exceeded" in issue for issue in errors))

    def test_unreachable_leaf_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            agents = Path(tmpdir)
            _write_agent(agents / "joe.md", "jerry-crew-chief", "Agent(alpha), Read")
            _write_agent(agents / "alpha.md", "alpha", "Read")
            _write_agent(agents / "orphan.md", "orphan", "Read")
            passed, errors = check_graph(agents)
            self.assertFalse(passed)
            self.assertTrue(any("Leaf agents unreachable" in issue for issue in errors))


if __name__ == "__main__":
    unittest.main()
