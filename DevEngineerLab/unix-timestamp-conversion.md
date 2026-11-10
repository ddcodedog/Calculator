# Unix timestamp conversion

Locale: en

## Direct Answer

The timestamp converter maps a date string to Unix milliseconds and maps a numeric Unix time back to an ISO-8601 UTC string. Local wall time is `Date.toString()`, which follows the browser timezone, so this note records only the UTC fields that stay the same on every machine.


## Overview

The converter is TOOL-007 in the production page script, read 2026-11-07. Date mode uses `new Date(input)`. Numeric mode uses `Number` on the trimmed text (https://devengineerlab.com/tools/timestamp-converter).
## Formula

Date mode, after a valid `Date`:

$$
t_{\mathrm{ms}} = \mathrm{getTime}(), \qquad t_{\mathrm{s}} = \mathrm{trunc}(t_{\mathrm{ms}}/1000), \qquad \mathrm{ISO} = \mathrm{toISOString}()
$$

Numeric mode: if the unit is seconds, \(t_{\mathrm{ms}} = n\times 1000\); if the unit is milliseconds, \(t_{\mathrm{ms}} = n\). Seconds out are again `Math.trunc(t_ms/1000)`. A non-finite number is the error “Timestamp must be numeric.” A date the engine cannot represent is an out-of-range error. An unparseable date string is “Invalid date/time.”

## Variables

| Name | Meaning |
|---|---|
| Mode | `date` or numeric |
| Unit | Seconds or milliseconds, numeric mode only |
| Input | ISO-8601 or another string `Date` accepts, or a trimmed number |

## Engineering Principles

Unix time here is milliseconds since 1970-01-01T00:00:00.000Z, which is what `getTime` returns. Multiplying seconds by 1000 is the whole unit conversion. Truncation toward zero means a negative fractional millisecond does not round away from zero; the examples below are whole seconds, so truncation does not change them. The local string is intentionally left out of the worked result because it is not a property of the instant alone.

## Worked Example

Numeric mode, unit seconds, input `1700000000`.

1. \(t_{\mathrm{ms}} = 1700000000\times 1000 = 1700000000000\).
2. ISO-8601 UTC = `2023-11-14T22:13:20.000Z`.
3. Seconds out = `Math.trunc(1700000000000/1000) = 1700000000`.

The same instant in date mode, input `2023-11-14T22:13:20Z`, returns the same millisecond value and the same ISO string.

Boundary: `abc` in numeric mode is non-finite and is rejected. An empty date string is invalid. A number that cannot be represented as a JavaScript date returns the out-of-range error rather than a wrapped year.

## Limitations

- Leap seconds are not a separate input. `Date` does not add them.
- The local line on screen depends on the browser timezone and should not be copied as the UTC result.
- This does not convert calendar systems other than what `Date.parse` already accepts.

## Reference Standards

The epoch and the ISO string are the behavior of the production `Date` calls. ECMA-262 was not re-read. Status: pending.
## Online Calculator

Enter `1700000000` as seconds:

https://devengineerlab.com/tools/timestamp-converter

## Related Formulas

- [Integer base conversion](integer-base-conversion.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DevEngineerLab TOOL-007 timestamp converter |
| Evidence | Production date and numeric branches: `getTime`, `toISOString`, seconds `× 1000`, `Math.trunc` |
| Method | Converted 1700000000 seconds with the Python UTC calendar and the same integer scaling |
| Example result | `2023-11-14T22:13:20.000Z`, milliseconds 1700000000000 |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |