#!/usr/bin/env python3
"""Validate the durable structure of the investment research repository."""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from yaml_subset import YamlSubsetError, load_flat_yaml


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "README.md",
    "PROJECT_CONTEXT.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    ".ai/context.md",
    ".ai/style.md",
    ".ai/workflow.md",
    "docs/Framework.md",
    "docs/ResearchPrinciples.md",
    "docs/ResearchChecklist.md",
    "docs/Scoring.md",
    "docs/Valuation.md",
    "docs/Workflow.md",
    "docs/proposals/SearchStrategyArchitecture.md",
    "schemas/screen-run.schema.json",
    "schemas/screen-state.schema.json",
    "schemas/screen.schema.json",
    "schemas/strategy.schema.json",
}

REQUIRED_DIRECTORIES = {
    ".ai",
    "docs",
    "companies",
    "industries",
    "models",
    "templates",
    "watchlist",
    "research-log",
    "scripts",
    "schemas",
    "screens",
    "strategies",
}

COMPANY_FILES = {
    "01_business.md",
    "02_financials.md",
    "03_growth_drivers.md",
    "04_eps_model.md",
    "05_timeline.md",
    "06_notes.md",
    "07_open_questions.md",
    "08_thesis.md",
    "09_valuation.md",
    "meta.yaml",
}

META_KEYS = {
    "ticker",
    "company",
    "industry",
    "market",
    "status",
    "confidence",
    "priority",
    "last_update",
    "next_action",
    "watch_items",
}

VALID_STATUS = {"discovery", "qualifying", "active", "monitoring", "archived"}
VALID_CONFIDENCE = {"low", "medium", "high"}
COMPANY_DIR_PATTERN = re.compile(r"^[a-z0-9.]+-[a-z0-9][a-z0-9-]*$")
UNRESOLVED_MARKERS = ("...", "<company", "<ticker", "tbd", "todo")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

STRATEGY_KEYS = {
    "schema_version", "id", "name", "enabled", "validation_state",
    "confidence", "created_on", "last_reviewed", "claim",
    "causal_mechanism", "expected_time_window", "minimum_validation_periods",
    "minimum_validation_unit", "minimum_observations",
    "forecast_interval_hit_rate_target_pct", "median_dps_error_target_pct",
    "candidate_precision_target_pct", "baseline_precision_improvement_target_pp",
    "screen_ids", "confirmation_signals",
    "rejection_signals",
}
SCREEN_KEYS = {
    "schema_version", "id", "title", "enabled", "definition_version",
    "definition_updated_on", "refresh_mode", "timezone",
    "routine_cadence_days", "stale_after_days", "minimum_coverage_pct",
    "target_yield_pct", "minimum_eps_coverage_x", "minimum_downside_yield_pct",
    "market_discovery_adapter", "source_snapshot_directory",
    "universe", "fallback_behavior", "strategy_ids", "required_filters",
    "ranking_factors", "warning_flags", "event_triggers", "primary_sources",
    "fallback_sources", "required_input_fields", "required_output_fields",
}
SCREEN_STATE_KEYS = {
    "schema_version", "screen_id", "status", "definition_version",
    "last_successful_run", "last_data_as_of", "next_due_at",
    "latest_run_path", "updated_at", "reason_codes",
}
VALID_STRATEGY_STATES = {
    "idea", "testing", "validated", "monitoring", "rejected", "archived",
}
VALID_SCREEN_STATES = {"fresh", "due", "overdue", "blocked", "disabled"}
RUN_KEYS = {
    "schema_version", "run_id", "screen_id", "screen_definition_version",
    "screen_definition_hash", "started_at", "finished_at", "status",
    "price_date", "financial_period", "universe_count", "evaluated_count",
    "retained_count", "coverage_pct", "fallback_source_count",
    "failed_source_count", "error_codes", "parameters", "source_urls",
    "results_path", "results_sha256", "summary_path", "confidence",
    "human_review_required",
}
MARKET_DISCOVERY_KEYS = {
    "schema_version", "snapshot_id", "adapter_id", "screen_id",
    "started_at", "finished_at", "status", "data_date",
    "minimum_displayed_yield_pct", "minimum_coverage_pct",
    "universe_count", "complete_count", "incomplete_count", "priority_count",
    "coverage_pct", "twse_yield_count", "twse_price_count",
    "tpex_yield_count", "tpex_price_count", "source_urls", "error_codes",
    "raw_artifacts", "discovery_path", "discovery_sha256", "summary_path",
    "human_review_required",
}
MARKET_DISCOVERY_FIELDS = [
    "market", "ticker", "company", "price_date", "price_twd",
    "displayed_dividend_yield_pct", "displayed_dps_twd", "pe_ratio", "pb_ratio",
    "discovery_priority", "market_data_status", "warning_flags", "source_tier",
    "evidence_reference", "yield_source_url", "price_source_url",
]


