# Market Discovery Source Snapshots

Each child directory is an append-only, point-in-time capture produced by `scripts/collect_market_discovery.py`. A snapshot preserves the four official TWSE and TPEx JSON responses, a normalized `market-discovery.csv`, a manifest with checksums and completeness counts, and paired summaries.

These snapshots contain current price and exchange-displayed historical yield data only. They do not contain normalized EPS, estimated forward DPS, distributable-cash capacity, or a completed screen result. A human or company-specific model must review and add those assumptions before creating the CSV accepted by `scripts/run_screen.py`.

Never modify a completed snapshot. Correct source or parsing errors by creating a new snapshot ID and recording the reason in the research log when the correction is material.
