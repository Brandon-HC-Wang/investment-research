# 市場搜尋

Screen 定義可重現的候選搜尋。Screen definition 包含母體、輸入、篩選條件、排序因子、警示旗標、來源階級、刷新政策及輸出契約。

Definitions 登錄於 [`registry.yaml`](registry.yaml)。每次成功或具有診斷價值的執行都必須建立新的 append-only run，不得覆寫舊結果。Screen 候選需要人工研究，不構成投資建議。

## 啟用中的定義

功能概要、操作命令、限制與恢復待辦請閱讀[搜尋策略指南](../docs/SearchStrategyGuide.md)。

- [`forward-dividend-yield/`](forward-dividend-yield/README.md) — 估計標準化盈餘與現金能力是否可能支持至少 7% 的前瞻現金殖利率。