def parse_simple_yaml(path: Path) -> dict[str, str]:
    """Read top-level scalar keys without requiring a third-party YAML package."""
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line or raw_line.lstrip().startswith("#") or raw_line[0].isspace():
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$", raw_line)
        if match:
            values[match.group(1)] = (match.group(2) or "").strip().strip("'\"")
    return values


def is_missing(value: str | None) -> bool:
    return value is None or value.strip().lower() in {"", "null", "~", "none", "[]"}


def validate_markdown(path: Path, errors: list[str]) -> None:
    content = path.read_text(encoding="utf-8").strip()
    relative = path.relative_to(ROOT)
    if not content:
        errors.append(f"{relative}: file is empty")
    elif not content.startswith("# "):
        errors.append(f"{relative}: Markdown must begin with one H1 heading")

    for raw_target in MARKDOWN_LINK.findall(content):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local_target = unquote(target.split("#", 1)[0])
        if local_target and not (path.parent / local_target).exists():
            errors.append(f"{relative}: broken relative link: {target}")


def validate_json(path: Path, errors: list[str]) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")


def validate_iso_date(
    value: object, field: str, relative: Path, errors: list[str]
) -> None:
    if not isinstance(value, str):
        errors.append(f"{relative}: {field} must be an ISO date")
        return
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        errors.append(f"{relative}: {field} must use YYYY-MM-DD")


def validate_iso_datetime_or_null(
    value: object, field: str, relative: Path, errors: list[str]
) -> None:
    if value is None:
        return
    if not isinstance(value, str):
        errors.append(f"{relative}: {field} must be an ISO datetime or null")
        return
    try:
        dt.datetime.fromisoformat(value)
    except ValueError:
        errors.append(f"{relative}: {field} must use ISO 8601")


def validate_scalar_list(
    value: object, field: str, relative: Path, errors: list[str]
) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{relative}: {field} must be a non-empty list")
        return
    if any(not isinstance(item, str) or len(item.strip()) < 2 for item in value):
        errors.append(f"{relative}: {field} must contain non-empty strings")
    if len(value) != len(set(value)):
        errors.append(f"{relative}: {field} must not contain duplicates")


def validate_string(
    value: object, field: str, relative: Path, errors: list[str], minimum: int = 3
) -> None:
    if not isinstance(value, str) or len(value.strip()) < minimum:
        errors.append(f"{relative}: {field} must be a string of at least {minimum} characters")


