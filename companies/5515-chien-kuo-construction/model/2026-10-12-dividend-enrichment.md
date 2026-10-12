# 5515 Chien Kuo — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

Construction revenue depends on executable backlog, progress and cost-to-complete; disclosed backlog 46520 does not guarantee a particular annual margin. FY2025 parent CFO 2690.591 includes 1587.090 increased advances: it is not recurring free cash. Cash allocation 50%-60% of reported-style FY2026 profit is below the roughly 64%-74% recent total-profit payout, reserving more funding after a gain-heavy H1. This can exceed normalized EPS and is explicitly portfolio-supported. The budget reserves 450 total projected fund/project calls plus 1100 for advances and operations; the call schedule is not verified. The FY2025 parent statement printed equity total 5803.634 differs from component/equity-change total 5252.615; no capital headroom is inferred from it.

## Normalization and EPS scenarios

Core H1 proxy removes FVTPL 724.148, disposal 111.000 and compensation reversal 16.600 from H1 group pretax 1407.063, then applies estimated 20% tax and zero NCI. Reported-style FY2026 retains actual H1 parent profit plus H2 core, with no forecast additional portfolio gain. Actual portfolio and NCI attribution remains unverified.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 6.62 | 2.78 | 2.80 |
| 2026E | base | 7.81 | 3.97 | 4.00 |
| 2026E | upside | 8.61 | 4.76 | 4.80 |
| 2027E | downside | 2.93 | 2.93 | 2.95 |
| 2027E | base | 4.13 | 4.13 | 4.16 |
| 2027E | upside | 5.00 | 5.00 | 5.04 |
| 2028E | downside | 3.09 | 3.09 | 3.12 |
| 2028E | base | 4.37 | 4.37 | 4.40 |
| 2028E | upside | 5.40 | 5.40 | 5.44 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / H2 core proxy | not separately forecast | Core basic EPS 4.00; H1 normalized profit 444.252; H2 core profit 362.148 |
| 2027E / FY | 8,700.000 | GM 17.00%; opex 455.000; other 25.000; tax 20.0% |
| 2028E / FY | 9,200.000 | GM 17.00%; opex 480.000; other 25.000; tax 20.0% |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 2,110.165 at 2025-12-31; parent FY2025 CFO 2,690.591. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 2,110.165 |
| `FY26_CFO` | 1,000.000 |
| `FY26_dividends_outside_CFO` | 50.000 |
| `prior_declared_cash` | -665.280 |
| `FY26_capex` | -150.000 |
| `FY26_lease` | -20.000 |
| `FY26_debt_principal` | -100.000 |
| `FY26_fund_project_calls` | -300.000 |
| `H127_CFO` | 350.000 |
| `H127_dividends_outside_CFO` | 25.000 |
| `H127_capex` | -75.000 |
| `H127_lease` | -10.000 |
| `H127_debt_principal` | -50.000 |
| `H127_fund_project_calls` | -150.000 |
| `advance_and_operating_reserve` | -1,100.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 914.885 | 0.000 | 4.54 |
| base_low | 714.885 | 0.000 | 3.55 |
| base_high | 1,114.885 | 0.000 | 5.53 |
| downside | 364.885 | 0.000 | 1.81 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **3.55-4.72**, point **4.33**, downside **1.81**. Payout sensitivity 50%-60%, point 55%; income basis `reported_profit_with_portfolio_support`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 1.00 | 0 |
| 2024 | 2025 | 2.15 | 0 |
| 2025 | 2026 | 3.30 | 0 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: +0.000 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 6.73%-8.96%, downside 3.43%, normalized EPS / required 7% DPS 1.08x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Portfolio profit/NCI reconciliation, capital-call schedule and parent equity total discrepancy. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
