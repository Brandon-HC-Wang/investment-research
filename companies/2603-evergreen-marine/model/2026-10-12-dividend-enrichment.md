# 2603 Evergreen Marine — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

Liner-network scale supports service, but freight rates and effective capacity dominate EPS. Elevated FY2026 profit is ordinary cyclical earnings; FY2027 margin is reduced rather than carrying the peak forward. Parent FY2025 cash 12583.307 cannot be replaced by consolidated cash. Subsidiary dividend receipts were 4446.274 in FY2025 versus 71371.602 in FY2024, demonstrating large remittance variability. Base FY2026 remittances 35000 plus H1 2027 20000 and parent CFO 20000/10000 are hypotheses. Parent lease principal 862.777 is not group lease principal; budget vessel/subsidiary calls separately, without charging the entire multi-year group orderbook immediately. Cash payout 45%-50% of normalized current common profit reflects recent roughly half-profit cash allocation. The downside models remittance/funding pressure and zero ordinary payout, not a claim that all profits disappear.

## Normalization and EPS scenarios

Remove H1 FX 336.733 and FVTPL 0.931 at estimated 20% tax, NCI unchanged. Freight-rate cyclicality remains ordinary earnings, not a one-off to delete. Use a separate TWD 22-28 mid-cycle valuation sensitivity; FY2026 is a peak-cycle forecast.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 28.64 | 28.52 | 28.53 |
| 2026E | base | 36.77 | 36.65 | 36.67 |
| 2026E | upside | 43.92 | 43.80 | 43.82 |
| 2027E | downside | 12.52 | 12.52 | 12.53 |
| 2027E | base | 26.48 | 26.48 | 26.49 |
| 2027E | upside | 43.57 | 43.57 | 43.59 |
| 2028E | downside | 13.01 | 13.01 | 13.02 |
| 2028E | base | 26.93 | 26.93 | 26.95 |
| 2028E | upside | 47.34 | 47.34 | 47.36 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / FY | 473,452.810 | Q3 revenue 146780.356, OM 25.0%; Q4 revenue 135000.000, OM 22.0% |
| 2027E / FY | 440,000.000 | OM 15.50%; normal nonop 5000.000; tax 20.0%; NCI 1200.000 |
| 2028E / FY | 450,000.000 | OM 15.50%; normal nonop 4800.000; tax 20.0%; NCI 1300.000 |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 12,583.307 at 2025-12-31; parent FY2025 CFO -1,965.465. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 12,583.307 |
| `FY26_CFO` | 20,000.000 |
| `FY26_subdiv_outside_CFO` | 35,000.000 |
| `prior_declared_cash` | -34,640.688 |
| `FY26_PPE` | -600.000 |
| `FY26_intangibles` | -100.000 |
| `FY26_parent_lease` | -1,000.000 |
| `FY26_vessel_subfunding` | -5,000.000 |
| `FY26_debt_principal` | -1,000.000 |
| `H127_CFO` | 10,000.000 |
| `H127_subdiv_outside_CFO` | 20,000.000 |
| `H127_PPE` | -300.000 |
| `H127_intangibles` | -50.000 |
| `H127_parent_lease` | -500.000 |
| `H127_vessel_subfunding` | -4,000.000 |
| `H127_debt_principal` | -1,000.000 |
| `operating_reserve` | -10,000.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 39,392.619 | 0.000 | 18.19 |
| base_low | 24,392.619 | 0.000 | 11.27 |
| base_high | 54,392.619 | 0.000 | 25.12 |
| downside | -5,607.381 | 5,607.381 | 0.00 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **11.27-18.33**, point **17.97**, downside **0.00**. Payout sensitivity 45%-50%, point 49%; income basis `normalized_common_profit`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 9.96505 | 0 |
| 2024 | 2025 | 32.5 | 0 |
| 2025 | 2026 | 16 | 0 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: -4.250 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 4.85%-7.89%, downside 0.00%, normalized EPS / required 7% DPS 2.25x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Subsidiary remittances, vessel funding schedule, freight volume/rate mix and payment-window cash. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