def load_structured_file(
    path: Path, errors: list[str]
) -> dict[str, object] | None:
    try:
        return load_flat_yaml(path)
    except (OSError, YamlSubsetError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML subset: {exc}")
        return None


def registry_entries(kind: str, errors: list[str]) -> list[Path]:
    root = ROOT / kind
    registry_path = root / "registry.yaml"
    values = load_structured_file(registry_path, errors)
    if values is None:
        return []
    relative = registry_path.relative_to(ROOT)
    if set(values) != {"schema_version", "entries"} or values.get("schema_version") != 1:
        errors.append(f"{relative}: registry must contain schema_version 1 and entries")
        return []
    entries = values.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append(f"{relative}: entries must be a non-empty list")
        return []
    if len(entries) != len(set(entries)):
        errors.append(f"{relative}: entries must not contain duplicates")

    paths: list[Path] = []
    for entry in entries:
        if not isinstance(entry, str):
            errors.append(f"{relative}: every entry must be a relative path")
            continue
        path = (root / entry).resolve()
        if root.resolve() not in path.parents:
            errors.append(f"{relative}: entry escapes {kind}/: {entry}")
        elif not path.is_file():
            errors.append(f"{relative}: registered file does not exist: {entry}")
        else:
            paths.append(path)
    definition_name = "strategy.yaml" if kind == "strategies" else "screen.yaml"
    registered = set(paths)
    for unregistered in sorted(root.glob(f"*/{definition_name}")):
        if unregistered.resolve() not in registered:
            errors.append(
                f"{unregistered.relative_to(ROOT)}: definition is not registered"
            )
    return paths


def validate_strategy(path: Path, errors: list[str]) -> dict[str, object] | None:
    values = load_structured_file(path, errors)
    if values is None:
        return None
    relative = path.relative_to(ROOT)
    if set(values) != STRATEGY_KEYS:
        missing = sorted(STRATEGY_KEYS - set(values))
        extra = sorted(set(values) - STRATEGY_KEYS)
        errors.append(f"{relative}: strategy keys differ; missing={missing}, extra={extra}")
    strategy_id = values.get("id")
    if not isinstance(strategy_id, str) or not ID_PATTERN.fullmatch(strategy_id):
        errors.append(f"{relative}: id must be lowercase kebab-case")
    elif path.parent.name != strategy_id:
        errors.append(f"{relative}: id must match its directory name")
    if values.get("schema_version") != 1:
        errors.append(f"{relative}: schema_version must be 1")
    if not isinstance(values.get("enabled"), bool):
        errors.append(f"{relative}: enabled must be boolean")
    if values.get("validation_state") not in VALID_STRATEGY_STATES:
        errors.append(f"{relative}: invalid validation_state")
    if values.get("confidence") not in VALID_CONFIDENCE:
        errors.append(f"{relative}: invalid confidence")
    for field, minimum in (
        ("name", 3), ("claim", 20), ("causal_mechanism", 20),
        ("expected_time_window", 3),
    ):
        validate_string(values.get(field), field, relative, errors, minimum)
    validate_iso_date(values.get("created_on"), "created_on", relative, errors)
    validate_iso_date(values.get("last_reviewed"), "last_reviewed", relative, errors)
    periods = values.get("minimum_validation_periods")
    if not isinstance(periods, int) or periods < 1:
        errors.append(f"{relative}: minimum_validation_periods must be positive")
    observations = values.get("minimum_observations")
    if not isinstance(observations, int) or observations < 1:
        errors.append(f"{relative}: minimum_observations must be positive")
    for field in (
        "forecast_interval_hit_rate_target_pct", "median_dps_error_target_pct",
        "candidate_precision_target_pct", "baseline_precision_improvement_target_pp",
    ):
        value = values.get(field)
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            errors.append(f"{relative}: {field} must be between 0 and 100")
    if values.get("minimum_validation_unit") not in {"quarters", "annual_cohorts", "runs"}:
        errors.append(f"{relative}: invalid minimum_validation_unit")
    for field in ("screen_ids", "confirmation_signals", "rejection_signals"):
        validate_scalar_list(values.get(field), field, relative, errors)
    for filename in ("README.md", "README.zh-TW.md"):
        if not (path.parent / filename).is_file():
            errors.append(f"{relative}: missing {filename}")
    return values


def validate_screen(path: Path, errors: list[str]) -> dict[str, object] | None:
    values = load_structured_file(path, errors)
    if values is None:
        return None
    relative = path.relative_to(ROOT)
    if set(values) != SCREEN_KEYS:
        missing = sorted(SCREEN_KEYS - set(values))
        extra = sorted(set(values) - SCREEN_KEYS)
        errors.append(f"{relative}: screen keys differ; missing={missing}, extra={extra}")
    screen_id = values.get("id")
    if not isinstance(screen_id, str) or not ID_PATTERN.fullmatch(screen_id):
        errors.append(f"{relative}: id must be lowercase kebab-case")
    elif path.parent.name != screen_id:
        errors.append(f"{relative}: id must match its directory name")
    if values.get("schema_version") != 1:
        errors.append(f"{relative}: schema_version must be 1")
    if not isinstance(values.get("enabled"), bool):
        errors.append(f"{relative}: enabled must be boolean")
    version = values.get("definition_version")
    if not isinstance(version, int) or version < 1:
        errors.append(f"{relative}: definition_version must be positive")
    validate_iso_date(values.get("definition_updated_on"), "definition_updated_on", relative, errors)
    if values.get("refresh_mode") not in {"remind_only", "explicit_run"}:
        errors.append(f"{relative}: invalid refresh_mode")
    for field, minimum in (
        ("title", 3), ("timezone", 3), ("universe", 10),
        ("fallback_behavior", 10),
    ):
        validate_string(values.get(field), field, relative, errors, minimum)
    try:
        ZoneInfo(values.get("timezone", ""))
    except (TypeError, ZoneInfoNotFoundError):
        errors.append(f"{relative}: timezone must be a valid IANA time zone")
    cadence = values.get("routine_cadence_days")
    if not isinstance(cadence, int) or cadence < 1:
        errors.append(f"{relative}: routine_cadence_days must be positive")
    stale_after = values.get("stale_after_days")
    if not isinstance(stale_after, int) or stale_after < 0:
        errors.append(f"{relative}: stale_after_days must be non-negative")
    coverage = values.get("minimum_coverage_pct")
    if not isinstance(coverage, (int, float)) or not 0 <= coverage <= 100:
        errors.append(f"{relative}: minimum_coverage_pct must be between 0 and 100")
    for field in ("target_yield_pct", "minimum_eps_coverage_x"):
        value = values.get(field)
        if not isinstance(value, (int, float)) or value <= 0:
            errors.append(f"{relative}: {field} must be positive")
    downside = values.get("minimum_downside_yield_pct")
    if not isinstance(downside, (int, float)) or downside < 0:
        errors.append(f"{relative}: minimum_downside_yield_pct must be non-negative")
    adapter = values.get("market_discovery_adapter")
    if not isinstance(adapter, str) or not re.fullmatch(r"scripts/[a-z0-9_-]+\.py", adapter):
        errors.append(f"{relative}: market_discovery_adapter must be a scripts/*.py path")
    elif not (ROOT / adapter).is_file():
        errors.append(f"{relative}: market_discovery_adapter does not exist")
    if values.get("source_snapshot_directory") != "source-snapshots":
        errors.append(f"{relative}: source_snapshot_directory must be source-snapshots")
    for field in (
        "strategy_ids", "required_filters", "ranking_factors", "warning_flags",
        "event_triggers", "primary_sources", "fallback_sources",
        "required_input_fields", "required_output_fields",
    ):
        validate_scalar_list(values.get(field), field, relative, errors)
    for filename in ("README.md", "README.zh-TW.md", "state.yaml"):
        if not (path.parent / filename).is_file():
            errors.append(f"{relative}: missing {filename}")
    return values


def validate_screen_state(
    path: Path, definition: dict[str, object], errors: list[str]
) -> None:
    values = load_structured_file(path, errors)
    if values is None:
        return
    relative = path.relative_to(ROOT)
    if set(values) != SCREEN_STATE_KEYS:
        missing = sorted(SCREEN_STATE_KEYS - set(values))
        extra = sorted(set(values) - SCREEN_STATE_KEYS)
        errors.append(f"{relative}: state keys differ; missing={missing}, extra={extra}")
    if values.get("schema_version") != 1:
        errors.append(f"{relative}: schema_version must be 1")
    if values.get("screen_id") != definition.get("id"):
        errors.append(f"{relative}: screen_id must match screen definition")
    if values.get("definition_version") != definition.get("definition_version"):
        errors.append(f"{relative}: definition_version must match screen definition")
    if values.get("status") not in VALID_SCREEN_STATES:
        errors.append(f"{relative}: invalid status")
    validate_iso_datetime_or_null(values.get("last_successful_run"), "last_successful_run", relative, errors)
    if values.get("last_data_as_of") is not None:
        validate_iso_date(values.get("last_data_as_of"), "last_data_as_of", relative, errors)
    if values.get("next_due_at") is not None:
        validate_iso_date(values.get("next_due_at"), "next_due_at", relative, errors)
    validate_iso_datetime_or_null(values.get("updated_at"), "updated_at", relative, errors)
    reasons = values.get("reason_codes")
    if not isinstance(reasons, list):
        errors.append(f"{relative}: reason_codes must be a list")
    elif any(not isinstance(reason, str) or len(reason.strip()) < 2 for reason in reasons):
        errors.append(f"{relative}: reason_codes must contain non-empty strings")


def validate_screen_run(
    run_dir: Path, definition: dict[str, object], errors: list[str]
) -> None:
    manifest_path = run_dir / "manifest.yaml"
    values = load_structured_file(manifest_path, errors)
    if values is None:
        return
    relative = manifest_path.relative_to(ROOT)
    if set(values) != RUN_KEYS:
        missing = sorted(RUN_KEYS - set(values))
        extra = sorted(set(values) - RUN_KEYS)
        errors.append(f"{relative}: run keys differ; missing={missing}, extra={extra}")
    if values.get("schema_version") != 1:
        errors.append(f"{relative}: schema_version must be 1")
    if values.get("run_id") != run_dir.name:
        errors.append(f"{relative}: run_id must match its directory name")
    if not isinstance(values.get("run_id"), str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._+-]{9,127}", values["run_id"]
    ):
        errors.append(f"{relative}: run_id has an unsafe or invalid format")
    if values.get("screen_id") != definition.get("id"):
        errors.append(f"{relative}: screen_id must match screen definition")
    if not isinstance(values.get("screen_definition_version"), int):
        errors.append(f"{relative}: screen_definition_version must be an integer")
    elif not 1 <= values["screen_definition_version"] <= definition.get("definition_version", 0):
        errors.append(f"{relative}: screen_definition_version is outside known history")
    definition_hash = values.get("screen_definition_hash")
    if not isinstance(definition_hash, str) or not re.fullmatch(r"[a-f0-9]{64}", definition_hash):
        errors.append(f"{relative}: screen_definition_hash must be SHA-256")
    for field in ("started_at", "finished_at"):
        validate_iso_datetime_or_null(values.get(field), field, relative, errors)
    if values.get("price_date") is not None:
        validate_iso_date(values.get("price_date"), "price_date", relative, errors)
    if values.get("status") not in {"running", "success", "partial", "failed"}:
        errors.append(f"{relative}: invalid run status")
    counts: dict[str, int] = {}
    for field in (
        "universe_count", "evaluated_count", "retained_count",
        "fallback_source_count", "failed_source_count",
    ):
        value = values.get(field)
        if not isinstance(value, int) or value < 0:
            errors.append(f"{relative}: {field} must be a non-negative integer")
        else:
            counts[field] = value
    if all(field in counts for field in ("universe_count", "evaluated_count", "retained_count")):
        if not counts["retained_count"] <= counts["evaluated_count"] <= counts["universe_count"]:
            errors.append(f"{relative}: run counts must satisfy retained <= evaluated <= universe")
    coverage = values.get("coverage_pct")
    if not isinstance(coverage, (int, float)) or not 0 <= coverage <= 100:
        errors.append(f"{relative}: coverage_pct must be between 0 and 100")
    elif counts.get("universe_count", 0) > 0:
        expected = counts.get("evaluated_count", 0) / counts["universe_count"] * 100
        if abs(float(coverage) - expected) > 0.01:
            errors.append(f"{relative}: coverage_pct does not match evaluated/universe")
    for field in ("error_codes", "parameters", "source_urls"):
        if not isinstance(values.get(field), list):
            errors.append(f"{relative}: {field} must be a list")
    if values.get("confidence") not in VALID_CONFIDENCE:
        errors.append(f"{relative}: invalid confidence")
    if not isinstance(values.get("human_review_required"), bool):
        errors.append(f"{relative}: human_review_required must be boolean")
    if values.get("status") == "success":
        if counts.get("failed_source_count") != 0:
            errors.append(f"{relative}: successful run cannot have failed sources")
        if isinstance(coverage, (int, float)) and coverage < definition.get("minimum_coverage_pct", 100):
            errors.append(f"{relative}: successful run is below minimum coverage")

    if values.get("status") not in {"success", "partial"}:
        return
    results_name = values.get("results_path")
    summary_name = values.get("summary_path")
    if not isinstance(results_name, str) or not isinstance(summary_name, str):
        errors.append(f"{relative}: completed runs require result and summary paths")
        return
    results_path = (run_dir / results_name).resolve()
    summary_path = (run_dir / summary_name).resolve()
    if run_dir.resolve() not in results_path.parents or run_dir.resolve() not in summary_path.parents:
        errors.append(f"{relative}: artifact path escapes the run directory")
        return
    for artifact in (results_path, summary_path, summary_path.with_name(f"{summary_path.stem}.zh-TW.md")):
        if not artifact.is_file():
            errors.append(f"{relative}: missing run artifact: {artifact.name}")
    if not results_path.is_file():
        return
    actual_hash = hashlib.sha256(results_path.read_bytes()).hexdigest()
    if values.get("results_sha256") != actual_hash:
        errors.append(f"{relative}: results_sha256 does not match results.csv")
    with results_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != definition.get("required_output_fields"):
            errors.append(f"{relative}: results.csv header differs from screen contract")
        result_count = sum(1 for _ in reader)
    if result_count != values.get("retained_count"):
        errors.append(f"{relative}: retained_count does not match results.csv rows")


