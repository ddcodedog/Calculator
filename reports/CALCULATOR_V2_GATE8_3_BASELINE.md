# GATE8.3 baseline

Recorded before the GATE8.3 checker edits. Live GitHub was read on 2026-11-10.

- PR #14: https://github.com/ddcodedog/Calculator/pull/14 OPEN, not draft, mergeable, title unchanged
- Branch: `codex/calculator-v2.0-seo-geo-i18n-ci-20261110`
- Head: `adfadc69d6641a011a759803daea37e56c0e4f65`
- `origin/main`: `0952aa2cb4d52e94b7a53777a50087e43b1db2db` (unchanged)
- Work continued from that tip. No rebase, amend, or force-push.

The GATE8.2 reaudit files were read from the runner uploads and were not copied into this repo. At that tip the live checker still exited 0 after these temporary mutations: `website`, `inventoryToolId`, a source-synced wrong website, a non-empty wrong `standardsEvidence`, and a wrong `standardsCheckedDate`. Canonical comparison used the language-stripped path, so a Chinese page canonicalizing to the English URL, a foreign host, a missing tag, or two conflicting tags could pass. A locale-only HTTP 200 page titled "Page not found" could be counted as a language pass.
