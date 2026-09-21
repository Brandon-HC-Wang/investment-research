# 結構化資料模式

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

模式定義了人工智慧代理和未來工具共享的穩定的機器可讀合約。

- [`company-meta.schema.json`](company-meta.schema.json) 驗證公司身分和向後相容的元資料。
- [`research-state.schema.json`](research-state.schema.json) 驗證可變的研究工作流程狀態。
- [`strategy.schema.json`](strategy.schema.json) 驗證可測試 strategy definitions 及生命週期狀態。
- [`screen.schema.json`](screen.schema.json) 驗證可重現 screen definitions 及刷新政策。
- [`screen-run.schema.json`](screen-run.schema.json) 定義不可變點時 run manifests。
- [`screen-state.schema.json`](screen-state.schema.json) 驗證可重建刷新狀態。
- [`market-discovery-snapshot.schema.json`](market-discovery-snapshot.schema.json) 驗證在分析補充前保存的官方市場來源 snapshots。

Markdown 仍然是敘事推理的規範。模式必須在可能的情況下進行加法演化；重大變更需要遷移文件和變更日誌條目。

Strategy 與 screen YAML 使用 `scripts/yaml_subset.py` 實作的 dependency-free flat subset：只允許 top-level scalars 與 top-level scalar lists。Repository validator 不需下載套件即可強制目前契約；對持久化 screen runs 也會檢查 artifact 路徑限制、CSV headers 與筆數、成功 run 完整性及 results checksum。JSON Schemas 則是較完整工具使用的明確 interoperability contract。
