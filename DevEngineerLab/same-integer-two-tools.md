# One integer, a clock in one tool and hex in the other

## Do not pick a tool by the shape of the digits

`1712345678` can be typed into the timestamp converter and into the integer base converter. Both accept it. They do not describe the same object, and the hex string is not a time zone.

## As a Unix time

Numeric mode, unit seconds. The converter multiplies by 1000 and formats with `toISOString`:

$$
t_{\mathrm{ms}} = 1712345678\times 1000
$$

UTC instant: `2024-04-05T19:34:38.000Z`. Seconds out, truncated toward zero, are the same `1712345678`. The local-time string is deliberately not the result; the note on that tool leaves it out because it is not a property of the instant alone. `abc` is rejected. This input is an integer, so truncation does not move it.

## As a base conversion

The same digits in the base converter are an integer, not an epoch. Hexadecimal spelling of \(1712345678_{10}\) is `6610524e`. That is \(6\times 16^{7} + 6\times 16^{6} + \cdots\), and it is not `2024-04-05`. Pasting `6610524e` back into the timestamp tool is not a numeric timestamp; the timestamp tool’s numeric mode wants a finite number, and a hex letter is not one unless you convert it back to decimal first. The base tool’s job is the digit map. It does not call `Date`.

## What a ticket may say

- “The event time is 2024-04-05T19:34:38.000Z” only after the timestamp tool, unit seconds.
- “The flag word prints as 6610524e” only after the base tool, and only if `1712345678` was actually the flag word and not the epoch. In this note it is the same character sequence used twice on purpose, to show the collision. A real ticket should not use one integer for both roles.

Adding the hex digits to the year, or treating `6610524e` as milliseconds, is not a conversion either tool performs.

## Limits

- No leap-second table. Unix time here is the JavaScript instant.
- Base conversion of a leading-zero string is a digit-syntax question; this input has no leading zero.
- Neither tool stores the ticket.

## Tools

- Instant: https://devengineerlab.com/tools/timestamp-converter
- Hex spelling: https://devengineerlab.com/tools/number-base-converter

## Online Calculator

If the integer is an epoch, use the timestamp page:

https://devengineerlab.com/tools/timestamp-converter

## Related Formulas

- [Unix timestamp conversion](unix-timestamp-conversion.md)
- [Integer base conversion](integer-base-conversion.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Timestamp numeric mode `n × 1000` and `toISOString`; base conversion via the integer value |
| Evidence | Python `datetime` UTC for the instant; Python `hex()` for `6610524e`, matching the digit map the base tool documents |
| Not done | No browser session |
| Dedup scope | Dev category pages list tools; they do not compare these two readings. The 1700000000 example was not reused. Not a web-wide scan |
| Example result | `2024-04-05T19:34:38.000Z` versus hex `6610524e` |
| Date | 2026-11-10 |
| Status | VERIFIED |
