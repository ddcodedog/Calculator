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

The commit SHA for this acceptance snapshot is written in [FINAL_ACCEPTANCE.json](FINAL_ACCEPTANCE.json) after `git rev-parse HEAD`. If that field is `PENDING_AFTER_COMMIT`, the SHA was not known yet because the commit that adds this file did not exist.

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

No Actions run for this commit had been queried when this paragraph was written. Local exit code 0 is not an Actions result. See the `actions` object in the JSON file; it is updated only after `gh run list` returns a real run.

## Unfinished

- 350 inventory tools have no formula page. Names and IDs are in [FIRST_RELEASE.md](FIRST_RELEASE.md). No filler pages were added.
- External standards are still pending on most topics. ITU, IEEE, and textbook PDFs cited by the product pages were not re-read, except NIST FS 376B for the mechanical horsepower factor.
- GitHub Actions for the commit that contains this file was not yet observed at first write.
- This branch is not merged.

## Later increments

- Add one deferred tool only after its production script is read and one example is recomputed. PoE voltage drop was the shortest closed form left out of batch 1.
- Re-run `python3 scripts/check-docs.py` when a production route changes. The four slash redirects are already accepted by the checker.
- Replace a “pending” standards line only after opening the cited document.

## Status

`PASS_WITH_WARNINGS`

Local doc checks passed with no URL or Markdown failures. The warning is the unobserved Actions run, plus standards text that is still pending. This is not `FAIL` and not `BLOCKED`.
