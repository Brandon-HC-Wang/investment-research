# Research Workflow

## Lifecycle states

| State | Purpose | Exit condition |
|---|---|---|
| `discovery` | Determine whether the company merits research time | Business and potential earnings mechanism are identifiable |
| `qualifying` | Establish business quality and materiality | Major segments, moat evidence, and key questions are documented |
| `active` | Build the full causal and earnings model | Thesis, scenarios, risks, and valuation are internally consistent |
| `monitoring` | Test the thesis against new evidence | A thesis condition changes or scheduled deep review is due |
| `archived` | Preserve inactive research | Reopened only when a dated reason is recorded |

These states describe research maturity, not an investment rating.

## New-company workflow

1. Create `companies/<ticker>-<slug>/` from `templates/company/`.
2. Complete `meta.yaml` for company identity and backward compatibility, then complete `research.yaml` for coverage state, review timing, confidence, priority, and watch items.
3. Map products, customers, revenue model, cost structure, and competitive landscape in `01_business.md`.
4. Establish historical revenue, margin, cash-flow, balance-sheet, and share-count baselines in `02_financials.md`.
5. Define revenue drivers, backlog or forward indicators, and replacement drivers in `03_growth_drivers.md`.
6. Build base, upside, and downside causal forecasts in `04_eps_model.md`.
7. Record material dated history in `05_timeline.md` and supporting observations in `06_notes.md`.
8. Create durable, testable questions in `07_open_questions.md`.
9. Synthesize the thesis, risks, falsification tests, and confidence in `08_thesis.md`.
10. Apply appropriate methods and scenario valuation in `09_valuation.md`.
11. Create the assumptions register, source categories, and first quarterly snapshot; update metadata, run validation, and review the full record for contradictions.

## Event-driven update

An event earns repository space only when it changes evidence, assumptions, or monitoring.

1. Capture the primary source and date.
2. Identify the changed operating variable.
3. Trace the effect through revenue, margins, EPS, and cash flow.
4. Compare the evidence with the current model and thesis.
5. Update every affected canonical record atomically.
6. Resolve, reject, reopen, or add questions without deleting history.
7. Append a timeline event and research-log entry when the conclusion is important or reusable.
8. Update `last_update`, `next_action`, watch items, confidence, and priority where warranted.

## Periodic review

For quarterly or annual results:

1. Compare reported operating drivers with prior assumptions.
2. Reconcile reported and normalized EPS.
3. Explain revenue and margin variance rather than listing results.
4. Assess backlog or leading indicators and replacement drivers.
5. Roll forecast years only after preserving the prior forecast snapshot.
6. Re-test downside mechanisms and balance-sheet resilience.
7. Reassess the thesis before valuation.
8. Set the next review trigger.

## Search strategy and screen workflow

1. Define the testable economic mechanism, confirmation and rejection signals, time window, and validation threshold under `strategies/`.
2. Define the reproducible universe, filters, ranking, warning flags, source hierarchy, output fields, and refresh policy under `screens/`.
3. Register both definitions and keep their references reciprocal.
4. Before a refresh, run the local due check and confirm that network access or execution was explicitly requested.
5. Create a new timestamped run; never overwrite an earlier manifest or result.
6. Record definition version, source and data dates, coverage, fallback usage, failures, parameters, and limitations.
7. Update rebuildable screen state only after the run outcome is known. A failed run does not advance the last-successful timestamp.
8. Promote only material cross-run conclusions to `research-log/`; promote individual companies to coverage only after human review.

Strategy validation states are `idea`, `testing`, `validated`, `monitoring`, `rejected`, and `archived`. Screen refresh states are `fresh`, `due`, `overdue`, `blocked`, and `disabled`. Neither lifecycle is an investment rating.

## Contradiction handling

When credible evidence conflicts:

- keep both claims and their sources;
- identify differences in definitions, periods, incentives, or scope;
- reduce confidence if the conflict is material;
- add an open question with a resolution method;
- do not force a conclusion merely to make files appear consistent.

## Completion criteria

A change is complete when canonical files are synchronized, history is preserved, evidence is cited, uncertainty is explicit, the next action is executable, reusable findings are promoted, and `scripts/validate_repository.py` passes.
