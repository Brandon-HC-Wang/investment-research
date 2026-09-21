# 搜尋策略功能：概要、使用方式與交接

<!-- 衍生繁體中文閱讀版；英文原檔 `SearchStrategyGuide.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

## 目前檢查點 — 2026-09-15

基礎架構與離線執行流程已存在，但尚無正式前瞻股利 screen run，也未保存正式官方市場 snapshot。Strategy 為 `testing`；screen definition version 為 3。本機刷新檢查回報 `due`，原因為 `definition_changed` 與 `never_run`。

**使用者決定：** TPEx TLS 問題先暫擱。除非使用者明確要求恢復，否則不排查憑證、不安裝信任憑證，也不繞過 TLS verification。這是工作流程暫停，不代表 TPEx 資料不可取得或不適合使用。

此檢查點的 Phase 2 與 Phase 3 實作仍未 commit。本文件不授權 commit、push、live refresh 或進一步實作。

## 功能概要

此功能保存可重複使用的研究策略、可重現搜尋條件、點時結果與刷新提醒。輸出是研究佇列，不是投資建議或公司 thesis。

| 分層 | 責任 | 入口 |
|---|---|---|
| Strategy | 經濟假說、信心、結果驗證要求 | [前瞻股利收益](../strategies/forward-dividend-income/README.md) |
| Screen | 母體、條件、排序、輸入／輸出契約、刷新政策 | [前瞻股利殖利率](../screens/forward-dividend-yield/README.md) |
| Source snapshot | 官方原始回應與標準化市場探索資料 | [來源快照](../screens/forward-dividend-yield/source-snapshots/README.md) |
| Run | Append-only manifest、結果 CSV、雙語摘要 | `screens/forward-dividend-yield/runs/` — 僅在持久化時建立 |
| Refresh state | 最後成功 run、資料日、下次到期日、原因碼 | [state.yaml](../screens/forward-dividend-yield/state.yaml) |

預期流程為：

```text
官方市場資料 → source snapshot
                   ↓
財報 + 經審查的公司模型 → normalized EPS / 可支持 DPS
                   ↓
經審查的 input CSV → dry run → 獲授權的持久化 run → 人工審查
```

財報／模型 enrichment 步驟尚未實作。Market-discovery CSV 不能直接替換 runner 的 input CSV。

## 第一個 screen 與分析邊界

目前時間範圍是以標準化 2026 年盈餘，在 2027 年配發現金股利。必要數值條件為：

- 基本情境前瞻現金殖利率 ≥ 7%。
- 標準化基本情境 EPS / 必要 DPS ≥ 1.25 倍。
- 下行情境前瞻現金殖利率 ≥ 5%。

`必要 DPS = 搜尋日股價 × 7%`

`前瞻殖利率 = 預估現金 DPS / 搜尋日股價 × 100%`

排序使用下行情境殖利率、標準化 EPS 覆蓋、自由現金流股利覆蓋與配息穩定年數。警示旗標與所有保留候選皆須人工審查。Executor 不會驗證業務品質、產業標準化、母公司現金能力，或分析師估計是否有支持證據。

Market collector 的顯示殖利率門檻預設為 5%，只標記審查優先度，不刪除列，也不建立前瞻殖利率。歷史顯示殖利率不是預估現金殖利率。

## 使用方式

所有命令皆從 repository root 執行，使用支援 `zoneinfo` 的 Python 3。腳本使用標準庫與 repository 的 flat-YAML helper。

### 1. 調用已保存定義與檢查刷新狀態

閱讀已登錄 screen 的 [README](../screens/forward-dividend-yield/README.md) 與 [screen.yaml](../screens/forward-dividend-yield/screen.yaml)。可透過 [screens/registry.yaml](../screens/registry.yaml) 與 [strategies/registry.yaml](../strategies/registry.yaml) 找到 definitions。

```bash
python3 scripts/check_screen_refresh.py --due-only
python3 scripts/check_screen_refresh.py --due-only --json
```

新 session 載入 repository context 後，會執行這個本機 read-only check。它不擷取來源、不偵測外部新公告、不排程背景工作，也不修改 state。目前事件觸發的新鮮度依賴本機記錄的 state，不是自動外部監測。

### 2. 離線驗證市場資料蒐集

以下命令只使用 synthetic fixtures，不寫入任何資料：

```bash
python3 scripts/collect_market_discovery.py \
  --source-dir scripts/tests/fixtures/market-discovery \
  --snapshot-id fixture-contract-dry-run \
  --as-of 2026-09-14 \
  --output-dir screens/forward-dividend-yield/source-snapshots/fixture-contract-dry-run \
  --dry-run --json
