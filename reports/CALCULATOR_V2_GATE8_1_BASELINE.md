# GATE8.1 baseline

Recorded before the GATE8.1 code edits. Live GitHub was read on 2026-11-10. Nothing was reset, rebased, or force-pushed.

## Git

- Repository: https://github.com/ddcodedog/Calculator
- `origin/main`: `0952aa2cb4d52e94b7a53777a50087e43b1db2db`
- PR #14: https://github.com/ddcodedog/Calculator/pull/14
- State: OPEN, not draft, mergeable, base `main`
- Head branch: `codex/calculator-v2.0-seo-geo-i18n-ci-20261110`
- Head SHA: `c3ac9672dd581623c2a8bf0af3eec273d3381b77`
- This matches the expected tip. No unexpected commits were on the branch. Work continued from this tip.
- `main` has not moved past `0952aa2`. No rebase was required.
- Worktree at the start of GATE8.1: clean.
- Diff versus `main`: 134 files, 8726 insertions, 326 deletions.
- Commits on the PR, oldest first:
  - `044f7b4a78cde39ca41f7a5a51e6a303252c3869` feat(calculator-v2): improve SEO GEO i18n and documentation CI
  - `3327efa9722720b128548abbbe95cc618404307c` docs: record the passing Calculator V2 Actions run
  - `c3ac9672dd581623c2a8bf0af3eec273d3381b77` docs: list the successful Calculator V2 Actions runs

## Actions already on this tip

These runs are history. They are not the GATE8.1 proof.

- https://github.com/ddcodedog/Calculator/actions/runs/42819970432 push, success, `c3ac967`
- https://github.com/ddcodedog/Calculator/actions/runs/42819984301 pull_request, success, `c3ac967`

## Audit files

`CALCULATOR_V2_GATE8_INDEPENDENT_AUDIT.md` and `.json` were not present on the runner filesystem. The defect list in the GATE8.1 task was re-checked against `scripts/check-docs.py` at `c3ac967`.

## Defects confirmed in the current checker

- G8-001. `FIVE_XX` is only `{500, 502, 503, 504}`. Statuses such as 501, 505, 507, and 599 leave the HTTP-error path as inconclusive after one attempt. The failure class is `hard_5xx`, not `HTTP_SERVER_ERROR`.
- G8-002. `check_indexes` compares the topic file set and a few summary counts. It does not rebuild the expected rows from the formula files plus `reports/FORMULA_VERIFICATION.json`, and it does not require H1, tool id, production URL, companion path, or evidence fields.
- G8-003. Live checks request Online Calculator URLs from the topic files. A `VERIFIED` row in `config/locale-routes.json` is not rechecked for final URL, HTML language, Content-Language, canonical, and tool identity. HTTP 200 can still be stored as `ok`.

## Out of scope, left untouched

Formula topics, Chinese companions, `FORMULA_VERIFICATION.json` conclusions, `llms.txt`, `docs/CITATION.md`, site READMEs, and pull requests #4, #5, #6, and #7.
