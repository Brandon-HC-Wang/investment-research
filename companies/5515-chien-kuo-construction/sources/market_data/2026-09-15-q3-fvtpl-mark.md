# 2026-09-15 FVTPL-to-EPS Refresh

## Scope

Estimate, not reported Q3 earnings. Chien Kuo is a contract constructor; these treasury marks do not change construction revenue, margin, backlog, or normalized earnings. Currency: TWD million except per-share prices and EPS. June 30 units and carrying values are retained from the [prior calculation](2026-09-09-q3-fvtpl-mark.md); post-June trades are unverified. Quotes are September 14, except Allianz NAV September 11. No September 15 quote is assumed.

## Repriced positions

| Position | Units (thousand) | Price / NAV (TWD) | June carrying value | Estimated value | Pretax change |
|---|---:|---:|---:|---:|---:|
| AuthenX / 合聖科技 (7928) | 323 | 375.80 average | 165.933 | 121.38340 | -44.54960 |
| 恆勁科技 (6920) | 651 | 97.80 average | 64.992 | 63.66780 | -1.32420 |
| 泰宗 (4169) | 538 | 142.50 close | 117.015 | 76.66500 | -40.35000 |
| 安聯四季雙收入息 A累積新臺幣 | 2,888 | 20.74 | 61.778 | 59.89712 | -1.88088 |
| 瀚亞高科技 | 102 | 668.43 | 67.035 | 68.17986 | +1.14486 |
| 野村高科技累積台幣 | 659 | 121.20 | 79.390 | 79.87080 | +0.48080 |
| 富邦新台商 A | 149 | 370.01 | 60.870 | 55.13149 | -5.73851 |
| **Total** | | | **617.013** | **524.79547** | **-92.21753** |

Value = thousand units × price ÷ 1,000. Displayed units are rounded filing inputs, not an exact share register. Emerging-stock averages are secondary-source proxies, not independently verified TPEx reporting-date fair values. The named money-market pool of 1,662.046 retains the earlier illustrative 0.30% return (+4.986138); it is not refreshed fund-by-fund. The remaining 3,172.702 is not directly repriced.

## EPS bridge

EPS effect = pretax FVTPL gain or loss × (1 − assumed tax rate) ÷ weighted-average shares. Use 20% and 201.6 million shares, with no new minority-interest adjustment; actual tax, ownership and share count must be reconciled in Q3.

- H1 reported FVTPL gain: **724.148**, refreshed against MOPS Q2 Inline XBRL note N7235. Indicative EPS contribution: **+2.87360**. The amount is reported; this item-level tax-adjusted EPS is an estimate.
- Q3-to-date base: **-92.21753 + 4.986138 = -87.231392**, or **-0.34616 EPS**.
- YTD indicative FVTPL gain: **724.148 − 87.231392 = 636.916608**, or **+2.52745 EPS**. This is FVTPL contribution only, not total company EPS.
- Compared with September 9's same-input model, Q3 EPS contribution deteriorated by approximately **0.052 EPS**.
- At 0% assumed tax, H1 / Q3 base / YTD contributions would be **+3.592 / -0.433 / +3.159**. A tax benefit on a valuation loss is not assured.

| Unpriced bucket scenario | Q3 pretax change | Q3 EPS contribution | YTD EPS contribution |
|---|---:|---:|---:|
| -3% | -182.412452 | -0.724 | +2.150 |
| Flat (base) | -87.231392 | -0.346 | +2.527 |
| +3% | +7.949668 | +0.032 | +2.905 |

These are sensitivities, not probabilities or bounds on actual losses. Base current FVTPL asset value is approximately **5,364.530 million** (5,451.761 − 87.231392); the asset balance itself must not be divided by shares and called EPS.

## Limits and next verification

Only 617.013 million (11.3% of the June pool) is directly repriced. Excluded: purchases, sales, dividends/distributions, FX details, private valuation changes, ownership changes, and portfolio turnover. A NAV-only fall after a distribution does not necessarily equal an economic loss; distributions are not added here. The TPEx API returned 403 in browsing; certificate troubleshooting remains deferred and TLS verification was not bypassed. Eastspring's primary NAV page did not expose usable data; Nomura's primary page exposed no usable NAV. Secondary quotes/NAVs therefore lower confidence.

Retain full-year reported and normalized scenarios. Q-2026-003 and A-2026-004 remain Open; confidence in the full portfolio estimate is low-to-medium. Reconcile actual September 30 holdings, transaction movements, FVTPL gain/loss, tax and EPS with the Q3 filing.

## Sources

All accessed 2026-09-15. Short observed data retained above; primary holdings provenance remains in the prior calculation.

- *2026 Q2 Consolidated Inline XBRL*, Chien Kuo / MOPS, approved 2026-08-12; other-gains note N7235, Q2 665.350 and H1 724.148 million: <https://mopsov.twse.com.tw/server-java/t164sb01?step=1&CO_ID=5515&SYEAR=2026&SSEASON=2&REPORT_ID=C>.
- *TWSE Daily Trading Summary*, Taiwan Stock Exchange, data 1150914 / 2026-09-14; 4169 closing price 142.50: <https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL>.
- *Latest Fund NAV*, Allianz Global Investors Taiwan, NAV 2026-09-11; A cumulative TWD 20.74: <https://ifund.allianzgi.com.tw/WebNav.aspx>.
- *7928 Quote*, Yahoo Taiwan, 2026-09-14 14:58; average 375.8, last 376.0 (secondary; retrieved search text): <https://tw.stock.yahoo.com/quote/7928.TWO>.
- *6920 Quote*, Yahoo Taiwan, 2026-09-14 14:44; average 97.8, last 98.1 (secondary): <https://tw.stock.yahoo.com/quote/6920.TW>.
- *Eastspring High Tech NAV*, KGI Life / MoneyDJ, 2026-09-14 668.43 (secondary): <https://kgilife.moneydj.com/w/wr/wr02.djhtm?a=ACCP03-TF45>.
- *Nomura High Tech Cumulative TWD NAV*, MoneyDJ, 2026-09-14 121.2000 (secondary): <https://www.moneydj.com/FUNDDJ/YA/YP010000_ACKH19.DJHTM>.
- *Fubon New Taiwan Merchant A NAV*, Taipei Fubon Bank fund-data service, 2026-09-14 370.01 (secondary): <https://fund.taipeifubon.com.tw/w/wr/wr02_ACJS13-4405.djhtm>.
