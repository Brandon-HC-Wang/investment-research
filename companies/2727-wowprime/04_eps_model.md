# EPS Model

> Current state: 2026-11-09. All earlier sections retained below describe prior research and are superseded where this dated update differs.

## 2026-11-09 — Current conditional EPS scenarios

**Estimates, not guidance:** Replace the 2026-10-12 forward scenarios with a model locking reviewed 9M profit and forecasting Q4 only. FY2026 base ex-selected-gain diluted EPS becomes **18.43**, versus 19.21; FY2027/FY2028 base becomes **19.73/21.54**, versus 20.99/22.46. The selected-gain exclusion is a normalization proxy, not verified sustainable EPS. Forecast confidence remains 35%, status Open. Amounts TWD million, shares million, EPS TWD/share. [Reproducible model](model/2026-11-09-q3-refresh.json); [S1-S2](sources/2026-11-09-refresh.json).

| FY | Case | Revenue | Reported-style diluted EPS | Ex-selected-gain diluted EPS |
|---|---|---:|---:|---:|
| 2026E | downside | 26,024.973 | 17.44 | 17.26 |
| 2026E | base | 26,624.973 | 18.61 | 18.43 |
| 2026E | upside | 27,124.973 | 19.65 | 19.47 |
| 2027E | downside | 25,500.000 | 14.52 | 14.52 |
| 2027E | base | 28,000.000 | 19.73 | 19.73 |
| 2027E | upside | 30,000.000 | 23.60 | 23.60 |
| 2028E | downside | 26,000.000 | 14.84 | 14.84 |
| 2028E | base | 29,650.000 | 21.54 | 21.54 |
| 2028E | upside | 32,500.000 | 26.49 | 26.49 |

### Geographic operating assumptions

| Period | Case | Taiwan revenue / margin | China revenue / margin | Nonoperating | NCI |
|---|---|---:|---:|---:|---:|
| 2026 Q4 | downside | 5,250 / 7.5% | 1,250 / 2.0% | -30 | 10 |
| 2026 Q4 | base | 5,700 / 8.5% | 1,400 / 3.5% | -20 | 9 |
| 2026 Q4 | upside | 6,100 / 9.2% | 1,500 / 5.0% | -10 | 10 |
| 2027 FY | downside | 20,500 / 7.5% | 5,000 / 2.0% | -70 | 16 |
| 2027 FY | base | 22,700 / 8.8% | 5,300 / 3.5% | -50 | 20 |
| 2027 FY | upside | 24,000 / 9.5% | 6,000 / 5.0% | -25 | 25 |
| 2028 FY | downside | 21,000 / 7.5% | 5,000 / 2.0% | -70 | 18 |
| 2028 FY | base | 24,000 / 9.0% | 5,650 / 4.0% | -55 | 23 |
| 2028 FY | upside | 25,800 / 9.8% | 6,700 / 5.5% | -25 | 30 |

Taiwan/China revenue proxies combine net capacity, mature-store productivity, average spend/mix and FX; the model cannot identify those components separately. The base assumes existing capacity and Q4 seasonal demand support Taiwan 5,700 and China 1,400, with margins 8.5%/3.5%. This requires recovery from Taiwan Q3 8.01%, while China remains near Q3 3.62%. It is conditional, not a revenue booking. For 2027/2028, base total revenue stays at the prior 28,000/29,650, but lower China mix margins reduce the profit path. Base margins assume Taiwan 8.8%/9.0%, China 3.5%/4.0%; improvements require cohort evidence.

### Formula and normalization

Segment profit = Taiwan revenue × Taiwan margin + China revenue × China margin - other-segment loss (Q4 0.140; future FY 0.600). Common profit = (segment profit + normal nonoperating) × (1 - 20% tax) - NCI. Diluted numerator adds after-tax if-converted interest (Q4 2.700; future FY 10.800). Lease interest remains an expense in normal nonoperating; do not add it back as if it were convertible interest.

The 9M reported diluted numerator is 1,193.583. Remove FX gain 12.278, lease-modification gain 6.547 and financial-asset gain 0.240 at assumed 20% tax: adjustment **15.252**, normalized diluted numerator **1,178.331**. The numerator already reverses issuer gain 0.350; do not subtract it again. Normalized common profit also removes issuer gain at the same assumed marginal tax, giving **1,170.305**. Selected-item tax/NCI attribution is not independently disclosed; this is an analyst convention. Ordinary disposal 16.187, impairment 15.781 and share compensation 5.766 remain expenses. FX is not economically non-recurring; the exclusion provides comparability to the previous supplement.

For FY2026, add Q4 parent profit and if-converted interest to the matching 9M numerator, then divide by **85.860** weighted diluted shares. The base reported-style numerator is **1,597.971**, selected-gain-adjusted **1,582.719**; reported-style EPS **18.61**, adjusted proxy **18.43**. Future years use **86.000** diluted shares. Full-year weighting is an estimate; conversion, buybacks, employee transfers and employee compensation can change it. Do not add rounded quarterly EPS.

### Sensitivity and rejection

With Q4 revenue 7,100 and other inputs fixed, a 1 percentage-point consolidated operating-margin change moves FY2026 EPS by **0.66**. At FY2027 revenue 28,000, it moves EPS by **2.60**; a 1 percentage-point China-only margin change on revenue 5,300 moves EPS by **0.49**. These assume 20% tax and no NCI change. Base 2026 fails if Q4 sales/margins fall materially short of 5,700/1,400 and 8.5%/3.5%; re-estimate rather than increasing multiples. The downside changes sales and margins, not merely valuation.

### Dividend boundary

No new 2027 cash-DPS forecast is adopted. The old **16.03-19.78**, point **18.79**, is historical and superseded as a current conclusion because the parent cash bridge and later buyback effects are unverified. On base adjusted common profit 1,571.993 and an illustrative **82.200 million** dividend-share proxy, payout rates of 90%/95%/100% imply earnings-only DPS **17.21/18.17/19.12**. This is neither cash capacity nor a declaration. The share proxy approximates September issued shares 82.940 less own treasury 0.738; later conversion, buybacks and employee transfers remain unresolved. The legal policy is 50%-100% of distributable surplus, with cash at least 20% of total dividends; it does not guarantee the modeled 90%-100% cash payout. Do not calculate a current forward yield from this sensitivity. [S1, pp. 30-33](sources/2026-11-09-refresh.json).

### FY2025 reference anchor

The retained FY2025 parent-only filing reports basic EPS **16.02** and diluted EPS **15.55** (S6, p. 54). These are a reported historical-year reference, not normalized forecasts. Parent-only profit and cash are not substituted for the current consolidated profit bridge. A consistent five-year consolidated history remains incomplete.

## Prior research — preserved through 2026-10-12

> Current dated supplement: [2026-10-12](model/2026-10-12-dividend-enrichment.md). Older dated sections below remain historical.

## Model status

- **As of:** 2026-08-05
- **Currency:** TWD
- **Fiscal year-end:** December
- **Latest reported period:** 2026 Q1; monthly revenue through 2026-06
- **Forecast horizon:** Not initiated
- **EPS definition:** Reported basic EPS until diluted share history and normalization are reconciled

No forward EPS estimate is adopted at discovery. Q1 and monthly revenue establish momentum, but same-store sales, opening cohorts, restaurant-level margins, lease-adjusted returns, and 2026 Q2 segment results are missing. A precise forecast would conceal rather than resolve those uncertainties.

## Operating assumptions

| ID | Period | Assumption | Current value | Confidence | Revision date |
|---|---|---|---|---|---|
| A-2026-001 | 2026 | Revenue growth is supported by more than calendar timing | Open; no model value | 35% | 2026-08-05 |
| A-2026-002 | 2026–2027 | Expansion earns an adequate lease-adjusted return | Open; no model value | 25% | 2026-08-05 |
| A-2026-003 | 2026–2027 | China format recovery can lift segment profit without excessive new-store losses | Open; no model value | 35% | 2026-08-05 |

## Revenue model

The intended model is geographic and store-driven:

`Taiwan revenue = mature-store revenue × same-store growth + net-new-store cohort revenue`

`China revenue = mature-store revenue × same-store growth + replicated/new-format cohort revenue + FX`

Retail and other channels will be separated only if disclosure becomes material. 2026 Q1 reported revenue was TWD 5.294 billion in Taiwan and TWD 1.225 billion in China; these are anchors, not forecasts.

## Margin model

Gross margin will be modeled through average spend and menu mix less food costs. Operating margin will then reflect labor, occupancy and lease depreciation, utilities, pre-opening expense, closure/impairment costs, and central overhead. The key operating-leverage variable is sales per mature store. No margin path is assumed before Q2 and store-cohort evidence are reviewed.

## EPS bridge

The future bridge will run from geographic revenue to gross profit, operating expenses, operating profit, interest and lease finance costs, FX and other non-operating items, tax, non-controlling interests, diluted shares, reported EPS, and normalized EPS. For 2026 Q1, parent net income was TWD 417.5 million and basic EPS was TWD 5.04.

## Normalization

No adjustment is currently adopted. FX, asset disposal, and impairment items were identified in Q1 but were individually modest. New-store opening and closure costs may be economically recurring for an expanding restaurant operator and should not be removed automatically.

## Scenarios

Scenarios remain qualitative pending evidence:

- **Downside:** mature-store traffic weakens while labor and occupancy costs remain sticky; expansion adds lease and pre-opening costs, compressing margin and EPS.
- **Base:** positive but moderate mature-store sales and disciplined openings sustain revenue growth with broadly stable margins.
- **Upside:** Taiwan cohorts reach payback quickly and China's revised formats produce durable same-store growth and margin expansion.

The two largest expected EPS-spread variables are same-store sales and restaurant-level operating margin.

## Sensitivities

Not yet quantified. The first sensitivity table should vary consolidated same-store sales and operating margin, while keeping store count, tax, non-controlling interests, and diluted shares explicit.

## Assumption history

- **2026-08-05:** Model opened without a forward EPS estimate. The next gate is the 2026 Q2 filing and reconciliation of store counts, geographic growth, and margins.

## Model limitations

Missing disclosures include brand-level revenue and margins, same-store sales, customer traffic and spend, openings and closures by period, new-store capex and payback, active app economics, maintenance capex, and lease principal payments by operating cohort. The current model cannot reliably separate organic growth from capacity growth or calculate normalized per-store returns.

## Sources

- *2026 Q1 Consolidated Financial Statements*, Wowprime Corp., issued 2026-05-07, pp. 4–8 and 49–50, <https://www.wowprime.com/upload_cg/img020260511160600.pdf>, accessed 2026-08-05.
- *TWSE Company Profile: 2727 Wowprime*, Taiwan Stock Exchange, produced 2026-08-05, pp. 1–2, <https://www.twse.com.tw/pdf/ch/2727_ch.pdf>, accessed 2026-08-05.

## 2026-10-12 — Eight-company dividend enrichment

Current task estimates: FY2026E normalized diluted EPS 19.21; FY2027E/FY2028E 20.99/22.46. Estimated 2027 ordinary cash DPS 16.03-19.78, point 18.79, downside 13.94. Basic/common profit removes H1 FX 8.780, issuer FVTPL gain 0.350 and lease-modification gain 4.646 at estimated 20% tax. Diluted numerator starts from actual 821.952, which already reverses issuer gain 0.350; remove only FX and lease gain, retaining known H1 if-converted interest and estimated H2 addback 5. Retain disposal loss 6.851 and impairment 8.552 as ordinary closure/expansion costs. Annual dilution proxy uses H1 85.865 million, dividend-participating shares 82.8591 million; future conversion can raise the cash denominator. [dated EPS/dividend/cash supplement](model/2026-10-12-dividend-enrichment.md) contains the reproducible drivers, tax/NCI/share bridges and cash budgets. Earlier points remain historical and are superseded for this task; the underlying reported model for Crete/Capital/Lang is retained as the baseline.
