# Research Log

The research log is an append-only record of findings that materially affect more than one company, change a reusable hypothesis, or explain a major repository-level research decision. Company-only history belongs in the company timeline.

## File organization

- [`companies/`](companies/README.md) contains one append-only log per company, named exactly like the company directory.
- [`industries/`](industries/README.md) contains one append-only log per industry or durable cycle.
- Existing annual files such as [`2026.md`](2026.md) remain as backward-compatible repository-wide logs and are not moved or deleted.

Append entries in chronological order with the format in [`../templates/ResearchLogEntry.md`](../templates/ResearchLogEntry.md).

## Inclusion standard

An entry should record a material finding, its evidence, causal mechanism, confidence, affected canonical records, and next verification step. Routine news, untested commentary, and duplicate company observations do not belong here.

Never delete or silently rewrite an entry. Add a later correction, resolution, rejection, or superseding hypothesis and link it to the earlier entry.
