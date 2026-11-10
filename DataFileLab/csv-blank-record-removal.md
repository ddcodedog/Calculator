# Dropping CSV records whose cells are all empty

## Overview

The blank-row tool deletes logical CSV records that have no content, and it can keep the first record even when that record is blank because that record is the header. A record counts as blank when every cell is `""`. If you turn on whitespace-only mode, a cell that is only spaces, tabs, or line breaks also counts as empty. Cells that contain text stay byte-for-byte. This is not a statistics routine and it does not impute missing values.

Production `blank-rows.js`, read 2026-11-08. The example uses a comma and unquoted fields so the record split is obvious without re-deriving the quoted-field state machine. Limits in the module are 25 MiB input, 250,000 records, 1,000 columns, and 2,000,000 cells (https://datafilelab.com/csv-blank-rows).

## Formula

Let records be \(r_0, r_1, \ldots\) after the CSV split. With the header option left on, which is the default (`firstRowHeader !== false`):

$$
\mathrm{keep}(r_i) = \begin{cases} \mathrm{true} & i=0 \text{ and a header is kept} \\ \mathrm{every\ cell\ is\ empty} = \mathrm{false} & \text{otherwise} \end{cases}
$$

Returned counts:

$$
\begin{align*}
\mathrm{inputRows} &= \text{record count} \\
\mathrm{bodyRows} &= \mathrm{inputRows} - [i_0 \text{ is a header}] \\
\mathrm{keptRows} &= |\{i : \mathrm{keep}(r_i)\}| \\
\mathrm{removedRows} &= \mathrm{inputRows} - \mathrm{keptRows}
\end{align*}
$$

The output CSV is the kept records serialized again. A header that is itself blank is still kept when the header option is on.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| text | CSV input | characters |
| firstRowHeader | Keep record 0 even if blank | boolean, default true |
| whitespaceOnly | Treat whitespace cells as empty | boolean, default false |
| delimiter | Field separator | character, default comma |

## Engineering Principles

“Blank” is a property of a whole record. A row with one empty cell and one SKU is kept. A row of empty fields between real rows is removed, so the physical blank line in the file is not preserved as a spacer. Header detection is positional: record 0, not a guess from the words in the cells.

## Worked Example

Input, four records, comma separated:

```
sku,qty
,
A1,2
B2,3
```

1. Record 0 is `sku,qty`. It is kept because it is the header.
2. Record 1 is two empty cells. Every cell is `""`, so it is removed.
3. Records `A1,2` and `B2,3` are kept.
4. inputRows = 4, bodyRows = 3, keptRows = 3, removedRows = 1, headerKept = true.

Output:

```
sku,qty
A1,2
B2,3
```

Boundary: the same file with `firstRowHeader` false still removes the empty record, and it would also remove record 0 if that record were empty. A record whose only cell is a space is kept when whitespace-only mode is off, and removed when that mode is on. A non-boolean `whitespaceOnly` throws before the filter.

## Limitations

- Quoted commas, escaped quotes, and multiline cells follow `splitter.js`. This example does not exercise those paths.
- Removing a blank record renumbers nothing. Pair it with the row-number tool only if you want new numbers after the filter.
- The filter does not decide that `NA` or `0` is missing.

## Reference Standards

RFC 4180 is the usual CSV reference. It was not re-read against this splitter. Status: pending.
## Online Calculator

Paste the four-line sample into the production tool:

https://datafilelab.com/csv-blank-rows

## Related Formulas

- [CSV value frequency counts](csv-value-frequency.md)
- [CSV encoding detection](csv-encoding-detection.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DataFileLab blank-row removal |
| Evidence | Production `removeBlankCsvRows`: header kept when `firstRowHeader !== false`, empty means every cell is `""` |
| Method | Applied the keep rule to the four-record sample |
| Example result | kept 3, removed 1, body 3, input 4 |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
