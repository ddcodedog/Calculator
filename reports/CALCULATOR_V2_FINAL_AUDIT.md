# Calculator V2 final audit

Verdict: **READY_FOR_HUMAN_REVIEW**

This is not a clean PASS. Standards status is still pending for 87 topics, two beam calculations stay `REVIEW_REQUIRED`, Chinese topic files exist only for NetEngineerLab, and the GitHub description and topics could not be written with this token.

Baseline: `0952aa2cb4d52e94b7a53777a50087e43b1db2db`. Counts below are the same numbers as `indexes/topics.json`, `indexes/verification-index.json`, `config/locale-routes.json`, and `reports/FORMULA_VERIFICATION.json`.

## A. SEO

- Root README is the hub: eleven domain rows, per-site topic lists, search index, English and Chinese entries, verification method, standards notes, calculator use, citation, contribution, and a changelog.
- Each site README links the other ten indexes.
- Twelve NetEngineerLab topics open with a direct answer that names the real question (power budget, STP path cost, DNS TTL, and the rest of that set). Titles and paths were kept.
- No homepage was set. There is no single official URL that represents all eleven sites.
- Description and topics were not changed. `PATCH /repos/ddcodedog/Calculator` returned HTTP 403, `Resource not accessible by integration`. Suggested description, for a person who can edit repository settings: `Engineering formula library for 11 specialized calculator websites. Verified calculations, worked examples, technical references, and multilingual engineering documentation.`
- Suggested topics: `engineering-formulas`, `engineering-calculators`, `network-engineering`, `electrical-engineering`, `hvac`, `water-engineering`, `structural-engineering`, `diy-calculators`, `data-analysis`, `worked-examples`, `technical-documentation`.

## B. GEO

- Notes that already had an overview now lead with a direct answer. Where the variables table had a constraint column, that column is repeated as constraints. Where a worked example had a `Steps:` block, those steps are a calculation-steps section. Empty sections were not added.
- `llms.txt` maps the eleven domains, the languages, and the limits. It does not claim search or answer-engine inclusion.
- `docs/CITATION.md` is the citation form.
- `indexes/topics.json` and `indexes/verification-index.json` are the machine-readable indexes.
- Tool links checked on this branch returned the tool page, not the site homepage.

## C. i18n

- Locale matrix: `reports/LOCALE_ROUTE_MATRIX.md` and `config/locale-routes.json`, probed 2026-11-10.
- Route status: 50 VERIFIED, 38 NOT_SUPPORTED, 0 MISSING, 0 REDIRECTED, 0 INCONCLUSIVE.
- VERIFIED means the Chinese production URL returned HTTP 200 with `zh-CN` (or `zh`) and did not land on the homepage. NetEngineerLab uses `/tools/<slug>/zh/`. AIMarkTool, HVACEngineerLab, PCDog, PowerEngineerLab, and PrivacyFileLab use the `/zh-CN/` prefix advertised by hreflang.
- NOT_SUPPORTED is DIYCalcLab, WaterEngineerLab, StructuralEngineerLab, DataFileLab, and DevEngineerLab: the English page did not advertise a Chinese alternate, and the `/zh` suffix returned 404.
- Chinese topic files: 12, all NetEngineerLab. The other verified Chinese pages have no companion note. That was a scope stop, not a claim that the pages are missing.
- STP: `/tools/stp-path-cost-calculator/zh/` is HTTP 200, language `zh-CN`, canonical is that URL. `/zh-CN/tools/stp-path-cost-calculator/` and `/tools/stp-path-cost-calculator/zh-CN/` are HTTP 404.
- Some hreflang tags also advertise `es`, and the NetEngineerLab `es` URLs that were fetched returned HTTP 200. No Spanish topic files were added.
- English and Chinese display math matches. `reports/ZH_FORMULA_REVIEW.json` is empty.

## D. Bug and CI

