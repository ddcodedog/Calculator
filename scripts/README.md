# scripts/

Helper scripts for this documentation repository.

- `extract-gate1-inventory.cjs`, `patch-gate1.cjs`, and `patch-pcdog.cjs` rebuild inventory notes from a local export. They are not run in CI.
- `check-docs.py` is read-only. It scans Markdown in this repository and requests tool URLs. It does not rewrite files.

```bash
python3 scripts/check-docs.py
python3 scripts/check-docs.py --skip-urls
```

Exit 0 means no hard failure. A connection error or a non-404 HTTP status is a warning. HTTP 404 and 410 on a tool URL are failures. GitHub Actions runs the same command from `.github/workflows/doc-checks.yml` and uploads the JSON. That workflow does not commit changes and does not touch the eleven product-site repositories.
