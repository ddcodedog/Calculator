# Integer base conversion

Locale: en

## Direct Answer

The number-base converter reads an integer in one base from 2 through 36 and writes it in another base in that same range. Digits above 9 are letters. The output is lowercase. This is integer notation, not a floating-point format and not a checksum.


## Overview

TOOL-028 in the production page script, read 2026-11-07. The input may be at most 4096 UTF-16 code units, including spaces. The output may be at most 32768 code units (https://devengineerlab.com/tools/number-base-converter).
## Formula

Trim the text. An optional leading `+` or `-` sets the sign. Each next character is a digit:

| Character | Value |
|---|---|
| `0`–`9` | code − 48 |
| `A`–`Z` | code − 55 |
| `a`–`z` | code − 87 |

A digit value greater than or equal to the source base is an invalid digit. The rest is a base-\(b\) place value accumulated with `BigInt`, then `BigInt.toString(targetBase)`, which emits lowercase digits and a leading minus when the value is negative.

## Variables

| Name | Constraint |
|---|---|
| Source base, target base | Integers 2…36 |
| Text | Trimmed integer, optional sign, no fractional point |
| Length | 4096 code units in, 32768 out |


## Constraints

- Source base, target base: Integers 2…36
- Text: Trimmed integer, optional sign, no fractional point
- Length: 4096 code units in, 32768 out

## Engineering Principles

`FF` and `ff` are the same magnitude because both letter cases map onto 10…35. The output does not preserve the input’s letter case. A leading minus is a sign on the integer, not a two’s-complement bit pattern, so converting −10 from base 10 to base 2 yields the characters `-1010`, not a fixed-width binary word.

## Worked Example

1. `FF` from base 16 to base 10: \(15\times 16+15 = 255\). Output `255`.
2. `255` from base 10 to base 16: \(255 = 15\times 16+15\), written `ff`.
3. `-10` from base 10 to base 2: \(10 = 8+2\), so the digits are `1010` and the sign stays. Output `-1010`.
4. `1010` from base 2 to base 10: \(8+2 = 10\).

Boundary: digit `2` in base 2 is rejected because its value is not less than the base. A base of 1 or 37 is rejected before any digit is read. A decimal point is not a digit and fails the character check.

## Limitations

- Integers only. No fractional bits and no scientific notation.
- No fixed width, prefix (`0x`, `0b`), or thousands separator.
- Output length is capped at 32768 code units.

## Reference Standards

Digit values are the ones in the production converter. No numeric-representation standard was re-read. Status: pending.
## Online Calculator

Try `FF` from base 16 to base 10:

https://devengineerlab.com/tools/number-base-converter

## Related Formulas

- [Unix timestamp conversion](unix-timestamp-conversion.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DevEngineerLab TOOL-028 number base converter |
| Evidence | Production digit map, `BigInt` accumulation, and `toString(targetBase)` |
| Method | Recomputed `FF`, `255`, `-10`, and `1010` from those rules |
| Example result | `255`, `ff`, `-1010`, `10` |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |