# CSV encoding detection

## Overview

The encoding detector labels a CSV as UTF-8 with BOM, UTF-16 LE, UTF-16 BE, UTF-8 without BOM, or unknown. It does not convert the file and it does not name a legacy code page. Bytes that are not valid UTF-8 and do not look like UTF-16 come back as `unknown` with the offset of the first failing byte.

`detectCsvEncoding` in production `encoding-browser.js`, read 2026-11-07. The file comment says it matches `src/core/csv/encoding.ts` (https://datafilelab.com/encoding).

## Formula

The checks run in order:

1. Bytes `EF BB BF` → `utf-8-bom`, confidence high, `hasBom` true.
2. Bytes `FF FE` → `utf-16le`, high, BOM.
3. Bytes `FE FF` → `utf-16be`, high, BOM.
4. Otherwise a UTF-16 guess: length at least 4, and zero bytes on the high side of each pair at least \(\max(2,\lfloor n/8\rfloor)\) times. Little-endian is tested before big-endian.
5. Otherwise strict UTF-8, including a rejection of overlong sequences and surrogates → `utf-8`, confidence medium, no BOM.
6. Otherwise `unknown`, confidence low, with `invalidByteOffset`.

## Variables

| Name | Meaning |
|---|---|
| Input | The file bytes, not a re-encoded string |
| Result fields | `encoding`, `confidence`, `hasBom`, and on failure `invalidByteOffset` |

## Engineering Principles

A BOM is a prefix check, so it wins over the statistical UTF-16 test. UTF-8 without a BOM is reported at medium confidence because any ASCII file is valid UTF-8; the detector is not claiming the file was saved “as UTF-8” by a person, only that the bytes decode. Unknown means “not these four answers,” not “this is Windows-1252.”

## Worked Example

1. Bytes `EF BB BF 61 2C 62 0A` (`a,b` plus a newline, with a UTF-8 BOM) → `utf-8-bom`, high, BOM present.
2. Bytes `61 2C 62 0A 31 2C 32 0A` (`a,b` newline `1,2` newline) → `utf-8`, medium, no BOM.
3. Bytes `FF FE` followed by UTF-16 LE `a` (`61 00`) → `utf-16le`, high, BOM present.

Boundary: a single byte `FF` fails the BOM checks, is too short for the UTF-16 zero test, and is not valid UTF-8, so the result is `unknown` at low confidence with the invalid offset at that byte.

## Limitations

- No Windows-1252, Shift_JIS, or GB18030 label.
- The UTF-16 path without a BOM is a zero-byte heuristic, so short binary can be mislabeled.
- Detection does not transcode. Saving still depends on the export step you choose after the label.

## Reference Standards

The UTF-8 and BOM byte values are the ones in `encoding-browser.js`. Unicode’s encoding specifications were not re-read. Status: pending.
## Online Calculator

Upload the same byte prefixes in the encoding detector:

https://datafilelab.com/encoding

## Related Formulas

- [CSV value frequency counts](csv-value-frequency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DataFileLab encoding detector |
| Evidence | Production `detectCsvEncoding` BOM order, UTF-16 zero test, and strict UTF-8 fallback |
| Method | Applied the function’s branches to the three byte strings and to a lone `FF` |
| Example result | `utf-8-bom`, `utf-8` medium, `utf-16le`; lone `FF` is `unknown` |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