def validate_market_discovery_snapshot(
    snapshot_dir: Path, screen_id: str, errors: list[str]
) -> None:
    manifest_path = snapshot_dir / "manifest.yaml"
    values = load_structured_file(manifest_path, errors)
    if values is None:
        return
    relative = manifest_path.relative_to(ROOT)
    if set(values) != MARKET_DISCOVERY_KEYS:
        missing = sorted(MARKET_DISCOVERY_KEYS - set(values))
        extra = sorted(set(values) - MARKET_DISCOVERY_KEYS)
        errors.append(
            f"{relative}: discovery snapshot keys differ; missing={missing}, extra={extra}"
        )
    if values.get("schema_version") != 1:
        errors.append(f"{relative}: schema_version must be 1")
    snapshot_id = values.get("snapshot_id")
    if snapshot_id != snapshot_dir.name:
        errors.append(f"{relative}: snapshot_id must match its directory name")
    if not isinstance(snapshot_id, str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._+-]{9,127}", snapshot_id
    ):
        errors.append(f"{relative}: snapshot_id has an unsafe or invalid format")
    if values.get("adapter_id") != "taiwan-market-discovery":
        errors.append(f"{relative}: unsupported adapter_id")
    if values.get("screen_id") != screen_id:
        errors.append(f"{relative}: screen_id must match its parent screen")
    for field in ("started_at", "finished_at"):
        validate_iso_datetime_or_null(values.get(field), field, relative, errors)
    validate_iso_date(values.get("data_date"), "data_date", relative, errors)
    if values.get("status") not in {"success", "partial", "failed"}:
        errors.append(f"{relative}: invalid snapshot status")
    for field in (
        "minimum_displayed_yield_pct", "minimum_coverage_pct", "coverage_pct",
    ):
        value = values.get(field)
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            errors.append(f"{relative}: {field} must be between 0 and 100")
    counts: dict[str, int] = {}
    for field in (
        "universe_count", "complete_count", "incomplete_count", "priority_count",
        "twse_yield_count", "twse_price_count", "tpex_yield_count", "tpex_price_count",
    ):
        value = values.get(field)
        if not isinstance(value, int) or value < 0:
            errors.append(f"{relative}: {field} must be a non-negative integer")
        else:
            counts[field] = value
    if counts.get("universe_count", 0) < 1:
        errors.append(f"{relative}: universe_count must be positive")
    if all(field in counts for field in ("universe_count", "complete_count", "incomplete_count")):
        if counts["complete_count"] + counts["incomplete_count"] != counts["universe_count"]:
            errors.append(f"{relative}: complete and incomplete counts must equal universe")
    if counts.get("priority_count", 0) > counts.get("universe_count", 0):
        errors.append(f"{relative}: priority_count cannot exceed universe_count")
    coverage = values.get("coverage_pct")
    if isinstance(coverage, (int, float)) and counts.get("universe_count", 0) > 0:
        expected = counts.get("complete_count", 0) / counts["universe_count"] * 100
        if abs(float(coverage) - expected) > 0.01:
            errors.append(f"{relative}: coverage_pct does not match complete/universe")
    for field in ("source_urls", "error_codes", "raw_artifacts"):
        if not isinstance(values.get(field), list):
            errors.append(f"{relative}: {field} must be a list")
    if values.get("human_review_required") is not True:
        errors.append(f"{relative}: human_review_required must be true")

    raw_artifacts = values.get("raw_artifacts")
    if isinstance(raw_artifacts, list):
        if len(raw_artifacts) != 4:
            errors.append(f"{relative}: exactly four raw artifacts are required")
        for entry in raw_artifacts:
            if not isinstance(entry, str) or "=" not in entry:
                errors.append(f"{relative}: invalid raw artifact entry")
                continue
            name, expected_hash = entry.rsplit("=", 1)
            if Path(name).name != name or not re.fullmatch(r"[a-f0-9]{64}", expected_hash):
                errors.append(f"{relative}: invalid raw artifact path or checksum")
                continue
            artifact = snapshot_dir / name
            if not artifact.is_file():
                errors.append(f"{relative}: missing raw artifact: {name}")
            elif hashlib.sha256(artifact.read_bytes()).hexdigest() != expected_hash:
                errors.append(f"{relative}: raw artifact checksum differs: {name}")

    discovery_name = values.get("discovery_path")
    summary_name = values.get("summary_path")
    if discovery_name != "market-discovery.csv" or summary_name != "summary.md":
        errors.append(f"{relative}: unexpected discovery or summary path")
        return
    discovery_path = snapshot_dir / discovery_name
    summary_path = snapshot_dir / summary_name
    for artifact in (
        discovery_path, summary_path, snapshot_dir / "summary.zh-TW.md",
    ):
        if not artifact.is_file():
            errors.append(f"{relative}: missing discovery artifact: {artifact.name}")
    if not discovery_path.is_file():
        return
    actual_hash = hashlib.sha256(discovery_path.read_bytes()).hexdigest()
    if values.get("discovery_sha256") != actual_hash:
        errors.append(f"{relative}: discovery_sha256 does not match market-discovery.csv")
    with discovery_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != MARKET_DISCOVERY_FIELDS:
            errors.append(f"{relative}: market-discovery.csv header differs from contract")
        rows = list(reader)
    if len(rows) != values.get("universe_count"):
        errors.append(f"{relative}: universe_count does not match discovery rows")
    if sum(row.get("market_data_status") == "complete" for row in rows) != values.get(
        "complete_count"
    ):
        errors.append(f"{relative}: complete_count does not match discovery rows")
    identities = [(row.get("market"), row.get("ticker")) for row in rows]
    if len(identities) != len(set(identities)):
        errors.append(f"{relative}: discovery rows contain duplicate market/ticker identities")


