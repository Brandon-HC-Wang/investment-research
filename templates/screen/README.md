# Screen Template

Copy this directory to `screens/<screen-id>/`, replace every instructional value, and register `screen.yaml` in `screens/registry.yaml`. Keep the definition and reasoning synchronized.

Each execution creates a new timestamped directory under `runs/` containing `manifest.yaml`, `results.csv`, and paired `summary.md` files. Runs are append-only. `state.yaml` is a committed, rebuildable cache and cannot contain unique research conclusions.

Set `base_yield_rule` to `point` for a point threshold or `range_upper_bound` for interval nomination. The latter requires base DPS low/high inputs plus corresponding DPS/yield bounds and qualification labels in outputs. Keep a representative base DPS within the non-negative interval. Forward-dividend definition version 4 uses an inclusive upper-bound gate and distinguishes `partial_range` from `entire_range`; the EPS/downside gates remain separate. New executor runs retain `definition.yaml`; archive an exact old definition before changing its CSV contract so old runs remain verifiable.

Executable screens must declare their flat CSV input and output fields in `screen.yaml`. Validate input with a dry run before persistence. An executor must separate retrieval from evaluation, reject duplicate or unsafe run IDs, write artifacts atomically, and update state only after a complete successful run.

When a screen has an official-source collector, retain each raw-source package and its normalized discovery table as a separate append-only snapshot using `source-snapshot-manifest.yaml`. A source snapshot is not a screen run and must not contain unsupported forward estimates.
