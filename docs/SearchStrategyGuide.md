# Search Strategy Feature: Overview, Usage, and Handoff

## Current checkpoint — 2026-09-15

The infrastructure and offline execution path exist, but no formal forward-dividend screen run or retained official market snapshot exists. The registered strategy is `testing`; screen definition version is 3. The local refresh checker reports `due` with `definition_changed` and `never_run`.

**User decision:** Defer the TPEx TLS issue. Do not investigate certificates, install trust anchors, or bypass TLS verification unless the user explicitly resumes that work. This is a workflow pause, not evidence that TPEx data is unavailable or unsuitable.

Phase 2 and Phase 3 implementation changes remain uncommitted at this checkpoint. This document does not authorize a commit, push, live refresh, or further implementation.

## Feature overview

The feature preserves reusable research strategies, reproducible search conditions, point-in-time results, and refresh reminders. Its output is a research queue, not a recommendation or a company thesis.

| Layer | Responsibility | Entry point |
|---|---|---|
| Strategy | Economic hypothesis, confidence, outcome-validation requirements | [Forward dividend income](../strategies/forward-dividend-income/README.md) |
| Screen | Universe, filters, ranking, input/output contracts, refresh policy | [Forward dividend yield](../screens/forward-dividend-yield/README.md) |
| Source snapshot | Raw official responses and normalized market-discovery data | [Source snapshots](../screens/forward-dividend-yield/source-snapshots/README.md) |
| Run | Append-only manifest, result CSV, paired summaries | `screens/forward-dividend-yield/runs/` — created only on persistence |
| Refresh state | Last successful run, data date, next due date, reason codes | [state.yaml](../screens/forward-dividend-yield/state.yaml) |

The intended sequence is:

```text
Official market data → source snapshot
                            ↓
Filings + reviewed company models → normalized EPS / supportable DPS
                            ↓
Reviewed input CSV → dry run → authorized persisted run → human review
```

The filing/model enrichment step is not implemented. A market-discovery CSV is not directly interchangeable with the runner's input CSV.

## First screen and analytical boundaries

The current time horizon is cash dividends distributed in 2027 from normalized 2026 earnings. Required numerical conditions are:

- Base forward cash yield ≥ 7%.
- Normalized base EPS / required DPS ≥ 1.25 times.
- Downside forward cash yield ≥ 5%.

`required DPS = screen-date price × 7%`

`forward yield = estimated cash DPS / screen-date price × 100%`

Ranking uses downside yield, normalized EPS coverage, free-cash-flow dividend coverage, and payout-consistency years. Warning flags and all retained candidates require human review. The executor does not verify business quality, sector normalization, parent-company cash capacity, or whether analyst estimates are supportable.

The market collector's displayed-yield threshold defaults to 5% and only labels review priority; it does not remove rows or establish forward yield. Historical displayed yield is not estimated cash yield.

## Usage

Run all commands from the repository root with Python 3 supporting `zoneinfo`. The scripts use the standard library and the repository's flat-YAML helper.

### 1. Call a saved definition and check refresh status

Read the registered screen's [README](../screens/forward-dividend-yield/README.md) and [screen.yaml](../screens/forward-dividend-yield/screen.yaml). Definitions are discoverable through [screens/registry.yaml](../screens/registry.yaml) and [strategies/registry.yaml](../strategies/registry.yaml).

```bash
python3 scripts/check_screen_refresh.py --due-only
python3 scripts/check_screen_refresh.py --due-only --json
```

New sessions run this local, read-only check after loading repository context. It does not fetch sources, detect new external disclosures, schedule a background job, or modify state. Event-trigger freshness currently depends on locally recorded state rather than automatic external monitoring.

### 2. Verify market collection offline

This command uses synthetic fixtures only and writes nothing:

```bash
python3 scripts/collect_market_discovery.py \
  --source-dir scripts/tests/fixtures/market-discovery \
  --snapshot-id fixture-contract-dry-run \
  --as-of 2026-09-14 \
  --output-dir screens/forward-dividend-yield/source-snapshots/fixture-contract-dry-run \
  --dry-run --json
```

Expected fixture result: `success`, 4 universe records, 4 complete prices, 2 review-priority labels. Synthetic values are software tests, not investment evidence; never persist them as a formal research snapshot.

For reviewed official replay, `--source-dir` must contain `twse_yield.json`, `twse_price.json`, `tpex_yield.json`, and `tpex_price.json`. All four source dates must equal `--as-of`. Removing `--dry-run` persists raw JSON, `market-discovery.csv`, `manifest.yaml`, and bilingual summaries to a new directory whose name matches `--snapshot-id`.

**Deferred:** The existing `--fetch-live` mode retrieves all four TWSE/TPEx endpoints with strict TLS. Do not run it while TPEx work is paused. There is currently no TWSE-only option; adding one requires an explicit market-scope contract, not empty TPEx files or a silently reduced universe.

### 3. Prepare reviewed analytical input

The exact header is defined in [screen.yaml](../screens/forward-dividend-yield/screen.yaml):

```csv
market,ticker,company,price_date,price_twd,financial_period,normalized_eps_base_twd,normalized_eps_downside_twd,estimated_dps_base_twd,estimated_dps_downside_twd,fcf_dividend_coverage_x,payout_consistency_years,warning_flags,source_tier,evidence_reference,source_url
```

Use TWD per share for price, EPS, and DPS; use times for cash-flow coverage and whole years for payout consistency. Preserve the distinction between reported financial periods and forecast years. Every estimate needs dated filing/model provenance, recurring-versus-one-off adjustments, scenario logic, and cash-capacity review. Market and ticker identities must be unique; price dates and financial periods must be consistent across valid rows. `source_tier` is `primary` or `secondary`, and `source_url` is an absolute HTTP(S) URL.

The current implementation measures coverage against supplied CSV rows, not an independently verified full-market universe. A manually selected subset cannot be described as complete TWSE/TPEx coverage even when its input-row coverage is 100%.

### 4. Verify screen execution offline

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input scripts/tests/fixtures/forward-dividend-yield-input.csv \
  --as-of 2026-09-14 \
  --run-id verification-dry-run \
  --dry-run --json
```

Expected synthetic result: `success`, 3 evaluated rows, 2 candidates, 100% input-row coverage. No run or state update is written.

For an authorized formal run, replace the fixture with a reviewed input, choose a new run ID, set `--as-of` to the common input `price_date`, and only then remove `--dry-run`. Only `forward-dividend-yield` is supported by the executor. Run IDs are 10–128 characters, start with an alphanumeric character, and otherwise allow letters, numbers, `.`, `_`, `+`, and `-`.

### 5. Review saved results and state

A persisted run creates `manifest.yaml`, `results.csv`, `summary.md`, and `summary.zh-TW.md` under a new `runs/<run-id>/` directory. Read the manifest's status, parameters, provenance, errors, and coverage before interpreting results. Correct old results with a new run, never an overwrite.

- `success`: evaluation completed without row errors and met the configured input coverage requirement; only this status updates refresh state.
- `partial`: some rows could not be evaluated or coverage was insufficient; results are diagnostic and state is not advanced.
- `failed`: no rows could be evaluated; state is not advanced.

Fatal input/header/date errors can terminate before persistence; not every failure produces a manifest. A software `success` is not analytical approval or proof of full-market completeness.

Refresh cadence is seven days with seven days of stale tolerance. Monthly revenue, filings, dividend decisions, capital actions, and definition changes are declared triggers; external event detection is not automated.

### 6. Validate a checkpoint

```bash
python3 -m unittest discover -s scripts/tests -v
python3 scripts/validate_repository.py
git diff --check
```

On 2026-09-15, all 32 existing tests passed. Repository validation checks contracts and artifact integrity, not forecast accuracy or source truthfulness. Commit only when requested; do not push implicitly.

## To-do list and resume order

- [x] Strategy/screen registries, schemas, templates, and bilingual reasoning.
- [x] Read-only startup reminder and deterministic refresh tests.
- [x] Offline executor, append-only artifacts, hashes, state-success boundary, and fixture tests.
- [x] TWSE/TPEx market-discovery collector, source snapshot contract, and fixture tests.
- [ ] **Next without TPEx:** Define an enrichment contract linking normalized EPS, estimated DPS, parent cash, financial periods, assumption IDs, and dated primary evidence; do not implement forecasts from historical yield or annualized monthly revenue.
- [ ] Specify how a partial-market/TWSE-only mode names its scope, verifies its denominator, and represents missing markets before adding that mode. No such option exists today.
- [ ] Add separately tested official filing retrieval and sector-specific normalization for financial, construction/property, and cyclical companies.
- [ ] Independently verify market-universe completeness and input staleness; supplied-row coverage alone is insufficient.
- [ ] Review failure-manifest behavior, original input retention/hash provenance, lock recovery after interruption, historical definition reconstruction, and refresh-state rebuilding before treating automation as production-ready.
- [ ] Retain and validate the first reviewed official market snapshot when the chosen source scope is ready.
- [ ] Authorize the first formal run only after data scope and analytical inputs are reviewed; manually examine candidates and warnings.
- [ ] Compare forecasts with later declarations using the strategy's predeclared metrics; keep `testing` until its evidence requirements are met.
- [ ] Add external event monitoring or scheduled refresh only under a separate authorization and design.
- [ ] **Deferred by user:** TPEx certificate-chain diagnosis and trusted-bundle configuration. Resume only on explicit request; never disable TLS verification.
- [ ] Create a local implementation checkpoint when requested; Phase 2/3 changes are still pending commit as of this document's date.

To resume, load the repository's required context, read this guide, check due state and the worktree, rerun validation, and begin with the enrichment contract. Do not restart TPEx investigation or assume a prior diagnostic count is current market evidence.

## References and history

- [Architecture proposal and implementation decisions](proposals/SearchStrategyArchitecture.md)
- [Script reference](../scripts/README.md)
- [Screen definition and boundaries](../screens/forward-dividend-yield/README.md)
- [Strategy outcome-validation metrics](../strategies/forward-dividend-income/README.md)
- [Append-only research log](../research-log/2026.md)

- **2026-09-15:** Consolidated overview, executable offline commands, limitations, and resume tasks. Recorded the user's decision to defer TPEx rather than treating TLS repair as the immediate next step. No network collection or formal research run was performed for this documentation task.
