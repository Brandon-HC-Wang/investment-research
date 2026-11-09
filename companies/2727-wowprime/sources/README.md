# Source Library

Store retained source artifacts by evidence type. Do not move numbered research files here. Conclusions remain in canonical company records and link back to the artifact or original URL.

- `earnings/`: audited and interim financial materials.
- `conference_calls/`: transcripts, presentations, and event notes.
- `monthly_revenue/`: exchange disclosures and reconciliations.
- `news/`: decision-relevant secondary evidence only.

Use ISO dates in filenames and preserve publication date, source, access date, reporting period, units, and page references.

## 2026-11-09 — Q3 refresh source register

All sources below were accessed 2026-11-09. The [machine-readable register](2026-11-09-refresh.json) records complete URLs, report scope, dates, PDF pages and SHA-256 of retained files. Publication dates are not inferred from download filenames.

| ID | Title / publisher / date | Sections and retained evidence |
|---|---|---|
| S1 | Wowprime, *2026 Q3 consolidated financial statements and independent review report*, board approval/review dated 2026-11-05 | pp. 3-8 statements; 21-22 leases; 30-35 equity/revenue/nonoperating; 38-39 EPS; 41 lease bridge; 46-47 restrictions/commitments; 50-51 segments. [PDF](earnings/2026Q3-consolidated.pdf). |
| S2 | Wowprime, *2026 Q2 consolidated financial statements*, approval 2026-08-06 | p. 5 H1/Q2 income; pp. 37-38 EPS; 49-50 segments. [Previously retained PDF](earnings/2026Q2-consolidated.pdf), reread this task. |
| S3 | Taiwan Stock Exchange, *Monthly operating revenue*, undated API; returned output date 1151017 | September and cumulative 9M company 2727 complete [row](monthly_revenue/2026-11-09-twse-latest.json). October not returned. |
| S4 | Wowprime, *Investor relations / Taiwan brand counts*, page update 2026-09-30 | Web-read counts 374 Taiwan / 108 China / 482 total; selected brand counts. Selected observations retained in JSON; raw HTML download was rejected, so no raw HTML is represented as a successful capture. |
| S5 | Taiwan Stock Exchange, *2727 November daily trading information*, undated API | [Retained response](2026-11-09-twse-price.json); latest returned close 225.00 on 2026-11-06. |
| S6 | Wowprime, *FY2025 parent-only financial statements*, approval 2026-03-05 | pp. 10-12 statements; 44-46 distribution context; 54 EPS. [Previously retained PDF](earnings/2025FY-parent-only.pdf), reread this task. |

Primary retrieval URLs: [S1/S2 public document portal](https://doc.twse.com.tw/server-java/t57sb01), [S3 monthly API](https://openapi.twse.com.tw/v1/opendata/t187ap05_L), [S4 investor relations](https://www.wowprime.com/zh-tw/investor), [S4 Taiwan brands](https://www.wowprime.com/zh-tw/investors-sub-menu/about-wowprime/brand-introduction/taiwan), [S5 price API](https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20261101&stockNo=2727), [S6 parent PDF](https://www.wowprime.com/upload_cg/img020260313152234.pdf). The document portal requires company 2727 and filenames `202603_2727_AI1.pdf` / `202602_2727_AI1.pdf`; exact form requests and the downloaded S1 URL are in JSON.

The [current report](../reports/2026-11-09-research-report.md) uses reviewed 9M revenue, not the conflicting monthly total. H1 monthly figures remain sourced to the [retained 2026-10-12 packet](2026-10-12-dividend-enrichment.json) and its linked monthly register; the discrepancy is not resolved by the latest cumulative difference.
