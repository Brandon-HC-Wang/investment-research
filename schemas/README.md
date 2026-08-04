# Structured Data Schemas

Schemas define stable machine-readable contracts shared by AI agents and future tooling.

- [`company-meta.schema.json`](company-meta.schema.json) validates company identity and backward-compatible metadata.
- [`research-state.schema.json`](research-state.schema.json) validates mutable research workflow state.

Markdown remains canonical for narrative reasoning. Schemas must evolve additively when possible; breaking changes require a migration document and changelog entry.
