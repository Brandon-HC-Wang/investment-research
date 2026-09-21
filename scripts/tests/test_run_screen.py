from __future__ import annotations

import csv
import datetime as dt
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_screen import RunError, execute_screen  # noqa: E402
import validate_repository as repository_validator  # noqa: E402
from yaml_subset import load_flat_yaml  # noqa: E402


FIXTURE = SCRIPTS / "tests" / "fixtures" / "forward-dividend-yield-input.csv"


class RunScreenTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.screen_dir = self.root / "screens" / "forward-dividend-yield"
        self.screen_dir.mkdir(parents=True)
        source = ROOT / "screens" / "forward-dividend-yield"
        shutil.copy(source / "screen.yaml", self.screen_dir / "screen.yaml")
        shutil.copy(source / "state.yaml", self.screen_dir / "state.yaml")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def execute(
        self,
        run_id: str,
        *,
        input_path: Path = FIXTURE,
        as_of: dt.date = dt.date(2026, 9, 14),
        dry_run: bool = False,
    ):
        return execute_screen(
            "forward-dividend-yield",
            input_path,
            as_of,
            run_id,
            root=self.root,
            dry_run=dry_run,
        )

    def test_dry_run_does_not_write(self) -> None:
        report = self.execute("fixture-dry-run", dry_run=True)
        self.assertEqual(report["status"], "success")
        self.assertFalse((self.screen_dir / "runs").exists())
        self.assertEqual(load_flat_yaml(self.screen_dir / "state.yaml")["status"], "due")

    def test_success_writes_immutable_artifacts_and_updates_state(self) -> None:
        report = self.execute("2026-09-14T120000+08-00")
        run_dir = self.root / report["run_path"]
        self.assertEqual(report["retained_count"], 2)
        for filename in ("manifest.yaml", "results.csv", "summary.md", "summary.zh-TW.md"):
            self.assertTrue((run_dir / filename).is_file())
        manifest = load_flat_yaml(run_dir / "manifest.yaml")
        self.assertEqual(manifest["status"], "success")
        self.assertEqual(len(manifest["screen_definition_hash"]), 64)
        state = load_flat_yaml(self.screen_dir / "state.yaml")
        self.assertEqual(state["status"], "fresh")
        self.assertEqual(state["next_due_at"], "2026-09-21")
        self.assertEqual(state["latest_run_path"], "runs/2026-09-14T120000+08-00")
        with (run_dir / "results.csv").open(newline="", encoding="utf-8") as handle:
            results = list(csv.DictReader(handle))
        self.assertEqual([row["ticker"] for row in results], ["SYNTH-A", "SYNTH-B"])
        self.assertEqual([row["rank"] for row in results], ["1", "2"])

    def test_duplicate_run_id_is_rejected_without_overwrite(self) -> None:
        self.execute("duplicate-run")
        manifest = self.screen_dir / "runs" / "duplicate-run" / "manifest.yaml"
        original = manifest.read_text(encoding="utf-8")
        with self.assertRaises(RunError):
            self.execute("duplicate-run")
        self.assertEqual(manifest.read_text(encoding="utf-8"), original)

    def test_unsafe_run_id_is_rejected_without_write(self) -> None:
        with self.assertRaises(RunError):
            self.execute("../escaped-run")
        self.assertFalse((self.screen_dir / "runs").exists())
        self.assertFalse((self.root / "escaped-run").exists())

    def test_short_run_id_is_rejected(self) -> None:
        with self.assertRaises(RunError):
            self.execute("short")

    def test_as_of_must_match_input_price_date(self) -> None:
        with self.assertRaises(RunError):
            self.execute("mismatched-date", as_of=dt.date(2026, 9, 13))
        self.assertFalse((self.screen_dir / "runs").exists())

    def test_concurrent_persisted_run_is_rejected(self) -> None:
        runs_dir = self.screen_dir / "runs"
        runs_dir.mkdir()
        lock = runs_dir / ".run-screen.lock"
        lock.write_text("", encoding="utf-8")
        with self.assertRaises(RunError):
            self.execute("concurrent-run")
        self.assertTrue(lock.exists())
        self.assertFalse((runs_dir / "concurrent-run").exists())

    def validate_run(self, run_dir: Path) -> list[str]:
        definition = load_flat_yaml(self.screen_dir / "screen.yaml")
        errors: list[str] = []
        original_root = repository_validator.ROOT
        try:
            repository_validator.ROOT = self.root
            repository_validator.validate_screen_run(run_dir, definition, errors)
        finally:
            repository_validator.ROOT = original_root
        return errors

    def test_repository_validator_accepts_generated_run(self) -> None:
        report = self.execute("validated-run")
        self.assertEqual(self.validate_run(self.root / report["run_path"]), [])

    def test_repository_validator_detects_result_tampering(self) -> None:
        report = self.execute("tampered-run")
        run_dir = self.root / report["run_path"]
        with (run_dir / "results.csv").open("a", encoding="utf-8") as handle:
            handle.write("tampered\n")
        errors = self.validate_run(run_dir)
        self.assertTrue(any("results_sha256" in error for error in errors))

    def test_partial_run_does_not_advance_state(self) -> None:
        input_path = self.root / "partial.csv"
        content = FIXTURE.read_text(encoding="utf-8").replace(
            "TEST,SYNTH-C,Synthetic Gamma,2026-09-14,100,",
            "TEST,SYNTH-C,Synthetic Gamma,2026-09-14,invalid,",
        )
        input_path.write_text(content, encoding="utf-8")
        report = self.execute("partial-run", input_path=input_path)
        self.assertEqual(report["status"], "partial")
        self.assertEqual(load_flat_yaml(self.screen_dir / "state.yaml")["status"], "due")
        manifest = load_flat_yaml(self.screen_dir / "runs" / "partial-run" / "manifest.yaml")
        self.assertEqual(manifest["failed_source_count"], 1)

    def test_duplicate_company_row_makes_run_partial(self) -> None:
        input_path = self.root / "duplicate-row.csv"
        lines = FIXTURE.read_text(encoding="utf-8").splitlines()
        input_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")
        report = self.execute("duplicate-row-run", input_path=input_path)
        self.assertEqual(report["status"], "partial")
        self.assertEqual(report["universe_count"], 4)
        self.assertEqual(report["evaluated_count"], 3)


if __name__ == "__main__":
    unittest.main()
