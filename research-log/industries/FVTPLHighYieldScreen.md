# FVTPL High-Dividend-Yield Screen

## 2026-09-09 — TWSE and TPEx screen

### Question and scope

- **Question:** Which currently listed TWSE and TPEx common stocks have an exchange-reported dividend yield above 5% and a positive FVTPL financial-asset balance?
- **Price and yield date:** 2026-09-08, the latest common date returned by the TWSE and TPEx APIs when accessed on 2026-09-09.
- **Financial position date:** 2026-06-30 consolidated balance sheet (2026Q2).
- **Universe:** TWSE and TPEx common-stock records returned by the two exchange yield APIs. Emerging stocks and ETFs are excluded.
- **Thresholds:** Exchange-reported dividend yield strictly above 5.00%; FVTPL financial assets strictly above TWD 0.
- **Full matching list:** [`data/2026-09-09-fvtpl-high-yield-screen.csv`](data/2026-09-09-fvtpl-high-yield-screen.csv).

### Result

**Fact:** The yield filter retained 434 stocks: 240 TWSE and 194 TPEx. Of these, 264 had a positive 2026Q2 FVTPL balance: 165 TWSE and 99 TPEx. The other 170 passed the yield filter but had no positive FVTPL balance in the retrieved 2026Q2 facts.

**Fact:** FVTPL exposure was at least 1% of total assets for 160 matches, at least 5% for 71, and at least 10% for 35.

**Interpretation:** The 264-name result is a broad accounting-presence list. The 35 names below are a more useful first-pass exposure list, but even this ratio does not measure EPS sensitivity because FVTPL may contain money-market funds, bonds, listed shares, unlisted shares, private equity, or derivatives with very different volatility.

| Market | Ticker | Company | Yield (%) | FVTPL (TWD mn) | FVTPL / assets (%) | Evidence |
|---|---:|---|---:|---:|---:|---|
| TPEx | 4123 | 晟德 | 7.39 | 14,519.4 | 60.58 | FinMind secondary extract |
| TWSE | 2820 | 華票 | 5.29 | 160,980.9 | 58.96 | TWSE OpenAPI |
| TWSE | 3356 | 奇偶 | 5.87 | 1,899.1 | 54.93 | FinMind secondary extract |
| TWSE | 3257 | 虹冠電 | 5.86 | 1,241.9 | 52.51 | FinMind secondary extract |
| TWSE | 5515 | 建國 | 6.33 | 5,451.8 | 42.51 | FinMind extract; cross-checked to retained 2026Q2 filing |
| TPEx | 4167 | 松瑞藥 | 7.85 | 1,742.3 | 33.74 | FinMind secondary extract |
| TPEx | 4754 | 國碳科 | 5.97 | 324.4 | 30.64 | FinMind secondary extract |
| TWSE | 3014 | 聯陽 | 6.54 | 3,364.6 | 30.45 | FinMind secondary extract |
| TWSE | 1608 | 華榮 | 5.46 | 6,080.8 | 30.39 | MOPS Inline XBRL |
| TPEx | 8435 | 鉅邁 | 5.99 | 414.2 | 29.43 | FinMind secondary extract |
| TPEx | 4735 | 豪展 | 5.46 | 448.7 | 24.87 | MOPS Inline XBRL |
| TPEx | 4303 | 信立 | 14.03 | 1,193.3 | 24.38 | FinMind secondary extract |
| TPEx | 6016 | 康和證 | 6.07 | 25,508.4 | 23.90 | FinMind secondary extract |
| TWSE | 4441 | 振大環球 | 6.17 | 2,338.8 | 23.62 | FinMind secondary extract |
| TWSE | 6005 | 群益證 | 5.24 | 115,719.8 | 21.99 | MOPS Inline XBRL |
| TPEx | 4933 | 友輝 | 5.41 | 1,116.6 | 21.55 | MOPS Inline XBRL |
| TPEx | 7819 | 精誠金融 | 5.04 | 165.2 | 21.35 | FinMind secondary extract |
| TWSE | 9927 | 泰銘 | 7.19 | 1,389.7 | 20.60 | FinMind secondary extract |
| TWSE | 9905 | 大華 | 5.14 | 2,692.3 | 20.51 | MOPS Inline XBRL |
| TPEx | 5212 | 凌網 | 9.09 | 229.6 | 19.07 | FinMind secondary extract |
| TWSE | 2031 | 新光鋼 | 5.57 | 5,865.8 | 18.81 | MOPS Inline XBRL |
| TPEx | 5878 | 台名 | 6.29 | 115.4 | 15.66 | FinMind secondary extract |
| TPEx | 6026 | 福邦證 | 8.86 | 2,580.1 | 14.84 | FinMind secondary extract |
| TWSE | 2707 | 晶華 | 6.04 | 1,301.8 | 13.52 | FinMind secondary extract |
| TPEx | 5520 | 力泰 | 8.51 | 623.1 | 13.12 | FinMind secondary extract |
| TWSE | 2458 | 義隆 | 5.42 | 2,098.1 | 12.46 | MOPS Inline XBRL |
| TPEx | 4702 | 中美實 | 5.33 | 202.6 | 12.40 | MOPS Inline XBRL |
| TWSE | 5203 | 訊連 | 6.52 | 744.8 | 12.24 | FinMind secondary extract |
| TWSE | 6951 | 青新-創 | 7.46 | 204.2 | 11.94 | FinMind secondary extract |
| TWSE | 2852 | 第一保 | 5.92 | 2,269.2 | 11.30 | TWSE OpenAPI |
| TPEx | 5312 | 寶島科 | 7.09 | 1,100.2 | 11.03 | FinMind secondary extract |
| TPEx | 5315 | 光聯 | 8.70 | 250.3 | 10.93 | FinMind secondary extract |
| TWSE | 1423 | 利華 | 10.11 | 414.9 | 10.40 | FinMind secondary extract |
| TWSE | 1102 | 亞泥 | 6.53 | 34,603.4 | 10.26 | MOPS Inline XBRL |
| TPEx | 6577 | 勁豐 | 6.23 | 261.2 | 10.02 | FinMind secondary extract |

