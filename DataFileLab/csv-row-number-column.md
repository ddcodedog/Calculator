# A leading row-number column

## Overview

The row-number tool inserts one column at the left of every CSV record. With the default header option, the first record receives a header name and the following records receive integers. The number does not come from a value already in the file. Existing cells are copied after the new column.

Production `row-numberer.js`, read 2026-11-08. Default start is 1. Default header name is `row_number`. Start must be a safe integer ≥ 0. The last issued number must not pass `Number.MAX_SAFE_INTEGER`. The header name may be at most 1 Mi characters. Column, cell, and output-size caps match the other CSV tools: 1,000 columns after the insert, 2,000,000 cells, 16 MiB of output characters.

## Formula

For record index \(i\) starting at 0, with a header present:

$$
\mathrm{cell}_0 = \mathrm{headerName}, \qquad \mathrm{number}(i) = \mathrm{start}+i-1 \quad (i\ge 1)
$$

With the header option off, every record is numbered and \(\mathrm{number}(i)=\mathrm{start}+i\). The new cell is placed before the original cells. `numberedRows` is the count of records that received an integer, which excludes the header record when the header option is on.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| text | CSV input | characters |
| start | First integer | safe integer, default 1 |
| headerName | Name written into record 0 | text, default `row_number` |
| firstRowHeader | Record 0 is a header | boolean, default true |

## Engineering Principles

The counter is positional after parsing, so a blank-looking record still receives a number if you did not remove it first. Starting at 10 does not mean “add 10 to an existing id column”; there is no existing id column in this operation. The header name is literal text. It is not translated and it is not checked for collisions with a column you already have.

## Worked Example

```
name,city
Ada,Rome
Bo,Oslo
```

Defaults: start 1, header on, name `row_number`.

1. Record 0 becomes `row_number,name,city`.
2. Record 1 becomes `1,Ada,Rome` because \(1+1-1=1\).
3. Record 2 becomes `2,Bo,Oslo`.
4. recordCount = 3. numberedRows = 2.

Boundary: the same two body rows with the header option off and start 10 numbers every record, so the first output record is `10,name,city` and the next are `11,Ada,Rome` and `12,Bo,Oslo`. Start −1 throws. A start so large that the last row exceeds the safe integer throws before serialization.

## Limitations

- Unquoted commas in this example. Quoted fields follow the shared splitter, which was not re-walked for a multiline cell.
- The new column consumes one of the 1,000 column slots.
- Numbers are decimal text. A delimiter that is itself a digit would be quoted by the length helper; the default comma is not a digit.

## Reference Standards

No external numbering standard is cited in the module. Status: pending.

## Online Calculator

Number the name/city sample on the production page:

https://datafilelab.com/csv-row-numberer

## Related Formulas

- [CSV value frequency counts](csv-value-frequency.md)
- [CSV encoding detection](csv-encoding-detection.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DataFileLab row numberer |
| Evidence | Production `numberCsvRows`: number = start + row − 1 when the first row is a header |
| Method | Applied the map to the three-record sample and to start 10 with the header off |
| Example result | `row_number` plus 1 and 2; alternate path starts at 10 |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
