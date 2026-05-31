from pathlib import Path
import unittest

from scripts.sync_five_over_rules import (
    END_MARKER,
    HEADING,
    PROJECT_ROOT,
    SOURCE_FILE,
    START_MARKER,
    extract_canonical_rules,
    find_targets,
    sync_one,
)


class TestFiveOverRulesSync(unittest.TestCase):
    def test_targets_cover_expected_surface(self) -> None:
        targets = find_targets(PROJECT_ROOT)
        self.assertGreaterEqual(len(targets), 20)

    def test_sync_is_idempotent(self) -> None:
        canonical = extract_canonical_rules(SOURCE_FILE)
        targets = find_targets(PROJECT_ROOT)
        drifted = []
        for path in targets:
            _, changed = sync_one(path, canonical)
            if changed:
                drifted.append(path.relative_to(PROJECT_ROOT).as_posix())
        self.assertEqual(drifted, [], f"Drifted files: {drifted}")

    def test_markers_exist_for_all_targets(self) -> None:
        targets = find_targets(PROJECT_ROOT)
        for path in targets:
            rel = path.relative_to(PROJECT_ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            self.assertIn(HEADING, text, rel)
            self.assertIn(START_MARKER, text, rel)
            self.assertIn(END_MARKER, text, rel)


if __name__ == "__main__":
    unittest.main()
