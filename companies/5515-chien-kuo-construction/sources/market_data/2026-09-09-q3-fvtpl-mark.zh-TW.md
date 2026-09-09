# 2026-09-09 Q3-to-date FVTPL 評價

<!-- 衍生繁體中文閱讀版；英文原檔 `2026-09-09-q3-fvtpl-mark.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

## 範圍與截止時間

- **目的：** 估算建國 2026-06-30 FVTPL 組合至 2026-09-09 的價值變動。
- **幣別：** 除另有說明外均為 TWD million。
- **持倉假設：** 2026-06-30 單位數維持不變。此點未經證實，是估算的最大限制。
- **市場截止：** 興櫃股票採 2026-09-09 14:00:05 均價；上市股票採 2026-09-08 收盤價；基金採 2026-09-04 至 2026-09-08 間最新可得淨值。
- **會計範圍：** 僅估 FVTPL；FVOCI 與攤銷後成本資產不納入 EPS 估算。

## 可直接重估部位

| 部位 | 2026-06-30 帳面價值 | 目前估計價值 | 稅前變動 | 目前價格輸入 |
| --- | ---: | ---: | ---: | --- |
| 合聖科技（`7928`）323 thousand 股 | 165.933 | 124.746 | (41.187) | 櫃買均價 TWD 386.21 |
| 恆勁科技（`6920`）651 thousand 股 | 64.992 | 63.577 | (1.415) | 櫃買均價 TWD 97.66 |
| 泰宗（`4169`）538 thousand 股 | 117.015 | 80.162 | (36.853) | 證交所收盤 TWD 149.00 |
| 安聯四季雙收入息 2,888 thousand 單位 | 61.778 | 60.417 | (1.361) | 淨值 TWD 20.92 |
| 瀚亞高科技 102 thousand 單位 | 67.035 | 69.510 | 2.475 | 淨值 TWD 681.47 |
| 野村高科技 659 thousand 單位 | 79.390 | 82.922 | 3.532 | 淨值 TWD 125.83 |
| 富邦新台商 149 thousand 單位 | 60.870 | 56.452 | (4.418) | 淨值 TWD 378.87 |
| **合計** | **617.013** | **537.785** | **(79.228)** | |

具名台灣貨幣市場基金合計 TWD 1,662.046 million，模型假設 Q3-to-date 報酬率 0.30%，增加 TWD 4.986 million。這是代理假設，不是逐檔評價。

## 情境估算

扣除可直接重估部位與具名貨幣市場基金後，仍有 TWD 3,172.702 million 無法定價，包括境外基金、Brain Navi、私募股權、未上市股票及低於 TWD 50 million 揭露門檻的部位。對此部分分別採用負 3%、零及正 3% 變動：

| 情境 | 未定價部位假設 | 估計 FVTPL 變動 | 目前估計 FVTPL 價值 | 稅後 EPS 影響 |
| --- | ---: | ---: | ---: | ---: |
| 保守 | (3.0%) | (169) | 5,282 | (0.67) |
| 基準 | 0.0% | (74) | 5,378 | (0.29) |
| 樂觀 | +3.0% | +21 | 5,473 | +0.08 |

EPS 採簡化稅率 20% 與 201.6 million 股計算。估算衡量市場變動而非現金流，未納入 2026-06-30 後的買賣、配息、逐檔匯率、評價模型變更或持倉調整。這是 Q3-to-date 指標，不是季底預測。

## 來源

- *2026 Q2 Consolidated Financial Statements*, approved 2026-08-12, pp. 14, 31–32 and 45–47, <https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=5515&year=115&seamon=2&mtype=A&dtype=AI1>, accessed 2026-09-09.
- *TWSE Daily Trading Summary*, Taiwan Stock Exchange OpenAPI, data date 2026-09-08, <https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL>, accessed 2026-09-09.
- *Emerging Stock Latest Statistics*, Taipei Exchange OpenAPI, timestamp 2026-09-09 14:00:05, <https://www.tpex.org.tw/openapi/v1/tpex_esb_latest_statistics>, accessed 2026-09-09.
- *Fund NAV*, Eastspring Investments, NAV date 2026-09-08, <https://www.eastspring.com.tw/our-funds/nav>, accessed 2026-09-09.
- *Fund NAV*, Allianz Global Investors Taiwan, NAV date 2026-09-04, <https://ifund.allianzgi.com.tw/WebNav.aspx>, accessed 2026-09-09.
- *Nomura High Tech Fund NAV*, MoneyLink, NAV date 2026-09-08, <https://tweb.money-link.com.tw/Fund/FundNetTrend.aspx?FundCode=0P00006AHA>, accessed 2026-09-09.
- *Fubon New Taiwan Merchant Fund NAV*, SinoPac fund data service, NAV date 2026-09-08, <https://mmafund.sinopac.com/w/wr/wr02.djhtm?a=ACJS13-Z10>, accessed 2026-09-09.
