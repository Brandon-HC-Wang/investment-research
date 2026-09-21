# Forward Dividend Yield Screen

## Purpose and status

This `testing` screen searches TWSE and TPEx common stocks whose normalized 2026 earnings and distributable cash may support cash dividends distributed in 2027 at a forward yield of at least 7%. It is linked to the [`forward-dividend-income`](../../strategies/forward-dividend-income/README.md) strategy.

No formal run has completed. The existing [2026-09-09 FVTPL high-yield screen](../../research-log/industries/FVTPLHighYieldScreen.md) is prior discovery evidence, not a run under this definition.

The Phase 2 offline executor is implemented. It evaluates an explicitly prepared CSV and persists a run only when `--dry-run` is omitted. Official market discovery is separate from execution; filing retrieval and analytical normalization remain unimplemented.

The Phase 3 market-discovery collector is implemented at [`scripts/collect_market_discovery.py`](../../scripts/collect_market_discovery.py). It can explicitly retrieve four official TWSE and TPEx datasets and preserve them under [`source-snapshots/`](source-snapshots/README.md). This does not complete the analytical input: normalized EPS, forward DPS, free-cash-flow coverage, and sector-specific adjustments still require reviewed company evidence.

## Calculation boundary

`forward cash dividend yield = estimated 2027 cash DPS / price on the screen date`

`required DPS = price on the screen date × 7%`

`normalized EPS coverage = normalized attributable 2026 diluted EPS / required DPS`

Estimated DPS must use the lower of a conservatively supported payout ratio and parent-company distributable cash capacity. Exchange-displayed yield is a discovery input only because it reflects a historical distribution and may include non-recurring or non-earnings-funded components.

## Candidate and warning logic

Required conditions are a base forward yield of at least 7%, normalized-EPS coverage of at least 1.25 times, and downside forward yield of at least 5%. Ranking considers downside yield, coverage, free-cash-flow dividend coverage, and payout consistency.

Asset disposals, FVTPL and FX gains, tax reversals, capital-surplus distributions, capital reductions, leverage, dilution, weak liquidity, and missing parent-company cash evidence are warning flags. Financial, construction, property, and cyclical companies require sector-specific normalization rather than mechanical annualization.

## Offline input and execution contract

Each CSV row must provide identity (`market`, `ticker`, `company`), a common `price_date` and `financial_period`, price, normalized base and downside EPS, estimated base and downside DPS, free-cash-flow dividend coverage, payout-consistency years, warning flags, source tier, evidence reference, and source URL. Numeric assumptions must already have passed human analytical review; the executor does not derive normalized EPS or distributable cash from filings.

Run a non-persisting validation with:

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input <reviewed-input.csv> \
  --as-of <YYYY-MM-DD> \
  --run-id <unique-run-id> \
  --dry-run --json
```

A persisted run is append-only and records the definition hash, exact thresholds, source URLs, coverage, row errors, result checksum, and paired summaries. Duplicate or unsafe run IDs are rejected. Only a complete `success` run updates refresh state; every retained row remains a research candidate requiring human review.

## Refresh policy

- Perform a light price-input review every seven days.
- Reassess earnings inputs after official monthly revenue.
- Require a full refresh after quarterly or annual filings.
- Require a refresh after dividend decisions or material capital actions.
- Mark the prior run due immediately after a definition change.

The local session-startup check is reminder-only and never accesses the network. A failed or incomplete run cannot advance the last-successful-run timestamp.

## Source hierarchy

Primary sources are TWSE, TPEx, MOPS, official filings, and company disclosures. Secondary structured data may fill a documented gap only when labeled and reconciled where possible. Every run must record source dates, coverage, fallback use, errors, and the exact definition version.
