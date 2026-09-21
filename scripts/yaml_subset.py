"""Parse the repository's dependency-free, flat YAML contract.

This is intentionally not a general YAML parser. Structured repository state uses
top-level scalar keys and top-level lists of scalars so startup checks can run on a
clean Python installation without downloading dependencies.
"""

from __future__ import annotations

import json
import os
import tempfile
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


def _dump_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    if not isinstance(value, str):
        raise YamlSubsetError(f"unsupported scalar type: {type(value).__name__}")
    return json.dumps(value, ensure_ascii=False)


def dump_flat_yaml(values: dict[str, Any]) -> str:
    """Serialize the supported subset with stable key and list ordering."""

    lines: list[str] = []
    for key, value in values.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {_dump_scalar(item)}" for item in value)
        else:
            lines.append(f"{key}: {_dump_scalar(value)}")
    return "\n".join(lines) + "\n"


def atomic_write_flat_yaml(path: Path, values: dict[str, Any]) -> None:
    """Atomically replace ``path`` with a serialized flat-YAML document."""

    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", dir=path.parent, text=True
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(dump_flat_yaml(values))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
