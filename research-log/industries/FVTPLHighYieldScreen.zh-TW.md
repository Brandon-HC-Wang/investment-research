# FVTPL 高殖利率篩選

<!-- 衍生繁體中文閱讀版；英文原檔 `FVTPLHighYieldScreen.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

## 2026-09-09 — 上市與上櫃篩選

### 問題與範圍

- **問題：** 目前上市、上櫃普通股中，哪些股票的交易所顯示殖利率高於 5%，且帳上有正數 FVTPL 金融資產？
- **價格與殖利率日期：** 2026-09-08，為 2026-09-09 存取 TWSE 與 TPEx API 時兩者共同的最新日期。
- **財務狀況日期：** 2026-06-30 合併資產負債表（2026Q2）。
- **母體：** TWSE 與 TPEx 殖利率 API 回傳的上市、上櫃普通股；不含興櫃與 ETF。
- **門檻：** 交易所顯示殖利率嚴格高於 5.00%；FVTPL 金融資產嚴格大於 TWD 0。
- **完整符合清單：** [`data/2026-09-09-fvtpl-high-yield-screen.csv`](data/2026-09-09-fvtpl-high-yield-screen.csv)。

### 結果

**事實：** 殖利率篩選留下 434 檔：上市 240 檔、上櫃 194 檔。其中 264 檔的 2026Q2 FVTPL 期末餘額為正數：上市 165 檔、上櫃 99 檔。其餘 170 檔通過殖利率條件，但在取得的 2026Q2 facts 中沒有正數 FVTPL 餘額。

**事實：** 160 檔的 FVTPL 至少占總資產 1%，71 檔至少占 5%，35 檔至少占 10%。

**解讀：** 264 檔是廣義的「會計科目存在」清單。下列 35 檔是較有用的第一層曝險清單；但即使如此，該比率也不等於 EPS 敏感度，因為 FVTPL 可能包含波動度差異很大的貨幣市場基金、債券、上市股票、未上市股票、私募股權或衍生性商品。

| 市場 | 代號 | 公司 | 殖利率（%） | FVTPL（TWD mn） | FVTPL／資產（%） | 證據 |
|---|---:|---|---:|---:|---:|---|
| TPEx | 4123 | 晟德 | 7.39 | 14,519.4 | 60.58 | FinMind 次級資料 |
| TWSE | 2820 | 華票 | 5.29 | 160,980.9 | 58.96 | TWSE OpenAPI |
| TWSE | 3356 | 奇偶 | 5.87 | 1,899.1 | 54.93 | FinMind 次級資料 |
| TWSE | 3257 | 虹冠電 | 5.86 | 1,241.9 | 52.51 | FinMind 次級資料 |
| TWSE | 5515 | 建國 | 6.33 | 5,451.8 | 42.51 | FinMind；已與留存 2026Q2 財報交叉核對 |
| TPEx | 4167 | 松瑞藥 | 7.85 | 1,742.3 | 33.74 | FinMind 次級資料 |
| TPEx | 4754 | 國碳科 | 5.97 | 324.4 | 30.64 | FinMind 次級資料 |
| TWSE | 3014 | 聯陽 | 6.54 | 3,364.6 | 30.45 | FinMind 次級資料 |
| TWSE | 1608 | 華榮 | 5.46 | 6,080.8 | 30.39 | MOPS Inline XBRL |
| TPEx | 8435 | 鉅邁 | 5.99 | 414.2 | 29.43 | FinMind 次級資料 |
| TPEx | 4735 | 豪展 | 5.46 | 448.7 | 24.87 | MOPS Inline XBRL |
| TPEx | 4303 | 信立 | 14.03 | 1,193.3 | 24.38 | FinMind 次級資料 |
| TPEx | 6016 | 康和證 | 6.07 | 25,508.4 | 23.90 | FinMind 次級資料 |
| TWSE | 4441 | 振大環球 | 6.17 | 2,338.8 | 23.62 | FinMind 次級資料 |
| TWSE | 6005 | 群益證 | 5.24 | 115,719.8 | 21.99 | MOPS Inline XBRL |
| TPEx | 4933 | 友輝 | 5.41 | 1,116.6 | 21.55 | MOPS Inline XBRL |
| TPEx | 7819 | 精誠金融 | 5.04 | 165.2 | 21.35 | FinMind 次級資料 |
| TWSE | 9927 | 泰銘 | 7.19 | 1,389.7 | 20.60 | FinMind 次級資料 |
| TWSE | 9905 | 大華 | 5.14 | 2,692.3 | 20.51 | MOPS Inline XBRL |
| TPEx | 5212 | 凌網 | 9.09 | 229.6 | 19.07 | FinMind 次級資料 |
| TWSE | 2031 | 新光鋼 | 5.57 | 5,865.8 | 18.81 | MOPS Inline XBRL |
| TPEx | 5878 | 台名 | 6.29 | 115.4 | 15.66 | FinMind 次級資料 |
| TPEx | 6026 | 福邦證 | 8.86 | 2,580.1 | 14.84 | FinMind 次級資料 |
| TWSE | 2707 | 晶華 | 6.04 | 1,301.8 | 13.52 | FinMind 次級資料 |
| TPEx | 5520 | 力泰 | 8.51 | 623.1 | 13.12 | FinMind 次級資料 |
| TWSE | 2458 | 義隆 | 5.42 | 2,098.1 | 12.46 | MOPS Inline XBRL |
| TPEx | 4702 | 中美實 | 5.33 | 202.6 | 12.40 | MOPS Inline XBRL |
| TWSE | 5203 | 訊連 | 6.52 | 744.8 | 12.24 | FinMind 次級資料 |
| TWSE | 6951 | 青新-創 | 7.46 | 204.2 | 11.94 | FinMind 次級資料 |
| TWSE | 2852 | 第一保 | 5.92 | 2,269.2 | 11.30 | TWSE OpenAPI |
| TPEx | 5312 | 寶島科 | 7.09 | 1,100.2 | 11.03 | FinMind 次級資料 |
| TPEx | 5315 | 光聯 | 8.70 | 250.3 | 10.93 | FinMind 次級資料 |
| TWSE | 1423 | 利華 | 10.11 | 414.9 | 10.40 | FinMind 次級資料 |
| TWSE | 1102 | 亞泥 | 6.53 | 34,603.4 | 10.26 | MOPS Inline XBRL |
| TPEx | 6577 | 勁豐 | 6.23 | 261.2 | 10.02 | FinMind 次級資料 |

### 殖利率口徑限制

本結果採交易所顯示的殖利率欄位，不是自行建立的預估現金殖利率。TWSE 的定義為近期每股股利除以收盤價，且可能包含盈餘、法定盈餘公積或資本公積發放的現金，以及股票股利。TPEx 文件則說明其顯示殖利率採最近一次完成除權息的股利計算。因此，這裡的「2026 殖利率」是 2026-09-08 當日顯示值，不一定只代表來自 2026 年盈餘的現金股利。特殊分配、股票股利、減資與面額變更可能造成極端數值。

### 證據與資料血緣

1. **殖利率母體—主要來源：** TWSE，「上市個股日本益比、殖利率及股價淨值比」，資料日 2026-09-08，存取日 2026-09-09，[`BWIBBU_ALL`](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL)。TPEx，「上櫃股票個股本益比、殖利率、股價淨值比」，資料日 2026-09-08，存取日 2026-09-09，[`tpex_mainboard_peratio_analysis`](https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis)。
2. **殖利率方法—主要來源：** TWSE，「個股日本益比、殖利率及股價淨值比」，存取日 2026-09-09，[計算說明](https://accessibility.twse.com.tw/zh/trading/historical/bwibbu.html)。TPEx，「新版收市後交易資訊格式說明 V1.33」，發布日 2025-11-27，存取日 2026-09-09，[PDF](https://www.tpex.org.tw/storage/regular_system/%E6%96%B0%E7%89%88%E6%94%B6%E5%B8%82%E5%BE%8C%E4%BA%A4%E6%98%93%E8%B3%87%E8%A8%8A%E6%A0%BC%E5%BC%8F%E8%AA%AA%E6%98%8E%28V1.33%E7%89%88%29.pdf?t=20251127)，第 31 頁。
3. **FVTPL 與總資產—可取得時採主要來源：** MOPS，2026Q2 合併 Inline XBRL，存取日 2026-09-09，擷取 `AsOf20260630` 的標準 facts：`CurrentFinancialAssetsAtFairValueThroughProfitOrLoss`、`NoncurrentFinancialAssetsAtFairValueThroughProfitOrLoss`、`FinancialAssetsAtFairValueThroughProfitOrLoss` 與 `Assets`。範例：[5515 財報](https://mopsov.twse.com.tw/server-java/t164sb01?step=1&CO_ID=5515&SYEAR=2026&SSEASON=2&REPORT_ID=C)。另在 TWSE 金融業資產負債表 OpenAPI 明確提供 FVTPL 欄位時使用該資料。
4. **FVTPL 與總資產—次級來源補缺：** FinMind，`TaiwanStockBalanceSheet`，資料日 2026-06-30，存取日 2026-09-09，[API 文件](https://finmind.github.io/en/quickstart/)。其 5515 數字與已留存的官方 2026Q2 財報完全勾稽，均為 TWD 5,451.761 million。264 檔符合者中，100 檔由 MOPS／TWSE 直接支持，164 檔因 MOPS 對批次查詢限流而採 FinMind 擷取值。

### 本篩選無法證明的事項

- 高顯示殖利率不代表股息可重複，也不代表標準化盈餘與現金流足以支應。
- FVTPL 餘額為正不代表公司持有上市股票；必須從財報附註辨識金融工具內容。
- FVTPL／總資產不等於 EPS 敏感度；後續仍須辨識工具組合、槓桿、稅率、非控制權益與母公司可分配現金。
- 金融公司與工業公司不應直接比較，因為交易與投資資產可能是金融公司的正常營運模型之一。

### 下一步驗證

任何要升級為公司研究的候選人，都應直接核對 2026Q2 財報，將貨幣市場與固定收益工具和股票、私募市場曝險分開，建立 2026 年 FVTPL 損益到歸屬 EPS 的橋接，並以標準化盈餘與母公司現金檢驗股息覆蓋。
