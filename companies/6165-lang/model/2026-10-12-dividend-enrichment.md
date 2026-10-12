# 6165 Lang — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

Live-platform creator economics and other/device revenue drive profit. FY2025 parent CFO 114.932 already includes subsidiary dividends 117.397: never add them twice. Parent bank borrowing is 750, not 785; the 35 amount is prior-year comparative. The base FY2026 CFO estimate 490 includes roughly 290 recurring remittances plus a 200 catch-up of retained subsidiary profit; neither timing nor cash backing is confirmed. The catch-up is not new EPS. Bond redemption 300, buyback 49.032 and declared cash 367.928 leave the cash budget binding. H1 2027 CFO 200 is also conditional. Failure to remit or refinance causes an explicit cash-retention downside DPS of zero. FY2024 original parent CFO 77.227 versus FY2025 comparative 72.891 differs by 4.336; no formal restatement is asserted. FY2024 exact adjusted DPS and stock-dividend completeness remain gaps.

## Normalization and EPS scenarios

Neutralize H1 discrete bond-redemption loss 18.032, disposal gain 7.997, FVTPL loss 11.069 and FX gain 5.582; tax sensitivity 22%-25%, point 23.5%, NCI 1.390 unchanged. Forecast shares 75.7/77.9 are inherited proxies and not a completed dilution reconciliation.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 2.81 | 2.96 | 2.88 |
| 2026E | base | 3.79 | 3.94 | 3.84 |
| 2026E | upside | 4.57 | 4.73 | 4.60 |
| 2027E | downside | 1.86 | 1.86 | 1.87 |
| 2027E | base | 3.94 | 3.94 | 3.95 |
| 2027E | upside | 5.42 | 5.42 | 5.43 |
| 2028E | downside | 1.81 | 1.81 | 1.82 |
| 2028E | base | 4.26 | 4.26 | 4.27 |
| 2028E | upside | 6.35 | 6.35 | 6.36 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / H2 | 1,790.000 | GM 30.00%; opex 335.000; nonop -10.000; tax 23.0% |
| 2027E / FY | 3,669.757 | GM 30.30%; opex 690.000; nonop -18.000; tax 23.0% |
| 2028E / FY | 3,834.642 | GM 30.50%; opex 715.000; nonop -18.000; tax 23.0% |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 351.322 at 2025-12-31; parent FY2025 CFO 114.932. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 351.322 |
| `FY26_CFO_including_subdiv` | 490.000 |
| `prior_declared_cash` | -367.928 |
| `bond_redemption` | -300.000 |
| `FY26_capex` | -15.000 |
| `FY26_lease` | -3.000 |
| `FY26_strategic_investment` | -50.000 |
| `actual_buyback` | -49.032 |
| `H127_CFO_including_subdiv` | 200.000 |
| `H127_capex` | -10.000 |
| `H127_lease` | -1.500 |
| `H127_strategic_investment` | -20.000 |
| `operating_reserve` | -90.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 134.862 | 0.000 | 1.73 |
| base_low | 54.862 | 0.000 | 0.71 |
| base_high | 234.862 | 0.000 | 3.02 |
| downside | -115.138 | 115.138 | 0.00 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **0.71-2.88**, point **1.73**, downside **0.00**. Payout sensitivity 55%-75%, point 65%; income basis `normalized_common_profit`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 0.40 | unverified |
| 2024 | 2025 | 0.60 | unverified |
| 2025 | 2026 | 5.00 | unverified |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: -2.406 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 1.47%-6.01%, downside 0.00%, normalized EPS / required 7% DPS 1.18x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Subsidiary remittance timing, redemption funding, latest diluted shares, historical exact DPS/stock completeness and comparative CFO classification. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
