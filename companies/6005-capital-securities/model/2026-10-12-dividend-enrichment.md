# 6005 Capital Securities — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

The revenue mix is brokerage, financing and underwriting/service fees plus net trading; ETF management profit enters through the associate and is not all revenue. Financial CFO -8333.763 includes funded trading/financing assets and is not industrial FCF. Parent cash 21955.301 and company-disclosed capital ratio 265% are facts; monetary eligible capital and risk denominator are missing. The base liquidity reserve 13000 plus market/settlement buffer 2500 is an analyst stress budget, not statutory free capital. A 15%-50% cash payout band reflects 2025 cash 0.40 plus stock 1.31 versus previous cash 1.33/1.50; 35% is a conditional point, not the historical total payout ratio. Dividend legality and post-payout capital adequacy remain unverified; base earnings include realized selected gains that may support actual cash distribution.

## Normalization and EPS scenarios

Remove selected H1 investment disposal 1178.667 and liability release 43.295 at estimated 20% marginal tax, NCI unchanged. Retain net ordinary trading and paired hedge P&L. This is a selected-gain sensitivity, not through-cycle EPS. Nine-month profit inferred from rounded EPS has +/-12.276485 million uncertainty.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 3.69 | 3.29 | 3.30 |
| 2026E | base | 4.69 | 4.29 | 4.30 |
| 2026E | upside | 5.41 | 5.01 | 5.02 |
| 2027E | downside | 0.45 | 0.45 | 0.45 |
| 2027E | base | 4.10 | 4.10 | 4.10 |
| 2027E | upside | 5.71 | 5.71 | 5.72 |
| 2028E | downside | 0.83 | 0.83 | 0.83 |
| 2028E | base | 4.41 | 4.41 | 4.41 |
| 2028E | upside | 6.24 | 6.24 | 6.25 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / Q4 | 6,700.000 | Service 4000.000; net trading 1200.000; opex 5400.000; tax 15.0% |
| 2027E / FY | 26,800.000 | Service 13600.000; net trading 7200.000; opex 17400.000; tax 14.0% |
| 2028E / FY | 28,350.000 | Service 14500.000; net trading 7600.000; opex 18200.000; tax 14.0% |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 21,955.301 at 2026-06-30; parent 2026H1 CFO -8,333.763. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_H126_parent_cash` | 21,955.301 |
| `future_net_funding_credit` | 0.000 |
| `prior_declared_cash` | -868.363 |
| `future_capex` | -250.000 |
| `future_lease` | -100.000 |
| `settlement_and_market_buffer` | -2,500.000 |
| `retained_corporate_liquidity` | -13,000.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 5,236.938 | 0.000 | 2.13 |
| base_low | 1,736.938 | 0.000 | 0.71 |
| base_high | 7,236.938 | 0.000 | 2.95 |
| downside | 736.938 | 0.000 | 0.30 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **0.70-2.35**, point **1.64**, downside **0.30**. Payout sensitivity 15%-50%, point 35%; income basis `reported_profit_with_portfolio_support`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 1.33 | 0 |
| 2024 | 2025 | 1.50 | 0 |
| 2025 | 2026 | 0.40 | 1.31 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 2.20%-7.33%, downside 0.94%, normalized EPS / required 7% DPS 1.91x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Monetary eligible capital, risk denominator, segregated/pledged cash, post-distribution stress and cash/stock allocation. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
