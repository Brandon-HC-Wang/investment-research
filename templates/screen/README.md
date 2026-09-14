# Screen Template

Copy this directory to `screens/<screen-id>/`, replace every instructional value, and register `screen.yaml` in `screens/registry.yaml`. Keep the definition and reasoning synchronized.

Each execution creates a new timestamped directory under `runs/` containing `manifest.yaml`, `results.csv`, and paired `summary.md` files. Runs are append-only. `state.yaml` is a committed, rebuildable cache and cannot contain unique research conclusions.
