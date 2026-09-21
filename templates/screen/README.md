# Screen Template

Copy this directory to `screens/<screen-id>/`, replace every instructional value, and register `screen.yaml` in `screens/registry.yaml`. Keep the definition and reasoning synchronized.

Each execution creates a new timestamped directory under `runs/` containing `manifest.yaml`, `results.csv`, and paired `summary.md` files. Runs are append-only. `state.yaml` is a committed, rebuildable cache and cannot contain unique research conclusions.

Executable screens must declare their flat CSV input and output fields in `screen.yaml`. Validate input with a dry run before persistence. An executor must separate retrieval from evaluation, reject duplicate or unsafe run IDs, write artifacts atomically, and update state only after a complete successful run.

When a screen has an official-source collector, retain each raw-source package and its normalized discovery table as a separate append-only snapshot using `source-snapshot-manifest.yaml`. A source snapshot is not a screen run and must not contain unsupported forward estimates.
