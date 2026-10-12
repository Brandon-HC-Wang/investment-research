# 2382 Quanta — dividend enrichment, 2026-10-12

Facts: retained primary filings and three-year declarations. Estimates: all forward EPS, margins, cash flows, reserves and dividends. Hypotheses: cash/remittance timing. Amounts TWD million, shares million, EPS/DPS TWD/share; fiscal year-end 12-31. Earnings FY2026 normally support payment year 2027. No 2027 cash dividend is declared in this model.

## Business and earnings mechanism

AI-system integration and qualification support customer value; accelerator pass-through expands revenue without equal margin. H1 reviewed operating economics anchor the model, while future systems/content and customer mix remain proxies. The new 245 million GDR shares dilute EPS and distribution shares; gross estimated fundraising about 70330 is not EPS. Estimated net 69000 is a financing inflow, with 20000 of unspent earmarks reserved in the base cash case. Materials already paid through CFO are not reserved a second time. 2026-07-28 AUO asset purchase commitment 19700 is deducted in full, pending payment timing. Parent FY2025 CFO -81576.741 reflects working-capital movement -167195.173; the base forecasts CFO 75000 and H1 2027 65000, requiring substantial conversion improvement. Historical cash 9/13/15.6 supports a roughly 75%-85% normalized-profit payout sensitivity, not a guaranteed board decision. The 2026-08-13 announcement states no distribution of H1 2026 earnings.

## Normalization and EPS scenarios

H1 diluted numerator 49950.168 already reverses issuer embedded-derivative gain 408.202: remove FX 6521.848 + remaining FVTPL 411.934 + disposal 178.561 at estimated 20% tax, not all FVTPL a second time. Basic profit removes full FVTPL 820.136. GDR adds 245 million shares on 2026-08-03; weighted issuance and convertible/employee dilution modeled explicitly. Future if-converted addbacks are estimates.

| Year | Case | Reported-style diluted EPS | Normalized diluted EPS | Cash-basis earnings/share |
|---|---|---:|---:|---:|
| 2026E | downside | 20.85 | 19.48 | 19.47 |
| 2026E | base | 24.08 | 22.71 | 22.73 |
| 2026E | upside | 26.84 | 25.47 | 25.52 |
| 2027E | downside | 15.02 | 15.02 | 15.54 |
| 2027E | base | 24.18 | 24.18 | 25.15 |
| 2027E | upside | 28.17 | 28.17 | 29.34 |
| 2028E | downside | 16.11 | 16.11 | 16.68 |
| 2028E | base | 26.09 | 26.09 | 27.16 |
| 2028E | upside | 32.49 | 32.49 | 33.86 |

Reported-style forecasts lock known profit and forecast ordinary future earnings; they do not predict future portfolio marks. Normalization uses marginal tax estimates, not a filing restatement. Product/store/project proxies remain material limitations. [Machine-readable drivers and formulas](2026-10-12-dividend-enrichment.json) preserve all cases and denominators.

## Base operating inputs (estimates)

| Year / modeled period | Revenue | Operating assumptions |
|---|---:|---|
| 2026E / H2 | 2,054,186.233 | OM 3.25%; normal nonop -4500.000; tax 20.0%; NCI 250.000 |
| 2027E / FY | 4,240,000.000 | OM 3.20%; normal nonop -6000.000; tax 20.0%; NCI 450.000 |
| 2028E / FY | 4,580,000.000 | OM 3.20%; normal nonop -6500.000; tax 20.0%; NCI 500.000 |

TWD million except ratios/EPS. H1 profit is locked; future margins and cash collections are assumptions. For all downside/upside driver inputs, use the adjacent JSON.

## Parent cash evidence and conditional budget

Fact: parent cash 31,201.457 at 2025-12-31; parent FY2025 CFO -81,576.741. Consolidated cash is not substituted. Source: [retained parent statements](../sources/2026-10-12-dividend-enrichment.json), balance sheet/cash flow and dividends notes.

Assumed payment window: through 2027-06-30, not a board-approved date. Signed cash budget: opening unrestricted parent cash + projected cash receipts + explicitly modeled funding - prior dividends - capex - leases - interest outside CFO - debt/project calls - operating/earmark reserves. CFO estimates include taxes; interest already in CFO is not subtracted again. Capacity is a liquidity ceiling under assumptions, not verified legally distributable reserves. A negative residual is additional funding need; downside DPS zero means retention, never missing data.

| Signed parent cash item (TWD million) | Base estimate / actual opening |
|---|---:|
| `opening_cash` | 31,201.457 |
| `FY26_CFO` | 75,000.000 |
| `estimated_net_GDR_funding` | 69,000.000 |
| `prior_declared_cash` | -60,256.988 |
| `FY26_PPE` | -3,200.000 |
| `FY26_intangibles` | -200.000 |
| `FY26_lease` | -900.000 |
| `FY26_subcapital` | -10,000.000 |
| `AUO_asset_commitment` | -19,700.000 |
| `H127_CFO` | 65,000.000 |
| `H127_PPE` | -1,800.000 |
| `H127_intangibles` | -100.000 |
| `H127_lease` | -450.000 |
| `H127_subcapital` | -5,000.000 |
| `operating_reserve` | -18,000.000 |
| `unspent_earmarked_fund_reserve` | -20,000.000 |

| Cash path | Residual after reserves | Funding gap | DPS capacity |
|---|---:|---:|---:|
| base | 100,594.469 | 0.000 | 24.49 |
| base_low | 55,594.469 | 0.000 | 13.53 |
| base_high | 116,594.469 | 0.000 | 28.38 |
| downside | 16,594.469 | 0.000 | 4.04 |

Low/high cash changes are explicit in JSON and hold the base operating earnings constant. They represent funding sensitivities, not extra independent pessimistic haircuts on every operating variable. The downside combines a distinct adverse operating and cash path.

Estimated ordinary cash DPS paid in 2027: **13.53-19.32**, point **18.19**, downside **4.04**. Payout sensitivity 75%-85%, point 80%; income basis `normalized_common_profit`. Each cash path caps its matched income-based allocation; no 7% threshold is used to choose dividend assumptions.

## Three-year declared distributions

| Earnings year | Payment year | Declared cash DPS | Stock DPS at par |
|---|---|---:|---:|
| 2023 | 2024 | 9 | 0 |
| 2024 | 2025 | 13 | 0 |
| 2025 | 2026 | 15.6 | 0 |

[History, exact amounts and caveats](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/dividend-history.csv). Earnings-year distributions differ from cash-flow-year payments; preserve original share bases across bonus shares and capital reduction. Stock dividends do not enter cash yield. Historical declarations do not imply a forward floor.

Monthly H1 minus reviewed H1 revenue difference: +0.440 million. This gap is unresolved; derive Q3 from monthly nine-month minus monthly six-month totals, then use reviewed H1 plus Q3 proxy plus estimated Q4. Do not infer audited profit from monthly revenue.

## Thesis, rejection and valuation implications

Forward yield is conditional on the cash paths; it is not independently verified income. At the 2026-10-08 close, estimated base yield 4.16%-5.94%, downside 1.24%, normalized EPS / required 7% DPS 1.00x. Full economic gates: False. This is a diagnostic, not a formal run or backtest. Preserve the sector valuation method; do not capitalize selected gains or assume cash-supported estimates deserve a higher multiple.

Unresolved: GDR actual net receipts/use, asset payment schedule, working-capital conversion and convertible/employee-share reconciliation. Review Q3 2026 filings and payment/capital announcements through 2027 H1. Model confidence 35%; cash confidence 30%; status Open. Confirm when actual operating drivers and parent collections match the bridge; reject/rebuild when margin or collections miss materially, required funding/reserves exceed this budget, or the board selects a materially different cash/stock distribution.

## Source provenance

[Company primary source register](../sources/2026-10-12-dividend-enrichment.json) gives publisher, period, report approval excerpt, access date, public URL/request, SHA-256 and sections. [Shared primary monthly revenue and price register](../../../screens/forward-dividend-yield/cohorts/2026-10-12-covered-enrichment/sources.json) and [prior canonical financial sources](../02_financials.md) complete the H1 anchors. Undated web pages are labeled undated; PDF approval is not an inferred upload date. This dated supplement supersedes earlier forward dividend proxies/current forecast points for this task, preserving their history.
