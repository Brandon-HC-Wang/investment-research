# 2727 Wowprime — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

Brands and operating execution create customer value; restaurant returns require mature-store sales and disciplined opening costs. Food, wages, occupancy and recurring closures remain expenses. Parent FY2025 CFO 2228.809, capex/prepayments 949.845 and lease principal 579.969 show why consolidated CFO alone exaggerates distributable cash. Base CFO 2800, capex 920, leases 650 and H1 2027 cash inputs are projected; restricted gift-voucher/guarantee assets are not added to unrestricted cash. Cash allocation 90%-100% references recent high payouts, but the lower bound is limited by reinvestment/reserves. CB conversion is reflected in diluted EPS while additional cash shares remain a sensitivity. Confirm mature-store traffic and China cohort returns before raising the operating margin.

## Normalization and EPS scenarios

Basic/common profit removes H1 FX 8.780, issuer FVTPL gain 0.350 and lease-modification gain 4.646 at estimated 20% tax. Diluted numerator starts from actual 821.952, which already reverses issuer gain 0.350; remove only FX and lease gain, retaining known H1 if-converted interest and estimated H2 addback 5. Retain disposal loss 6.851 and impairment 8.552 as ordinary closure/expansion costs. Annual dilution proxy uses H1 85.865 million, dividend-participating shares 82.8591 million; future conversion can raise the cash denominator.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 17.06 | 16.94 | 17.43 |
| 2026E | base | 19.33 | 19.21 | 19.78 |
| 2026E | upside | 20.85 | 20.73 | 21.35 |
| 2027E | downside | 15.36 | 15.36 | 15.87 |
| 2027E | base | 20.99 | 20.99 | 21.71 |
| 2027E | upside | 24.80 | 24.80 | 25.67 |
| 2028E | downside | 15.66 | 15.66 | 16.18 |
| 2028E | base | 22.46 | 22.46 | 23.24 |
| 2028E | upside | 27.14 | 27.14 | 28.10 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / H2 | 13,467.667 | OM 8.00%; normal nonop -25.000; tax 20.0%; NCI 9.000 |
| 2027E / FY | 28,000.000 | OM 8.30%; normal nonop -50.000; tax 20.0%; NCI 20.000 |
| 2028E / FY | 29,650.000 | OM 8.40%; normal nonop -55.000; tax 20.0%; NCI 23.000 |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 1,548.982 at 2025-12-31; parent FY2025 CFO 2,228.809. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 1,548.982 |
| `FY26_CFO` | 2,800.000 |
| `FY26_subdiv_outside_CFO` | 230.000 |
| `prior_declared_cash` | -1,335.453 |
| `FY26_PPE` | -900.000 |
| `FY26_intangibles` | -20.000 |
| `FY26_lease` | -650.000 |
| `FY26_subcapital` | -150.000 |
| `H127_CFO` | 1,400.000 |
| `H127_subdiv_outside_CFO` | 110.000 |
| `H127_PPE` | -420.000 |
| `H127_intangibles` | -10.000 |
| `H127_lease` | -325.000 |
| `H127_subcapital` | -75.000 |
| `operating_reserve` | -600.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 1,603.529 | 0.000 | 19.35 |
| base_low | 1,328.529 | 0.000 | 16.03 |
| base_high | 1,868.529 | 0.000 | 22.55 |
| downside | 1,195.529 | 0.000 | 14.43 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **16.03-19.78**, point **18.79**, downside **13.94**. Payout sensitivity 90%-100%, point 95%; income basis `normalized_common_profit`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 14.94369495 | 0 |
| 2024 | 2025 | 14.5925781 | 0 |
| 2025 | 2026 | 16.11714977 | 0 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: -101.574 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 6.75%-8.33%, downside 5.87%, normalized EPS / required 7% DPS 1.16x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: Monthly/filing reconciliation, same-store/cohort margins, maintenance versus opening capex and conversion timing. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
