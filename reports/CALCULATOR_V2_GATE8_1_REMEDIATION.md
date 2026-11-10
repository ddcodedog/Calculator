# GATE8.1 remediation

Developer remediation only. This is not an approval to merge.

Verdict: **REMEDIATION_PASS**

Final status: **READY_FOR_INDEPENDENT_REAUDIT**

The three merge-blocking CI gaps are closed, the original 10 unit tests still pass, the new negative tests pass, the local full check passed, and a new push run plus a new pull-request run succeeded on the fix SHA. No out-of-scope file was edited.

## A. Git baseline

| Item | Value |
| --- | --- |
| Old PR head | `c3ac9672dd581623c2a8bf0af3eec273d3381b77` |
| Fix commit | `32c920cea5d81b73b93959f7576b225f1d16f753` |
| `origin/main` | `0952aa2cb4d52e94b7a53777a50087e43b1db2db` (unchanged; no rebase) |
| PR | https://github.com/ddcodedog/Calculator/pull/14 OPEN, not draft |
| Branch | `codex/calculator-v2.0-seo-geo-i18n-ci-20261110` |
| History | Append-only. No amend, force-push, or rebase. |

Commits on the PR before this report, oldest first:

- `044f7b4a78cde39ca41f7a5a51e6a303252c3869` feat(calculator-v2): improve SEO GEO i18n and documentation CI
- `3327efa9722720b128548abbbe95cc618404307c` docs: record the passing Calculator V2 Actions run
- `c3ac9672dd581623c2a8bf0af3eec273d3381b77` docs: list the successful Calculator V2 Actions runs
- `32c920cea5d81b73b93959f7576b225f1d16f753` fix(calculator-v2): close gate8 CI validation gaps

Diff of the fix commit against `c3ac967`: 3 files, 949 insertions, 53 deletions. The 53 deletions are replaced lines inside `scripts/check-docs.py`. No file was deleted.

Files in that commit:

- `scripts/check-docs.py`
- `tests/test_doc_checks.py` (original 10 tests kept; new tests appended)
- `reports/CALCULATOR_V2_GATE8_1_BASELINE.md`

Unexpected edits: none. Formula topics, Chinese companions, `FORMULA_VERIFICATION.json`, `llms.txt`, `docs/CITATION.md`, site READMEs, `indexes/topics.json`, `indexes/verification-index.json`, `config/locale-routes.json`, the workflow, and pull requests #4–#7 were not modified. This report commit adds only the two GATE8.1 remediation files.

Diff of the branch against `main` after the fix commit: 135 files, 9625 insertions, 329 deletions.

## B. G8-001

`is_http_server_error` is true for every integer status from 500 through 599 inclusive. 499 and 600 are outside that range. `fetch_url` still uses three attempts (`--retries` default 3). After those attempts a 5xx result is class `HTTP_SERVER_ERROR`, `summary.http5xx` increments, `failures` increments, and the process exits 1. It is not stored as a warning. 403 and 429 stay `inconclusive` on the first response. DNS, TLS, timeout, and other transport errors retry three times and stay `inconclusive`, with status left unset rather than recorded as HTTP 200.

The tests open a local HTTP server and count hits. Sleep between retries is disabled in the test; the retry loop still runs.

| Status | Requests | Class | Failures | Warnings | Exit | `http5xx` |
| --- | --- | --- | --- | --- | --- | --- |
| 499 | 1 | inconclusive | 0 | 1 | 0 | 0 |
| 500, 501, 502, 503, 504, 505, 507, 599 | 3 each | HTTP_SERVER_ERROR | 1 | 0 | 1 | 1 |
| 600 | 1 | inconclusive | 0 | 1 | 0 | 0 |
| 403 | 1 | inconclusive | 0 | 1 | 0 | 0 |
| 429 | 1 | inconclusive | 0 | 1 | 0 | 0 |

Transport error to `127.0.0.1:9`: 3 attempts, status `null`, final URL `null`, class `inconclusive`, failures 0, warnings 1, exit 0.

## C. G8-002

`audit_indexes` rebuilds the expected baseline from English formula files, Chinese companions, and `reports/FORMULA_VERIFICATION.json`. It does not treat `indexes/topics.json` and `indexes/verification-index.json` as proof of each other. It checks counts, unique document keys, empty keys, duplicate keys, real paths, H1 title, companion path, and `toolId` / `productionUrl` / `calculationStatus` / `standardsStatus` against the source record. A calculation `VERIFIED` row must have `sourceEvidence` or `exampleResult`. A standards `VERIFIED` row must have `standardsEvidence` and `standardsCheckedDate`. Summary totals are counted from the current files. Chinese companions are not English topics. The two index files were not rewritten. No verification conclusion was changed. Index agreement is consistency with the source records, not a new standards certification.

Negative tests copy a one-topic tree into a temporary directory. The candidate index files in the repo are not modified. Each mutation makes `audit_indexes` fail:

- empty `verification-index.json` topics
- formula row deleted from `FORMULA_VERIFICATION.json`
- document row whose file does not exist
- duplicate document key
- tampered title, `productionUrl`, `toolId`, `standardsStatus`, `calculationStatus`
- evidence fields removed from the source record and the verification index
- companion path pointing at a missing file
- summary counts that disagree with the files

The untouched fixture passes. The real repository indexes also pass `audit_indexes`.

## D. G8-003

