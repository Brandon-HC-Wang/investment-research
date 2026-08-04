#!/usr/bin/env python3
"""Validate the durable structure of the investment research repository."""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import unquote


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
    "docs/Workflow.md",
    "docs/Scoring.md",
    "docs/Valuation.md",
    "docs/ResearchChecklist.md",
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


def main() -> int:
    errors: list[str] = []

    for relative in sorted(REQUIRED_FILES):
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{relative}: required file is missing")
        elif path.suffix == ".md":
            validate_markdown(path, errors)

    for relative in sorted(REQUIRED_DIRECTORIES):
        if not (ROOT / relative).is_dir():
            errors.append(f"{relative}/: required directory is missing")

    companies_dir = ROOT / "companies"
    if companies_dir.is_dir():
        for child in sorted(companies_dir.iterdir()):
            if child.is_dir() and not child.name.startswith("."):
                validate_company(child, errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
