# Changelog

All material changes to the research system are recorded here. This file tracks methodology, structure, schema, and automation changes; company-specific research history belongs in each company timeline.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow semantic versioning for the repository contract.

## [Unreleased]

### Added

- Modular industry knowledge packages with overview, metrics, valuation, and open-question records.
- Company-level source categories, quarterly history, assumptions register, and separate research-state YAML.
- Reusable `knowledge/`, macro `theses/`, and portfolio-level research layers.
- Scoped append-only company and industry research logs.
- Documentation-only future automation backlog.
- Research-state schema and a migration record for the architecture refactor.

### Changed

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
