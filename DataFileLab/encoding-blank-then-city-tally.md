# Label the bytes, drop the empty record, then tally the city

Locale: en

## Pipeline

Three tools, one file, and the middle step changes the tally. Encoding detection does not count cities. Blank-row removal does not guess an encoding. Frequency counts whatever cells remain.

## Bytes, then text

The file below is ASCII, so it is valid UTF-8. With no `EF BB BF` prefix the detector’s order returns `utf-8`, confidence medium, `hasBom` false. Medium confidence means the bytes decode, not that a person chose a menu labeled UTF-8. A leading `EF BB BF` would have won as `utf-8-bom` at high confidence and would still need to be stripped before you treat the first cell as `sku`. This sample has no BOM. A single `FF` byte would be `unknown` and should stop the pipeline; do not frequency-count an unknown file as if it were text.

```
sku,city
A1,Lima
,
B2,Lima
C3,Oslo
```

## What the blank record does to the tally

Header on, comma, city is column index 1.

If the empty record stays, the body has four rows. `Lima` appears twice, `Oslo` once, and `""` once. The empty record is two empty cells, so `missingCells` stays 0. The empty string is a real bucket.

Blank-row removal, header kept, whitespace-only off, deletes a record only when every cell is `""`. The middle record goes. Kept rows = 4 input records minus 1, header included, so three records remain:

```
sku,city
A1,Lima
B2,Lima
C3,Oslo
```

Frequency on column 1 now returns `Lima,2` then `Oslo,1`. The empty bucket is gone. `Rome` and `rome` would still be different; nothing here case-folds.

## Order is the whole method

Run frequency first and you publish an empty city that the blank-row tool would have deleted. Run blank-row removal first and the tally matches the cities a person can see. Encoding does not belong after the tally: if you transcode only in your head, the frequency tool never saw those bytes.

Row numbers are a later tool. They are not part of this tally. Adding a `row_number` column and then counting column 0 would count the integers, not the cities.

## Limits

- Unquoted commas. A quoted city with a comma inside is a splitter case this file does not contain.
- The detector does not label Windows-1252. Unknown stays unknown.
- Counts are not a mean and not a map.

## Tools

- Bytes: https://datafilelab.com/encoding
- Empty records: https://datafilelab.com/csv-blank-rows
- Tally: https://datafilelab.com/csv-frequency

## Online Calculator

The tally that should match the cleaned file is the frequency page:

https://datafilelab.com/csv-frequency

## Related Formulas

- [CSV encoding detection](csv-encoding-detection.md)
- [Dropping CSV records whose cells are all empty](csv-blank-record-removal.md)
- [CSV value frequency counts](csv-value-frequency.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Encoding check order; blank-row “every cell is empty”; frequency with header skipped |
| Evidence | Rules applied to this four-record ASCII file. No browser session |
| Dedup scope | Data sitemap is tools, not a guide that chains these three. Repo notes cover each tool alone. Not a web-wide scan |
| Example result | `utf-8` medium; 1 record removed; Lima 2, Oslo 1 |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |