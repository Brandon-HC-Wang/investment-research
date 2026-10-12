# EPS model — explicit operating scenarios

> Current dated supplement: [2026-10-12](model/2026-10-12-dividend-enrichment.md). Older dated sections below remain historical.

As of 2026-09-21. Latest reported FY2025 basic/diluted EPS: 4.02/3.59; H126: 1.91/1.91. [Financial evidence](02_financials.md). Forecasts are analyst estimates with low confidence, not guidance or consensus. Amounts below are TWD million, shares million and EPS TWD/share.

## Reproducible inputs and formula

[Inputs](model/scenario-inputs.json), [outputs](model/scenario-results.csv). Revenue = live revenue + other revenue; gross profit = revenue × gross margin; operating profit = gross profit − expenses; parent income = (operating profit + net nonoperating income) × (1 − tax rate) − minority income. FY2026 combines reported H1 amounts with estimated H2; FY2027–2028 are fully estimated. No unverified overseas/poker/cooperation profit is added.

| H2 2026 input | downside | base | upside |
|---|---:|---:|---:|
| Live revenue | 1,450 | 1,600 | 1,750 |
| Other revenue | 150 | 190 | 220 |
| Gross margin | 28% | 30% | 31% |
| Operating expenses | 335 | 335 | 340 |
| Net nonoperating income | -15 | -10 | -5 |
| Tax | 25% | 23% | 22% |
| Minority income | 2 | 2 | 2 |

Base H2 live revenue is 3.85% above H1; downside is -5.88% and upside +13.59%. Base preserves H1's roughly 30% margin while increasing expenses. The observed monthly revenue provides a scale check, not a segment forecast. FY2027/2028 live growth is -5%/0% downside, +5%/+5% base and +10%/+10% upside; other growth -5%/0%, 0%/0%, +5%/+5%. Respective gross margins: 28%/28%, 30.3%/30.5%, 31.5%/32%; expenses 660/665, 690/715, 715/765. Annual nonoperating income -25/-18/-12 by scenario, taxes 25%/23%/22%, minority income 4. SBC, amortization, credit costs and development remain within expenses.

Share assumptions: 75.7 million FY2026 approximates H1 diluted 73.685 and H2 near fully issued 77.753; 77.9 million thereafter allows a small employee dilution buffer. This is conservative versus permanent treasury-share exclusion, but not a ceiling if new placements occur. The redeemed 300 million bond is not carried as future dilution. Actual later employee transfers and placements remain Q-2026-004.

| Scenario | Year | Revenue | Operating profit | Parent income | Diluted-share assumption | EPS estimate |
|---|---:|---:|---:|---:|---:|---:|
| downside | 2026 | 3322.7 | 314.8 | 212.4 | 75.7 | 2.81 |
| downside | 2027 | 3156.6 | 223.8 | 145.1 | 77.9 | 1.86 |
| downside | 2028 | 3156.6 | 218.8 | 141.4 | 77.9 | 1.81 |
| base | 2026 | 3512.7 | 403.8 | 286.8 | 75.7 | 3.79 |
| base | 2027 | 3669.8 | 421.9 | 307.0 | 77.9 | 3.94 |
| base | 2028 | 3834.6 | 454.6 | 332.2 | 77.9 | 4.26 |
| upside | 2026 | 3692.7 | 472.5 | 346.2 | 75.7 | 4.57 |
| upside | 2027 | 4041.9 | 558.2 | 422.0 | 77.9 | 5.42 |
| upside | 2028 | 4425.0 | 651.0 | 494.4 | 77.9 | 6.35 |

## Normalization bridge: illustrative, not audited adjusted EPS

FY2025 reported pretax 361.946 − disposal gains 11.903 + FVTPL loss 5.171 + FX loss 4.142 = 359.356. With 22–25% assumed normalized tax and unchanged minority 8.113, earnings per historical basic share (76.671 million) are 3.41–3.55. This is a basic-share earnings-quality comparison, not diluted EPS; historical convertible dilution is not erased from reported figures.

H126 reported pretax 185.652 + bond redemption loss 18.032 − disposal gains 7.997 + FVTPL loss 11.069 − FX gain 5.582 = 201.174. Applying 22–25% tax and unchanged minority 1.390 yields parent income 149.491–155.526, or 2.03–2.11 on disclosed diluted shares 73.685. Actual tax deductibility and attribution of adjustments are unverified. FX and portfolio marks are volatile rather than necessarily non-recurring; neutralizing both gains and losses is an analytical convention, not a claim that they disappear.

Substituting this normalized H1 into the 2026 base gives EPS 3.90–3.98, compared with reported-style scenario EPS 3.79. H2 nonoperating assumption already omits a second bond-redemption event: do not add it back twice. No automatic amortization or SBC addback is made.

## Sensitivities and invalidation

At base 2026 scale, one percentage point of annual gross margin changes EPS by approximately 0.36 at 23% tax, before behavioral responses. Five extra percentage points of tax on TWD 400 million pretax cost about 0.26/share on 77.9 million shares. A 10% share increase reduces EPS by 9.09% at unchanged income. Two consecutive quarters of declining live revenue with gross margin below 28%, or recurring other-business losses above TWD 20 million per half-year, trigger a base-case reassessment.

## 2026-10-12 — Eight-company dividend enrichment

Current task estimates: FY2026E normalized diluted EPS 3.94; FY2027E/FY2028E 3.94/4.26. Estimated 2027 ordinary cash DPS 0.71-2.88, point 1.73, downside 0.00. Neutralize H1 discrete bond-redemption loss 18.032, disposal gain 7.997, FVTPL loss 11.069 and FX gain 5.582; tax sensitivity 22%-25%, point 23.5%, NCI 1.390 unchanged. Forecast shares 75.7/77.9 are inherited proxies and not a completed dilution reconciliation. [dated EPS/dividend/cash supplement](model/2026-10-12-dividend-enrichment.md) contains the reproducible drivers, tax/NCI/share bridges and cash budgets. Earlier points remain historical and are superseded for this task; the underlying reported model for Crete/Capital/Lang is retained as the baseline.
