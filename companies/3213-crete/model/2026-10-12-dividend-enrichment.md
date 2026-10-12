# 3213 Crete — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

Rugged computers provide high-value engineering and service content; commercial distribution has lower margin. Durability depends on qualification and replacement orders, not a single monthly shipment. Inventory and advance payments absorbed H1 cash even though profit was strong. FY2025 parent cash includes 1227.871 of FVOCI disposal proceeds; the opening balance already contains that cash, so the budget never adds it again. Base FY2026 parent CFO 400 and H1 2027 CFO 220 assume inventory conversion. Reject this cash path if Q3 inventory or advances keep rising without collections. Cash allocation 65%-75% of normalized common profit is close to the roughly 69%-95% historical EPS payout band and avoids using disposal cash as recurring income.

## Normalization and EPS scenarios

Remove H1 FVTPL 2.962 and FX 3.275 at estimated 25% marginal tax; unchanged NCI. FVOCI equity disposal gains are already outside EPS. Retain ordinary interest and associate profit; do not remove inventory and scrap costs.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 9.38 | 9.30 | 9.40 |
| 2026E | base | 12.15 | 12.07 | 12.20 |
| 2026E | upside | 14.26 | 14.18 | 14.33 |
| 2027E | downside | 8.01 | 8.01 | 8.10 |
| 2027E | base | 13.86 | 13.86 | 14.01 |
| 2027E | upside | 17.62 | 17.62 | 17.81 |
| 2028E | downside | 7.23 | 7.23 | 7.31 |
| 2028E | base | 14.53 | 14.53 | 14.69 |
| 2028E | upside | 19.71 | 19.71 | 19.92 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / H2 | 2,063.992 | GM 35.00%; opex 210.000; nonop 25.000; tax 25.0%; NCI 12.000 |
| 2027E / FY | 4,300.000 | GM 35.50%; opex 440.000; nonop 50.000; tax 25.0%; NCI 30.000 |
| 2028E / FY | 4,620.000 | GM 35.00%; opex 475.000; nonop 50.000; tax 25.0%; NCI 32.000 |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 1,431.536 at 2025-12-31; parent FY2025 CFO 592.677. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 1,431.536 |
| `FY26_CFO` | 400.000 |
| `FY26_capex` | -50.000 |
| `FY26_lease` | -32.000 |
| `FY26_interest_outside_CFO` | -1.100 |
| `prior_declared_cash` | -410.799 |
| `H127_CFO` | 220.000 |
| `H127_capex` | -25.000 |
| `H127_lease` | -16.000 |
| `H127_interest_outside_CFO` | -0.550 |
| `operating_reserve` | -600.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 916.087 | 0.000 | 15.61 |
| base_low | 776.087 | 0.000 | 13.22 |
| base_high | 1,056.087 | 0.000 | 18.00 |
| downside | 486.087 | 0.000 | 8.28 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **7.93-9.15**, point **8.54**, downside **6.11**. Payout sensitivity 65%-75%, point 70%; income basis `normalized_common_profit`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 5.40 | 0 |
| 2024 | 2025 | 6.00 | 0 |
| 2025 | 2026 | 7.00 | 0 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: -0.369 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 6.42%-7.41%, downside 4.95%, normalized EPS / required 7% DPS 1.40x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Inventory/advance conversion; parent H2 actual cash; future reserve and board cash allocation. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
