# Repository Scripts

## Validate the repository

Run from the repository root:

```bash
python3 scripts/validate_repository.py
```

The validator uses only the Python standard library. It checks required top-level files and directories, fixed company filenames, non-empty markdown, metadata fields and controlled values, ISO dates, and common unresolved template markers in active company records.

Exit code `0` means validation passed. Exit code `1` means one or more contract violations were printed. The validator is intentionally conservative: it checks structural integrity, not investment-analysis correctness or source quality.
