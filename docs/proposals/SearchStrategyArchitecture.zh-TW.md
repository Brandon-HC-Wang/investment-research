# 搜尋策略架構提案

> 狀態：第一階段已於 2026-09-10 實作，Phase 2 離線執行生命週期與 Phase 3 官方市場探索 collector 已於 2026-09-14 完成。現已有 definitions、validation、read-only 啟動提醒、不可變 source snapshots 及原子式 append-only run persistence；財報擷取、分析標準化與自動刷新仍未實作，也未獲授權。

## 目標

新增可長期維護的工作流程，用來定義可重複使用的研究策略、執行可重現的市場搜尋、保存點時結果，並告知人類或 AI agent 哪些搜尋已到刷新時間。搜尋只產生研究候選，不產生買進、賣出或持有指示。

## 語意邊界

| 物件 | 回答的問題 | Canonical 內容 |
|---|---|---|
| Strategy | 為什麼這個訊號可能找得到研究機會？ | 經濟機制、驗證狀態、支持與反對證據、否證條件、時間範圍、關聯 screens |
| Screen | 如何計算候選母體？ | 母體、欄位、條件、排序、來源階級、刷新政策、輸出契約 |
| Run | 搜尋在特定時間知道什麼、找到什麼？ | 不可變 manifest、定義版本、來源與資料日期、覆蓋率、失敗、結果表、摘要 |
| Refresh state | 現在有哪些項目需要處理？ | 衍生的最後成功執行、最後資料日、下次到期日、過期原因、最新 run 指標 |

一個 strategy 可以引用多個 screens，一個 screen 也可以支援多個 strategies。公司研究仍以 `companies/` 為 canonical；搜尋結果不得默默建立或修改公司 thesis。`watchlist/` 維持研究優先順序佇列，`research-log/` 只記錄跨 run 的重大結論，不記錄每一次執行。

## 建議目錄契約

```text
strategies/
  registry.yaml
  forward-dividend-income/
    strategy.yaml
    README.md
    README.zh-TW.md

screens/
  registry.yaml
  forward-dividend-yield/
    screen.yaml
    README.md
    README.zh-TW.md
    state.yaml
    source-snapshots/
      README.md
      <snapshot-id>/
        manifest.yaml
        market-discovery.csv
        <official-source>.json
        summary.md
        summary.zh-TW.md
    runs/
      2026-09-10T090000+08-00/
        manifest.yaml
        results.csv
        summary.md
        summary.zh-TW.md

schemas/
  strategy.schema.json
  screen.schema.json
  screen-run.schema.json
  screen-state.schema.json
  market-discovery-snapshot.schema.json

templates/
  strategy/
  screen/

scripts/
  check_screen_refresh.py
  collect_market_discovery.py
  run_screen.py
  validate_repository.py
```

`strategy.yaml` 與 `screen.yaml` 是 canonical machine-readable definitions，配對的 Markdown 說明推理與限制。Run 目錄僅能附加，不得用後見之明修改。`state.yaml` 可變但必須可由 definition 與 run manifests 重建，不得保存唯一的研究結論。

## Strategy 定義

必要欄位應包括：

- `schema_version`、穩定 `id`、名稱、狀態與驗證階段；
- claim 與因果機制；
- 支持與反對證據；
- 確認與否證訊號；
- 預期時間範圍及目前信心；
- 關聯 screen IDs；
- 最低點時驗證要求；
- 建立、審查及 supersession 歷史。

建議驗證階段為 `idea`、`testing`、`validated`、`monitoring`、`rejected` 及 `archived`。狀態歷史只可附加。`validated` 代表歷史點時證據支持所述機制，不代表策略必然有效，也不構成推薦。

## Screen 定義

必要欄位應包括：

- `schema_version`、穩定 `id`、標題、啟用狀態及定義版本；
- 母體與明確排除條件；
- 必要輸入欄位、單位、會計期間及允許延遲；
- 有來源階級的主要與備援資料來源；
- 硬性條件、排序因子、警示旗標及情境規則；
- 輸出欄位與證據要求；
- 刷新政策與過期政策；
- 覆蓋率最低門檻與失敗行為；
- 關聯 strategies、models 與相關 research logs。

條件應區分 `required`、`ranking` 與 `warning`。來源失敗、被限流、全市場覆蓋不完整或輸入過期，不得解讀為沒有搜尋結果。

## Run manifest 與結果

每次執行都應保存：

- run ID、開始與完成時間、狀態及工具版本；
- screen definition 版本或內容 hash；
- 股價日、財務期間、來源存取日及來源 URL；
- 候選母體數、已評估數、保留數及覆蓋率；
- 失敗與備援來源數量及錯誤分類；
- 實際使用的參數與門檻；
- 可行時保存結果 artifacts 的路徑與 checksum；
- 信心、限制，以及是否需要人工審查。

`results.csv` 每一列代表一個候選，並包含重建通過原因所需的事實、估計、情境輸出、警示旗標、來源階級及證據引用。之後的修正必須建立新 run 或 dated correction record，不得覆寫舊結果。

## 刷新政策

刷新判斷需要兩個獨立時鐘：

1. **執行新鮮度：** 距離上次成功完成搜尋多久。
2. **輸入新鮮度：** 是否已有較新的股價、月度揭露、季度財報、股利決議或其他必要來源。

每個 screen 應定義：

- 例行頻率，例如每日、每週、每月、每季或手動；
- `stale_after` 容忍值；
- 預定觸發，例如月營收或財報預計公布期間；
- 事件觸發，例如股利決議、新財報、重大價格變動或定義改版；
- 在基礎資料沒有變化時避免重複執行的 cool-down 規則；
- 刷新是 `remind_only`，或可在使用者明確授權後執行。

