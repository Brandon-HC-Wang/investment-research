# EPS and cash-dividend scenarios

2026-10-12. Analyst estimates, not company guidance, broker consensus or trade instructions. TWD million, shares million, EPS/DPS TWD/share. [Reproducible inputs](scenario-inputs.json). EPS confidence: medium for 2026, low for 2027/2028; cash payout confidence low.

## Forecast outputs

| Year / 盈餘年 | Case / 情境 | Forecast scope / 期間 | Net operating revenue / 淨營業收益 | Diluted EPS / 稀釋 | Basic EPS / 基本 | Cash DPS estimate / 現金估計 | Payment year / 發放年 |
|---|---|---|---|---|---|---|---|
| 2026 | downside | Q4 | 2,580 | 3.69 | 3.70 | 0.55 | 2027 |
| 2026 | base | Q4 | 6,700 | 4.69 | 4.70 | 1.64 | 2027 |
| 2026 | upside | Q4 | 9,540 | 5.41 | 5.42 | 2.71 | 2027 |
| 2027 | downside | FY | 11,000 | 0.45 | 0.45 | 0.07 | 2028 |
| 2027 | base | FY | 26,800 | 4.10 | 4.10 | 1.44 | 2028 |
| 2027 | upside | FY | 35,800 | 5.71 | 5.72 | 2.86 | 2028 |
| 2028 | downside | FY | 13,300 | 0.83 | 0.83 | 0.12 | 2029 |
| 2028 | base | FY | 28,350 | 4.41 | 4.41 | 1.55 | 2029 |
| 2028 | upside | FY | 38,800 | 6.24 | 6.25 | 3.13 | 2029 |

For 2026 the revenue column is **Q4 only**, not a full-year revenue forecast; September revenue is unverified. EPS/DPS are full-year estimates. For 2027/2028 revenue is the full year. The downside is a sustained trading/volume downturn, including trading losses; it is not an assertion that any 30% index fall produces those outputs. Years are independent bounds, without assigned probabilities.

The base gives **2026 diluted EPS 4.69**, **2027 4.10**, **2028 4.41**. Estimated cash DPS is **1.64 / 1.44 / 1.55**, assuming cash payout 35% of basic parent earnings and no new bonus issue. A practical base-EPS payout sensitivity of **15%–50%** gives cash DPS about **0.70–2.35 for FY2026** and **0.62–2.05 for FY2027**. These are allocation sensitivities, not approved dividend ranges. Full downside/upside combinations are in the table.

## Share and profit anchor

Current issued basic shares **2,455.297058**, diluted model shares **2,459.319**. Nine-month self-reported EPS **3.99** implies parent numerator **9,796.635** by multiplying current basic shares, with approximately **±12.276** from EPS rounding alone. This is an inferred provisional anchor, not an audited parent-profit disclosure. Group net profit **10,483.884** cannot substitute for it. H1 audited parent earnings **7,948.928** and disclosed diluted EPS **3.23** remain separate facts. Q3 audit adjustments/NCI and employee dilution may change the anchor.

`Net operating revenue = service revenue + operating interest + operating dividends + net trading − credit losses`

`Pretax = net operating revenue − operating expenses + associate profit + other income`

`Parent profit = pretax × (1 − effective tax rate) − NCI`

`FY2026 EPS = (inferred 9M parent profit + Q4 modeled parent profit) / assumed FY shares`

`FY2027/2028 EPS = modeled FY parent profit / assumed FY shares`

`Cash DPS = modeled FY parent profit / basic shares × assumed cash payout`

## Operating assumptions

| Year / 年 | Case / 情境 | Services / 服務 | Interest / 利息 | Dividend income / 股利收入 | Net trading / 交易 | Credit loss / 信用損失 |
|---|---|---|---|---|---|---|
| 2026 | downside | 3200 | 1150 | 180 | -1800 | 150 |
| 2026 | base | 4000 | 1350 | 200 | 1200 | 50 |
| 2026 | upside | 4800 | 1500 | 260 | 3000 | 20 |
| 2027 | downside | 7500 | 4000 | 900 | -1000 | 400 |
| 2027 | base | 13600 | 5100 | 1100 | 7200 | 200 |
| 2027 | upside | 17000 | 6000 | 1400 | 11500 | 100 |
| 2028 | downside | 8500 | 4200 | 900 | 0 | 300 |
| 2028 | base | 14500 | 5300 | 1150 | 7600 | 200 |
| 2028 | upside | 18500 | 6400 | 1500 | 12500 | 100 |

