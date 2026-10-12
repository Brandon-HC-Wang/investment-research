# Forward Dividend Yield Screen

## Purpose and status

This `testing` screen searches TWSE and TPEx common stocks whose normalized 2026 earnings and distributable cash may support cash dividends distributed in 2027 with a reviewed base-yield interval reaching at least 7%. It is linked to the [`forward-dividend-income`](../../strategies/forward-dividend-income/README.md) strategy. Definition version 4 admits an interval whose upper bound reaches the threshold, while distinguishing partial-range from entire-range qualification.

The first persisted exploratory attempt on 2026-10-12 is `partial`; no complete successful run has finished. See the [covered-company pilot worksheet](inputs/2026-10-12-covered-pilot/README.md). The existing [2026-09-09 FVTPL high-yield screen](../../research-log/industries/FVTPLHighYieldScreen.md) is prior discovery evidence, not a run under this definition.

The Phase 2 offline executor is implemented. It evaluates an explicitly prepared CSV and persists a run only when `--dry-run` is omitted. Official market discovery is separate from execution; filing retrieval and analytical normalization remain unimplemented.

The Phase 3 market-discovery collector is implemented at [`scripts/collect_market_discovery.py`](../../scripts/collect_market_discovery.py). It can explicitly retrieve four official TWSE and TPEx datasets and preserve them under [`source-snapshots/`](source-snapshots/README.md). This does not complete the analytical input: normalized EPS, forward DPS, free-cash-flow coverage, and sector-specific adjustments still require reviewed company evidence.

## Calculation boundary

`forward cash dividend yield = estimated 2027 cash DPS / price on the screen date`

`base yield interval = [estimated base cash DPS low, estimated base cash DPS high] / price`

The representative base DPS must lie within the supplied non-negative interval. A single-point estimate must explicitly supply identical low, point and high values; missing bounds are invalid inputs.

`required DPS = price on the screen date × 7%`

`normalized EPS coverage = normalized attributable 2026 diluted EPS / required DPS`

Estimated DPS must use the lower of a conservatively supported payout ratio and parent-company distributable cash capacity. Exchange-displayed yield is a discovery input only because it reflects a historical distribution and may include non-recurring or non-earnings-funded components.

## Candidate and warning logic

Required conditions are a base forward-yield interval upper bound of at least 7%, normalized-EPS coverage of at least 1.25 times, and downside forward yield of at least 5%. These comparisons use unrounded values. A lower bound below 7% with an upper bound at or above 7% is `partial_range`; a lower bound at or above 7% is `entire_range`. Both pass the base-yield gate. A partial-range candidate receives `base_yield_partial_range`; this label does not imply a probability of achieving the target. Ranking continues to consider downside yield, coverage, free-cash-flow dividend coverage, and payout consistency.

Asset disposals, FVTPL and FX gains, tax reversals, capital-surplus distributions, capital reductions, leverage, dilution, weak liquidity, and missing parent-company cash evidence are warning flags. Financial, construction, property, and cyclical companies require sector-specific normalization rather than mechanical annualization.

## Offline input and execution contract

Each CSV row must provide identity (`market`, `ticker`, `company`), a common `price_date` and `financial_period`, price, normalized base and downside EPS, representative base DPS plus `estimated_dps_base_low_twd` and `estimated_dps_base_high_twd`, downside DPS, free-cash-flow dividend coverage, payout-consistency years, warning flags, source tier, evidence reference, and source URL. Numeric assumptions must already have passed human analytical review; the executor does not derive normalized EPS or distributable cash from filings. A range must have evidence and a causal rationale; it cannot be widened merely to reach 7%.

Run a non-persisting validation with:

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input <reviewed-input.csv> \
  --as-of <YYYY-MM-DD> \
  --run-id <unique-run-id> \
  --dry-run --json
