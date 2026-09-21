from __future__ import annotations

import csv
import datetime as dt
import hashlib
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from collect_market_discovery import (  # noqa: E402
    CollectionError,
    SOURCE_FILENAMES,
    build_discovery,
    collect_snapshot,
)
import validate_repository as repository_validator  # noqa: E402
from yaml_subset import load_flat_yaml  # noqa: E402


FIXTURE = SCRIPTS / "tests" / "fixtures" / "market-discovery"


class MarketDiscoveryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.sources = {
            key: (FIXTURE / filename).read_bytes()
            for key, filename in SOURCE_FILENAMES.items()
        }

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def collect(self, snapshot_id: str = "fixture-snapshot", *, dry_run: bool = False):
        return collect_snapshot(
            self.sources,
            self.root / snapshot_id,
            snapshot_id,
            dt.date(2026, 9, 14),
            Decimal("5"),
            Decimal("99"),
            dry_run=dry_run,
        )

    def test_normalizes_both_official_contracts_without_forward_estimates(self) -> None:
        result = build_discovery(
            self.sources, dt.date(2026, 9, 14), Decimal("5"), Decimal("99")
        )
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["universe_count"], 4)
        self.assertEqual(result["priority_count"], 2)
        self.assertNotIn("normalized_eps_base_twd", result["rows"][0])
        rows = {(row["market"], row["ticker"]): row for row in result["rows"]}
        self.assertEqual(rows[("TWSE", "TEST1")]["price_twd"], "50.00")
        self.assertEqual(rows[("TPEx", "TEST3")]["displayed_dps_twd"], "3.00")

    def test_dry_run_writes_nothing(self) -> None:
        report = self.collect("fixture-dry-run", dry_run=True)
        self.assertEqual(report["status"], "success")
        self.assertFalse((self.root / "fixture-dry-run").exists())

    def test_snapshot_preserves_raw_sources_and_checksums(self) -> None:
        report = self.collect()
        snapshot = Path(report["snapshot_path"])
        for filename in (
            "manifest.yaml", "market-discovery.csv", "summary.md", "summary.zh-TW.md",
            *SOURCE_FILENAMES.values(),
        ):
            self.assertTrue((snapshot / filename).is_file())
        manifest = load_flat_yaml(snapshot / "manifest.yaml")
        self.assertEqual(manifest["status"], "success")
        digest = hashlib.sha256((snapshot / "market-discovery.csv").read_bytes()).hexdigest()
        self.assertEqual(manifest["discovery_sha256"], digest)
        with (snapshot / "market-discovery.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 4)

    def validate_snapshot(self, snapshot: Path) -> list[str]:
        errors: list[str] = []
        original_root = repository_validator.ROOT
        try:
            repository_validator.ROOT = self.root
            repository_validator.validate_market_discovery_snapshot(
                snapshot, "forward-dividend-yield", errors
            )
        finally:
            repository_validator.ROOT = original_root
        return errors

    def test_repository_validator_accepts_generated_snapshot(self) -> None:
        report = self.collect("validated-snapshot")
        self.assertEqual(self.validate_snapshot(Path(report["snapshot_path"])), [])

    def test_repository_validator_detects_raw_tampering(self) -> None:
        report = self.collect("tampered-snapshot")
        snapshot = Path(report["snapshot_path"])
        with (snapshot / "twse_yield.json").open("ab") as handle:
            handle.write(b"\n")
        errors = self.validate_snapshot(snapshot)
        self.assertTrue(any("raw artifact checksum" in error for error in errors))

    def test_existing_snapshot_is_not_overwritten(self) -> None:
        self.collect()
        with self.assertRaises(CollectionError):
            self.collect()

    def test_concurrent_snapshot_persistence_is_rejected(self) -> None:
        lock = self.root / ".concurrent-snapshot.lock"
        lock.write_text("", encoding="utf-8")
        with self.assertRaises(CollectionError):
            self.collect("concurrent-snapshot")
        self.assertTrue(lock.exists())
        self.assertFalse((self.root / "concurrent-snapshot").exists())

    def test_missing_price_is_partial_and_preserved(self) -> None:
        changed = dict(self.sources)
        changed["twse_price"] = b'[{"Date":"1150914","Code":"TEST1","Name":"Synthetic Listed One","ClosingPrice":"50.00"}]'
        result = build_discovery(
            changed, dt.date(2026, 9, 14), Decimal("5"), Decimal("99")
        )
        self.assertEqual(result["status"], "partial")
        self.assertEqual(result["complete_count"], 3)
        self.assertEqual(result["incomplete_count"], 1)

    def test_mixed_or_wrong_source_date_is_rejected(self) -> None:
        changed = dict(self.sources)
        changed["tpex_price"] = changed["tpex_price"].replace(b"1150914", b"1150913")
        with self.assertRaises(CollectionError):
            build_discovery(changed, dt.date(2026, 9, 14), Decimal("5"), Decimal("99"))

    def test_duplicate_yield_identity_is_rejected(self) -> None:
        changed = dict(self.sources)
        records = changed["twse_yield"].rstrip()[:-1]
        duplicate = b',{"Date":"1150914","Code":"TEST1","Name":"Duplicate","PEratio":"10","DividendYield":"6","PBratio":"1"}]'
        changed["twse_yield"] = records + duplicate
        with self.assertRaises(CollectionError):
            build_discovery(changed, dt.date(2026, 9, 14), Decimal("5"), Decimal("99"))


if __name__ == "__main__":
    unittest.main()
