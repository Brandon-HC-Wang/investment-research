# Repository Scripts

## Validate the repository

Run from the repository root:

```bash
python3 scripts/validate_repository.py
```

The validator uses only the Python standard library. It checks required top-level files and directories, fixed company filenames, non-empty markdown, metadata fields and controlled values, ISO dates, strategy and screen registries, reciprocal references, refresh state, and common unresolved template markers in active company records.

Exit code `0` means validation passed. Exit code `1` means one or more contract violations were printed. The validator is intentionally conservative: it checks structural integrity, not investment-analysis correctness or source quality.

## Check screen refresh status

Run the local, read-only startup check:

```bash
python3 scripts/check_screen_refresh.py --due-only
```

Add `--json` for machine-readable output or `--as-of YYYY-MM-DD` for deterministic testing. The command never accesses the network or modifies state. Strategy and screen YAML is limited to the dependency-free flat subset implemented by `yaml_subset.py`.

Refresh-state unit tests run with `python3 -m unittest discover -s scripts/tests -v`.

## Future scaffolding

[`future/`](future/README.md) documents possible automation without implementing it. Future scripts require explicit schemas, provenance, tests, and human-review boundaries before development.