```

A persisted run is append-only and records the definition hash, rule, exact thresholds, source URLs, coverage, row errors, result checksum, paired summaries and a frozen `definition.yaml`. Result columns preserve the representative yield, lower/upper yields and `base_yield_qualification`. Duplicate or unsafe run IDs are rejected. Only a complete `success` run updates refresh state; every retained row remains a research candidate requiring human review. Legacy runs use their recorded version and archived definition rather than the latest CSV header.

## Refresh policy

- Perform a light price-input review every seven days.
- Reassess earnings inputs after official monthly revenue.
- Require a full refresh after quarterly or annual filings.
- Require a refresh after dividend decisions or material capital actions.
- Mark the prior run due immediately after a definition change.

The local session-startup check is reminder-only and never accesses the network. A failed or incomplete run cannot advance the last-successful-run timestamp.

## Source hierarchy

Primary sources are TWSE, TPEx, MOPS, official filings, and company disclosures. Secondary structured data may fill a documented gap only when labeled and reconciled where possible. Every run must record source dates, coverage, fallback use, errors, and the exact definition version.

## 2026-10-12 — Readiness audit and discussion items

**Observed status:** The reminder, offline executor, market-discovery collector and repository validators are implemented. All 32 existing offline unit tests passed on 2026-10-12. No formal run manifest or persisted market-discovery snapshot exists for this screen; `last_successful_run` and `latest_run_path` remain null. This proves tested tooling behavior on fixtures, not live full-market availability or strategy performance. The strategy remains `testing`; filing retrieval and analytical normalization are not implemented.

**Decisions still open; no threshold or execution rule changed:**

1. First-run scope: a reviewed pilot of covered companies or the full TWSE/TPEx universe. A pilot should identify its scope explicitly; it cannot claim full-market coverage.
2. Forecast production: define sector-specific normalized EPS, parent distributable-cash capacity, and base/downside cash DPS. Brokerage operating FVTPL must be reconciled with hedge legs, not mechanically removed. Financial-company cash coverage should use capital, funding and parent distribution constraints rather than an unqualified industrial-company free-cash-flow ratio. The current input contract still requires numeric `fcf_dividend_coverage_x`; a suitable financial-sector treatment or exclusion needs a reviewed decision.
3. Threshold and payout meaning: current 7% base yield, 5% downside yield and 1.25× coverage are hypotheses, not validated optimal settings. Coverage is normalized EPS divided by the DPS required to yield 7%, not by estimated actual DPS. Discuss whether a separate actual-DPS coverage constraint is required, and how undeclared dividends, cash-versus-stock choices and payout confidence affect eligibility. Warning flags and free-cash-flow coverage currently inform review/ranking rather than automatic exclusion.
4. Coverage and validation: executor coverage is valid evaluated rows divided by supplied CSV rows. It does not prove analytical coverage of all listed companies. A full-market run needs an independently defined eligible universe and explicit missing-data handling. Validate forecasts against a historical-yield baseline using only information available at each screen date, retaining the strategy's predeclared annual cohorts and outcome metrics.

Suggested sequence: settle forecast/cash definitions and pilot scope, prepare reviewed inputs, complete a clearly scoped first formal run, then expand and test point-in-time outcomes. This audit did not create a run or refresh state. [Strategy validation requirements](../../strategies/forward-dividend-income/README.md).

## 2026-10-12 — Confirmed pilot preparation decisions

The owner confirmed a pilot using already researched companies, sector-specific estimates, separate declared/estimated dividends, and three years of dividend history. These decisions settle the preparation scope raised in the readiness audit above; they do not claim that a formal run or strategy validation has completed.

- **Scope:** Use a small sample from existing company coverage. Record the sample universe and any insufficient-evidence exclusions explicitly; do not label its input-row coverage as full-market coverage.
- **Sector estimates:** Apply the relevant industry model to normalized parent EPS and distributable cash. Retain ordinary expenses and economically related hedge legs. Financial-company coverage uses capital/funding/reserve and parent distribution constraints; project businesses use recognition and collection timing. Do not fabricate a generic free-cash-flow ratio merely to satisfy an executor field; record inapplicable/missing inputs and resolve the input-contract treatment before admitting a row.
- **Dividend status:** Keep declared amounts and analytical estimates separate, with earnings year, decision/payment year, cash/stock classification, source and confidence. An approved dividend may support the current distribution, but is not automatically the next year's cash-DPS forecast.
- **History window:** Initially use the latest three completed, verifiable earnings years: FY2023, FY2024 and FY2025 as of this decision. Record corresponding distribution years separately. Review cash DPS, matched-basis EPS/cash payout ratios, stock dividends/share changes, recurring versus non-earnings distributions, parent cash and capital retention. Preserve raw historical values; use share-consistent derived comparisons. History informs the forecast but does not replace current cash/capital evidence or become a simple three-year-average DPS forecast.
- **Existing thresholds:** For the first pilot, retain the registered base yield 7%, downside yield 5% and EPS coverage 1.25× of required DPS. Additional coverage of estimated actual DPS can be shown as a review diagnostic; no new hard filter is adopted by this preparation decision.

The three-year dividend-history lookback is distinct from the strategy's outcome-validation requirement of at least three annual cohorts and 100 point-in-time company-year observations. A small pilot can verify the workflow without establishing strategy efficacy. The next concrete work is sample selection and an evidence-backed input worksheet, followed by execution under the existing explicit-run policy.

## 2026-10-12 — First persisted exploratory pilot

Explicit run authorization followed the preparation decisions. [Inputs, assumptions and primary evidence](inputs/2026-10-12-covered-pilot/README.md) cover 3213, 5515, 6005 and 6165 with verified 2026-10-08 closes and FY2023–FY2025 dividend history. New cash assumptions remain conditional analyst scenarios requiring human review; consolidated cash proxies are not verified parent distributable cash. This exploratory attempt does not meet the reviewed-input standard for production use.

[Run 2026-10-12-covered-pilot-v1](runs/2026-10-12-covered-pilot-v1/summary.md) is `partial`: 4 input rows, 2 numerically evaluated, 0 retained among those 2, 50.00% coverage. Conditional base/downside forward yields are 4.86%/2.15% for 3213 and 3.89%/2.66% for 5515. The 6005 FCF field is inapplicable; 6165 lacks a coherent supported forward cash-DPS input. Blanks intentionally trigger row errors rather than fabricated zero forecasts. The manifest's `failed_source_count: 2` counts these row-validation errors, not two network failures. Supplementary diagnostics preserve reasons and metrics for rows absent from the candidate-only results CSV.

Thresholds and definition version 3 remain unchanged. Only complete success advances refresh state, so `last_successful_run` and `latest_run_path` remain null. `never_run` now means no successful run, not no attempted run. The 2026-10-08 CLI date is the shared price date; the information cutoff is 2026-10-12, so this is not a historical point-in-time backtest. Next: validate parent cash, complete the missing sector inputs and obtain concrete input review before a new production run. The strategy remains `testing`.

## 2026-10-12 — Baseline interpretation follow-up

The owner asked about replacing stacked conservative assumptions with an evidence-led baseline. The [dated comparison and reproducible sensitivity](../../research-log/industries/ForwardDividendPilot.md#2026-10-12--evidence-led-baseline-versus-stacked-conservative-assumptions) identifies the first pilot's DPS ceilings and minimum-year FCF cap as unverified normal-year restrictions. The operating base, historical cash-allocation behavior and actual parent cash/capital requirements should drive the baseline; stress mechanisms belong in the downside scenario. Earnings-to-payout sensitivity illustrates the effect but is not an admitted dividend forecast. Original input files/run, definition version 3, thresholds and success-only refresh policy are unchanged. Parent-cash and financial-sector contract gaps remain open. No additional formal run was executed by this methodological comparison.

## 2026-10-12 — Confirmed interval gate, definition version 4

The owner explicitly confirmed that 6.42%–7.41% counts as meeting the 7% base-yield criterion. The operative rule is now `base_yield_high_pct >= 7`, inclusive, using unrounded inputs. A range wholly above the threshold also qualifies. Preserve `partial_range` versus `entire_range` in results and retain the representative estimate for context; the point estimate need not independently reach 7%. This does not waive normalized EPS / required DPS 1.25×, downside yield 5%, completeness 95%, cash-capacity evidence or human review.

The prior definition is preserved exactly in [definition-history/3.yaml](definition-history/3.yaml), including the first pilot's manifest hash and legacy CSV fields. The first pilot remains unchanged under version 3; state is due under version 4 until a complete new run succeeds. New runs freeze their definition. The [dated research-log decision](../../research-log/industries/ForwardDividendPilot.md#2026-10-12--confirmed-interval-qualification-rule) records the changed interpretation of the two-company sensitivity. No new formal company run was performed for this rule change; software fixtures verify the boundary and independent gates.
