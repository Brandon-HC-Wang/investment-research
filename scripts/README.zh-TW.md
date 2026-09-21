# 儲存庫腳本

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

## 驗證儲存庫

從儲存庫根運行：

```bash
python3 scripts/validate_repository.py
```

驗證器僅使用 Python 標準庫。它檢查必要 top-level 檔案與目錄、固定公司檔名、非空 Markdown、metadata 欄位與受控值、ISO 日期、strategy 與 screen registries、雙向引用、刷新 state，以及 active 公司記錄中常見的未解析模板標記。

退出代碼 `0` 表示驗證已通過。退出代碼 `1` 表示列印了一項或多項合約違規行為。驗證器有意保守：它檢查結構完整性，而不是投資分析的正確性或來源品質。

## 檢查 screen 刷新狀態

執行本機 read-only 啟動檢查：

```bash
python3 scripts/check_screen_refresh.py --due-only
```

加上 `--json` 可取得 machine-readable output；加上 `--as-of YYYY-MM-DD` 可進行 deterministic testing。命令不會連線或修改 state。Strategy 與 screen YAML 限定使用 `yaml_subset.py` 實作的 dependency-free flat subset。

刷新狀態單元測試命令為 `python3 -m unittest discover -s scripts/tests -v`。

## 蒐集官方市場探索資料

`collect_market_discovery.py` 會在明確執行時擷取並連結 TWSE 與 TPEx 官方的目前股價及顯示殖利率資料。Live access 必須明確指定：

```bash
python3 scripts/collect_market_discovery.py \
  --fetch-live \
  --snapshot-id <unique-snapshot-id> \
  --as-of <official-data-date> \
  --output-dir screens/forward-dividend-yield/source-snapshots/<unique-snapshot-id>
```

若本機 Python trust store 無法驗證官方 endpoint，可使用 `--ca-file <pem-bundle>`；TLS verification 不得停用。Deterministic tests 或 replay 可將 `--fetch-live` 改成 `--source-dir <directory>`，目錄內須包含 `twse_yield.json`、`twse_price.json`、`tpex_yield.json` 與 `tpex_price.json`。加上 `--dry-run --json` 可只評估而不持久化。

Collector 會保存四份原始回應、確認其民國日期皆等於 `--as-of`、依市場與 ticker 連結收盤價，並寫入含 checksum 的 market-discovery snapshot。它不會估計前瞻 EPS、DPS、配息能力或現金流覆蓋，也不能建立 screen run。

## 執行離線 screen

`run_screen.py` 目前只會從備妥的 CSV 執行 `forward-dividend-yield`，不會擷取任何網路資料。可用以下命令驗證輸入，且不修改 repository：

```bash
python3 scripts/run_screen.py \
  --screen forward-dividend-yield \
  --input scripts/tests/fixtures/forward-dividend-yield-input.csv \
  --as-of 2026-09-14 \
  --run-id verification-dry-run \
  --dry-run --json
```

只有在已獲授權，且輸入資料經審查並標示日期的點時執行中，才可移除 `--dry-run`。持久化執行會在新的 append-only run 目錄中原子式建立 `manifest.yaml`、`results.csv`、`summary.md` 與 `summary.zh-TW.md`。既有 run ID 不得覆寫。只有 `success` run 可以推進 `state.yaml`；`partial` 與 `failed` run 不得推進。

## 未來的鷹架

[`future/`](future/README.md) 記錄了可能的自動化，但沒有實現它。未來的腳本在開發之前需要明確的模式、來源、測試和手動審查邊界。
