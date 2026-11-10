# GATE8.3 remediation

Developer CI fix only. This is not an approval to merge. PR #14 stays open.

## Git

| Item | Value |
| --- | --- |
| Previous head | `adfadc69d6641a011a759803daea37e56c0e4f65` |
| Fix commit | `6943d09a11543f542cb221ea088db24d856d8e27` |
| `origin/main` | `0952aa2cb4d52e94b7a53777a50087e43b1db2db` (unchanged) |
| History | Append-only |

Fix diff: `scripts/check-docs.py` and `tests/test_doc_checks.py`, 445 insertions, 15 deletions. The deletions are replaced lines in the checker. No formula file, index data file, locale route file, or production site was edited.

## What changed

- G82-001 closed. `website` must match the document directory, the source record, and a site present in `reports/GATE1_TOOL_INVENTORY.json`. `inventoryToolId` must be the inventory `ToolID` for that site and production URL, or null when the URL is absent. It is not accepted as free text and is not compared as if it were `toolId`. A wrong website copied into the source and both indexes still fails because the directory is the independent check.
- G82-002 closed. `standardsEvidence` and `standardsCheckedDate` on the verification index must equal the source record. A non-empty fabricated string or `1900-01-01` fails. This does not re-certify the standard text.
- G82-003 closed in the same summary path. `distinctToolIdStrings`, `inventoryTools`, `publishedInventoryTools`, and `inventoryToolsWithoutTopic` are recomputed from the source records and the inventory file.
- G82-004 closed. The final URL and canonical must share an allowed host alias (apex/www, http/https, default port, trailing slash) and the same path, so the language route is kept. A Chinese canonical that points at the English same-tool URL is `CANONICAL_NOT_LANGUAGE_ROUTE`. A foreign host is `WRONG_CANONICAL`. A missing tag on a VERIFIED row is `NOT_PRESENT`. Conflicting tags are `CONFLICTING_CANONICAL`. Identical duplicate tags warn. Homepage and other-tool canonicals still fail. `config/locale-routes.json` was not edited.
- G82-005 closed. Locale fetches reject the same soft-404 title signals as tool URLs. `check_urls` on a local server no longer counts that Chinese target as a pass.

## Tests

Previous 18 tests still pass with their assertions unchanged. New tests: 6. Total: 24 passed, 0 failed, 0 skipped.

Local `python3 scripts/check-docs.py --skip-urls`: exit 0, failures 0, warnings 0.

Local full `python3 scripts/check-docs.py --json-out /tmp/calculator-v2-gate83-check.json`: exit 0. 117 URL checks, `http5xx=0`, `inconclusive=0`, `localeLivePass=100`, `localeLiveInconclusive=0`, warnings 0. No INCONCLUSIVE URL.

## Actions on the fix SHA

These runs are for `6943d09a11543f542cb221ea088db24d856d8e27`. Older runs are not this proof.

- Push: https://github.com/ddcodedog/Calculator/actions/runs/42836400797 success. `Ran 24 tests` / `OK`. Checker `failures=0 warnings=0 localeLivePass=100 localeLiveInconclusive=0`. Artifact uploaded. `Contents: read`. Weekly job skipped. No deploy job.
- Pull request: https://github.com/ddcodedog/Calculator/actions/runs/42836408946 success, with the same test and checker lines. No deploy job.

This report commit records those runs. It does not change the checker.

## Left unchanged

- Standards `PENDING`: 87
- Calculation `REVIEW_REQUIRED`: 2 beam notes
- Locale `NOT_SUPPORTED`: 38
- Repository Topics: still empty
- Repository Description is already set and was not changed