def validate_search_contracts(errors: list[str]) -> None:
    strategy_paths = registry_entries("strategies", errors)
    screen_paths = registry_entries("screens", errors)
    strategies: dict[str, dict[str, object]] = {}
    screens: dict[str, dict[str, object]] = {}

    for path in strategy_paths:
        values = validate_strategy(path, errors)
        if values is not None and isinstance(values.get("id"), str):
            strategies[values["id"]] = values
    for path in screen_paths:
        values = validate_screen(path, errors)
        if values is not None and isinstance(values.get("id"), str):
            screens[values["id"]] = values
            validate_screen_state(path.parent / "state.yaml", values, errors)
            runs_root = path.parent / "runs"
            if runs_root.is_dir():
                for run_dir in sorted(runs_root.iterdir()):
                    if run_dir.is_dir() and not run_dir.name.startswith("."):
                        validate_screen_run(run_dir, values, errors)
            snapshots_root = path.parent / "source-snapshots"
            if snapshots_root.is_dir():
                for snapshot_dir in sorted(snapshots_root.iterdir()):
                    if snapshot_dir.is_dir() and not snapshot_dir.name.startswith("."):
                        validate_market_discovery_snapshot(
                            snapshot_dir, values["id"], errors
                        )

    for strategy_id, strategy in strategies.items():
        for screen_id in strategy.get("screen_ids", []):
            if screen_id not in screens:
                errors.append(f"strategies/{strategy_id}/strategy.yaml: unknown screen_id: {screen_id}")
            elif strategy_id not in screens[screen_id].get("strategy_ids", []):
                errors.append(f"strategies/{strategy_id}/strategy.yaml: non-reciprocal screen link: {screen_id}")
    for screen_id, screen in screens.items():
        for strategy_id in screen.get("strategy_ids", []):
            if strategy_id not in strategies:
                errors.append(f"screens/{screen_id}/screen.yaml: unknown strategy_id: {strategy_id}")