- `scripts/check-docs.py` still rejects duplicate H1s, broken relative links, a mismatched `Status` cell, a wrong topic count, and tool-page 404/410.
- It now checks Chinese files with the same math-fence rules, English/Chinese pairing, locale markers, table shape, and the separate standards status.
- Tool URL classes: 404/410 fail, persistent 5xx fail, homepage and error-page landings fail, wrong language on a `/zh/` URL fails, 403/429 and network errors are INCONCLUSIVE.
- Local live run on this branch: 88 URL checks, 77 tool and 11 domain, class `ok` for all, failures 0, warnings 0, English formulas 88, Chinese formulas 12.
- Workflow triggers: push, pull_request, workflow_dispatch, and Monday 06:00 UTC for external standards URLs. Standards fetches do not fail the run and do not replace official links.
- Actions are pinned: `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1, `using: node24`) and `actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9` (v7.0.2, `using: node24`).
- The workflow does not deploy, write product sites, or merge.

## E. Engineering quality

| Quantity | Value | Source |
|---|---:|---|
| Inventory tools | 375 | `reports/GATE1_TOOL_INVENTORY.json` `totalTools` |
| Published formula topics | 88 | English topic files, `indexes/topics.json` |
| Unique site-tool pairs | 70 | `(website, toolId)` in the verification file |
| Distinct tool-id strings | 69 | `toolId` strings; `TOOL-003` is used on two sites |
| Inventory URLs with a topic | 62 | exact production URL match |
| Inventory rows without an exact topic URL | 313 | 375 − 62 |
| Reviewed topics | 88 | every English topic has a verification row |
| Calculation VERIFIED | 86 | `calculationStatus` |
| Calculation REVIEW_REQUIRED | 2 | cantilever tip and simple-span midspan point load |
| Chinese editions | 12 | `*.zh-CN.md` |
| Standards VERIFIED | 1 | Fed. Std. 376B mechanical horsepower factor, read 2026-11-10 |
| Standards PENDING | 87 | not marked verified from an unread link |
| Standards NOT_APPLICABLE | 0 | |
| New formula topics in this branch | 0 | |

Five topic URLs returned HTTP 200 in the live check and are not exact keys in the 2026-11-04 inventory file: `datafilelab.com/csv-frequency`, `datafilelab.com/encoding`, `datafilelab.com/csv-blank-rows`, `aimarktool.com/tools/funnel-conversion-calculator`, and `aimarktool.com/tools/ab-test-sample-size-calculator`. They are published topics. They are not counted inside the 62.

The two structural notes were recomputed again (40 kN·m and 0.133333 m; 33.75 mm). The general integrator was not line-traced, so they stay `REVIEW_REQUIRED`.

No PR 4 file was imported. PR 4, 5, 6, and 7 were not merged or closed.

## F. Git evidence

- Branch: `codex/calculator-v2.0-seo-geo-i18n-ci-20261110`
- Base: `0952aa2cb4d52e94b7a53777a50087e43b1db2db`
- Local URL check: failures 0, warnings 0, formulas 88, chinese 12, tool URL checks 88, 404/410 0, 5xx 0, inconclusive 0
- GitHub Actions push run: https://github.com/ddcodedog/Calculator/actions/runs/42819636911 — success, `failures=0 warnings=0 formulas=88 chinese=12`
- Unit tests: `python3 -m unittest tests.test_doc_checks` — 9 tests, OK
- Rollback: close the pull request without merging. `main` stays at the baseline SHA.

## Pass criteria

| # | Criterion | Result |
|---:|---|---|
| 1 | Existing docs retained | Yes. No topic file deleted. |
| 2 | No production-site edits | Yes. This repository only. |
| 3 | English and Chinese math checks | Yes. |
| 4 | Language pairing is traceable | Yes. Review list is empty because the blocks match. |
| 5 | New tool links checked | The Chinese URLs already in the NetEngineerLab companions were fetched. No new topic URL was added. |
| 6 | New 404/410 | 0 on the URLs this checker requests. |
| 7 | No test regression | Existing status, count, and link checks still fail the run when broken. |
| 8 | Actions run | Push run https://github.com/ddcodedog/Calculator/actions/runs/42819636911 on `044f7b4a78cde39ca41f7a5a51e6a303252c3869` succeeded. Log: `failures=0 warnings=0 formulas=88 chinese=12`. |
| 9 | New formulas have evidence | None were added. |
| 10 | Standards statuses are truthful | 1 verified, 87 pending. |
| 11 | Counts recomputable | Yes, from the JSON indexes. |
| 12 | No assertion deleted | Checks were added. |
| 13 | No other site source mixed in | Yes. |
| 14 | No auto-merge or deploy | Yes. |
