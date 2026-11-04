# Final acceptance (GATE 8)

This file records checks that were actually run. It does not describe a merge, a deploy, or a GitHub Actions run that had not finished.

## Repository

| Item | Value |
|------|--------|
| Repository | https://github.com/ddcodedog/Calculator |
| Branch | `cursor/gate3-first-formulas-7b21` |
| Pull request | https://github.com/ddcodedog/Calculator/pull/2 |
| Base | `main` |
| Merge | not performed |

Doc checks ran on commit `30756538b83a22e9d6c67d508e3ad054f0905a08`. The machine-readable copy is [FINAL_ACCEPTANCE.json](FINAL_ACCEPTANCE.json).

## Site directories

`AIMarkTool`, `DIYCalcLab`, `DataFileLab`, `DevEngineerLab`, `HVACEngineerLab`, `NetEngineerLab`, `PCDog`, `PowerEngineerLab`, `PrivacyFileLab`, `StructuralEngineerLab`, `WaterEngineerLab`.

## Published formulas

| Count | Meaning |
|-------|---------|
| 25 | Formula topic files, all with verification status `VERIFIED` |
| 0 | Formula topic files with status `REVIEW_REQUIRED` or any other status |
| 350 | Inventory tools with no topic file ([FIRST_RELEASE.md](FIRST_RELEASE.md)) |
| 375 | Inventory rows |

`reports/FORMULA_VERIFICATION.json` has `countVerified` 25. Twenty of the 25 records still say the external standard text is pending or was not re-read in full. Those topics stay `VERIFIED` for the calculator math, not for a standards audit.

## URL check

Command: `python3 scripts/check-docs.py` on 2026-11-04, from this working tree, before this acceptance file existed.

| Result | Count |
|--------|-------|
| Requests | 36 (25 Online Calculator URLs + 11 production homepages) |
| Final HTTP 200 | 36 |
| Hard 404 or 410 | 0 |
| Other HTTP errors | 0 |
| Network errors | 0 |
| Attempts | 1 each |

Four tool URLs answered with a redirect that dropped a trailing slash, then HTTP 200:

- https://hvacengineerlab.com/tools/duct-airflow-design/
- https://waterengineerlab.com/tools/manning-open-channel-flow/
- https://waterengineerlab.com/tools/rational-method-peak-runoff/
- https://waterengineerlab.com/tools/water-pipe-flow-headloss/

The script follows redirects. A final 404 would have been a failure. These four were not failures.

## Markdown check

Same command. Exit code 0.

| Check | Result |
|-------|--------|
| Duplicate H1 titles | none |
| Relative links | none broken |
| Math / code fences on the 25 topics | balanced |
| Verification status vs `FORMULA_VERIFICATION.json` and site README rows | 25 `VERIFIED`, paths match |
| Topic index | each site `Published topics` count matches its files; root `Published formula topics: 25`; every topic is linked from the root README |
| Secret patterns | no match in tracked text (private key, GitHub token, `x-access-token`, AWS access key id, Stripe live secret) |

An earlier draft of the scanner matched its own token pattern. The pattern is now split in source so the script does not flag itself. The clean run above is the one after that fix.

## GitHub Actions

Workflow file: `.github/workflows/doc-checks.yml`.

It is set to run on `push` and `pull_request`, check out this repo, run `python3 scripts/check-docs.py`, and upload the JSON artifact. It does not commit and it does not edit the eleven product sites (those repos are not in this workspace).

Queried with `gh run view` after the push of `30756538b83a22e9d6c67d508e3ad054f0905a08`:

| Run | Event | Conclusion | Head SHA |
|-----|--------|------------|----------|
| https://github.com/ddcodedog/Calculator/actions/runs/41800933879 | push | success | `30756538b83a22e9d6c67d508e3ad054f0905a08` |
| https://github.com/ddcodedog/Calculator/actions/runs/41800933911 | pull_request | success | `30756538b83a22e9d6c67d508e3ad054f0905a08` |

The push log shows `python3 scripts/check-docs.py` and `failures=0 warnings=0 formulas=25`, with 36 URL results classified `ok` and `urlsSkipped` false. A later commit that only updates this report starts another run. That later run is not the table above.

## Unfinished

- 350 inventory tools have no formula page. Names and IDs are in [FIRST_RELEASE.md](FIRST_RELEASE.md). No filler pages were added.
- External standards are still pending on most topics. ITU, IEEE, and textbook PDFs cited by the product pages were not re-read, except NIST FS 376B for the mechanical horsepower factor.
- This branch is not merged. The commit that records the Actions URLs is newer than `3075653` and is not the run in the table above.

## Later increments

- Add one deferred tool only after its production script is read and one example is recomputed. PoE voltage drop was the shortest closed form left out of batch 1.
- Re-run `python3 scripts/check-docs.py` when a production route changes. The four slash redirects are already accepted by the checker.
- Replace a “pending” standards line only after opening the cited document.

## Status

`PASS`

Local `scripts/check-docs.py` exited 0 with no failures and no warnings. Both GitHub Actions runs on `30756538b83a22e9d6c67d508e3ad054f0905a08` completed with conclusion `success`. Deferred tools and unread standards are unfinished scope, recorded above, and did not fail these checks.
