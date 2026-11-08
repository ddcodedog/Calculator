# Local counts of code points, graphemes, and lines

## Overview

The text-statistics tool reports several sizes of one string: UTF-16 length, Unicode code points, grapheme clusters, UTF-8 bytes, line breaks, whitespace code points, and whitespace-separated tokens. It does not score readability and it does not send the text to a server. The production handler is `TOOL-030` in the DevEngineerLab page bundle, read 2026-11-08.

The input limit is 262,144 UTF-16 code units. Unpaired surrogates are rejected. An empty string reports 0 lines because the line counter starts at 1 only when the string is non-empty.

## Formula

- `utf16CodeUnits` is `string.length`.
- `unicodeCodePoints` counts one step per code point in a `for...of` loop.
- `graphemeClusters` counts segments from `Intl.Segmenter` with granularity `grapheme`.
- `utf8Bytes` is `TextEncoder.encode(text).length`.
- Lines start at 1 for a non-empty string and increase by one on each CR, and on each LF that is not the second half of a CRLF. A trailing break counts as an extra line. Empty input stays at 0.
- `whitespaceCodePoints` counts code points that match JavaScript `\s`.
- `whitespaceTokens` counts runs of non-whitespace code points.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| text | The whole input | Unicode text |
| lines | Break count as defined above | count |
| tokens | Non-whitespace runs | count |

## Engineering Principles

For a string that is only ASCII, code points, UTF-16 units, UTF-8 bytes, and graphemes are the same number. That equality is a property of this particular string, not a general rule. A line count that follows CRLF as one break will disagree with a counter that increments on every `\n` and every `\r`. Tokens treat `crates.` as one token because the period is not whitespace.

## Worked Example

```
Ada shipped 4 crates.
Bo shipped 7.
```

The newline is a single LF. There is no trailing newline.

1. UTF-16 length = 35. Node `for...of` code points = 35. `TextEncoder` UTF-8 length = 35.
2. Node `Intl.Segmenter` grapheme count = 35. The tool calls that same API.
3. Lines: start at 1, one LF, result 2.
4. Whitespace code points: three spaces in the first line, the LF, and two spaces in the second line, total 6.
5. Tokens: `Ada`, `shipped`, `4`, `crates.`, `Bo`, `shipped`, `7.`, total 7. The period stays on `crates.` and on `7.`.

An empty string returns lines 0 and every other count 0. A string that ends with an extra LF reports one more line than the number of text rows you see. An unpaired surrogate is rejected and produces no counts.

## Limitations

- `\s` is the JavaScript definition, including the LF in this example.
- Grapheme segmentation uses the runtime Segmenter. This ASCII check was run in Node, not by clicking the page.
- No word-language stemming. `4` is a token.

## Reference Standards

Unicode grapheme segmentation and UTF-8 are the relevant standards. The specification text was not re-read. Status: pending.

## Online Calculator

Paste the two-line note into the production tool:

https://devengineerlab.com/tools/text-statistics

## Related Formulas

- [Integer base conversion](integer-base-conversion.md)
- [Unix timestamp conversion](unix-timestamp-conversion.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DevEngineerLab `TOOL-030` |
| Evidence | Production counters for UTF-16, code points, Segmenter graphemes, TextEncoder bytes, CRLF-aware lines, `\s`, and non-whitespace runs |
| Method | Manual count plus Node Segmenter and TextEncoder on the 35-unit string |
| Example result | 35, 35, 35, 35, lines 2, whitespace 6, tokens 7 |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