| Year / 年 | Case / 情境 | Expenses / 費損 | Associate / 權益法 | Other / 其他 | Tax / 稅率 | NCI / 非控制 |
|---|---|---|---|---|---|---|
| 2026 | downside | 4000 | 150 | 600 | 0% | 50 |
| 2026 | base | 5400 | 200 | 750 | 15% | 170 |
| 2026 | upside | 6400 | 250 | 1000 | 15% | 230 |
| 2027 | downside | 12200 | 600 | 2300 | 20% | 250 |
| 2027 | base | 17400 | 900 | 2400 | 14% | 850 |
| 2027 | upside | 22000 | 1100 | 2700 | 14% | 1100 |
| 2028 | downside | 13300 | 650 | 2250 | 20% | 280 |
| 2028 | base | 18200 | 1000 | 2500 | 14% | 900 |
| 2028 | upside | 23600 | 1250 | 2800 | 14% | 1200 |

Base Q4 revenue **6,700** − expenses **5,400** + associate **200** + other **750** = pretax **2,250**; at 15% tax and NCI 170, parent **1,742.500**. Add inferred nine-month parent **9,796.635** to give FY parent **11,539.135** and diluted EPS **4.69**.

Base 2027 revenue **26,800** − expenses **17,400** + associate **900** + other **2,400** = pretax **12,700**; tax **1,778**, NCI **850**, parent **10,072**, diluted EPS **4.10**. The aggregate tax convention does not levy 14% statutory tax on an already-net associate profit; it approximates group mix/tax reconciliation.

Service baseline includes brokerage 11,400 and other services 2,200. Total 13,600 is below H1 service annualization 15,741.356, so it does not assume Q2's exceptional turnover continues. Financing supports operating interest 5,100, but funding costs remain in expenses. Associate 900 includes a provisional manager contribution 800 plus other equity-method profit 100. Other 2,400 includes financial interest and rents/bank allocations, with only a small disposal allowance; the H1 disposal gain 1,178.667 is not annualized. Net trading 7,200 is below doubling H1 8,083.486, preserving ordinary trading income while recognizing cyclicality.

Downside reduces services/financing and manager earnings, turns trading negative and retains substantial fixed cost; upside requires high trading activity, productive capital and effective net hedging. Costs include funding, compensation, taxes/fees, system costs and depreciation. No arbitrary removal of ordinary costs is made. A future stock bonus would reduce per-share estimates on the enlarged denominator; a hypothetical 10% bonus reduces identical-profit EPS/DPS by division by 1.10 and gives holders additional shares.

## Dividend year and capital retention

**2026 payment already declared for FY2025:** cash **0.40** + stock dividend **1.31**, equivalent to **13.1% more shares** at par 10. Nominal total 1.71 is not cash income or cash yield. Cash payout versus FY2025 reported EPS 2.64 is **15.15%**, total nominal payout **64.77%**. In FY2023/FY2024 cash DPS was 1.33/1.50, but the recent stock-heavy allocation prevents treating the earlier cash ratio as a commitment.

**FY2026 earnings** normally fund distributions in **2027**; **FY2027 earnings** normally fund distributions in **2028**. Thus the requested 2026/2027 estimates must distinguish earnings years from payment years. The 35% base cash ratio is a research assumption, with explicit 15% retention and 50% cash-oriented cases. No future stock-dividend amount or payment date is predicted.

H126 Note 6(21) specifies 10% legal reserve, 20% special reserve and other required amounts before distribution, with cash/stock choices linked to capital budgeting. The stated cash-share floor is not a promise of a 70% cash-earnings payout. Capital adequacy, unrealized-loss reserves, funding and parent-company approval can override the model's cash assumption. [Q-2026-004](07_open_questions.md).

## Earnings quality and sensitivities

Selected-gain H1 sensitivity: `(7,948.928 − (1,178.667 + 43.295) × 80%) / 2,459.319 = 2.83`, compared with reported 3.23. Uniform marginal tax 20%, unchanged NCI; this is not a full normalized result, and compensation releases are not separately double counted. FVOCI equity price changes/transfer gains do not enter EPS; debt realization and operating FVTPL have different rules.

At 2027 base, net trading pretax decrease **1,000** reduces diluted EPS about **0.35** at 14% tax, holding NCI fixed. Brokerage traded-value decline **30%**, assuming fixed share/yield and **40%** variable-cost absorption, reduces EPS about **0.72** before other effects. Capital Investment Trust's modeled contribution **800** falling **30%** changes EPS about **0.08** under the same aggregate tax convention. These are separate controlled sensitivities, not a complete crash forecast. An additional 1-point effective tax costs about **0.052** EPS. The report offers a labeled interactive version of these assumptions.
