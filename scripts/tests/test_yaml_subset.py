from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from yaml_subset import YamlSubsetError, load_flat_yaml  # noqa: E402


class FlatYamlTest(unittest.TestCase):
    def load_text(self, content: str) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.yaml"
            path.write_text(content, encoding="utf-8")
            return load_flat_yaml(path)

    def test_loads_scalars_and_lists(self) -> None:
        values = self.load_text(
            "schema_version: 1\nenabled: true\nlast_run: null\nentries:\n  - one\n  - two\n"
        )
        self.assertEqual(values["schema_version"], 1)
        self.assertIs(values["enabled"], True)
        self.assertIsNone(values["last_run"])
        self.assertEqual(values["entries"], ["one", "two"])

    def test_rejects_nested_mapping(self) -> None:
        with self.assertRaises(YamlSubsetError):
            self.load_text("outer:\n  nested: value\n")

    def test_rejects_duplicate_key(self) -> None:
        with self.assertRaises(YamlSubsetError):
            self.load_text("id: first\nid: second\n")


if __name__ == "__main__":
    unittest.main()
