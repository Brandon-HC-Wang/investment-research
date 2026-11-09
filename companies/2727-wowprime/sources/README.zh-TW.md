# 來源庫

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

按證據類型儲存保留的來源工件。不要將編號的研究文件移至此處。結論保留在規範的公司記錄中，並連結回工件或原始 URL。

- `earnings/`：經審計的中期財務資料。
- `conference_calls/`：文字記錄、簡報和活動筆記。
- `monthly_revenue/`：交換揭露與調節。
- `news/`：僅與決策相關的次要證據。

在文件名稱中使用 ISO 日期並保留發布日期、來源、存取日期、報告期間、單位和頁面引用。

## 2026-11-09 — 第三季更新來源清單

以下來源存取日均為 2026-11-09。[機器可讀登錄](2026-11-09-refresh.json)記錄完整網址、財報範圍、日期、PDF 頁碼與保存檔案的 SHA-256。發布日不由下載檔名推定。

| ID | 標題／發布者／日期 | 範圍與保存證據 |
|---|---|---|
| S1 | 王品，*2026 第三季合併財報暨會計師核閱報告*，董事會通過／核閱日期 2026-11-05 | 第 3-8 頁財報；21-22 租賃；30-35 權益／收入／業外；38-39 EPS；41 租賃橋接；46-47 限制／承諾；50-51 部門。[PDF](earnings/2026Q3-consolidated.pdf)。 |
| S2 | 王品，*2026 第二季合併財報*，通過 2026-08-06 | 第 5 頁上半年／第二季損益；37-38 EPS；49-50 部門。[先前保存 PDF](earnings/2026Q2-consolidated.pdf)，本次重讀。 |
| S3 | 證交所，*上市公司月營收*，API 無發布日；回傳出表日期 1151017 | 九月及前三季累計，公司 2727 完整[資料列](monthly_revenue/2026-11-09-twse-latest.json)。未回傳十月。 |
| S4 | 王品，*投資人專區／台灣品牌店數*，頁面更新 2026-09-30 | 網頁讀取台灣 374／中國 108／合計 482 及部分品牌店數。選取觀察存於 JSON；原始 HTML 下載被拒，未將拒絕頁假稱成功保存。 |
| S5 | 證交所，*2727 十一月各日成交資訊*，API 無發布日 | [保存回應](2026-11-09-twse-price.json)；最新回傳收盤為 2026-11-06 的 225.00。 |
| S6 | 王品，*FY2025 個體財報*，通過 2026-03-05 | 第 10-12 頁財報；44-46 分配背景；54 EPS。[先前保存 PDF](earnings/2025FY-parent-only.pdf)，本次重讀。 |

一手存取網址：[S1/S2 電子文件平台](https://doc.twse.com.tw/server-java/t57sb01)、[S3 月營收 API](https://openapi.twse.com.tw/v1/opendata/t187ap05_L)、[S4 投資人專區](https://www.wowprime.com/zh-tw/investor)、[S4 台灣品牌](https://www.wowprime.com/zh-tw/investors-sub-menu/about-wowprime/brand-introduction/taiwan)、[S5 股價 API](https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20261101&stockNo=2727)、[S6 個體 PDF](https://www.wowprime.com/upload_cg/img020260313152234.pdf)。文件平台使用公司 2727 及檔名 `202603_2727_AI1.pdf` / `202602_2727_AI1.pdf`；完整表單請求及 S1 下載網址見 JSON。

[最新報告](../reports/2026-11-09-research-report.md)採核閱前三季收入，不採有差異的月營收累計。上半年月營收仍依[保存的 2026-10-12 資料包](2026-10-12-dividend-enrichment.json)及其連結的月營收清單；最新累計差額不代表勾稽已解決。
