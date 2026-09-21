# 市場探索來源快照

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

每個子目錄都是由 `scripts/collect_market_discovery.py` 產生的 append-only 點時擷取。快照會保存四份 TWSE 與 TPEx 官方 JSON 回應、一份標準化 `market-discovery.csv`、包含 checksum 與完整性筆數的 manifest，以及雙語摘要。

這些快照只包含目前股價與交易所顯示的歷史殖利率資料，不含標準化 EPS、預估前瞻 DPS、可分配現金能力或完成的 screen 結果。建立 `scripts/run_screen.py` 可接受的 CSV 前，必須由人工或公司特定模型審查並加入這些假設。

完成的 snapshot 不得修改。來源或解析錯誤必須以新的 snapshot ID 修正；若修正重大，還需在 research log 記錄原因。