`plan_locale_checks` reads `config/locale-routes.json`. Expected language is `englishPageLanguage` or `chinesePageLanguage` on that row. Every `VERIFIED` row contributes an English target and a Chinese target. Requests are deduplicated by URL, and every row stays attached. A shared tool URL is not a duplicate-record error. `NOT_SUPPORTED` rows are not fetched, not treated as published Chinese pages, and not included in the verified totals. No production page was added. `config/locale-routes.json` was not edited; the expected-language fields were already present.

For each fetched VERIFIED URL the checker requires the HTTP status, final URL, HTML `lang`, `Content-Language` when the header is present, canonical when the tag is present, and tool identity. HTTP 200 alone is not a pass. Redirects to `/`, `/zh/`, or `/zh-CN/` are `LOCALIZED_HOMEPAGE_FALLBACK`. A redirect to another tool is `WRONG_TOOL`. A canonical that points at a homepage or a different tool is `WRONG_CANONICAL`. HTML language that does not match the row is `WRONG_LANGUAGE`.

Local server results (hit count is the request to the original path):

| Case | Requests | Final path | Language | Tool identity | Status | Class | Exit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| zh-CN tool page | 1 | `/zh-CN/tools/sample` | zh-CN | `tools/sample` | 200 | ok | 0 |
| Chinese URL, lang=en | 1 | `/zh-CN/tools/english-body` | en | `tools/english-body` | 200 | WRONG_LANGUAGE | 1 |
| English URL, lang=zh-CN | 1 | `/tools/sample` | zh-CN | `tools/sample` | 200 | WRONG_LANGUAGE | 1 |
| Redirect to `/zh/` | 1 | `/zh/` | zh-CN | empty | 200 | LOCALIZED_HOMEPAGE_FALLBACK | 1 |
| Redirect to `/zh-CN/` | 1 | `/zh-CN/` | zh-CN | empty | 200 | LOCALIZED_HOMEPAGE_FALLBACK | 1 |
| Redirect to `/` | 1 | `/` | en | empty | 200 | LOCALIZED_HOMEPAGE_FALLBACK | 1 |
| Redirect to another tool | 1 | `/tools/other/` | zh-CN | `tools/other` | 200 | WRONG_TOOL | 1 |
| Canonical is `/` | 1 | `/zh-CN/tools/bad-canonical` | zh-CN | `tools/bad-canonical` | 200 | WRONG_CANONICAL | 1 |
| 404 | 1 | `/missing` | en | `missing` | 404 | hard_404 | 1 |
| 410 | 1 | `/gone` | en | `gone` | 410 | hard_404 | 1 |
| 500, 501, 502, 503, 504, 505, 507, 599 | 3 each | same path | zh-CN | that path | that status | HTTP_SERVER_ERROR | 1 |
| 403 and 429 | 1 | same path | en | that path | 403 or 429 | inconclusive | 0 |

Live plan from the current config, computed rather than hard-coded: 50 VERIFIED rows, 100 targets, 77 unique URLs, 38 NOT_SUPPORTED rows. Twenty-three unique URLs are shared by two documents that name the same tool. Both documents are still judged. NOT_SUPPORTED URLs are absent from the unique-URL list.

## E. Regression and Actions

Original unit tests: 10, all present, none skipped, none marked expected-failure. New test methods: 8. Total: 18 passed, 0 failed, 0 skipped.

Local commands:

- `python3 -m unittest tests.test_doc_checks` — Ran 18 tests, OK (about 1.6s).
- `python3 scripts/check-docs.py --skip-urls` — exit 0. `failures=0 warnings=0 formulas=88 chinese=12 localeRows=50 localeUniqueUrls=77 localeNotSupported=38 localeLivePass=0 localeLiveInconclusive=0`.
- `python3 scripts/check-docs.py --json-out /tmp/calculator-v2-gate81-check.json` — exit 0. 117 URL checks, every one HTTP 200 on the first attempt, class `ok`. `http404Or410=0`, `http5xx=0`, `inconclusive=0`. Locale judgments: 100 `ok` (50 English and 50 Chinese). `localeLiveInconclusive=0`. No INCONCLUSIVE URL to disclose. Those 100 passes are the live judgments; the 38 NOT_SUPPORTED rows are not in that pass count.

Actions on the fix SHA `32c920cea5d81b73b93959f7576b225f1d16f753`, not the older green runs:

- Push: https://github.com/ddcodedog/Calculator/actions/runs/42829219740 success. Unit tests `Ran 18 tests` / `OK`. Checker `failures=0 warnings=0 formulas=88 chinese=12 localeRows=50 localeUniqueUrls=77 localeNotSupported=38 localeLivePass=100 localeLiveInconclusive=0`. Artifact `doc-check-report` uploaded. Weekly standards job skipped, which is expected for a push. Token permission `Contents: read`. No deploy job.
- Pull request: https://github.com/ddcodedog/Calculator/actions/runs/42829232131 success, with the same test and checker lines. Artifact uploaded. Weekly job skipped. No deploy job.

This report file is committed after those two runs. Its own Actions run is a later head and is not cited here as the fix proof.

## F. Leftover risks, unchanged

These were not part of GATE8.1 and are not solved:

- Standards `PENDING`: 87.
- Calculation `REVIEW_REQUIRED`: 2 (cantilever tip deflection and simply-supported midspan deflection).
- Repository description and topics are still unset. The earlier settings API call returned HTTP 403.

No merge, no deploy, and no second pull request.
