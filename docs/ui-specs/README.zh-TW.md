# UI 規格

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

本目錄定義研究輸出物可重複使用的呈現契約。這裡保存設計與互動規則，不保存公司證據或最新研究結論。

## Canonical 狀態

英文 Markdown 是 canonical 版本。依 Repository 雙語 Markdown 契約，每份英文檔都有同目錄的 `.zh-TW.md` 閱讀版。

## 現有規格

- [`research-report.md`](research-report.md) 定義投資研究 HTML 報告的資訊架構、design tokens、元件、響應式行為、無障礙、列印行為及品質檢查。
- [`../../templates/reports/investment-research-report.html`](../../templates/reports/investment-research-report.html) 是單一檔案、可自足運作的實作模板。

## 使用方式

1. 閱讀投資研究框架及相關公司的 canonical 記錄。
2. 將 HTML 模板複製到暫存位置或使用者指定的輸出位置。
3. 以具有來源的事實、清楚標記的估計、假設、意見及未決問題取代通用展示內容。
4. 除非公司經濟模式需要有明確說明的例外，否則保留報告章節順序。
5. 驗證內容、桌機與手機版面、鍵盤焦點、對比、列印及離線運作。

模板只定義結構，絕不能成為公司事實、財測或估值假設的來源。
