#!/usr/bin/env python3
"""Collect official Taiwan market discovery data without estimating forward EPS."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import ssl
import sys
import tempfile
import urllib.request
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from yaml_subset import dump_flat_yaml


ROOT = Path(__file__).resolve().parents[1]
ADAPTER_ID = "taiwan-market-discovery"
SCREEN_ID = "forward-dividend-yield"
TIMEZONE = "Asia/Taipei"
SNAPSHOT_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]{9,127}")
SOURCE_URLS = {
    "twse_yield": "https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL",
    "twse_price": "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL",
    "tpex_yield": "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis",
    "tpex_price": "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes",
}
SOURCE_FILENAMES = {key: f"{key}.json" for key in SOURCE_URLS}
OUTPUT_FIELDS = (
    "market",
    "ticker",
    "company",
    "price_date",
    "price_twd",
    "displayed_dividend_yield_pct",
    "displayed_dps_twd",
    "pe_ratio",
    "pb_ratio",
    "discovery_priority",
    "market_data_status",
    "warning_flags",
    "source_tier",
    "evidence_reference",
    "yield_source_url",
    "price_source_url",
)


class CollectionError(ValueError):
    """Raised when official source data cannot form a safe snapshot."""


def _sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _fetch(url: str, context: ssl.SSLContext) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "investment-research/1"},
    )
    with urllib.request.urlopen(request, timeout=30, context=context) as response:
        content_type = response.headers.get_content_type()
        if content_type != "application/json":
            raise CollectionError(f"unexpected content type from {url}: {content_type}")
        return response.read()


def _load_records(content: bytes, label: str) -> list[dict[str, Any]]:
    try:
        values = json.loads(content)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CollectionError(f"{label} is not valid UTF-8 JSON") from exc
    if not isinstance(values, list) or not values:
        raise CollectionError(f"{label} must contain a non-empty JSON array")
    if any(not isinstance(value, dict) for value in values):
        raise CollectionError(f"{label} must contain JSON objects")
    return values


def _roc_date(value: Any, label: str) -> dt.date:
    text = str(value).strip()
    if not text.isdigit() or len(text) < 6:
        raise CollectionError(f"invalid ROC date in {label}: {text}")
    year_text, month_text, day_text = text[:-4], text[-4:-2], text[-2:]
    try:
        return dt.date(int(year_text) + 1911, int(month_text), int(day_text))
    except ValueError as exc:
        raise CollectionError(f"invalid ROC date in {label}: {text}") from exc


def _common_date(records: list[dict[str, Any]], label: str) -> dt.date:
    dates = {_roc_date(record.get("Date"), label) for record in records}
    if len(dates) != 1:
        raise CollectionError(f"{label} contains mixed data dates")
    return next(iter(dates))


def _index_records(
    records: list[dict[str, Any]], code_field: str, label: str
) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for record in records:
        code = str(record.get(code_field, "")).strip()
        if not code:
            raise CollectionError(f"{label} contains a blank security code")
        if code in indexed:
            raise CollectionError(f"{label} contains duplicate security code {code}")
        indexed[code] = record
    return indexed


def _number(value: Any, *, positive: bool = False) -> str:
    text = str(value or "").strip().replace(",", "")
    if not text or text.upper() == "N/A" or text in {"--", "---"}:
        return ""
    try:
        number = Decimal(text)
    except InvalidOperation:
        return ""
    if not number.is_finite() or (positive and number <= 0):
        return ""
    return str(number.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _normalize_market(
    market: str,
    yield_records: list[dict[str, Any]],
    price_records: list[dict[str, Any]],
    threshold: Decimal,
) -> tuple[list[dict[str, str]], list[str]]:
    if market == "TWSE":
        code_field, name_field = "Code", "Name"
        price_code_field, price_name_field, close_field = "Code", "Name", "ClosingPrice"
        yield_field, dps_field, pe_field, pb_field = "DividendYield", None, "PEratio", "PBratio"
        evidence = "TWSE BWIBBU_ALL + STOCK_DAY_ALL"
        yield_source, price_source = SOURCE_URLS["twse_yield"], SOURCE_URLS["twse_price"]
    else:
        code_field, name_field = "SecuritiesCompanyCode", "CompanyName"
        price_code_field, price_name_field, close_field = (
            "SecuritiesCompanyCode", "CompanyName", "Close"
        )
        yield_field, dps_field, pe_field, pb_field = (
            "YieldRatio", "DividendPerShare", "PriceEarningRatio", "PriceBookRatio"
        )
        evidence = "TPEx tpex_mainboard_peratio_analysis + tpex_mainboard_daily_close_quotes"
        yield_source, price_source = SOURCE_URLS["tpex_yield"], SOURCE_URLS["tpex_price"]

    yields = _index_records(yield_records, code_field, f"{market} yield source")
    prices = _index_records(price_records, price_code_field, f"{market} price source")
    output: list[dict[str, str]] = []
    errors: list[str] = []
    for record in yields.values():
        ticker = str(record.get(code_field, "")).strip()
        company = str(record.get(name_field, "")).strip()
        if not ticker or not company:
            raise CollectionError(f"{market} yield source contains blank identity")
        price_record = prices.get(ticker)
        warnings: list[str] = []
        price = ""
        if price_record is None:
            warnings.append("missing_price_record")
        else:
            price = _number(price_record.get(close_field), positive=True)
            if not price:
                warnings.append("missing_or_invalid_close")
            price_name = str(price_record.get(price_name_field, "")).strip()
            if price_name and price_name != company:
                warnings.append("company_name_mismatch")
        displayed_yield = _number(record.get(yield_field))
        displayed_dps = _number(record.get(dps_field)) if dps_field else ""
        if not displayed_yield:
            warnings.append("missing_displayed_yield")
        priority = ""
        if displayed_yield and Decimal(displayed_yield) >= threshold:
            priority = "displayed_yield_review"
        status = "complete" if price and not any(
            warning in {"missing_price_record", "missing_or_invalid_close"}
            for warning in warnings
        ) else "incomplete"
        if status == "incomplete":
            errors.append(f"{market.lower()}_{ticker}:missing_price")
        output.append(
            {
                "market": market,
                "ticker": ticker,
                "company": company,
                "price_date": _roc_date(record.get("Date"), f"{market} yield source").isoformat(),
                "price_twd": price,
                "displayed_dividend_yield_pct": displayed_yield,
                "displayed_dps_twd": displayed_dps,
                "pe_ratio": _number(record.get(pe_field)),
                "pb_ratio": _number(record.get(pb_field)),
                "discovery_priority": priority,
                "market_data_status": status,
                "warning_flags": "|".join(warnings),
                "source_tier": "primary",
                "evidence_reference": evidence,
                "yield_source_url": yield_source,
                "price_source_url": price_source,
            }
        )
    return output, errors


def build_discovery(
    raw_sources: dict[str, bytes],
    as_of: dt.date,
    minimum_displayed_yield_pct: Decimal,
    minimum_coverage_pct: Decimal,
) -> dict[str, Any]:
    if set(raw_sources) != set(SOURCE_URLS):
        raise CollectionError("raw source set does not match the adapter contract")
    records = {
        key: _load_records(raw_sources[key], key)
        for key in SOURCE_URLS
    }
    dates = {
        key: _common_date(value, key)
        for key, value in records.items()
    }
    if set(dates.values()) != {as_of}:
        rendered = ", ".join(f"{key}={value.isoformat()}" for key, value in dates.items())
        raise CollectionError(f"--as-of does not match all source dates: {rendered}")

    twse_rows, twse_errors = _normalize_market(
        "TWSE", records["twse_yield"], records["twse_price"], minimum_displayed_yield_pct
    )
    tpex_rows, tpex_errors = _normalize_market(
        "TPEx", records["tpex_yield"], records["tpex_price"], minimum_displayed_yield_pct
    )
    rows = sorted([*twse_rows, *tpex_rows], key=lambda row: (row["market"], row["ticker"]))
    errors = [*twse_errors, *tpex_errors]
    complete_count = sum(row["market_data_status"] == "complete" for row in rows)
    coverage = Decimal(complete_count) / Decimal(len(rows)) * Decimal("100")
    if complete_count == 0:
        status = "failed"
    elif errors or coverage < minimum_coverage_pct:
        status = "partial"
    else:
        status = "success"
    return {
        "status": status,
        "data_date": as_of.isoformat(),
        "rows": rows,
        "universe_count": len(rows),
        "complete_count": complete_count,
        "incomplete_count": len(rows) - complete_count,
        "priority_count": sum(bool(row["discovery_priority"]) for row in rows),
        "coverage_pct": float(coverage.quantize(Decimal("0.01"))),
        "error_codes": errors,
        "source_counts": {key: len(value) for key, value in records.items()},
    }


def _write_csv(path: Path, rows: list[dict[str, str]]) -> str:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return _sha256(path.read_bytes())


def _summary(result: dict[str, Any], snapshot_id: str, chinese: bool = False) -> str:
    if chinese:
        return (
            f"# 市場探索快照：{snapshot_id}\n\n"
            f"- **狀態：** `{result['status']}`\n"
            f"- **資料日：** {result['data_date']}\n"
            f"- **母體：** {result['universe_count']}\n"
            f"- **完整價格：** {result['complete_count']}\n"
            f"- **顯示殖利率優先審查：** {result['priority_count']}\n"
            f"- **覆蓋率：** {result['coverage_pct']:.2f}%\n\n"
            "這是官方市場資料的探索快照，不含標準化 EPS、預估 DPS 或投資建議。\n"
        )
    return (
        f"# Market Discovery Snapshot: {snapshot_id}\n\n"
        f"- **Status:** `{result['status']}`\n"
        f"- **Data date:** {result['data_date']}\n"
        f"- **Universe:** {result['universe_count']}\n"
        f"- **Complete prices:** {result['complete_count']}\n"
        f"- **Displayed-yield review priority:** {result['priority_count']}\n"
        f"- **Coverage:** {result['coverage_pct']:.2f}%\n\n"
        "This is an official market-data discovery snapshot. It contains no normalized EPS, estimated DPS, or investment recommendation.\n"
    )


def collect_snapshot(
    raw_sources: dict[str, bytes],
    output_dir: Path,
    snapshot_id: str,
    as_of: dt.date,
    minimum_displayed_yield_pct: Decimal,
    minimum_coverage_pct: Decimal,
    *,
    dry_run: bool = False,
) -> dict[str, Any]:
    if SNAPSHOT_ID_PATTERN.fullmatch(snapshot_id) is None:
        raise CollectionError("snapshot_id has an unsafe or invalid format")
    if output_dir.name != snapshot_id:
        raise CollectionError("output directory name must match snapshot_id")
    result = build_discovery(
        raw_sources, as_of, minimum_displayed_yield_pct, minimum_coverage_pct
    )
    report = {
        "snapshot_id": snapshot_id,
        "status": result["status"],
        "data_date": result["data_date"],
        "universe_count": result["universe_count"],
        "complete_count": result["complete_count"],
        "priority_count": result["priority_count"],
        "coverage_pct": result["coverage_pct"],
        "dry_run": dry_run,
    }
    if dry_run:
        return report
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    lock_path = output_dir.parent / f".{snapshot_id}.lock"
    try:
        lock_descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise CollectionError(f"snapshot is already being persisted: {snapshot_id}") from exc
    temporary_dir: Path | None = None
    started = dt.datetime.now(ZoneInfo(TIMEZONE))
    try:
        if output_dir.exists():
            raise CollectionError(f"snapshot already exists: {output_dir}")
        temporary_dir = Path(
            tempfile.mkdtemp(prefix=f".{snapshot_id}.", dir=output_dir.parent)
        )
        raw_hashes: dict[str, str] = {}
        for key, content in raw_sources.items():
            path = temporary_dir / SOURCE_FILENAMES[key]
            path.write_bytes(content)
            raw_hashes[key] = _sha256(content)
        discovery_hash = _write_csv(temporary_dir / "market-discovery.csv", result["rows"])
        (temporary_dir / "summary.md").write_text(
            _summary(result, snapshot_id), encoding="utf-8"
        )
        (temporary_dir / "summary.zh-TW.md").write_text(
            _summary(result, snapshot_id, chinese=True), encoding="utf-8"
        )
        finished = dt.datetime.now(ZoneInfo(TIMEZONE))
        manifest = {
            "schema_version": 1,
            "snapshot_id": snapshot_id,
            "adapter_id": ADAPTER_ID,
            "screen_id": SCREEN_ID,
            "started_at": started.isoformat(timespec="seconds"),
            "finished_at": finished.isoformat(timespec="seconds"),
            "status": result["status"],
            "data_date": result["data_date"],
            "minimum_displayed_yield_pct": float(minimum_displayed_yield_pct),
            "minimum_coverage_pct": float(minimum_coverage_pct),
            "universe_count": result["universe_count"],
            "complete_count": result["complete_count"],
            "incomplete_count": result["incomplete_count"],
            "priority_count": result["priority_count"],
            "coverage_pct": result["coverage_pct"],
            "twse_yield_count": result["source_counts"]["twse_yield"],
            "twse_price_count": result["source_counts"]["twse_price"],
            "tpex_yield_count": result["source_counts"]["tpex_yield"],
            "tpex_price_count": result["source_counts"]["tpex_price"],
            "source_urls": list(SOURCE_URLS.values()),
            "error_codes": result["error_codes"],
            "raw_artifacts": [
                f"{SOURCE_FILENAMES[key]}={raw_hashes[key]}" for key in SOURCE_URLS
            ],
            "discovery_path": "market-discovery.csv",
            "discovery_sha256": discovery_hash,
            "summary_path": "summary.md",
            "human_review_required": True,
        }
        (temporary_dir / "manifest.yaml").write_text(
            dump_flat_yaml(manifest), encoding="utf-8"
        )
        os.replace(temporary_dir, output_dir)
        temporary_dir = None
    finally:
        if temporary_dir is not None and temporary_dir.exists():
            shutil.rmtree(temporary_dir)
        os.close(lock_descriptor)
        lock_path.unlink(missing_ok=True)
    report["snapshot_path"] = str(output_dir)
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--fetch-live", action="store_true")
    source.add_argument("--source-dir", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--as-of", required=True, type=dt.date.fromisoformat)
    parser.add_argument("--minimum-displayed-yield-pct", type=Decimal, default=Decimal("5"))
    parser.add_argument("--minimum-coverage-pct", type=Decimal, default=Decimal("99"))
    parser.add_argument("--ca-file", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    try:
        if not Decimal("0") <= args.minimum_displayed_yield_pct <= Decimal("100"):
            raise CollectionError("minimum displayed yield must be between 0 and 100")
        if not Decimal("0") <= args.minimum_coverage_pct <= Decimal("100"):
            raise CollectionError("minimum coverage must be between 0 and 100")
        if args.fetch_live:
            context = ssl.create_default_context(cafile=args.ca_file)
            raw_sources = {key: _fetch(url, context) for key, url in SOURCE_URLS.items()}
        else:
            raw_sources = {
                key: (args.source_dir / filename).read_bytes()
                for key, filename in SOURCE_FILENAMES.items()
            }
        report = collect_snapshot(
            raw_sources,
            args.output_dir,
            args.snapshot_id,
            args.as_of,
            args.minimum_displayed_yield_pct,
            args.minimum_coverage_pct,
            dry_run=args.dry_run,
        )
    except (CollectionError, OSError, KeyError, ValueError) as exc:
        print(f"Market discovery failed: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(
            f"{report['status']}: {report['complete_count']}/{report['universe_count']} "
            f"complete; {report['priority_count']} priority reviews"
        )
        if report.get("snapshot_path"):
            print(f"Snapshot saved to {report['snapshot_path']}")
        elif report["dry_run"]:
            print("Dry run; no files changed.")
    return 0 if report["status"] != "failed" else 1


if __name__ == "__main__":
    sys.exit(main())
