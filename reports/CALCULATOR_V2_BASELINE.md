# Calculator V2 baseline

Recorded before the V2 edits on this branch. The numbers below were read from the remote, not copied from an earlier brief as if they were new results.

## Git

- Remote: `https://github.com/ddcodedog/Calculator`
- `origin/main` after `git fetch origin main`: `0952aa2cb4d52e94b7a53777a50087e43b1db2db`
- Subject: `Merge pull request #13 from ddcodedog/cursor/markdown-seo-geo-590f`
- Author: NetEngineerLab `<netengineerlab@outlook.com>`
- Commit date: 2026-11-10 19:52:36 +0800
- The historical SHA in the execution brief is still HEAD. It had not moved past `0952aa2`.
- Local workspace before fetch was behind, at `e8a8d38aa91657df6ab4e5151a8ad29f5279ae17`. Work uses `origin/main`, not that older checkout.
- Worktree at branch creation: clean.
- Branch created from that main: `codex/calculator-v2.0-seo-geo-i18n-ci-20261110`
- `git ls-remote` for that branch name returned no existing head. It was not reused.

## Eleven site directories

`AIMarkTool`, `DIYCalcLab`, `DataFileLab`, `DevEngineerLab`, `HVACEngineerLab`, `NetEngineerLab`, `PCDog`, `PowerEngineerLab`, `PrivacyFileLab`, `StructuralEngineerLab`, `WaterEngineerLab`.

No twelfth site directory.

## Formula files on that main

| Site | English topics | Chinese companions |
|---|---:|---:|
| AIMarkTool | 6 | 0 |
| DIYCalcLab | 9 | 0 |
| DataFileLab | 6 | 0 |
| DevEngineerLab | 6 | 0 |
| HVACEngineerLab | 5 | 0 |
| NetEngineerLab | 12 | 12 |
| PCDog | 6 | 0 |
| PowerEngineerLab | 15 | 0 |
| PrivacyFileLab | 6 | 0 |
| StructuralEngineerLab | 9 | 0 |
| WaterEngineerLab | 8 | 0 |
| Total | 88 | 12 |

Chinese files, all under `NetEngineerLab/`:

- bandwidth-transfer-time.zh-CN.md
- chromatic-dispersion.zh-CN.md
- cutover-wait-versus-fiber-delay.zh-CN.md
- dns-ttl-cache-window.zh-CN.md
- fiber-link-loss.zh-CN.md
- fiber-propagation-latency.zh-CN.md
- mtu-mss-overhead.zh-CN.md
- on-wire-bytes-at-safe-uplink.zh-CN.md
- optical-power-budget.zh-CN.md
- ospf-interface-cost.zh-CN.md
- stp-path-cost.zh-CN.md
- switch-uplink-safe-capacity.zh-CN.md

## Tool and verification counts on that main

From `reports/GATE1_TOOL_INVENTORY.json`: `totalTools` 375. Sum of `countsByWebsite` is 46+27+32+52+13+12+43+18+25+67+40 = 375.

From `reports/FORMULA_VERIFICATION.json`: 88 topic records, `countVerified` 86, status `REVIEW_REQUIRED` on:

- `StructuralEngineerLab/cantilever-tip-deflection.md`
- `StructuralEngineerLab/simply-supported-midspan-deflection.md`

Unique `(website, toolId)` pairs among the 88 topics: 70. Distinct `toolId` strings: 69, because `TOOL-003` is used by both StructuralEngineerLab and WaterEngineerLab. Eighteen topics share a tool id with another topic on the same site. Those are not 88 tools.

The `standards` field on that JSON is a note, not a separate status. One note records a NIST PDF reading (kilowatt to horsepower). The others say the standard text was not read or that no standard URL was in the engine. The single `status` field does not say that.

## Repository metadata before this round

- Description: `Open engineering calculator formulas, explanations, examples and online tools.`
- Homepage: empty
- Topics: none
- Default branch: `main`

## CI before this round

Workflow: `.github/workflows/doc-checks.yml` on push and pull_request only. Permissions: `contents: read`. Actions: `actions/checkout@v4`, `actions/upload-artifact@v4`.

Latest run on `main`:

- Name: doc checks
- URL: https://github.com/ddcodedog/Calculator/actions/runs/42811032552
- SHA: `0952aa2cb4d52e94b7a53777a50087e43b1db2db`
- Conclusion: success
- Log line: `failures=0 warnings=0 formulas=88`
- The same log warns that Node.js 20 is deprecated and that `actions/checkout@v4` and `actions/upload-artifact@v4` were forced onto Node.js 24.

`scripts/check-docs.py` on that commit checks titles, relative links, math fences on English topics, verification status, topic indexes, secrets, and tool URLs. HTTP 404 and 410 fail. Other HTTP and network results are warnings. Chinese files are excluded from the formula count. Standards status is not a separate field.

## Open pull requests left untouched

| PR | Title | Head | Files |
|---:|---|---|---:|
| 4 | Add 53 formula topics for six engineering sites | `cursor/formula-topics-batch2-ff46` | 65 (53 added, 12 modified) |
| 5 | GATE 1 zero-cost promotion baseline for 11 sites | `cursor/gate1-zero-cost-baseline-a152` | 2 |
| 6 | GATE 0: DEV.to SEO growth plan and 30-day matrix | `cursor/devto-growth-gate0-c93d` | 2 |
| 7 | GATE 1: DEV.to Wave-1 fiber drafts and acceptance scaffolding | `cursor/devto-growth-gate1-3a92` | 6 |

None of these were merged or closed.

## Known issues at baseline

- Calculation status and standards status share one `VERIFIED` label.
- Two structural notes stay `REVIEW_REQUIRED` because the general EI integrator was not line-traced.
- Chinese companions exist only for NetEngineerLab, and the checker does not compare them with English math.
- Locale routes were not recorded as probed HTTP results.
- Actions major tags float and emit the Node.js 20 deprecation warning.

## Forbidden scope for this round

- No edits to the 11 production website source repositories, their content, Cloudflare, DNS, Workers, or GA4.
- No deploy. No merge of this PR. No merge or close of PR 4, 5, 6, 7, or any other open PR.
- No force-push, no reset of unrelated work, no change to `main` except by a later human merge.
- No deletion of historical reports, formulas, or evidence.
- No batch of new formula articles and no mass translation of all 88 topics.
- No invented tool URL, standard number, version, or publication date.
- No claim about ranking, traffic, Search Console, rich results, or AI citations.
- CI must not write product sites, deploy Cloudflare, publish external content, change repository settings other than the description and topics allowed below, or auto-merge.
- Description and topics may be updated. Homepage stays unset unless a real single official entry exists. Other repository settings stay as they are.
