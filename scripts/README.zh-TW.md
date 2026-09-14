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

## 未來的鷹架

[`future/`](future/README.md) 記錄了可能的自動化，但沒有實現它。未來的腳本在開發之前需要明確的模式、來源、測試和手動審查邊界。
