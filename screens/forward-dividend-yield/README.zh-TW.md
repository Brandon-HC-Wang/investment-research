# 前瞻現金殖利率搜尋

## 目的與狀態

這個 `testing` screen 搜尋標準化 2026 年盈餘與可分配現金可能支持 2027 年配發現金股利，且前瞻殖利率至少 7% 的上市與上櫃普通股。它連結至 [`forward-dividend-income`](../../strategies/forward-dividend-income/README.md) strategy。

目前尚未完成正式 run。既有的 [2026-09-09 FVTPL 高殖利率搜尋](../../research-log/industries/FVTPLHighYieldScreen.md) 是先前探索證據，不是依本 definition 產生的 run。

Phase 2 離線 executor 已完成。它評估明確備妥的 CSV，且只有移除 `--dry-run` 才會保存 run。官方市場探索與執行彼此分離；財報擷取與分析標準化仍未實作。

Phase 3 market-discovery collector 已實作於 [`scripts/collect_market_discovery.py`](../../scripts/collect_market_discovery.py)。它可以在明確執行時擷取四份 TWSE 與 TPEx 官方資料集，並保存至 [`source-snapshots/`](source-snapshots/README.md)。這不代表分析輸入已完成；標準化 EPS、前瞻 DPS、自由現金流覆蓋與產業特定調整仍須有經審查的公司證據。

## 計算邊界

`前瞻現金殖利率 = 預估 2027 年現金 DPS / 搜尋日股價`

`必要 DPS = 搜尋日股價 × 7%`

`標準化 EPS 覆蓋 = 標準化歸屬母公司 2026 年稀釋 EPS / 必要 DPS`

估計 DPS 必須採用保守可支持配息率與母公司可分配現金能力兩者中的較低者。交易所顯示殖利率僅作為探索輸入，因為它反映歷史配發，且可能包含非經常性或非盈餘支應項目。

## 候選與警示邏輯

必要條件為基本情境前瞻殖利率至少 7%、標準化 EPS 覆蓋至少 1.25 倍，以及下行情境前瞻殖利率至少 5%。排序考慮下行情境殖利率、覆蓋、自由現金流股利覆蓋及配息穩定性。

資產處分、FVTPL 與匯兌利得、稅務迴轉、資本公積配發、減資、槓桿、稀釋、低流動性及缺少母公司現金證據皆為警示旗標。金融、營建、房地產及景氣循環公司需要產業特定標準化，不得機械式年化。

## 離線輸入與執行契約

每一列 CSV 必須提供身分欄位（`market`、`ticker`、`company`）、一致的 `price_date` 與 `financial_period`、股價、標準化基本與下行情境 EPS、預估基本與下行情境 DPS、自由現金流股利覆蓋、配息穩定年數、警示旗標、來源階級、證據引用及來源 URL。數值假設必須先完成人工分析審查；executor 不會自行從財報推導標準化 EPS 或可分配現金。

使用以下命令執行不持久化驗證：

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input <reviewed-input.csv> \
  --as-of <YYYY-MM-DD> \
  --run-id <unique-run-id> \
  --dry-run --json
```

持久化 run 僅能附加，並記錄 definition hash、實際門檻、來源 URLs、覆蓋率、列錯誤、結果 checksum 與雙語摘要。重複或不安全的 run ID 會被拒絕。只有完整的 `success` run 會更新刷新 state；所有保留列仍只是需要人工審查的研究候選。

## 刷新政策

- 每七天進行一次輕量股價輸入檢查。
- 官方月營收公布後重新評估盈餘輸入。
- 季報或年報公布後必須完整刷新。
- 股利決議或重大資本事件後必須刷新。
- Definition 改版後立即將先前 run 標示為到期。

本機 session 啟動檢查僅提醒且永不連線。失敗或不完整 run 不得推進最後成功執行時間。

## 來源階級

主要來源為 TWSE、TPEx、MOPS、官方財報及公司揭露。次級結構化資料只能在記錄缺口、明確標示並盡可能核對時補缺。每個 run 都必須記錄來源日期、覆蓋率、備援使用、錯誤及實際 definition version。
