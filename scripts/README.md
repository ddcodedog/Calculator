# scripts/

Helper scripts for this documentation repository.

- `extract-gate1-inventory.cjs`, `patch-gate1.cjs`, and `patch-pcdog.cjs` rebuild inventory notes from a local export. They are not run in CI.
- `check-docs.py` is read-only. It scans Markdown in this repository and requests tool URLs. It does not rewrite files. Paths under `promo/` are outreach drafts and are skipped by the title, relative-link, and formula-verification gates.

```bash
python3 scripts/check-docs.py
python3 scripts/check-docs.py --skip-urls
```

Exit 0 means no hard failure. On a tool URL, HTTP 404 and 410 fail, a final site homepage fails, and HTTP 5xx fails after the retry budget. HTTP 403, 429, DNS errors, and other network errors are INCONCLUSIVE warnings, not passes. `python3 scripts/build_indexes.py` rewrites `indexes/topics.json` and `indexes/verification-index.json` from the verification file. GitHub Actions runs the unit tests and `check-docs.py` from `.github/workflows/doc-checks.yml` and uploads the JSON. A weekly job also requests cited external standards URLs and records inconclusive results without replacing those URLs. The workflow does not commit changes and does not touch the eleven product-site repositories.
