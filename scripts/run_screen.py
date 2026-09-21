#!/usr/bin/env python3
"""Execute one registered screen from an offline CSV and persist an immutable run."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from yaml_subset import atomic_write_flat_yaml, dump_flat_yaml, load_flat_yaml


ROOT = Path(__file__).resolve().parents[1]
SCREENS_ROOT = ROOT / "screens"
SUPPORTED_SCREEN = "forward-dividend-yield"
RUN_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]{9,127}")
NUMERIC_INPUTS = (
    "price_twd",
    "normalized_eps_base_twd",
    "normalized_eps_downside_twd",
    "estimated_dps_base_twd",
    "estimated_dps_downside_twd",
    "fcf_dividend_coverage_x",
    "payout_consistency_years",
)


class RunError(ValueError):
    """Raised when a run cannot be evaluated or persisted safely."""


def _decimal(row: dict[str, str], field: str) -> Decimal:
    try:
        value = Decimal(row[field].strip())
    except (KeyError, InvalidOperation) as exc:
        raise RunError(f"invalid {field}") from exc
    if not value.is_finite():
        raise RunError(f"invalid {field}")
    return value


def _format_decimal(value: Decimal, places: str = "0.01") -> str:
    return str(value.quantize(Decimal(places), rounding=ROUND_HALF_UP))


def _load_input(
    path: Path, definition: dict[str, Any]
) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        missing = [field for field in definition["required_input_fields"] if field not in fields]
        if missing:
            raise RunError(f"input is missing columns: {', '.join(missing)}")
        return list(reader), fields


def _evaluate_forward_dividend(
    rows: list[dict[str, str]], definition: dict[str, Any]
) -> dict[str, Any]:
    target = Decimal(str(definition["target_yield_pct"]))
    minimum_coverage = Decimal(str(definition["minimum_eps_coverage_x"]))
    minimum_downside = Decimal(str(definition["minimum_downside_yield_pct"]))
    output_fields = list(definition["required_output_fields"])
    retained: list[dict[str, str]] = []
    errors: list[str] = []
    price_dates: set[str] = set()
    financial_periods: set[str] = set()
    source_urls: set[str] = set()
    seen_identities: set[tuple[str, str]] = set()
    fallback_source_count = 0

    for row_number, row in enumerate(rows, start=2):
        try:
            for field in ("market", "ticker", "company", "price_date", "financial_period", "source_tier", "evidence_reference", "source_url"):
                if not row.get(field, "").strip():
                    raise RunError(f"missing {field}")
            values = {field: _decimal(row, field) for field in NUMERIC_INPUTS}
            if values["price_twd"] <= 0:
                raise RunError("price_twd must be positive")
            if values["payout_consistency_years"] < 0:
                raise RunError("payout_consistency_years must be non-negative")
            dt.date.fromisoformat(row["price_date"])
            source_tier = row["source_tier"].strip().lower()
            if source_tier not in {"primary", "secondary"}:
                raise RunError("source_tier must be primary or secondary")
            source_url = urlparse(row["source_url"].strip())
            if source_url.scheme not in {"http", "https"} or not source_url.netloc:
                raise RunError("source_url must be an absolute HTTP(S) URL")
            identity = (row["market"].strip(), row["ticker"].strip())
            if identity in seen_identities:
                raise RunError("duplicate market and ticker")
            seen_identities.add(identity)
        except (RunError, ValueError) as exc:
            errors.append(f"row_{row_number}:{str(exc).replace(' ', '_')}")
            continue

        price = values["price_twd"]
        required_dps = price * target / Decimal("100")
        base_yield = values["estimated_dps_base_twd"] / price * Decimal("100")
        downside_yield = values["estimated_dps_downside_twd"] / price * Decimal("100")
        eps_coverage = values["normalized_eps_base_twd"] / required_dps
        passes = (
            base_yield >= target
            and eps_coverage >= minimum_coverage
            and downside_yield >= minimum_downside
        )
        price_dates.add(row["price_date"])
        financial_periods.add(row["financial_period"])
        source_urls.add(row["source_url"])
        if source_tier != "primary":
            fallback_source_count += 1
        if not passes:
            continue

        result = {
            "rank": "0",
            "market": row["market"].strip(),
            "ticker": row["ticker"].strip(),
            "company": row["company"].strip(),
            "price_date": row["price_date"],
            "price_twd": _format_decimal(price),
            "required_dps_twd": _format_decimal(required_dps),
            "normalized_eps_base_twd": _format_decimal(values["normalized_eps_base_twd"]),
            "normalized_eps_downside_twd": _format_decimal(values["normalized_eps_downside_twd"]),
            "estimated_dps_base_twd": _format_decimal(values["estimated_dps_base_twd"]),
            "estimated_dps_downside_twd": _format_decimal(values["estimated_dps_downside_twd"]),
            "forward_yield_base_pct": _format_decimal(base_yield),
            "forward_yield_downside_pct": _format_decimal(downside_yield),
            "normalized_eps_coverage_x": _format_decimal(eps_coverage),
            "fcf_dividend_coverage_x": _format_decimal(values["fcf_dividend_coverage_x"]),
            "payout_consistency_years": _format_decimal(values["payout_consistency_years"], "1"),
            "screen_status": "candidate",
            "human_review_required": "true",
            "warning_flags": row.get("warning_flags", "").strip(),
            "source_tier": row["source_tier"].strip(),
            "evidence_reference": row["evidence_reference"].strip(),
        }
        retained.append({field: result[field] for field in output_fields})

    retained.sort(
        key=lambda item: (
            -Decimal(item["forward_yield_downside_pct"]),
            -Decimal(item["normalized_eps_coverage_x"]),
            -Decimal(item["fcf_dividend_coverage_x"]),
            -Decimal(item["payout_consistency_years"]),
            item["ticker"],
        )
    )
    for rank, result in enumerate(retained, start=1):
        result["rank"] = str(rank)

    evaluated_count = len(rows) - len(errors)
    coverage_pct = (
        Decimal(evaluated_count) / Decimal(len(rows)) * Decimal("100")
        if rows
        else Decimal("0")
    )
    if not rows or evaluated_count == 0:
        status = "failed"
    elif errors or coverage_pct < Decimal(str(definition["minimum_coverage_pct"])):
        status = "partial"
    else:
        status = "success"
    if len(price_dates) > 1:
        raise RunError("input contains mixed price_date values")
    if len(financial_periods) > 1:
        raise RunError("input contains mixed financial_period values")

    return {
        "status": status,
        "results": retained,
        "universe_count": len(rows),
        "evaluated_count": evaluated_count,
        "retained_count": len(retained),
        "coverage_pct": float(coverage_pct.quantize(Decimal("0.01"))),
        "fallback_source_count": fallback_source_count,
        "failed_source_count": len(errors),
        "error_codes": errors,
        "price_date": next(iter(price_dates), None),
        "financial_period": next(iter(financial_periods), None),
        "source_urls": sorted(source_urls),
    }


def _summary(result: dict[str, Any], run_id: str, chinese: bool = False) -> str:
    if chinese:
        return (
            f"# Screen Run 摘要：{run_id}\n\n"
            f"- **狀態：** `{result['status']}`\n"
            f"- **母體：** {result['universe_count']}\n"
            f"- **已評估：** {result['evaluated_count']}\n"
            f"- **保留候選：** {result['retained_count']}\n"
            f"- **覆蓋率：** {result['coverage_pct']:.2f}%\n"
            f"- **人工審查：** 必要\n\n"
            "本摘要由離線 screen executor 依 manifest 與 results 產生，不構成投資建議。\n"
        )
    return (
        f"# Screen Run Summary: {run_id}\n\n"
        f"- **Status:** `{result['status']}`\n"
        f"- **Universe:** {result['universe_count']}\n"
        f"- **Evaluated:** {result['evaluated_count']}\n"
        f"- **Retained candidates:** {result['retained_count']}\n"
        f"- **Coverage:** {result['coverage_pct']:.2f}%\n"
        f"- **Human review:** Required\n\n"
        "This summary was generated by the offline screen executor from the manifest and results. It is not an investment recommendation.\n"
    )


def _write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> str:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execute_screen(
    screen_id: str,
    input_path: Path,
    as_of: dt.date,
    run_id: str,
    *,
    root: Path = ROOT,
    dry_run: bool = False,
) -> dict[str, Any]:
    if screen_id != SUPPORTED_SCREEN:
        raise RunError(f"unsupported screen: {screen_id}")
    if RUN_ID_PATTERN.fullmatch(run_id) is None:
        raise RunError(
            "run_id must be 10 to 128 characters, start with an alphanumeric "
            "character, and contain only letters, numbers, dot, underscore, plus, "
            "or hyphen"
        )
    screen_dir = root / "screens" / screen_id
    definition_path = screen_dir / "screen.yaml"
    definition = load_flat_yaml(definition_path)
    if not definition.get("enabled"):
        raise RunError(f"screen is disabled: {screen_id}")
    rows, _ = _load_input(input_path, definition)
    started = dt.datetime.now(ZoneInfo(definition["timezone"]))
    evaluation = _evaluate_forward_dividend(rows, definition)
    if evaluation["price_date"] is not None and evaluation["price_date"] != as_of.isoformat():
        raise RunError("--as-of must match the common input price_date")
    finished = dt.datetime.now(ZoneInfo(definition["timezone"]))
    definition_hash = hashlib.sha256(definition_path.read_bytes()).hexdigest()
    parameters = [
        f"target_yield_pct={definition['target_yield_pct']}",
        f"minimum_eps_coverage_x={definition['minimum_eps_coverage_x']}",
        f"minimum_downside_yield_pct={definition['minimum_downside_yield_pct']}",
        f"minimum_coverage_pct={definition['minimum_coverage_pct']}",
    ]
    report = {
        "run_id": run_id,
        "screen_id": screen_id,
        "status": evaluation["status"],
        "universe_count": evaluation["universe_count"],
        "evaluated_count": evaluation["evaluated_count"],
        "retained_count": evaluation["retained_count"],
        "coverage_pct": evaluation["coverage_pct"],
        "dry_run": dry_run,
    }
    if dry_run:
        return report

    runs_root = screen_dir / "runs"
    runs_root.mkdir(parents=True, exist_ok=True)
    final_dir = runs_root / run_id
    lock_path = runs_root / ".run-screen.lock"
    try:
        lock_descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise RunError("another persisted screen run is in progress") from exc
    temporary_dir: Path | None = None
    try:
        if final_dir.exists():
            raise RunError(f"run already exists: {run_id}")
        temporary_dir = Path(tempfile.mkdtemp(prefix=f".{run_id}.", dir=runs_root))
        results_path = temporary_dir / "results.csv"
        results_hash = _write_csv(
            results_path,
            list(definition["required_output_fields"]),
            evaluation["results"],
        )
        (temporary_dir / "summary.md").write_text(
            _summary(evaluation, run_id), encoding="utf-8"
        )
        (temporary_dir / "summary.zh-TW.md").write_text(
            _summary(evaluation, run_id, chinese=True), encoding="utf-8"
        )
        manifest = {
            "schema_version": 1,
            "run_id": run_id,
            "screen_id": screen_id,
            "screen_definition_version": definition["definition_version"],
            "screen_definition_hash": definition_hash,
            "started_at": started.isoformat(timespec="seconds"),
            "finished_at": finished.isoformat(timespec="seconds"),
            "status": evaluation["status"],
            "price_date": evaluation["price_date"],
            "financial_period": evaluation["financial_period"],
            "universe_count": evaluation["universe_count"],
            "evaluated_count": evaluation["evaluated_count"],
            "retained_count": evaluation["retained_count"],
            "coverage_pct": evaluation["coverage_pct"],
            "fallback_source_count": evaluation["fallback_source_count"],
            "failed_source_count": evaluation["failed_source_count"],
            "error_codes": evaluation["error_codes"],
            "parameters": parameters,
            "source_urls": evaluation["source_urls"],
            "results_path": "results.csv",
            "results_sha256": results_hash,
            "summary_path": "summary.md",
            "confidence": "medium" if evaluation["status"] == "success" else "low",
            "human_review_required": True,
        }
        (temporary_dir / "manifest.yaml").write_text(
            dump_flat_yaml(manifest), encoding="utf-8"
        )
        os.replace(temporary_dir, final_dir)
        temporary_dir = None

        if evaluation["status"] == "success":
            next_due = as_of + dt.timedelta(days=definition["routine_cadence_days"])
            state = {
                "schema_version": 1,
                "screen_id": screen_id,
                "status": "fresh",
                "definition_version": definition["definition_version"],
                "last_successful_run": finished.isoformat(timespec="seconds"),
                "last_data_as_of": evaluation["price_date"],
                "next_due_at": next_due.isoformat(),
                "latest_run_path": f"runs/{run_id}",
                "updated_at": finished.isoformat(timespec="seconds"),
                "reason_codes": [],
            }
            atomic_write_flat_yaml(screen_dir / "state.yaml", state)
    finally:
        if temporary_dir is not None and temporary_dir.exists():
            shutil.rmtree(temporary_dir)
        os.close(lock_descriptor)
        lock_path.unlink(missing_ok=True)
    report["run_path"] = str(final_dir.relative_to(root))
    return report


def _default_run_id(timezone: str) -> str:
    return dt.datetime.now(ZoneInfo(timezone)).isoformat(timespec="seconds").replace(":", "-")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screen", required=True)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--as-of", required=True, type=dt.date.fromisoformat)
    parser.add_argument("--run-id")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    try:
        definition = load_flat_yaml(SCREENS_ROOT / args.screen / "screen.yaml")
        run_id = args.run_id or _default_run_id(definition["timezone"])
        report = execute_screen(
            args.screen, args.input, args.as_of, run_id, dry_run=args.dry_run
        )
    except (OSError, KeyError, RunError, ValueError) as exc:
        print(f"Screen run failed: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(
            f"{report['screen_id']} {report['status']}: "
            f"{report['retained_count']}/{report['evaluated_count']} candidates "
            f"from {report['universe_count']} rows"
        )
        if report.get("run_path"):
            print(f"Run saved to {report['run_path']}")
        elif report["dry_run"]:
            print("Dry run; no files changed.")
    return 0 if report["status"] != "failed" else 1


if __name__ == "__main__":
    sys.exit(main())
