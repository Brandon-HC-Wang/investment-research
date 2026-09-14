# Forward Dividend Yield Screen

## Purpose and status

This `testing` screen searches TWSE and TPEx common stocks whose normalized 2026 earnings and distributable cash may support cash dividends distributed in 2027 at a forward yield of at least 7%. It is linked to the [`forward-dividend-income`](../../strategies/forward-dividend-income/README.md) strategy.

No formal run has completed. The existing [2026-09-09 FVTPL high-yield screen](../../research-log/industries/FVTPLHighYieldScreen.md) is prior discovery evidence, not a run under this definition.

## Calculation boundary

`forward cash dividend yield = estimated 2027 cash DPS / price on the screen date`

`required DPS = price on the screen date × 7%`

`normalized EPS coverage = normalized attributable 2026 diluted EPS / required DPS`

Estimated DPS must use the lower of a conservatively supported payout ratio and parent-company distributable cash capacity. Exchange-displayed yield is a discovery input only because it reflects a historical distribution and may include non-recurring or non-earnings-funded components.

## Candidate and warning logic

Required conditions are a base forward yield of at least 7%, normalized-EPS coverage of at least 1.25 times, and downside forward yield of at least 5%. Ranking considers downside yield, coverage, free-cash-flow dividend coverage, and payout consistency.

Asset disposals, FVTPL and FX gains, tax reversals, capital-surplus distributions, capital reductions, leverage, dilution, weak liquidity, and missing parent-company cash evidence are warning flags. Financial, construction, property, and cyclical companies require sector-specific normalization rather than mechanical annualization.

## Refresh policy

- Perform a light price-input review every seven days.
- Reassess earnings inputs after official monthly revenue.
- Require a full refresh after quarterly or annual filings.
- Require a refresh after dividend decisions or material capital actions.
- Mark the prior run due immediately after a definition change.

The local session-startup check is reminder-only and never accesses the network. A failed or incomplete run cannot advance the last-successful-run timestamp.

## Source hierarchy

Primary sources are TWSE, TPEx, MOPS, official filings, and company disclosures. Secondary structured data may fill a documented gap only when labeled and reconciled where possible. Every run must record source dates, coverage, fallback use, errors, and the exact definition version.