### Yield-definition limitation

The result uses the exchanges' displayed dividend-yield fields, not a custom forward cash-yield forecast. TWSE defines the measure as recent per-share dividends divided by closing price and may include cash paid from earnings, legal reserve or capital reserve, plus stock dividends. TPEx documentation says its displayed yield uses the most recently completed ex-dividend distribution. Therefore, “2026 yield” here means the yield displayed on 2026-09-08, not necessarily cash dividends attributable only to 2026 earnings. Extraordinary distributions, stock dividends, capital reductions, and changed par values can create extreme readings.

### Evidence and data lineage

1. **Dividend-yield universe — primary:** TWSE, “上市個股日本益比、殖利率及股價淨值比,” data date 2026-09-08, accessed 2026-09-09, [`BWIBBU_ALL`](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL). TPEx, “上櫃股票個股本益比、殖利率、股價淨值比,” data date 2026-09-08, accessed 2026-09-09, [`tpex_mainboard_peratio_analysis`](https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis).
2. **Yield methodology — primary:** TWSE, “個股日本益比、殖利率及股價淨值比,” accessed 2026-09-09, [calculation notes](https://accessibility.twse.com.tw/zh/trading/historical/bwibbu.html). TPEx, “新版收市後交易資訊格式說明 V1.33,” published 2025-11-27, accessed 2026-09-09, [PDF](https://www.tpex.org.tw/storage/regular_system/%E6%96%B0%E7%89%88%E6%94%B6%E5%B8%82%E5%BE%8C%E4%BA%A4%E6%98%93%E8%B3%87%E8%A8%8A%E6%A0%BC%E5%BC%8F%E8%AA%AA%E6%98%8E%28V1.33%E7%89%88%29.pdf?t=20251127), p. 31.
3. **FVTPL and total assets — primary where accessible:** MOPS, 2026Q2 consolidated Inline XBRL, accessed 2026-09-09, using the standard `AsOf20260630` facts `CurrentFinancialAssetsAtFairValueThroughProfitOrLoss`, `NoncurrentFinancialAssetsAtFairValueThroughProfitOrLoss`, `FinancialAssetsAtFairValueThroughProfitOrLoss`, and `Assets`. Example: [5515 filing](https://mopsov.twse.com.tw/server-java/t164sb01?step=1&CO_ID=5515&SYEAR=2026&SSEASON=2&REPORT_ID=C). TWSE financial-industry balance-sheet OpenAPI was also used when it exposed an explicit FVTPL field.
4. **FVTPL and total assets — secondary gap fill:** FinMind, `TaiwanStockBalanceSheet`, 2026-06-30, accessed 2026-09-09, [API documentation](https://finmind.github.io/en/quickstart/). Its 5515 values reconciled exactly to the retained official 2026Q2 filing at TWD 5,451.761 million. Of the 264 matches, 100 were directly supported by MOPS/TWSE data and 164 used the FinMind extract because MOPS throttled the batch query.

### What this screen does not establish

- A high displayed yield is not evidence that the dividend is recurring or covered by normalized earnings and cash flow.
- A positive FVTPL balance does not mean the company owns listed equities; the instruments must be read from the financial-report notes.
- FVTPL balance divided by assets is not the same as EPS sensitivity. A follow-up must identify instrument composition, leverage, tax, non-controlling interests, and the parent company's distributable cash.
- Financial companies should not be compared directly with industrial companies because trading and investment assets can be part of their normal operating model.

### Next verification

For any candidate promoted to company research, verify the 2026Q2 filing directly, separate money-market and fixed-income holdings from equity and private-market exposures, bridge 2026 FVTPL gains or losses to attributable EPS, and test dividend coverage using normalized earnings and parent-company cash.
