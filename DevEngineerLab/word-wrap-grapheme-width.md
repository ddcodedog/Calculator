# Word wrap at a grapheme width

## Overview

The text-wrap tool breaks a string into lines whose grapheme width you choose. Word mode, the default, collapses runs of spaces, trims the ends of each input line, and keeps words together until a word itself is longer than the width. Hard mode keeps the original spaces and cuts every width graphemes. Neither mode measures pixels or font advances.

Production `TOOL-058` in the DevEngineerLab page bundle, read 2026-11-08. Width is an integer from 1 to 1,000, default 80. Input is at most 262,144 UTF-16 units and 20,000 lines. Output is at most 50,000 lines and 300,000 UTF-16 units. Unpaired surrogates, tabs, other C0/C1 controls, and a listed set of bidi and line-separator code points are rejected. The example is ASCII, so each grapheme is one code unit. Node’s `Intl.Segmenter` with grapheme granularity counted 29 graphemes in the sentence, matching its length. That is the same API the tool calls; this was not a click-through in a browser (https://devengineerlab.com/tools/text-wrap-calculator).

## Formula

Input lines split on CRLF, CR, or LF and are joined back with LF. In word mode, each line’s spaces collapse to one space and the ends are trimmed. Graphemes come from `Intl.Segmenter`. A word is a run of non-space graphemes. If the current line already holds \(d\) graphemes and \(d+1+t \le W\) for a word of \(t\) graphemes, the tool appends one space and then the word. If the line is non-empty and the word does not fit, it flushes the line first. A word longer than \(W\) is split: whenever \(d=W\), the line flushes before the next grapheme. Inserted breaks are output lines minus input lines. The longest line is the maximum grapheme count of an output line.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| text | Source | Unicode text |
| width | Line capacity | graphemes |
| mode | `word` or `hard` | enum |

## Engineering Principles

The width is a grapheme budget, not a column of a particular font. A flag emoji or a combining sequence can be one grapheme and several UTF-16 units; this ASCII sentence does not contain those. Word mode’s collapse means two spaces between words become one before packing. Hard mode does not do that, so the same sentence produces different lines.

## Worked Example

Sentence `Ada shipped four crates today`, word mode, width 12. One input line.

1. Words and grapheme lengths: Ada 3, shipped 7, four 4, crates 6, today 5.
2. `Ada` plus a space plus `shipped` is 11, which fits. `four` would make 16, so the line flushes.
3. `four` plus a space plus `crates` is 11. `today` does not fit, so it starts the last line.
4. Output lines are `Ada shipped`, `four crates`, and `today`. Inserted breaks = \(3-1 = 2\). Longest line = 11 graphemes.

Hard mode on the same sentence keeps spaces and cuts at 12: `Ada shipped ` (12, including the space), `four crates ` (12), `today` (5). Inserted breaks are again 2, and the longest line is 12. A width of 0 is rejected. A tab in the sentence is rejected before wrapping.

## Limitations

- No font, no CSS `ch`, no CJK width table.
- Segmenter locale is the runtime default. The ASCII result does not depend on locale-specific tailorings.
- The reported longest line is graphemes after wrapping, not the longest input word.

## Reference Standards

Unicode Standard Annex #29 describes grapheme clusters. The annex was not re-read. Status: pending.
## Online Calculator

Wrap the Ada sentence at width 12 on the production tool:

https://devengineerlab.com/tools/text-wrap-calculator

## Related Formulas

- [Unix timestamp conversion](unix-timestamp-conversion.md)
- [Integer base conversion](integer-base-conversion.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DevEngineerLab `TOOL-058` |
| Evidence | Production word-mode pack and hard-mode cut in the page bundle |
| Method | Python replay of the word loop; Node `Intl.Segmenter` counted 29 graphemes |
| Example result | Three word-mode lines, 2 inserted breaks, longest line 11 |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
