# Screen 模板

將本目錄複製至 `screens/<screen-id>/`、取代所有說明值，並在 `screens/registry.yaml` 登錄 `screen.yaml`。Definition 與推理內容必須同步。

每次執行都要在 `runs/` 下建立新的時間戳記目錄，內含 `manifest.yaml`、`results.csv` 及配對的 `summary.md`。Runs 僅能附加。`state.yaml` 是納入版本控制且可重建的 cache，不得保存唯一研究結論。

`base_yield_rule` 採 `point` 表示單點門檻，採 `range_upper_bound` 表示區間初選。後者須輸入基準 DPS 下緣／上緣，輸出對應 DPS／殖利率界限及達標類型；代表基準 DPS 須介於非負區間內。前瞻股利 definition version 4 採含等號的上緣門檻，區分 `partial_range`、`entire_range`；EPS／下行條件獨立。新 executor run 保留 `definition.yaml`；變更 CSV 契約前封存精確舊定義，讓舊 run 仍可驗證。

可執行 screen 必須在 `screen.yaml` 宣告 flat CSV 輸入與輸出欄位，並在持久化前先以 dry run 驗證輸入。Executor 必須分離擷取與評估、拒絕重複或不安全的 run ID、原子式寫入 artifacts，且只有完整成功後才能更新 state。

若 screen 有官方來源 collector，應使用 `source-snapshot-manifest.yaml`，將每份 raw-source package 與標準化 discovery table 保存成獨立、append-only snapshot。Source snapshot 不是 screen run，也不得包含缺乏支持的前瞻估計。
