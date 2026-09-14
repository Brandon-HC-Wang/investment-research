# Structured Data Schemas

Schemas define stable machine-readable contracts shared by AI agents and future tooling.

- [`company-meta.schema.json`](company-meta.schema.json) validates company identity and backward-compatible metadata.
- [`research-state.schema.json`](research-state.schema.json) validates mutable research workflow state.
- [`strategy.schema.json`](strategy.schema.json) validates testable strategy definitions and lifecycle state.
- [`screen.schema.json`](screen.schema.json) validates reproducible screen definitions and refresh policy.
- [`screen-run.schema.json`](screen-run.schema.json) defines immutable point-in-time run manifests.
- [`screen-state.schema.json`](screen-state.schema.json) validates rebuildable refresh state.

Markdown remains canonical for narrative reasoning. Schemas must evolve additively when possible; breaking changes require a migration document and changelog entry.

Strategy and screen YAML uses the dependency-free flat subset implemented in `scripts/yaml_subset.py`: top-level scalars and top-level scalar lists only. The repository validator enforces the active contracts without requiring downloaded packages; the JSON Schemas remain the explicit interoperability contract for richer tooling.
