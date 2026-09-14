#!/usr/bin/env python3
"""Report screens that are due for refresh without network access or writes."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from yaml_subset import YamlSubsetError, load_flat_yaml


ROOT = Path(__file__).resolve().parents[1]
SCREENS_ROOT = ROOT / "screens"
REGISTRY = SCREENS_ROOT / "registry.yaml"
VISIBLE_DUE_STATES = {"due", "overdue", "blocked"}


def _parse_date(value: Any, field: str) -> dt.date | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"{field} must be an ISO date, datetime, or null")
    try:
        return dt.datetime.fromisoformat(value).date()
    except ValueError:
        try:
            return dt.date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(f"{field} must use ISO 8601: {value}") from exc


def _due_state(
    definition: dict[str, Any], state: dict[str, Any], as_of: dt.date
) -> tuple[str, list[str]]:
    reasons = list(state.get("reason_codes", []))
    if not definition["enabled"]:
        return "disabled", reasons or ["screen_disabled"]
    if state.get("status") == "blocked":
        return "blocked", reasons or ["screen_blocked"]
    if state.get("last_successful_run") is None:
        return "due", sorted(set(reasons + ["never_run"]))
    if state.get("definition_version") != definition.get("definition_version"):
        return "due", sorted(set(reasons + ["definition_changed"]))
    if state.get("status") in {"due", "overdue"}:
        return state["status"], reasons or ["state_marked_due"]

    next_due = _parse_date(state.get("next_due_at"), "next_due_at")
    if next_due is None:
        return "blocked", sorted(set(reasons + ["next_due_missing"]))
    if as_of < next_due:
        return "fresh", reasons

    stale_after_days = definition["stale_after_days"]
    if as_of > next_due + dt.timedelta(days=stale_after_days):
        return "overdue", sorted(set(reasons + ["stale_after_exceeded"]))
    return "due", sorted(set(reasons + ["scheduled_refresh_due"]))


def collect_refresh_status(as_of: dt.date | None) -> list[dict[str, Any]]:
    registry = load_flat_yaml(REGISTRY)
    entries = registry.get("entries")
    if registry.get("schema_version") != 1 or not isinstance(entries, list):
        raise ValueError("screens/registry.yaml has an invalid contract")

    results: list[dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, str):
            raise ValueError("screen registry entries must be paths")
        definition_path = (SCREENS_ROOT / entry).resolve()
        if SCREENS_ROOT.resolve() not in definition_path.parents:
            raise ValueError(f"screen registry path escapes screens/: {entry}")
        definition = load_flat_yaml(definition_path)
        state_path = definition_path.parent / "state.yaml"
        state = load_flat_yaml(state_path)
        try:
            screen_as_of = as_of or dt.datetime.now(
                ZoneInfo(definition["timezone"])
            ).date()
        except (KeyError, TypeError, ZoneInfoNotFoundError) as exc:
            raise ValueError(f"invalid timezone for {definition.get('id', entry)}") from exc
        status, reasons = _due_state(definition, state, screen_as_of)
        results.append(
            {
                "id": definition["id"],
                "title": definition["title"],
                "evaluated_as_of": screen_as_of.isoformat(),
                "status": status,
                "reason_codes": reasons,
                "last_successful_run": state.get("last_successful_run"),
                "last_data_as_of": state.get("last_data_as_of"),
                "next_due_at": state.get("next_due_at"),
                "latest_run_path": state.get("latest_run_path"),
            }
        )
    return sorted(results, key=lambda item: item["id"])


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--due-only",
        action="store_true",
        help="show only due, overdue, or blocked screens",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument(
        "--as-of",
        type=dt.date.fromisoformat,
        default=None,
        help="evaluate status on YYYY-MM-DD (default: each screen's local date)",
    )
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    try:
        results = collect_refresh_status(args.as_of)
    except (KeyError, OSError, ValueError, YamlSubsetError) as exc:
        print(f"Refresh check failed: {exc}", file=sys.stderr)
        return 1

    if args.due_only:
        results = [item for item in results if item["status"] in VISIBLE_DUE_STATES]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    if not results:
        print("No screens need refresh.")
        return 0

    display_date = args.as_of.isoformat() if args.as_of else "each screen's local date"
    print(f"Screen refresh status as of {display_date}:")
    for item in results:
        reasons = ", ".join(item["reason_codes"]) or "none"
        next_due = item["next_due_at"] or "not set"
        print(f"- {item['id']}: {item['status']} (reasons: {reasons}; next due: {next_due})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