到期演算法應回傳 `fresh`、`due`、`overdue`、`blocked` 或 `disabled`，並附上 machine-readable reason codes。執行失敗不得推進 `last_successful_run`。

## Agent session 啟動

實作後，`AGENTS.md` 與 `.ai/context.md` 應要求執行 read-only 啟動檢查：

```bash
python3 scripts/check_screen_refresh.py --due-only
```

命令只讀取本機 definitions 與 state，不連線。它應輸出精簡的人類可讀內容，並支援供 agents 使用的 `--json`。新 session 啟動時只提醒哪些 screens 已到期及原因；不得自動刷新資料、修改檔案或連線外部服務。

之後可以由明確 refresh 命令執行一個指定 screen。它應原子式建立新 run，只在成功後更新衍生 state；若診斷有用，則保留 failed manifest。

## Forward-dividend-yield 首個實作

第一個 screen 可以是 `forward-dividend-yield`，並連結到 `testing` 狀態的 `forward-dividend-income` strategy。初期刷新政策建議如下：

- 股價與顯示殖利率輸入每週刷新；
- 官方月營收公布後每月刷新；
- 每次季度財報後強制刷新；
- 董事會股利決議或重大資本事件後強制刷新；
- 定義或標準化 EPS 方法改變時立即到期。

搜尋應輸出基本及下行情境前瞻殖利率、必要 DPS 與配息率、標準化 EPS 覆蓋、自由現金流覆蓋、一次性盈餘警示、來源階級及產業特定審查狀態。營建、金融及景氣循環公司需要不同的模型規則。

## 驗證與安全門

在接受可執行自動化之前：

- JSON Schemas 與 repository validation 必須涵蓋 definitions、state 及 run manifests；
- fixture-based tests 必須涵蓋到期計算、失敗 run、不完整資料、時區及定義改版；
- 網路擷取與分析轉換必須可分離；
- 必須強制主要來源優先及備援來源標記；
- runs 必須依 run ID 保持 idempotent，並依路徑僅附加；
- 搜尋不得自動新增公司 coverage、改變 thesis 或建立推薦；
- 啟動檢查必須維持 read-only 且快速。

## 建議實作順序

1. 核准術語、目錄名稱、生命週期狀態及僅提醒的啟動邊界。
2. 新增 schemas、templates、registry 契約與 validation，但不實作網路擷取。
3. 登錄 forward-dividend strategy 與 screen，再把目前方法移入 definitions。
4. 新增 read-only refresh checker 與 session 啟動指示。
5. 實作一個明確、可重現的 screen runner；只有在官方來源輸入完成審查後，才保存第一次點時 run。
6. 將估計與後續股利決議比較；在達到既定歷史驗證門檻前，strategy 保持 `testing`。

## 第一階段已實作決策

- 對外總稱使用「搜尋策略」，內部契約保留 `strategy` 與 `screen` 的區分。
- `state.yaml` 作為可重建 cache 納入版本控制，不得保存唯一結論。
- Session 啟動只執行本機 read-only 提醒，不查詢官方來源，也不執行刷新。
- 驗證長度依 strategy 類型決定。第一個年度股利 strategy 至少需要三個年度 cohorts；季度 strategies 通常至少需要 8–12 個點時季度。實際成功指標必須在結果測試開始前先聲明。

## Phase 2 已實作決策

- `forward-dividend-yield` 現可在不連網的情況下評估經審查的 flat CSV。擷取與分析標準化仍是分離的責任。
- Dry run 只驗證與評估，不修改 repository。持久化 run 會將 manifest、results 與雙語摘要原子式寫入新的 run ID；重複與不安全 ID 會被拒絕。
- 只有完整的 `success` run 能推進可重建刷新 state。`partial` run 可保留供診斷，但維持先前 state 不變。
- Run validation 會檢查 screen definition version、artifact paths、結果欄位與筆數、完整性不變條件及 SHA-256 integrity。
- 年度 strategy 預先聲明的測試門檻為三個年度 cohorts、至少 100 個 company-year observations、至少 70% forecast-interval coverage、DPS 絕對誤差中位數不高於 15%、候選 precision 至少 60%，且 precision 至少比顯示殖利率 baseline 高 10 個百分點。這些是待驗證假說，不是有效性證據。
- Repository 目前只有 synthetic executor fixtures，尚未建立官方點時 run，因此 screen 維持 `due`，reason codes 為 `never_run` 與 `definition_changed`。

## Phase 3 已實作決策

- 現可明確擷取 TWSE `BWIBBU_ALL`、`STOCK_DAY_ALL`，以及 TPEx `tpex_mainboard_peratio_analysis`、`tpex_mainboard_daily_close_quotes` 官方資料，也可從本機 JSON fixtures replay；live retrieval 強制 TLS verification。
- Collector 會將各交易所顯示殖利率母體與收盤價連結、轉換民國日期、保留缺價診斷，並以 SHA-256 保存完整官方回應。
- 標準化 discovery table 會保留官方股票殖利率資料集中的所有證券。顯示殖利率門檻只改變 `discovery_priority`，不會刪除列或定義前瞻殖利率 screen 母體。
- Market-discovery snapshot 與 screen run 不同。它不能填入標準化 EPS、預估前瞻 DPS、可分配現金或自由現金流覆蓋，也不能推進 screen 刷新 state。
- Live retrieval 一律必須明確執行。Session startup 維持本機 read-only；TLS 失敗必須以可信任 CA bundle 解決，不得停用憑證驗證。
