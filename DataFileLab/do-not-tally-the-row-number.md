# Number the kept rows. Do not frequency-count that new column.

Locale: en

## After the cities are clean

The cleaned shipment file is:

```
sku,city
A1,Lima
B2,Lima
C3,Oslo
```

City frequency is Lima 2, Oslo 1. The next operation is a row number, not another statistic.

## What the numberer writes

Defaults: start 1, header on, header name `row_number`. Record 0 receives the name. Body row \(i\) receives \(1+i-1\).

```
row_number,sku,city
1,A1,Lima
2,B2,Lima
3,C3,Oslo
```

`numberedRows` = 3. The city strings are copied. Lima is still Lima.

## The tally you must not run on column 0

Frequency on column 0, header on, sees `1`, `2`, and `3` once each. Sorted by count, they tie, and first-seen order keeps `1` then `2` then `3`. That output is a list of the numbers the tool just invented. Adding those counts to Lima’s count produces `1+2` or `3+2` depending on which cells you mix, and neither sum is a city. Column index 2 is still the city, and it still says Lima 2, Oslo 1. The new column shifted nothing to the right of `city` because it was inserted on the left; the city index moved from 1 to 2. Using the old index 1 after the insert tallies SKUs (`A1`, `B2`, `C3`) and calls them cities.

## A start value does not encode the city

Start 10 with the header off would number every record, including the words `sku` and `city`. That mode is a different file. It does not mean Lima is city number 10. The frequency tool will not interpret the integers as ranks of Lima.

## Limits

- The numberer does not delete blanks. This file was already cleaned.
- Header name `row_number` is literal. A column that already had that name would sit beside it, not replace it.
- No spreadsheet formula is evaluated.

## Tools

- Numbers: https://datafilelab.com/csv-row-numberer
- Counts, on the city index after the insert: https://datafilelab.com/csv-frequency

## Online Calculator

Insert the column here, then change the frequency index if you still need cities:

https://datafilelab.com/csv-row-numberer

## Related Formulas

- [A leading row-number column](csv-row-number-column.md)
- [CSV value frequency counts](csv-value-frequency.md)

## Verification

| Item | Value |
|---|---|
| Source tools | `numberCsvRows` with start 1 and a header; frequency on a zero-based index |
| Evidence | Both rules applied to the three-record cleaned file. No browser session |
| Dedup scope | No DataFileLab guide chains these two. Single-tool notes use other sample rows. Not a web-wide scan |
| Example result | Numbers 1, 2, 3; city index becomes 2; column 0 is not a city tally |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |