# Search Strategy Architecture Proposal

> Status: Phase 1 implemented on 2026-09-10. Schemas, templates, registries, the first definitions, validation, and a read-only startup reminder exist. Network retrieval and automatic refreshes remain unimplemented and unauthorized.

## Objective

Add a durable workflow that can define reusable research strategies, execute reproducible market screens, retain point-in-time results, and tell a human or AI agent which screens are due for refresh. A screen produces research candidates, not buy, sell, or hold instructions.

## Semantic boundary

| Object | Question answered | Canonical content |
|---|---|---|
| Strategy | Why might this signal identify a research opportunity? | Economic mechanism, validation state, supporting and contradicting evidence, falsification, time horizon, linked screens |
| Screen | How is the candidate universe computed? | Universe, fields, filters, ranking, source hierarchy, refresh policy, output contract |
| Run | What did the screen know and return at one point in time? | Immutable manifest, definition version, source and data dates, coverage, failures, result table, summary |
| Refresh state | What needs attention now? | Derived last successful run, last data date, next due date, staleness reasons, latest run pointer |

A strategy may reference several screens, and a screen may support several strategies. Company research remains canonical under `companies/`; screen results must not silently create or modify company theses. `watchlist/` remains the prioritized research queue, while `research-log/` records only material cross-run conclusions rather than every execution.

## Proposed directory contract

```text
strategies/
  registry.yaml
  forward-dividend-income/
    strategy.yaml
    README.md
    README.zh-TW.md

screens/
  registry.yaml
  forward-dividend-yield/
    screen.yaml
    README.md
    README.zh-TW.md
    state.yaml
    runs/
      2026-09-10T090000+08-00/
        manifest.yaml
        results.csv
        summary.md
        summary.zh-TW.md

schemas/
  strategy.schema.json
  screen.schema.json
  screen-run.schema.json
  screen-state.schema.json

templates/
  strategy/
  screen/

scripts/
  check_screen_refresh.py
  validate_repository.py
```

`strategy.yaml` and `screen.yaml` are canonical machine-readable definitions. Their paired Markdown files explain reasoning and limitations. A run directory is append-only and must never be edited to incorporate later knowledge. `state.yaml` is mutable but derived and rebuildable from the definition and run manifests; it must not contain unique research conclusions.

## Strategy definition

Required fields should include:

- `schema_version`, stable `id`, names, status, and validation state;
- claim and causal mechanism;
- supporting and contradicting evidence;
- confirmation and rejection signals;
- expected time window and current confidence;
- linked screen IDs;
- minimum point-in-time validation requirement;
- creation, review, and supersession history.

Recommended validation states are `idea`, `testing`, `validated`, `monitoring`, `rejected`, and `archived`. Status history is append-only. `validated` means historical point-in-time evidence supports the stated mechanism; it does not mean the strategy is guaranteed to work or constitutes a recommendation.

## Screen definition

Required fields should include:

- `schema_version`, stable `id`, title, enabled state, and definition version;
- universe and explicit exclusions;
- required input fields, units, fiscal periods, and allowed lags;
- primary and fallback data sources with source tiers;
- hard filters, ranking factors, warning flags, and scenario rules;
- output columns and evidence requirements;
- refresh policy and staleness policy;
- completeness threshold and failure behavior;
- links to strategies, models, and relevant research logs.

Filters should distinguish `required`, `ranking`, and `warning` conditions. A source failure, throttled response, incomplete market coverage, or stale input must not be interpreted as an empty result.

## Run manifest and results

Every run should preserve:

- run ID, start and finish timestamps, status, and tool version;
- screen definition version or content hash;
- price date, financial period, source access dates, and source URLs;
- candidate-universe count, evaluated count, retained count, and coverage percentage;
- failed and fallback-source counts with error categories;
- the exact parameters and thresholds used;
- paths and checksums for result artifacts where practical;
- confidence, limitations, and whether human review is required.

`results.csv` should contain one row per candidate and include the facts, estimates, scenario outputs, warning flags, source tier, and evidence reference needed to reconstruct why the candidate passed. Later corrections require a new run or a dated correction record; they must not overwrite the prior result.

## Refresh policy

Refresh decisions need two separate clocks:

1. **Execution freshness:** how long since the screen last completed successfully.
2. **Input freshness:** whether a newer price, monthly disclosure, quarterly filing, dividend decision, or other required source is available.

Each screen should define:

- routine cadence, such as daily, weekly, monthly, quarterly, or manual;
- `stale_after` tolerance;
- scheduled triggers, such as the expected monthly-revenue or filing window;
- event triggers, such as a dividend resolution, new financial filing, material price move, or definition change;
- cool-down rules to prevent repeated runs when the underlying data have not changed;
- whether refresh is `remind_only` or may be executed after explicit user authorization.

The due-state algorithm should return `fresh`, `due`, `overdue`, `blocked`, or `disabled`, together with machine-readable reason codes. A failed run does not advance `last_successful_run`.

## Agent session startup

After implementation, `AGENTS.md` and `.ai/context.md` should require a read-only startup check:

```bash
python3 scripts/check_screen_refresh.py --due-only
```

The command should read local definitions and state without making network calls. It should print a compact human view and support `--json` for agents. Session startup should remind the user which screens are due and why; it should not refresh data, change files, or contact external services automatically.

An explicit refresh command can later execute one named screen. It should create a new run atomically, update derived state only after success, and leave a failed manifest when diagnostics are useful.

## Forward-dividend-yield first implementation

The first screen can be `forward-dividend-yield`, linked to a `forward-dividend-income` strategy in `testing` state. Its refresh policy should initially be:

- weekly for price and displayed-yield inputs;
- monthly after official monthly-revenue publication;
- mandatory after each quarterly filing;
- mandatory after a board dividend resolution or material capital action;
- immediately due when the definition or normalized-EPS methodology changes.

The screen should produce base and downside forward-yield scenarios, required DPS and payout ratio, normalized-EPS coverage, free-cash-flow coverage, one-off earnings flags, source tier, and sector-specific review status. Construction, financial, and cyclical companies require separate model rules.

## Validation and safety gates

Before executable automation is accepted:

- JSON Schemas and repository validation must cover definitions, state, and run manifests;
- fixture-based tests must cover due-state calculations, failed runs, incomplete data, time zones, and definition changes;
- network retrieval and analytical transformation must be separable;
- primary-source priority and fallback labeling must be enforced;
- runs must be idempotent by run ID and append-only by path;
- no screen may automatically add a company to coverage, change a thesis, or create a recommendation;
- startup checks must remain read-only and fast.

## Suggested implementation sequence

1. Approve terminology, directory names, lifecycle states, and the reminder-only startup boundary.
2. Add schemas, templates, registry contracts, and validation without implementing network retrieval.
3. Register the forward-dividend strategy and screen, then migrate the current methodology into their definitions.
4. Add the read-only refresh checker and session-startup instruction.
5. Implement one explicit, reproducible screen runner and retain its first point-in-time run.
6. Compare estimates with later dividend decisions and keep the strategy in `testing` until its stated historical validation threshold is met.

## Implemented Phase 1 decisions

- The public umbrella term is “search strategy,” while the internal contract retains the `strategy` versus `screen` distinction.
- `state.yaml` is committed as a rebuildable cache and may not contain unique conclusions.
- Session startup performs a local, read-only reminder. It does not query official sources or run a refresh.
- Validation duration is strategy-specific. The first annual dividend strategy requires at least three annual cohorts; quarterly strategies should ordinarily require at least 8–12 point-in-time quarters. Exact success metrics must be declared before outcome testing begins.
