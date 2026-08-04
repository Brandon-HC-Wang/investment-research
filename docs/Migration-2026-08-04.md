# Architecture Migration — 2026-08-04

## Purpose

This additive refactor introduces modular knowledge layers and explicit research history while preserving every pre-migration path and all company research. It is designed to remain readable by humans and addressable by Codex, Claude Code, GPT, Gemini CLI, and future agents.

## Changes applied

### Industry packages

Each existing industry now has a lowercase package containing `README.md`, `metrics.md`, `valuation.md`, and `open_questions.md`. The original single-file industry guides remain in place as backward-compatible overviews and link to the new canonical packages.

### Company research state

Each company now adds:

- `sources/earnings/`, `sources/conference_calls/`, `sources/monthly_revenue/`, and `sources/news/`, each with usage guidance;
- `history/` for immutable quarterly snapshots;
- `assumptions.md` for append-only `Open`, `Verified`, and `Rejected` assumptions;
- `research.yaml` for mutable coverage and review state.

No numbered company file or `meta.yaml` was removed, renamed, or rewritten. `meta.yaml` remains the stable identity and backward-compatibility contract. New workflow consumers should prefer `research.yaml` for coverage state.

### Shared knowledge and theses

`knowledge/` stores reusable concepts that do not belong to one company. `theses/` stores macro or cross-industry views with explicit stage, companies, risks, catalysts, and verification tests. Company records link to these layers but retain their own causal and earnings analysis.

### Portfolio layer

`portfolio/` adds portfolio-level watchlist, allocation, and risk frameworks. The existing `watchlist/` remains the canonical research-priority queue.

### Research logs

`research-log/companies/` and `research-log/industries/` add scoped append-only histories. Existing annual logs remain in their original locations and are not migrated or deleted.

### Scripts

`scripts/future/README.md` documents automation ideas only. No future script was implemented. The existing repository validator remains unchanged.

## Compatibility matrix

| Existing interface | Status | New preferred interface |
|---|---|---|
| `industries/Construction.md` and peers | Preserved | Matching lowercase industry package |
| Company numbered files | Preserved and canonical | No replacement |
| `meta.yaml` | Preserved | Identity remains here; mutable workflow also uses `research.yaml` |
| `research-log/2026.md` | Preserved | Scoped new entries use `companies/` or `industries/` |
| `watchlist/` | Preserved and canonical for research priority | `portfolio/watchlist.md` provides portfolio context only |
| `scripts/validate_repository.py` | Preserved | No replacement |

## Migration rules for future agents

1. Do not move old industry content merely to make the tree look uniform.
2. Add new reusable industry findings to package files and link from legacy guides only when necessary.
3. Keep identity synchronized in `meta.yaml`; keep research workflow in `research.yaml`.
4. Never revise committed files in `history/` to reflect later information.
5. Never delete assumptions or scoped log entries; append status changes or corrections.
6. Store source artifacts without moving canonical analysis out of numbered company files.
7. Treat portfolio files as derived research context, not as company truth.

## Rollback characteristics

The migration is additive. Legacy readers can ignore the new directories and continue using existing files. Removing the new layers would not require reconstructing or moving pre-existing company research, although any research created in the new layers must be preserved before such a rollback.
