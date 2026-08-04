# Company Research Records

Each child directory is the canonical, cumulative record for one publicly traded company. Directories use `<ticker>-<slug>` in lowercase ASCII; the primary listing market belongs in `meta.yaml`. Do not create demonstration or placeholder companies here.

## Permanent file contract

Every company directory must contain:

| File | Canonical responsibility |
|---|---|
| `01_business.md` | Products, customers, revenue model, industry position, and competitive advantage |
| `02_financials.md` | Historical results, earnings quality, cash flow, balance sheet, and capital allocation |
| `03_growth_drivers.md` | Revenue drivers, backlog or leading indicators, replacement drivers, and risks |
| `04_eps_model.md` | Causal forecast, scenarios, assumptions, and reported-to-normalized EPS bridge |
| `05_timeline.md` | Append-only dated milestones and thesis/model changes |
| `06_notes.md` | Sourced observations not yet fully integrated elsewhere |
| `07_open_questions.md` | Durable question registry with `Open`, `Resolved`, or `Rejected` status |
| `08_thesis.md` | Current thesis, variant view, risks, falsification tests, and scorecard |
| `09_valuation.md` | Method selection, normalized valuation, scenarios, and sensitivity |
| `meta.yaml` | Machine-readable identity, workflow state, confidence, priority, and next action |

Copy [`../templates/company/`](../templates/company/) to begin a real company. Replace all instructional content with sourced research; template instructions must not remain in an active company folder.

Supporting material may be stored in a `sources/` subdirectory when local retention is lawful and necessary. Prefer links and source metadata over copied documents.
