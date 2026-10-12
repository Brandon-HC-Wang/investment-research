# Changelog

All material changes to the research system are recorded here. This file tracks methodology, structure, schema, and automation changes; company-specific research history belongs in each company timeline.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow semantic versioning for the repository contract.

## [Unreleased]

### Added

- Completed eight-company sector EPS/normalization, conditional parent-cash budgets and 2027 cash-dividend intervals with three-year declared histories and retained primary filings; supplemental diagnostics only, no formal run/state advancement (2026-10-12).
- Fixed eight-company forward-dividend readiness cohort with sector input gaps, local evidence hashes and a staged workflow-versus-outcome validation plan (2026-10-12); no forecast, threshold or refresh-state advancement.
- First persisted covered-company forward-dividend pilot with bilingual assumptions, three-year cash/stock history, retained price evidence, input checksums and explicit partial-coverage diagnostics (2026-10-12); thresholds and executor schema remain unchanged.
- Securities-brokerage industry package covering hedge-netted trading earnings, associate asset-management exposure, bonus-share denominators and cash-versus-stock dividend scenarios (2026-10-12).
- First-class `strategies/` and `screens/` contracts with registries, bilingual reasoning, rebuildable refresh state, and append-only run semantics.
- JSON Schemas and templates for strategy definitions, screen definitions, screen state, and point-in-time run manifests.
- Dependency-free, read-only screen-refresh checker with JSON output, deterministic date evaluation, and unit tests.
- Offline `forward-dividend-yield` executor with explicit CSV input, dry-run mode, atomic append-only run artifacts, checksum validation, and success-only refresh-state advancement.
- Predeclared annual dividend-strategy validation metrics covering sample size, forecast calibration, DPS error, candidate precision, and baseline improvement.
- Explicit TWSE/TPEx market-discovery collector with strict TLS, ROC-date reconciliation, retained raw JSON, normalized full-universe output, completeness diagnostics, and immutable snapshot checksums.
- Schema, template, validator support, and bilingual operating guidance for market-discovery source snapshots.
- Bilingual investment-research report UI specification and a self-contained, responsive, printable HTML skeleton under `templates/reports/`.
- Same-directory `.zh-TW.md` reading companions for every canonical English Markdown file, with validation and synchronization rules.
- Modular industry knowledge packages with overview, metrics, valuation, and open-question records.
- Company-level source categories, quarterly history, assumptions register, and separate research-state YAML.
- Reusable `knowledge/`, macro `theses/`, and portfolio-level research layers.
- Scoped append-only company and industry research logs.
- Documentation-only future automation backlog.
- Research-state schema and a migration record for the architecture refactor.

### Changed

- Changed forward-dividend screen definition to version 4: an evidenced base cash-yield interval qualifies when its unrounded upper bound reaches 7%, with explicit partial/entire-range labels, required DPS bounds, immutable definition snapshots and historical-contract validation; EPS/downside/completeness gates remain unchanged (2026-10-12).
- Recorded an evidence-led dividend-baseline comparison and reproducible earnings/payout sensitivities; corrected interpreting stacked pilot haircuts as a normal-year forecast, while preserving historical runs, missing-cash gates and registered thresholds (2026-10-12).
- Documented the confirmed forward-dividend pilot preparation policy: covered-company sample, sector-specific earnings/cash estimates, declared-versus-estimated dividends, and a three-completed-earnings-year history window; registered thresholds remain unchanged (2026-10-12).
- Extended repository validation and agent startup guidance to detect due screens locally without automatic network access or mutation, and to validate persisted run artifacts and result integrity.
- Preserved legacy industry guides and annual research logs as backward-compatible entry points while directing new work to modular packages.
- Separated stable company identity in `meta.yaml` from workflow state in `research.yaml`.

## [1.0.0] - 2026-08-04

### Added

- Durable company record contract with nine numbered markdown files and `meta.yaml`.
- AI operating context, writing standards, and change workflow.
- Canonical research framework, scoring rubric, valuation policy, and checklist.
- Industry-specific analytical guides.
- EPS and scenario-model conventions.
- Company, source, quarterly-review, and research-log templates.
- Machine-readable metadata schema and local repository validator.
- Watchlist and append-only research-log protocols.

### Changed

- Reframed the repository from a markdown note collection into an AI-native investment research system.
