# 架構遷移 — 2026-08-04

<!-- 衍生繁體中文閱讀版；英文原檔 `Migration-2026-08-04.md` 是唯一 canonical source。若內容衝突，以英文版為準。 -->

## 目的

這種附加重構引入了模組化知識層和明確的研究歷史，同時保留了每條遷移前路徑和所有公司研究。它的設計目的是保持人類可讀，並可由 Codex、Claude Code、GPT、Gemini CLI 和未來代理尋址。

## 已套用更改

### 業界套餐

每個現有產業現在都有一個小寫包，其中包含 `README.md`、`metrics.md`、`valuation.md` 和 `open_questions.md`。原始的單文件行業指南仍然作為向後相容的概述，並連結到新的規範包。

### 公司研究狀況

每家公司現在都會增加：

- `sources/earnings/`、`sources/conference_calls/`、`sources/monthly_revenue/` 和 `sources/news/`，皆附有使用指南；
- `history/` 用於不可變的季度快照；
- `assumptions.md` 用於僅附加 `Open`、`Verified` 和 `Rejected` 假設；
- `research.yaml` 用於可變覆蓋和審查狀態。

沒有編號的公司檔案或 `meta.yaml` 被刪除、重新命名或重寫。 `meta.yaml` 仍然是穩定的身份和向後相容性合約。新工作流程使用者應該會偏好 `research.yaml` 的覆蓋狀態。

### 共享知識與論文

`knowledge/` 儲存不屬於一家公司的可重複使用概念。 `theses/` 儲存宏觀或跨產業的觀點，具有明確的階段、公司、風險、催化劑和驗證測試。公司記錄連結到這些層，但保留自己的因果和收益分析。

### 投資組合層

`portfolio/` 新增了投資組合層級的觀察清單、分配和風險框架。現有的 `watchlist/` 仍然是規範的研究優先隊列。

### 研究日誌

`research-log/companies/` 和 `research-log/industries/` 新增範圍內的僅追加歷史記錄。現有年度日誌保留在原始位置，不會移轉或刪除。

### 腳本

`scripts/future/README.md` 僅記錄自動化想法。沒有實施未來的腳本。現有的儲存庫驗證器保持不變。

## 相容性矩陣

|現有介面 |狀態 |新的首選介面 |
|---|---|---|
| `industries/Construction.md` 及同業 |存檔|配套小寫行業包|
|公司編號文件 |保留並規範 |沒有替代品 |
| `meta.yaml` |儲存|身分仍然存在；可變工作流程也使用`research.yaml` |
| `research-log/2026.md` |儲存|範圍內的新條目使用 `companies/` 或 `industries/` |
| `watchlist/` |為研究優先事項保留並規範 | `portfolio/watchlist.md` 僅提供投資組合上下文 |
| `scripts/validate_repository.py` |保存|沒有替代品 |

## 未來代理人的遷移規則

1. 不要僅僅為了使樹看起來統一而移動舊的行業內容。
2. 僅在必要時將新的可重複使用產業發現新增至打包檔案和舊指南中的連結。
3. 在`meta.yaml`中保持身分同步；將研究工作流程保存在 `research.yaml` 中。
4. 切勿修改 `history/` 中已提交的文件以反映後續資訊。
5. 切勿刪除假設或範圍日誌條目；附加狀態變更或更正。
6. 儲存來源工件，無需將規格分析移出編號的公司文件。
7. 將投資組合文件視為衍生的研究背景，而不是公司事實。

## 回滾特性遷移是累加性的。舊版讀者可以忽略新目錄並繼續使用現有文件。刪除新層不需要重建或移動現有的公司研究，儘管在新層中創建的任何研究都必須在回滾之前保留。