```

Fixture 預期結果：`success`、4 筆母體、4 筆完整股價、2 筆優先審查標籤。Synthetic 數值是軟體測試，不是投資證據；不得持久化為正式研究 snapshot。

Replay 經審查的官方資料時，`--source-dir` 必須包含 `twse_yield.json`、`twse_price.json`、`tpex_yield.json` 與 `tpex_price.json`，四個來源日期皆須等於 `--as-of`。移除 `--dry-run` 後，會將 raw JSON、`market-discovery.csv`、`manifest.yaml` 與雙語摘要保存至名稱符合 `--snapshot-id` 的新目錄。

**暫擱：** 既有 `--fetch-live` 模式會以 strict TLS 擷取全部四個 TWSE／TPEx endpoints。TPEx 工作暫停期間不要執行。目前沒有 TWSE-only 選項；新增此模式必須明確定義市場範圍契約，不得使用空 TPEx 檔案或默默縮小母體。

### 3. 準備經審查的分析輸入

完整 header 定義於 [screen.yaml](../screens/forward-dividend-yield/screen.yaml)：

```csv
market,ticker,company,price_date,price_twd,financial_period,normalized_eps_base_twd,normalized_eps_downside_twd,estimated_dps_base_twd,estimated_dps_downside_twd,fcf_dividend_coverage_x,payout_consistency_years,warning_flags,source_tier,evidence_reference,source_url
```

股價、EPS、DPS 單位為每股 TWD；現金流覆蓋使用倍數；配息穩定性使用整年。保留已報導財務期間與預測年度的差異。每個估計皆須有具日期的財報／模型 provenance、經常性與一次性調整、情境邏輯及現金能力審查。市場與 ticker 身分必須唯一；有效列的股價日與財務期間須一致。`source_tier` 為 `primary` 或 `secondary`；`source_url` 為絕對 HTTP(S) URL。

目前實作的覆蓋率分母是提供的 CSV 列，不是獨立驗證過的全市場母體。即使 input-row coverage 為 100%，人工挑選的子集也不能稱為完整 TWSE／TPEx coverage。

### 4. 離線驗證 screen 執行

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input scripts/tests/fixtures/forward-dividend-yield-input.csv \
  --as-of 2026-09-14 \
  --run-id verification-dry-run \
  --dry-run --json
```

Synthetic 預期結果：`success`、3 筆已評估、2 筆候選、100% input-row coverage。不會寫入 run 或更新 state。

獲授權建立正式 run 時，先以經審查的 input 取代 fixture、選擇新 run ID、將 `--as-of` 設為 input 一致的 `price_date`，之後才移除 `--dry-run`。Executor 目前只支援 `forward-dividend-yield`。Run ID 為 10–128 字元，以英數字起始，其餘允許英文字母、數字、`.`、`_`、`+`、`-`。

### 5. 閱讀已保存結果與 state

持久化 run 會在新的 `runs/<run-id>/` 目錄建立 `manifest.yaml`、`results.csv`、`summary.md` 與 `summary.zh-TW.md`。解讀結果前先閱讀 manifest 的 status、參數、provenance、錯誤與覆蓋率。舊結果必須以新 run 修正，不得覆寫。

- `success`：評估無列錯誤，並達到設定的 input coverage 要求；只有此狀態更新刷新 state。
- `partial`：部分列無法評估或覆蓋不足；結果供診斷，不推進 state。
- `failed`：沒有列能完成評估；不推進 state。

重大 input／header／日期錯誤可能在持久化前終止；不是每個失敗都會產生 manifest。軟體 `success` 不代表分析核准，也不證明全市場完整性。

刷新頻率為七天，過期容忍值為七天。月營收、財報、股利決議、資本事件與 definition changes 已宣告為 triggers；外部事件偵測尚未自動化。

### 6. 驗證檢查點

```bash
python3 -m unittest discover -s scripts/tests -v
python3 scripts/validate_repository.py
git diff --check
```

2026-09-15 重新執行時，既有 32 個測試全部通過。Repository validation 檢查契約與 artifact integrity，不驗證預測準確度或來源真實性。只有明確要求時才 commit；不得默默 push。

## 待辦事項與恢復順序

- [x] Strategy／screen registries、schemas、templates 與雙語推理。
- [x] Read-only startup reminder 與 deterministic refresh tests。
- [x] 離線 executor、append-only artifacts、hashes、state-success 邊界與 fixture tests。
- [x] TWSE／TPEx market-discovery collector、source snapshot 契約與 fixture tests。
- [ ] **不需處理 TPEx 的下一步：** 定義 enrichment contract，連結標準化 EPS、預估 DPS、母公司現金、財務期間、assumption IDs 與具日期的主要證據；不得從歷史殖利率或年化月營收實作預測。
- [ ] 新增 partial-market／TWSE-only 模式前，先定義範圍名稱、分母驗證與缺少市場的表示方式。目前沒有此選項。
- [ ] 新增分離測試的官方財報擷取，以及金融、營建／代銷與景氣循環公司的產業標準化。
- [ ] 獨立驗證全市場母體完整性與輸入過期；只看提供列的覆蓋率不足。
- [ ] 自動化視為 production-ready 前，審查 failure manifests、原始 input 保留／hash provenance、中斷後 lock recovery、歷史 definition reconstruction 與刷新 state 重建。
- [ ] 選定來源範圍準備完成後，保存並驗證第一份經審查的官方市場 snapshot。
- [ ] 資料範圍與分析 input 審查完成後，才授權第一個正式 run；人工核對候選與警示。
- [ ] 依預先聲明指標，將預測與後續股利決議比較；證據要求達成前保持 `testing`。
- [ ] 外部事件監測或排程刷新需另外授權與設計。
- [ ] **使用者決定暫擱：** TPEx certificate-chain diagnosis 與 trusted-bundle configuration。只有明確要求才恢復；不得停用 TLS verification。
- [ ] 明確要求時建立本機實作 checkpoint；截至本文件日期，Phase 2／3 變更仍待 commit。

恢復時先載入 repository 必要 context、閱讀本指南、檢查 due state 與 worktree、重新驗證，然後從 enrichment contract 開始。不要重啟 TPEx 排查，也不要把先前診斷數量當成目前市場證據。

## 參考與歷史

- [架構提案與實作決策](proposals/SearchStrategyArchitecture.md)
- [腳本參考](../scripts/README.md)
- [Screen definition 與邊界](../screens/forward-dividend-yield/README.md)
- [Strategy 結果驗證指標](../strategies/forward-dividend-income/README.md)
- [Append-only research log](../research-log/2026.md)

- **2026-09-15：** 整理概要、可執行離線命令、限制與恢復工作。記錄使用者決定暫擱 TPEx，不再將 TLS 修復列為立即下一步。本次文件工作沒有連網蒐集，也未執行正式研究 run。
