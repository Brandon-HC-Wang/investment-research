# Future Automation Ideas

This directory is a design backlog, not executable automation. No scripts are implemented here.

## `update_monthly_revenue.py`

Potential purpose: ingest official monthly disclosures, preserve the raw source, normalize period and units, compare revisions, and prepare a reviewable company update. It must never infer thesis impact or overwrite company research automatically.

## `update_watchlist.py`

Potential purpose: build derived watchlist views from validated `research.yaml` files. `research.yaml` remains canonical; generated views must be reproducible and clearly marked.

## `check_open_questions.py`

Potential purpose: index company and industry questions, validate allowed statuses, flag stale review triggers, and preserve resolved or rejected history.

## `earnings_calendar.py`

Potential purpose: assemble upcoming reporting dates from official exchange or company sources, record provenance, and flag uncertainty. It must not create earnings forecasts or trading signals.

## Implementation gate

Before any idea becomes code, define input sources, schema, failure behavior, idempotency, audit trail, tests, human-review boundary, and whether network or credentials are required. Automation may propose changes; it must not silently modify append-only history.
