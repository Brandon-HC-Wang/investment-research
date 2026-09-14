"""Parse the repository's dependency-free, flat YAML contract.

This is intentionally not a general YAML parser. Structured repository state uses
top-level scalar keys and top-level lists of scalars so startup checks can run on a
clean Python installation without downloading dependencies.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class YamlSubsetError(ValueError):
    """Raised when a file uses syntax outside the supported YAML subset."""


def _parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value in {"null", "~"}:
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise YamlSubsetError(f"invalid quoted scalar: {value}") from exc
        if not isinstance(parsed, str):
            raise YamlSubsetError(f"quoted scalar must be a string: {value}")
        return parsed
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def load_flat_yaml(path: Path) -> dict[str, Any]:
    """Load top-level scalars and scalar lists from ``path``."""

    values: dict[str, Any] = {}
    active_list: str | None = None

    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith("  - "):
            if active_list is None:
                raise YamlSubsetError(
                    f"{path}:{line_number}: list item has no top-level key"
                )
            values[active_list].append(_parse_scalar(raw_line[4:]))
            continue

        if raw_line[0].isspace():
            raise YamlSubsetError(
                f"{path}:{line_number}: nested mappings are not supported"
            )
        if ":" not in raw_line:
            raise YamlSubsetError(f"{path}:{line_number}: expected key: value")

        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        if not key or key in values:
            raise YamlSubsetError(f"{path}:{line_number}: invalid or duplicate key")

        if raw_value.strip():
            values[key] = _parse_scalar(raw_value)
            active_list = None
        else:
            values[key] = []
            active_list = key

    return values
