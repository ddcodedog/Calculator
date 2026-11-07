# CSV value frequency counts

## Overview

The CSV frequency tool counts how many times each exact cell text appears in one column. It does not trim, parse numbers, or fold case. A missing cell and an empty cell are different: a row that is too short increments `missingCells` and still counts an empty value, while a present empty field is only a value.

Counting rules are in production `dist/csv/frequency.js`, read 2026-11-07. The row splitter is a separate module. The example below uses no quotes, so the splitter’s quote rules are not exercised. Limits stated in the UI: 25 MiB, 250000 records, 1000 columns, 2e6 cells, 1e5 distinct values. Bytes must be valid UTF-8. The delimiter is one character and cannot be the quote or a newline.

## Formula

This is a count, not a physical formula. For the selected column index, walk records after the header when “header” is on (the default):

- If the index is past the end of the row, add 1 to `missingCells` and use `""` as the value.
- Otherwise use the cell string unchanged.
- Increment that string’s count. Ties in the output order break by first appearance.
- Sort by count descending.

The download is CSV with the header `value,count`.

## Variables

| Name | Meaning |
|---|---|
| Column index | Zero-based position. Column 1 is the second field. |
| Header | Default on. The first row is not counted. |
| Delimiter | One character, default comma. |

## Engineering Principles

`Rome` and `rome` are two values. `  Rome` with a leading space is a third. A numeric-looking cell stays text, so `01` and `1` do not merge. Sorting by count answers “what dominates this column”; it does not compute a mean or a histogram bin width.

## Worked Example

```
name,city
Ada,Rome
Bo,Rome
Ada,Oslo
Cy,
```

Column index 1, header on.

1. The `name,city` row is skipped.
2. `Rome` is seen first and ends at 2. `Oslo` is 1. The fourth data row has an empty second field, so `""` is 1. `missingCells` stays 0 because the field is present.
3. Output order is `Rome,2`, then `Oslo,1`, then the empty value, because 2 > 1 and the two singles keep first-seen order (`Oslo` before the empty field).

Boundary: a data row `Ada` with no second field increments `missingCells` and also increments the empty-string count. Turning the header off would count `city` as a value. More than 100000 distinct values stops at the stated limit rather than returning a partial vocabulary silently; the UI copy is the limit list above.

## Limitations

- Exact string match. No locale case fold and no numeric binning.
- Quoted fields and embedded delimiters follow `splitter.js`, which was not re-derived in this example.
- A frequency table describes the file you uploaded. It is not a population estimate.

## Reference Standards

No statistics standard is cited in the frequency module. Status: pending.

## Online Calculator

The same four-row file can be counted in the frequency tool:

https://datafilelab.com/csv-frequency

## Related Formulas

- [CSV encoding detection](csv-encoding-detection.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DataFileLab CSV frequency |
| Evidence | Production `dist/csv/frequency.js` exact-string counts, missing-cell rule, and sort |
| Method | Counted the unquoted sample by hand from those rules |
| Example result | Rome 2, Oslo 1, empty 1, missingCells 0 |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
