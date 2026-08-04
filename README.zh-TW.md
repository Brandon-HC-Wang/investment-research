# 投資研究系統

<!-- 衍生繁體中文閱讀版；英文原檔 `README.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

這是一套用來累積長期股票研究的AI原生知識系統。repository供人類分析師與多種AI程式助理共同建立、挑戰並長期保存投資知識。

它不是新聞資料庫、交易日誌或股票推薦動態。目標是找出未來二至五年可能持續增加獲利的公司，並使背後假設可供稽核。

## 研究順序

所有公司研究遵循同一條因果鏈：

> 商業品質 → 競爭優勢 → 營收驅動因素 → EPS驅動因素 → 經常性獲利 → 案量與能見度 → 風險 → 投資論點 → 估值

估值是最後一步。低倍數不能彌補商業品質差或獲利能見度不足。

## Repository導覽

| 路徑 | 用途 |
|---|---|
| `PROJECT_CONTEXT.md` | 穩定的使命、邊界與系統設計 |
| `AGENTS.md` | AI助理必須遵守的操作規則 |
| `.ai/` | 精簡情境、寫作風格與執行協議 |
| `docs/` | Canonical研究方法及評分標準 |
| `companies/` | 每家公司一份可長期維護的研究記錄 |
| `industries/` | 共用的產業經濟、指標與循環知識 |
| `knowledge/` | 可跨公司與產業引用的概念 |
| `theses/` | 總體及跨產業投資論點 |
| `portfolio/` | 投資組合層級的觀察、配置及風險思考 |
| `models/` | 建模慣例及可重複分析方法 |
| `templates/` | 新研究記錄的受控起點 |
| `watchlist/` | 研究優先佇列，不是買賣建議 |
| `research-log/` | 只能附加的公司、產業與repository歷史 |
| `scripts/` | Repository驗證及維護工具 |
| `schemas/` | 結構化metadata的機器可讀契約 |

## 從這裡開始

進行任何修改前，依序閱讀：

1. [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md)
2. [`AGENTS.md`](AGENTS.md)
3. [`.ai/context.md`](.ai/context.md)
4. [`docs/Framework.md`](docs/Framework.md)

接著遵循[`docs/Workflow.md`](docs/Workflow.md)及相關模板或產業指南。

## 語言版本

英文`.md`是canonical版本，供AI協作使用。每份英文檔都有同目錄`.zh-TW.md`繁體中文閱讀版，例如`docs/Framework.md`對應`docs/Framework.zh-TW.md`。兩者若有差異，以英文版為準，並應同步修正中文版。

## 新增公司

1. 將`templates/company/`複製至`companies/<ticker>-<slug>/`。
2. 在`meta.yaml`填入真實公司身分；在`research.yaml`填入研究狀態、下次複查、信心、優先序及觀察項目。
3. 先研究商業模式，再預測獲利或討論估值。
4. 在`07_open_questions.md`記錄未決問題。
5. 在`assumptions.md`登錄重大假設，依法按類別保留來源資料，並建立第一份季度歷史快照。
6. 將啟動事件附加至`05_timeline.md`；若具重大性，也更新所屬研究日誌。
7. 執行`python3 scripts/validate_repository.py`。

十個標準公司檔名是永久介面，不得重新命名、排序或移除。

## 證據與不確定性

分開具來源事實、分析師估計與假設。在可得時記錄來源名稱、發布者、發布日期、查閱日期及URL。每個重大數字都應說明單位與期間。若精確數字會掩蓋不確定性，使用區間或情境。

只有當證據、因果機制及影響都清楚時，一項主張才成為可長期保存的知識。

## 授權

Repository結構與原始文件依[MIT License](LICENSE)提供。第三方來源仍受原權利約束，通常應以連結取代複製。
