# 來源登錄 — 群益證（6005）

除另註外，存取日 2026-10-12。財務文件單位 TWD 千元；分析表採 TWD 百萬元，EPS／DPS 為 TWD／股。PDF 頁與印刷頁分開。留存檔及 SHA-256：[artifacts.json](artifacts.json)。

## 一級來源

| ID | 發行者／名稱 | 發布／期間 | 證據與段落 |
|---|---|---|---|
| H126 | 群益證／合併查核財報 | 簽署 2026-08-28；2026 H1 及比較 H1 2025 | [官方](https://www.capital.com.tw/CapitalGWAPI/srvcms/api/FinancialStatementsAndCreditRating/GetFile/176)、[留存](earnings/2026Q2-consolidated.pdf)；PDF 頁 7–12 資產負債／損益／現金流，24–25 持股及權益法，35 股利，36 EPS 追溯，37–40 交易／其他收入及酬勞，22 股票 VaR，51 匯率／利率，92–93 部門。本文上述 PDF 頁比印刷頁多 5 頁。 |
| FY25 | 群益證／合併查核財報 | 簽署 2026-03-06；FY2025／FY2024 | [官方](https://www.capital.com.tw/CapitalGWAPI/srvcms/api/FinancialStatementsAndCreditRating/GetFile/171)、[留存](earnings/2025FY-consolidated.pdf)；PDF 頁 8–13 報表、52 公積／分配、56 其他損益及末尾部門表。年度簽署／通過 2026-03-06。 |
| AR25 | 群益證／2025 年報 | 刊印 2026-04-11；FY2025 | [官方](https://www.capital.com.tw/CapitalGWAPI/srvcms/api/ShareholdersMeeting/GetFile/63)、[留存](annual_reports/2025-annual-report.pdf)；封面日期、持股／分配提案及五年財務比率，以標題定位，不採 PDF 搜尋摘要。 |
| IR26 | 群益證／2026 Q2 法說簡報 | 活動 2026-09-11；H1 財務及七月自結 | [官方](https://www.capital.com.tw/CapitalGWAPI/srvcms/api/ShareholdersMeeting/GetFile/66)、[留存](conference_calls/2026-09-11-presentation.pdf)；PDF 頁 13–18 報表、獲利組合、市占、股利及資本，20–25 自結與計畫，集團持股圖。活動日期以公開股東 API 核實。 |
| SELF9 | 公司申報／MOPS 九月合併自結 | 發布 2026-10-07 14:01:11；一至九月 2026 | [MOPS](https://mopsov.twse.com.tw/mops/web/t05st01)、[留存公告](announcements/2026-10-07-september-self-profit.html)、[精確 POST 與金額](announcements/2026-10-07-request-and-values.json)。EPS 3.99 為捨入，集團淨利不是歸母 EPS 分子，明列未查核／核閱。 |
| REV8 | 公司／MOPS 月營收 | 2026-08；公司網站發布 2026-09-10 | [MOPS 表](https://mopsov.twse.com.tw/nas/t21/sii/t21sc03_115_8_0.html)、[擷取列](monthly_revenue/2026-08-mops-row.json)；6005 列及成長歸因，月報加總未查核。 |
| SERIES | 群益證／公開營運及營收表 | 網站陣列至 2026-08，另含 FY2025 月營收 | [營運 API](https://www.capital.com.tw/CapitalGWAPI/srvcms/api/About/OperatingCondition/publish?Year=115)、[營收 API](https://www.capital.com.tw/CapitalGWAPI/srvcms/api/About/MonthlyRevenue/publish)、[留存財務欄](monthly_revenue/2026-08-company-series.json)。排除介面編輯 metadata；後續零欄代表缺資料。 |
| ETF919 | 群益投信／00919 月報及產品頁 | 月報截止 2026-08-31；頁面無日期 | [月報](https://www.capitalfund.com.tw/ECStorge/fund/M195.pdf)、[留存](annual_reports/00919-2026-08-factsheet.pdf)、[費率頁](https://www.capitalfund.com.tw/etf/product/detail/195/basic)；PDF 頁 1：AUM TWD 581.612 十億元、年費 0.30%。僅一檔基金，不是投信全部 AUM。 |
| RISK26 | 群益證／公開風險管理 | 頁面無日期；Q2 2026 資本快照 | [官方](https://esg.capital.com.tw/company/risk)，最近一年資本適足及風控方法段落。資本率 265%，市場風險約當額 TWD 7.703 十億元。屬管理慣例，不是壓力損失保證上限。 |
| PRICE | TWSE／個股日成交 | 已完成 2026-10-08 交易日 | [官方](https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20261008&stockNo=6005)、[留存](market_data/2026-10-08-twse-price.json)；收盤欄 32.05。API 請求日期 2026-10-08，不是 2026-10-12 即時價。 |

公司文件端點可能需一般網站 `Referer`／`Origin`，未使用登入帳號。一級 PDF 優先於把現金／股票欄倒置或混用配股前後 EPS 的次級摘要。公司 API 僅更新至八月，SELF9 另由 MOPS 取得並留存精確查詢。九月營收、精確歸母分子仍在 Q-2026-005。未把次級券商預測當作已核實共識。[問題](../07_open_questions.md)。
