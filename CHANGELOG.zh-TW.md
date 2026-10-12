# 變更日誌

<!-- 衍生繁體中文閱讀版；英文原檔 `CHANGELOG.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

研究系統的所有重大變更都記錄在這裡。該文件追蹤方法、結構、模式和自動化更改；公司特定的研究歷史屬於每個公司的時間軸。

格式遵循[保留變更日誌](https://keepachangelog.com/en/1.1.0/)，版本遵循儲存庫合約的語意版本控制。

## [未發布]

### 新增

- 完成八家產業 EPS／正常化、條件式母公司現金預算與 2027 現金股利區間，含三年已決議歷史與保留原始財報；僅補充診斷，無正式 run／state 推進（2026-10-12）。
- 固定八家公司前瞻股利準備度族群，包含產業輸入缺口、本地證據雜湊與分階段流程／結果驗證計畫（2026-10-12）；未變更預估、門檻或推進更新狀態。
- 首次保存已研究公司前瞻股利試跑，包含雙語假設、三年現金／股票股利歷史、保留股價證據、輸入校驗碼與部分覆蓋診斷（2026-10-12）；門檻與執行器 schema 維持不變。
- 新增證券經紀產業知識包，涵蓋交易與避險淨損益、關聯投信曝險、無償配股分母及現金／股票股利情境（2026-10-12）。
- 第一級 `strategies/` 與 `screens/` 契約，包含 registries、雙語推理、可重建刷新 state 及 append-only run semantics。
- Strategy definitions、screen definitions、screen state 及點時 run manifests 的 JSON Schemas 與 templates。
- Dependency-free、read-only screen 刷新檢查器，支援 JSON output、deterministic date evaluation 及單元測試。
- 離線 `forward-dividend-yield` executor，具明確 CSV 輸入、dry-run 模式、原子式 append-only run artifacts、checksum validation，以及僅成功時推進刷新 state 的控制。
- 預先聲明的年度股利 strategy 驗證指標，涵蓋樣本數、forecast calibration、DPS error、候選 precision 與 baseline improvement。
- 明確執行的 TWSE／TPEx market-discovery collector，包含 strict TLS、民國日期核對、保留 raw JSON、標準化全母體輸出、完整性診斷及不可變 snapshot checksums。
- Market-discovery source snapshots 的 schema、template、validator 支援及雙語操作指引。
- 雙語投資研究報告 UI 規格，以及位於 `templates/reports/`、單一檔案、響應式且可列印的 HTML 骨架。
- 每個規範英語 Markdown 文件的同一目錄 `.zh-TW.md` 閱讀伴侶，具有驗證和同步規則。
- 模組化產業知識包，包含概述、指標、評估和懸而未決的問題記錄。
- 公司級來源類別、季度歷史記錄、假設登記冊和單獨的研究狀態 YAML。
- 可重複使用的`knowledge/`、宏`theses/`及投資組合級研究層。
- 僅限範圍附加的公司和行業研究日誌。
- 僅包含文件的未來自動化積壓工作。
- 架構重構的研究狀態模式與遷移記錄。

### 已更改

- 前瞻股利 screen definition 改為 version 4：有證據的基準現金殖利率區間，未取整上緣達 7% 即符合此門檻；新增部分／整段區間標示、必填 DPS 界限、不可變定義快照及歷史契約驗證，EPS／下行／完整度條件維持不變（2026-10-12）。
- 記錄證據導向股利基準比較與可重算盈餘／配發率敏感度；修正將試跑疊加折扣解讀為正常年度預估，保留歷史 run、缺現金資料條件及登錄門檻（2026-10-12）。
- 記錄已確認的前瞻股利小樣本準備政策：已研究公司、產業別盈餘／現金估算、已決議／預估股利及最近三個完整盈餘年度歷史；登錄門檻維持不變（2026-10-12）。
- 擴充 repository validation 與 agent startup guidance，在不自動連線或修改的前提下偵測已到期 screens，並驗證持久化 run artifacts 與結果完整性。
- 保留傳統產業指南和年度研究日誌作為向後相容的切入點，同時將新工作引導到模組化套件。
- 將 `meta.yaml` 中的穩定公司身分與 `research.yaml` 中的工作流程狀態分開。

## [1.0.0] - 2026-08-04

### 新增

- 持久的公司記錄合同，包含九個編號的降價文件和 `meta.yaml`。
- 人工智慧操作環境、編寫標準和更改工作流程。
- 規範研究架構、評分標準、估價政策和清單。
- 特定產業的分析指南。
- EPS 和場景模型約定。
- 公司、來源、季度審查和研究日誌範本。
- 機器可讀的元資料模式和本機儲存庫驗證器。
- 觀察清單和僅附加研究日誌協定。

### 已更改

- 將儲存庫從降價筆記集合重新建構為人工智慧原生投資研究系統。
