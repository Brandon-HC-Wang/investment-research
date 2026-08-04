# Agent Operating Contract

These instructions apply to every human or AI assistant modifying this repository.

## Required context load

Before any modification, read in this order:

1. `PROJECT_CONTEXT.md`
2. `AGENTS.md`
3. `.ai/context.md`
4. `docs/Framework.md`

For company work, then read the company’s `meta.yaml`, `research.yaml`, `08_thesis.md`, `assumptions.md`, `07_open_questions.md`, latest quarterly snapshot, and the remaining numbered files. Read the relevant industry package and model documentation before changing forecasts.

## Primary obligation

Every analysis must improve the repository. Do not leave a material conclusion only in a chat response. Update the canonical company, industry, model, or research-log record in the same task.

## Research sequence

Always reason in this order:

1. Business model and customer value.
2. Competitive advantage and its durability.
3. Revenue drivers: volume, price, mix, share, capacity, cycle, new products, or acquisitions.
4. EPS drivers: gross margin, operating leverage, FX, inventory, amortization, investment income, tax, share count, and one-off items.
5. Recurring versus non-recurring earnings.
6. Backlog, pipeline, replacement drivers, and future visibility.
7. The one or two risks most likely to reduce EPS.
8. Thesis, falsification conditions, and monitoring signals.
9. Valuation using a method appropriate to the business.

Never begin with valuation or a stock-price target.

## Evidence discipline

- Label facts, estimates, hypotheses, and opinions explicitly when ambiguity is possible.
- Cite primary sources whenever available. Use secondary sources to add context, not to replace accessible filings or company disclosures.
- Record source title, publisher, date, access date, and URL. Include page or section references for long documents.
- State currency, units, fiscal period, and whether values are reported, adjusted, or estimated.
- Do not convert management targets into facts. Preserve the attribution and time horizon.
- Do not invent missing data. Record the gap in `07_open_questions.md` and define how it can be resolved.
- Prefer ranges and scenarios to unsupported precision.

## Change rules

### Append history; do not rewrite it

Historical assumptions, thesis changes, question resolutions, and dated observations are append-only. If an earlier item is wrong, mark it superseded or rejected, explain why, and link to the new evidence. Never silently edit history into agreement with the present view.

### Update canonical records

- Financial results, margins, balance-sheet changes, and cash flow → `02_financials.md`.
- Growth assumptions, backlog, pipeline, and replacement drivers → `03_growth_drivers.md`.
- Forecast logic, scenario assumptions, and EPS bridges → `04_eps_model.md`.
- Dated corporate, industry, model, and thesis milestones → `05_timeline.md`.
- New observations that do not yet alter the thesis → `06_notes.md`.
- Unanswered or invalidated questions → `07_open_questions.md`.
- Thesis, confidence, variant perception, and falsification conditions → `08_thesis.md`.
- Multiple history and valuation assumptions → `09_valuation.md`.
- Stable company identity and backward-compatible metadata → `meta.yaml`.
- Coverage workflow, review timing, confidence, priority, and watch items → `research.yaml`.
- Testable assumptions and their `Open`, `Verified`, or `Rejected` history → `assumptions.md`.
- Point-in-time quarterly research state → a new append-only file under `history/`.
- Retained primary and secondary artifacts → the appropriate category under `sources/`.
- Cross-company or reusable findings → the relevant industry file or `research-log/`.

### Synchronize dependent records

When evidence changes an earnings assumption, update the financial record, EPS model, thesis implication, timeline, metadata, and relevant open question together. Do not leave contradictory current views in separate files.

## Open-question protocol

Never delete a question. Each question has a durable ID and one status:

- `Open`: evidence is insufficient.
- `Resolved`: evidence supports an answer.
- `Rejected`: the premise was invalid, immaterial, or unanswerable as framed.

When changing status, append the resolution date, evidence, conclusion, and effect on the thesis. New evidence may reopen a resolved question by adding a dated status event; do not erase the prior resolution.

## Hypothesis protocol

State every material hypothesis in testable form:

- claim;
- causal mechanism;
- supporting and contradicting evidence;
- observable confirmation signals;
- observable rejection signals;
- expected time window;
- current status and confidence.

## Assumption protocol

Never delete an assumption. Each assumption has a durable ID, description, confidence percentage, evidence test, model effect, and one status:

- `Open`: not adequately verified.
- `Verified`: current evidence supports the assumption.
- `Rejected`: current evidence invalidates the assumption.

Append dated confidence and status changes. If later evidence challenges a verified assumption, append a new `Open` event rather than erasing the verification history.

## Industry requirements

- **Construction:** track backlog, land bank, completion schedule, joint development, urban renewal, funding, and recognition timing. Monthly revenue is insufficient.
- **Property agency:** separate brokerage, development, and investment projects. Estimate earnings by project and year.
- **Semiconductor:** track inventory, utilization, ASP, mix, capacity, AI exposure, gross margin, customer mix, and end demand.
- **Engineering:** track backlog, order quality, cancellation terms, recognition timing, execution risk, and margin.
- **AI hardware:** track AI servers, edge AI, AI PCs, memory standards, GPU roadmaps, content per system, and customer concentration.

## Writing standard

- Be concise, specific, and neutral.
- Use descriptive headings, short paragraphs, and tables only when they improve comparison.
- Separate fact from interpretation and state uncertainty.
- Explain why a metric changed and what should happen next.
- Use ISO dates (`YYYY-MM-DD`) and consistent units.
- Avoid sensational language, generic risks, vague catalysts, and unsupported adjectives.
- Do not reproduce long source passages; summarize and link.

## Repository integrity

- Company core filenames and numbering are immutable.
- `meta.yaml` remains the stable identity contract; do not replace it with `research.yaml`.
- Where fields temporarily overlap, `research.yaml` is canonical for current research state; keep legacy fields in `meta.yaml` synchronized for backward compatibility.
- Never modify a committed quarterly snapshot to reflect later knowledge; add a new snapshot or dated correction.
- Do not add empty files, placeholder companies, fabricated examples, or unresolved template tokens to active research.
- Keep links relative within the repository.
- Keep one company per directory named `<ticker>-<slug>` using lowercase ASCII and hyphens; store the primary market in `meta.yaml`.
- Run `python3 scripts/validate_repository.py` after structural or company changes.
- Update `CHANGELOG.md` for material changes to schemas, methodology, directory contracts, or automation.

## Prohibited outputs

- Standalone news summaries without analytical integration.
- Buy, sell, or hold instructions.
- Daily price forecasts or momentum-led conclusions.
- Technical analysis as the primary thesis.
- Valuation multiples presented before business and earnings quality.
- Generic risk lists that do not connect to EPS.
- Silent deletion or rewriting of historical research.
