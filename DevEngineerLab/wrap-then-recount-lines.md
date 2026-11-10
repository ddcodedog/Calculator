# Wrap the relay note, then count again

Locale: en

## What should change

`Relay 7 tripped at dawn` is one line, 23 UTF-16 units, five tokens. Word wrap at width 10 should add line breaks and should not invent tokens. The statistics tool is how you check that, on the wrapped output, not on the original sentence.

## Wrap

`TOOL-058`, word mode, width 10. Spaces collapse and ends trim; this sentence has single spaces already. Words and grapheme lengths, ASCII so graphemes equal characters: Relay 5, 7 is 1, tripped 7, at 2, dawn 4.

`Relay` plus a space plus `7` is 7, which fits. `tripped` does not fit on the remainder, so the line flushes. `tripped` plus a space plus `at` is 10, which fits exactly. `dawn` starts the last line.

```
Relay 7
tripped at
dawn
```

Output lines 3, input lines 1, inserted breaks 2, longest line 10 graphemes. Hard mode would cut every 10 graphemes including the spaces and would not be this packing. Width 0 is rejected. A tab would be rejected before any line is emitted.

## Recount

`TOOL-030` on the wrapped string, which is 23 UTF-16 units because the two spaces that used to separate the flushed words became LF characters:

| Counter | Before | After |
|---|---:|---:|
| UTF-16 units | 23 | 23 |
| Lines | 1 | 3 |
| Whitespace code points | 4 | 4 |
| Tokens | 5 | 5 |

Node `Intl.Segmenter` and `TextEncoder` on both strings agree that graphemes and UTF-8 bytes stay 23. The statistics tool calls those same APIs. Lines start at 1 for a non-empty string and increase on each LF that is not the second half of a CRLF. Two LF characters take the line count from 1 to 3. Tokens stay `Relay`, `7`, `tripped`, `at`, `dawn`. The period is absent, so `dawn` is not `dawn.`.

## Judgment

If the recount shows a new token, the wrap output was edited, not merely broken. If the line count stays 1, the width was never applied. A readability score is not in either tool. Pixel width is not in either tool.

## Limits

- ASCII only in this check. A combining mark would make graphemes and UTF-16 diverge; this sentence has none.
- The Segmenter call that confirmed 23 was Node, the same API the page uses, not a click on the site.
- Empty input is 0 lines in the statistics tool and is rejected by wrap (“enter text”).

## Tools

- Wrap: https://devengineerlab.com/tools/text-wrap-calculator
- Recount: https://devengineerlab.com/tools/text-statistics

## Online Calculator

Produce the three lines here, then paste them into statistics:

https://devengineerlab.com/tools/text-wrap-calculator

## Related Formulas

- [Word wrap at a grapheme width](word-wrap-grapheme-width.md)
- [Local counts of code points, graphemes, and lines](local-text-size-counts.md)

## Verification

| Item | Value |
|---|---|
| Source tools | TOOL-058 word packing; TOOL-030 line and token counters |
| Evidence | Python replay of the wrap loop; Node Segmenter and TextEncoder on both strings |
| Dedup scope | Dev sitemap categories are tool lists, not this before/after. The Ada sentence from the wrap note was not reused. Not a web-wide scan |
| Example result | 3 lines, 2 inserted breaks, tokens still 5, length still 23 |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |