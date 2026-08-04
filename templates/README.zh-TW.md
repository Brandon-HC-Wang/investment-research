# 模板

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

範本強制執行持久的記錄形狀和證據規則。

|模板|使用|
|---|---|
| [`company/`](company/) |完整的固定公司記錄，包括研究狀態、假設、來源和歷史 |
| [`SourceRecord.md`](SourceRecord.md) |一致的源捕獲與分析提取|
| [`QuarterlyReview.md`](QuarterlyReview.md) |根據先前的假設定期檢視結果 |
| [`ResearchLogEntry.md`](ResearchLogEntry.md) |僅附加資料發現或假設事件 |
| [`reports/investment-research-report.html`](reports/investment-research-report.html) |衍生公司研究報告使用的單一檔案、響應式、可列印 HTML 骨架 |

範本包含說明和欄位定義，而不是虛構的證據。實例化活動記錄時刪除說明文本，同時保留所需的標題和表格。

HTML 報告模板只是衍生呈現起點。內容必須來自 canonical 研究記錄，並遵循 [`../docs/ui-specs/research-report.md`](../docs/ui-specs/research-report.md)；絕不能把模板當作證據。
