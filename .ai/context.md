# AI Context

## One-minute orientation

This repository is a long-term equity research system. Its unit of value is not a note; it is an evidence-backed improvement to a durable company or industry model.

The target is sustainable per-share earnings growth over a two-to-five-year horizon. Business quality and future earnings visibility come before valuation. Daily price movement, technical analysis, and unintegrated news are outside the primary scope.

## Required reasoning chain

`business → competitive advantage → revenue drivers → EPS drivers → earnings quality → backlog/visibility → risks → thesis → valuation`

Do not skip a stage merely because the current task starts with a financial result or valuation question.

## Repository semantics

- `companies/` contains company-specific truth and history.
- `industries/` contains reusable sector packages split into overview, metrics, valuation, and open questions.
- `models/` contains calculation and forecasting conventions.
- `knowledge/` contains reusable concepts that must not belong to one company.
- `theses/` contains macro and cross-industry theses.
- `portfolio/` contains portfolio-level monitoring, allocation, and risk policy.
- `research-log/companies/` and `research-log/industries/` contain append-only scoped findings.
- `watchlist/` is a research-priority queue, never a recommendation list.
- `templates/` defines structure only; it is not evidence.

## Current-state versus history

`meta.yaml` stores stable company identity. `research.yaml` and the current-summary sections of numbered files describe present research state. `assumptions.md`, dated sections, and quarterly files under `history/` preserve how that state evolved. Update the present state when evidence changes, then append a dated record explaining the change. Never delete open questions, assumptions, or historical snapshots.

## Minimum useful update

A research update should identify the source, observation, causal interpretation, affected assumptions, thesis implication, uncertainty, and next verification step. If it cannot do that, it likely belongs in a temporary working context rather than the repository.

## Navigation for company work

Read in this order after the global required files:

1. `meta.yaml` for company identity and `research.yaml` for current workflow state.
2. `08_thesis.md` for the current claim and falsification tests.
3. `assumptions.md` and `07_open_questions.md` for known uncertainty.
4. The latest file in `history/` for the prior point-in-time state.
5. `01_business.md` through `06_notes.md` for supporting analysis and history.
6. `09_valuation.md` only after the operating case is understood.

## Completion test

Before finishing, ask:

- Did the canonical record change?
- Are facts and estimates distinguishable?
- Is the causal effect on revenue or EPS explicit?
- Is prior reasoning preserved?
- Did the next action become more concrete?
- Are cross-file conclusions consistent?
- Does validation pass?
