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

## Collect official market discovery data

`collect_market_discovery.py` explicitly retrieves and joins the official TWSE and TPEx current price and displayed-yield datasets. Live access must be requested explicitly:

```bash
python3 scripts/collect_market_discovery.py \
  --fetch-live \
  --snapshot-id <unique-snapshot-id> \
  --as-of <official-data-date> \
  --output-dir screens/forward-dividend-yield/source-snapshots/<unique-snapshot-id>
```

Use `--ca-file <pem-bundle>` when the local Python trust store cannot validate an official endpoint. TLS verification cannot be disabled. For deterministic tests or replay, replace `--fetch-live` with `--source-dir <directory>` containing `twse_yield.json`, `twse_price.json`, `tpex_yield.json`, and `tpex_price.json`. Add `--dry-run --json` to evaluate without persistence.

The collector preserves all four raw responses, checks that their ROC dates equal `--as-of`, joins closing prices by market and ticker, and writes a checksummed market-discovery snapshot. It does not estimate forward EPS, DPS, payout capacity, or cash-flow coverage and cannot create a screen run.

## Run an offline screen

`run_screen.py` currently executes only `forward-dividend-yield` from a prepared CSV. It never retrieves network data. Validate an input without changing the repository:

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input scripts/tests/fixtures/forward-dividend-yield-input.csv \
  --as-of 2026-09-14 \
  --run-id verification-dry-run \
  --dry-run --json
```

Omit `--dry-run` only for an authorized point-in-time execution using reviewed, dated inputs. A persisted execution atomically creates `manifest.yaml`, `results.csv`, `summary.md`, and `summary.zh-TW.md` under a new append-only run directory. Existing run IDs cannot be overwritten. Only a `success` run advances `state.yaml`; `partial` and `failed` runs do not.

## Future scaffolding

[`future/`](future/README.md) documents possible automation without implementing it. Future scripts require explicit schemas, provenance, tests, and human-review boundaries before development.
