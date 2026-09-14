# Screen 模板

將本目錄複製至 `screens/<screen-id>/`、取代所有說明值，並在 `screens/registry.yaml` 登錄 `screen.yaml`。Definition 與推理內容必須同步。

每次執行都要在 `runs/` 下建立新的時間戳記目錄，內含 `manifest.yaml`、`results.csv` 及配對的 `summary.md`。Runs 僅能附加。`state.yaml` 是納入版本控制且可重建的 cache，不得保存唯一研究結論。
