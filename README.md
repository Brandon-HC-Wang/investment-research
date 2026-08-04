# Investment Research System

An AI-native knowledge system for accumulating long-term equity research. The repository is designed for human analysts and multiple AI coding assistants to build, challenge, and preserve investment knowledge over many years.

This is not a news archive, trading journal, or stock-recommendation feed. Its purpose is to identify companies capable of growing sustainable earnings over the next two to five years and to make the assumptions behind that view auditable.

## Research order

All company work follows one causal chain:

> Business quality → competitive advantage → revenue drivers → EPS drivers → recurring earnings → backlog and visibility → risks → thesis → valuation

Valuation is the final step. A low multiple does not compensate for weak business quality or poor earnings visibility.

## Repository map

| Path | Purpose |
|---|---|
| `PROJECT_CONTEXT.md` | Stable mission, boundaries, and system design |
| `AGENTS.md` | Mandatory operating rules for AI assistants |
| `.ai/` | Compact context, writing style, and execution protocol |
| `docs/` | Canonical research methodology and scoring standards |
| `docs/ui-specs/` | Bilingual presentation contracts for generated research artifacts |
| `companies/` | One durable research record per company |
| `industries/` | Shared industry economics, metrics, and cycle knowledge |
| `knowledge/` | Reusable concepts referenced across companies and industries |
| `theses/` | Macro and cross-industry investment theses |
| `portfolio/` | Portfolio-level watchlist, allocation, and risk thinking |
| `models/` | Modeling conventions and reusable analytical methods |
| `templates/` | Controlled starting points for new research records and derived report artifacts |
| `watchlist/` | Prioritized research queue, not buy or sell recommendations |
| `research-log/` | Append-only company, industry, and repository-wide history |
| `scripts/` | Repository validation and maintenance tools |
| `schemas/` | Machine-readable contracts for structured metadata |

## Start here

Before making any change, read these files in order:

1. [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md)
2. [`AGENTS.md`](AGENTS.md)
3. [`.ai/context.md`](.ai/context.md)
4. [`docs/Framework.md`](docs/Framework.md)

Then follow [`docs/Workflow.md`](docs/Workflow.md) and the relevant template or industry guide.

## Language versions

English `.md` files are canonical and optimized for AI collaboration. Each has a same-directory `.zh-TW.md` Traditional Chinese reading copy for the repository owner. For example, `docs/Framework.md` is paired with `docs/Framework.zh-TW.md`. When the two versions differ, the English file controls and the Chinese file should be synchronized.

## Adding a company

1. Copy `templates/company/` to `companies/<ticker>-<slug>/`.
2. Complete `meta.yaml` with real company identity and `research.yaml` with coverage state, next review, confidence, priority, and watch items.
3. Research the business before forecasting earnings or discussing valuation.
4. Record unresolved questions in `07_open_questions.md`.
5. Register material assumptions in `assumptions.md`, retain lawful source artifacts by category, and create the first quarterly history snapshot.
6. Append the initiating event to `05_timeline.md` and the scoped research log when material.
7. Run `python3 scripts/validate_repository.py`.

The ten standard company filenames are a permanent interface. Do not rename, reorder, or remove them.

## Evidence and uncertainty

Separate sourced facts, analyst estimates, and hypotheses. Record source title, publisher, publication date, access date, and URL where available. State the unit and period for every material number. Use ranges or scenarios when false precision would hide uncertainty.

An assertion becomes durable knowledge only when its evidence, causal mechanism, and implications are clear.

## License

The repository structure and original documentation are available under the [MIT License](LICENSE). Third-party source materials remain subject to their original rights and should normally be linked rather than copied.