def validate_meta(path: Path, errors: list[str]) -> None:
    relative = path.relative_to(ROOT)
    values = parse_simple_yaml(path)
    missing_keys = sorted(META_KEYS - values.keys())
    if missing_keys:
        errors.append(f"{relative}: missing metadata keys: {', '.join(missing_keys)}")
        return

    for key in META_KEYS - {"watch_items"}:
        if is_missing(values.get(key)):
            errors.append(f"{relative}: {key} must have a real value")

    if values.get("status", "").lower() not in VALID_STATUS:
        errors.append(f"{relative}: status must be one of {sorted(VALID_STATUS)}")
    if values.get("confidence", "").lower() not in VALID_CONFIDENCE:
        errors.append(f"{relative}: confidence must be one of {sorted(VALID_CONFIDENCE)}")

    try:
        priority = int(values.get("priority", ""))
        if priority not in range(1, 6):
            raise ValueError
    except ValueError:
        errors.append(f"{relative}: priority must be an integer from 1 to 5")

    try:
        dt.date.fromisoformat(values.get("last_update", ""))
    except ValueError:
        errors.append(f"{relative}: last_update must use YYYY-MM-DD")


def validate_company(company_dir: Path, errors: list[str]) -> None:
    relative = company_dir.relative_to(ROOT)
    if not COMPANY_DIR_PATTERN.fullmatch(company_dir.name):
        errors.append(f"{relative}: directory must match <ticker>-<slug>")

    present = {path.name for path in company_dir.iterdir() if path.is_file()}
    missing = sorted(COMPANY_FILES - present)
    if missing:
        errors.append(f"{relative}: missing core files: {', '.join(missing)}")
        return

    validate_meta(company_dir / "meta.yaml", errors)
    values = parse_simple_yaml(company_dir / "meta.yaml")
    if values.get("ticker") and company_dir.name.split("-", 1)[0] != values["ticker"].lower():
        errors.append(f"{relative}: directory ticker does not match meta.yaml")
    for filename in sorted(COMPANY_FILES - {"meta.yaml"}):
        path = company_dir / filename
        validate_markdown(path, errors)
        lowered = path.read_text(encoding="utf-8").lower()
        found = [marker for marker in UNRESOLVED_MARKERS if marker in lowered]
        if found:
            errors.append(f"{path.relative_to(ROOT)}: unresolved template marker: {found[0]}")


def validate_bilingual_markdown(errors: list[str]) -> None:
    """Require one Traditional Chinese reading copy per canonical Markdown file."""
    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts or path.name.endswith(".zh-TW.md"):
            continue
        companion = path.with_name(f"{path.stem}.zh-TW.md")
        if not companion.is_file():
            errors.append(f"{relative}: missing Traditional Chinese companion: {companion.name}")
        else:
            validate_markdown(companion, errors)


def main() -> int:
    errors: list[str] = []

    for relative in sorted(REQUIRED_FILES):
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{relative}: required file is missing")
        elif path.suffix == ".md":
            validate_markdown(path, errors)
        elif path.suffix == ".json":
            validate_json(path, errors)

    for relative in sorted(REQUIRED_DIRECTORIES):
        if not (ROOT / relative).is_dir():
            errors.append(f"{relative}/: required directory is missing")

    companies_dir = ROOT / "companies"
    if companies_dir.is_dir():
        for child in sorted(companies_dir.iterdir()):
            if child.is_dir() and not child.name.startswith("."):
                validate_company(child, errors)

    validate_bilingual_markdown(errors)
    validate_search_contracts(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
