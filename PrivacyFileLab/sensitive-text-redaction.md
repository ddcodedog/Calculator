# Sensitive text pattern redaction

## Overview

The text redactor scans a string for a fixed ruleset, replaces the ranges you confirm, and scans again. Verification passes only when that second scan finds none of the types you chose and the scan was not truncated. This is pattern replacement in the browser, not a guarantee that every secret in a document is gone.

Rules and the replacement worker were read from the production chunks on 2026-11-07. Ruleset version on the text scanner is `1.0.0`. The default replacement is `[REDACTED]` and it must be non-empty. The worker throws if the replacement itself contains the matched source slice. Overlapping ranges are merged before replacement. A private-key match is expanded to the full begin/end block by the worker’s block regular expression. The worker timeout is 45 seconds (https://privacyfilelab.com/text-redactor).

## Formula

The scan walks a list of regular expressions. The types used in the example below are the ones in that list:

| Type | Pattern behavior |
|---|---|
| `EMAIL_ADDRESS` | Local part, `@`, domain, and a letter TLD. Case-insensitive. |
| `US_PHONE_NUMBER` | Optional leading 1, then a 10-digit North American number. The area and exchange cannot start with 0 or 1. |
| `IPV4_ADDRESS` | Four decimal octets, each 0…255, not glued to a longer digit run. |

Other types in the same list look for private-key banners and for several vendor token shapes. Those patterns are not pasted here. A match stores a character range, a preview, and `removable: true`. Replacement walks the selected ranges from the end of the string so earlier indexes stay valid. Confirm-and-redact sends the selected finding ids. The follow-up verify call sets `expectedAbsentTypes` to the types of those findings.

## Variables

| Name | Meaning |
|---|---|
| Text | The textarea contents |
| Selected ids | Findings to replace. Unselected matches stay. |
| Replacement | Default `[REDACTED]`, must be non-empty and must not contain the matched slice |

## Engineering Principles

Detection is only as wide as the ruleset. An email that does not match the pattern is unchanged. A phone number outside the North American shape is unchanged. Replacing a match with a string that still contains the same digits or the same address fails the worker check on purpose, so the replacement cannot reintroduce the slice it just removed. The verify step is a second scan, not a human review.

## Worked Example

Input:

```
Contact ada@example.com or 415-555-0134 from 203.0.113.10.
```

1. `EMAIL_ADDRESS` matches `ada@example.com`.
2. `US_PHONE_NUMBER` matches `415-555-0134`.
3. `IPV4_ADDRESS` matches `203.0.113.10`. The address is in the documentation range 203.0.113.0/24.
4. The three ranges do not overlap, so merge leaves three spans.
5. Replacing each with `[REDACTED]` yields `Contact [REDACTED] or [REDACTED] from [REDACTED].`
6. A rescan of that result finds none of those three types, which is what verify requires for this selection.

Boundary: replacement text that still contains `ada@example.com` throws. An empty replacement is rejected. A scan that hits the truncation cap cannot verify, because the worker requires the rescan not to be truncated.

## Limitations

- Pattern list only. Names, account numbers without the contextual label, and non-US phone layouts can pass through.
- The English UI shows the engine type string. A short label such as “email” in another locale is a translation, not a different rule.
- A passed verify means the selected types were not found again. It does not mean the text is safe to publish.
- Photo and PDF cleaners on this site are separate scanners. They are not this text ruleset.

## Reference Standards

The expressions were read from the production ruleset. No privacy regulation was re-read, and none is claimed as the source of the patterns. Status: pending.
## Online Calculator

Paste the sample sentence into the text redactor:

https://privacyfilelab.com/text-redactor

## Related Formulas

- [Local SHA-256 file digest](sha256-file-digest.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PrivacyFileLab text redactor |
| Evidence | Production ruleset regular expressions for email, US phone, and IPv4, plus the worker’s merge, non-empty replacement, and rescan verify |
| Method | Applied those three expressions to the sample and walked the replacement |
| Example result | Three matches, replaced by `[REDACTED]`, rescan clear of those types |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
