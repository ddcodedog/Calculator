# PR 4 revalidation

PR: https://github.com/ddcodedog/Calculator/pull/4

- Title: Add 53 formula topics for six engineering sites
- Head: `cursor/formula-topics-batch2-ff46` at `a6a87ff605a3ba95bd3f892d7ae4d2d525ddb30e`
- State: open. This round did not merge it, close it, or push to it.
- Diff against its base: 65 files. 53 added topic files. 12 modified files (root README, six site READMEs, and five reports).

The 53 added paths are still absent from current `main` (`0952aa2cb4d52e94b7a53777a50087e43b1db2db`). None were copied onto this branch.

## What was read

Every added file was listed from the pull request API and read from `origin/cursor/formula-topics-batch2-ff46`. For each file the check recorded the H1, the `Status` cell, whether display math is present, and the production URL.

Findings:

- All 53 files contain a formula block and a `Status | VERIFIED` row.
- Each file's production URL is in `reports/GATE1_TOOL_INVENTORY.json`. None of those 53 URLs is missing from the inventory.
- One production URL is already used by a topic on main: `https://structuralengineerlab.com/tools/user-defined-utilization-calculator/` is the tool for `StructuralEngineerLab/axial-ratio-beside-moment.md`. PR 4 adds `StructuralEngineerLab/user-defined-utilization.md` for the same URL. That is a second note, not a duplicate path.
- `PowerEngineerLab/rc-time-constant.md` cites OpenStax section 10.5, says the page returned HTTP 200 on 2026-11-04, and says the textbook body was not transcribed. Its own status cell is still VERIFIED. That label is the PR's calculation label. It is not a standards verification from this round.
- Related links inside the PR point at other PR 4 files (for example conductor resistance). Importing one file alone would leave those links broken.
- The 12 modified files overlap reports and READMEs that have changed on main since the PR opened. Merging the PR as it stands would collide with that history.

## What this round did not do

The production engines behind the 53 notes were not re-executed here. Their examples were not recomputed here. Their standards PDFs were not read here. A `VERIFIED` cell inside the PR is therefore not evidence produced by this audit.

## Recommendation

Do not merge PR 4 as a batch.

No file from the PR is imported by this branch. A later, separate review can take a small set only after the engine is read again, the example is recomputed, standards stay pending unless the text is read, and related links are retargeted to notes that already exist. Candidates that are still absent from main and are ordinary closed-form tools, not a second copy of the utilization page, are:

- `NetEngineerLab/pon-splitter-loss.md`
- `NetEngineerLab/poe-voltage-drop.md`
- `NetEngineerLab/ethernet-serialization-delay.md`
- `PowerEngineerLab/rc-time-constant.md`
- `PowerEngineerLab/power-factor-correction.md`
- `WaterEngineerLab/kirpich-time-of-concentration.md`
- `WaterEngineerLab/manning-storm-drain-diameter.md`

Those seven are a review queue, not a verified import. `user-defined-utilization.md` should not be imported as a new tool; main already documents that URL.

PR 5, PR 6, and PR 7 were left open and were not edited. They add promotion plans and DEV.to drafts, not formula topics on main.
