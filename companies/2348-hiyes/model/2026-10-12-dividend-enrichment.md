# 2348 Hiyes — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

Agency fees depend on mandates, sell-through and fee yield; development earnings depend on handovers, ownership and margins. Monthly revenue does not prove project cash collection. FY2025 parent CFO 404.873 is before cash interest 557.551 classified in financing; subtract that interest once. Preferred dividends 48 are separate from ordinary dividends. FY2026 CFO before interest 1000, subsidiary remittances 250 and H1 2027 CFO 550 are scenario assumptions, not confirmed project proceeds. Margin scenarios use agency/development segments, but named-project ownership/guarantees and 2027 replacement remain unverified. Cash allocation 55%-65% of normalized common profit retains more capital than the three prior declared DPS points. Delayed collections and calls can require financing and zero ordinary cash distribution despite positive EPS.

## Normalization and EPS scenarios

Remove net H1 FVTPL gain 23.980 at estimated 20% tax; retain small FX 0.111. Do not mistake Q2 gain 112.849 for H1 net gain. Deduct annual preferred dividend 48 once. Common shares reflect 0.5 stock dividend; diluted 159.7 is an explicit employee-share proxy.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 2.07 | 1.95 | 1.95 |
| 2026E | base | 4.54 | 4.42 | 4.42 |
| 2026E | upside | 6.87 | 6.75 | 6.76 |
| 2027E | downside | 0.04 | 0.04 | 0.04 |
| 2027E | base | 3.46 | 3.46 | 3.46 |
| 2027E | upside | 7.10 | 7.10 | 7.11 |
| 2028E | downside | 0.29 | 0.29 | 0.30 |
| 2028E | base | 3.99 | 3.99 | 4.00 |
| 2028E | upside | 8.24 | 8.24 | 8.25 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / H2 | 7,183.911 | Agency/development 1100.000/6083.911, GM 44.0%/20.0%; finance 300.000; preferred 48.000 |
| 2027E / FY | 9,000.000 | Agency/development 2400.000/6600.000, GM 42.0%/18.0%; finance 600.000; preferred 48.000 |
| 2028E / FY | 9,400.000 | Agency/development 2500.000/6900.000, GM 43.0%/18.5%; finance 585.000; preferred 48.000 |

TWD million except ratios/EPS. The 2026 preferred dividend is deducted once for the full year. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 1,436.942 at 2025-12-31; parent FY2025 CFO 404.873. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 1,436.942 |
| `FY26_CFO_before_interest` | 1,000.000 |
| `FY26_subdiv_outside_CFO` | 250.000 |
| `FY26_other_investment_cash` | 50.000 |
| `prior_ordinary_cash` | -758.674 |
| `prior_preferred_cash` | -48.000 |
| `FY26_cash_interest` | -600.000 |
| `FY26_capex` | -5.000 |
| `FY26_lease` | -5.000 |
| `FY26_debt_principal` | -100.000 |
| `FY26_project_funding` | -250.000 |
| `H127_CFO_before_interest` | 550.000 |
| `H127_subdiv_outside_CFO` | 150.000 |
| `H127_other_investment_cash` | 20.000 |
| `H127_cash_interest` | -300.000 |
| `H127_project_funding` | -125.000 |
| `preferred_cash_reserve` | -48.000 |
| `H127_capex` | -3.000 |
| `H127_lease` | -3.000 |
| `H127_debt_principal` | -50.000 |
| `operating_reserve` | -650.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 511.268 | 0.000 | 3.21 |
| base_low | 271.268 | 0.000 | 1.70 |
| base_high | 1,001.268 | 0.000 | 6.28 |
| downside | -1,638.732 | 1,638.732 | 0.00 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **1.70-2.87**, point **2.65**, downside **0.00**. Payout sensitivity 55%-65%, point 60%; income basis `normalized_common_profit`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 7 | 3 |
| 2024 | 2025 | 9 | 0 |
| 2025 | 2026 | 5 | 0.5 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: +0.177 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 2.39%-4.03%, downside 0.00%, normalized EPS / required 7% DPS 0.88x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Project-level attribution/collections/guarantees, debt maturity and 2027 replacement. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
