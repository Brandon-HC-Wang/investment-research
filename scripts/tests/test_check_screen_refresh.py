from __future__ import annotations

import datetime as dt
import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from check_screen_refresh import _due_state  # noqa: E402


class DueStateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.definition = {
            "enabled": True,
            "definition_version": 1,
            "stale_after_days": 7,
        }
        self.state = {
            "status": "fresh",
            "definition_version": 1,
            "last_successful_run": "2026-09-01T09:00:00+08:00",
            "next_due_at": "2026-09-08",
            "reason_codes": [],
        }

    def test_never_run_is_due(self) -> None:
        self.state["last_successful_run"] = None
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 1))
        self.assertEqual(status, "due")
        self.assertIn("never_run", reasons)

    def test_future_due_date_is_fresh(self) -> None:
        status, _ = _due_state(self.definition, self.state, dt.date(2026, 9, 7))
        self.assertEqual(status, "fresh")

    def test_due_date_is_due(self) -> None:
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 8))
        self.assertEqual(status, "due")
        self.assertIn("scheduled_refresh_due", reasons)

    def test_stale_tolerance_exceeded_is_overdue(self) -> None:
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 16))
        self.assertEqual(status, "overdue")
        self.assertIn("stale_after_exceeded", reasons)

    def test_definition_change_is_due(self) -> None:
        self.definition["definition_version"] = 2
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 2))
        self.assertEqual(status, "due")
        self.assertIn("definition_changed", reasons)

    def test_failed_or_blocked_state_remains_blocked(self) -> None:
        self.state["status"] = "blocked"
        self.state["reason_codes"] = ["source_unavailable"]
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 2))
        self.assertEqual(status, "blocked")
        self.assertEqual(reasons, ["source_unavailable"])

    def test_event_marked_state_is_due_before_scheduled_date(self) -> None:
        self.state["status"] = "due"
        self.state["reason_codes"] = ["new_quarterly_filing"]
        self.state["next_due_at"] = "2026-10-01"
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 2))
        self.assertEqual(status, "due")
        self.assertEqual(reasons, ["new_quarterly_filing"])

    def test_disabled_definition_is_disabled(self) -> None:
        self.definition["enabled"] = False
        status, reasons = _due_state(self.definition, self.state, dt.date(2026, 9, 2))
        self.assertEqual(status, "disabled")
        self.assertIn("screen_disabled", reasons)


if __name__ == "__main__":
    unittest.main()
