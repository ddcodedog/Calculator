# Which sensitive-text types disappeared

## Overview

Metadata diff scans a before string and an after string with the local text rules, then classifies finding types as removed, remaining, or new. The page does not offer a download. Ranking is by type, not by how many times a type matched. A phone number that survives in the after string fails the comparison even if the email address is gone.

The compare button calls `diffMetadata`, which calls `verifyCleanScans` version 1.0.0, read from the production chunks on 2026-11-08. The same function is also used by the clean-file verifier. This note covers the diff page and a case that fails. The ruleset chunk `3fwb4spx8jiw7.js` still supplies `EMAIL_ADDRESS` (severity MEDIUM) and `US_PHONE_NUMBER` (severity MEDIUM). The example addresses are documentation values, and the regexes were applied locally to confirm they match.

## Formula

Let \(B\) be the set of finding types in the before scan and \(A\) the set in the after scan.

$$
\mathrm{removed} = \mathrm{sort}(B\setminus A), \qquad \mathrm{remaining} = \mathrm{sort}(A\cap B), \qquad \mathrm{new} = \mathrm{sort}(A\setminus B)
$$

Counts are the number of findings, not the number of types. The diff page always passes `reopened` and `rescanned` as true after both scans finish. Status becomes `VERIFICATION_FAILED` when either flag is false, when any type remains, or when a new finding has severity HIGH or CRITICAL. A new LOW or MEDIUM type does not, by itself, fail the status. The failed status is still what this example hits, because a type remains.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| before, after | Two texts | characters |
| removedTypes | Types only in the before scan | type ids |
| remainingTypes | Types in both scans | type ids |
| newTypes | Types only in the after scan | type ids |
| beforeCount, afterCount | Finding rows | count |

## Engineering Principles

One remaining phone number is enough to fail, because the remaining set is non-empty. The email match disappearing does not offset that. Severity matters for new types, and it does not excuse a remaining type: the remaining check runs before the severity check and does not look at MEDIUM versus HIGH.

## Worked Example

Before: `Mail ada@example.com or 415-555-0134.`

After: `Mail the desk or 415-555-0134.`

1. The email regex matches `ada@example.com` only in the before string. The US-phone regex matches `415-555-0134` in both.
2. Removed types: `EMAIL_ADDRESS`. Remaining types: `US_PHONE_NUMBER`. New types: none.
3. beforeCount = 2. afterCount = 1.
4. Status = `VERIFICATION_FAILED`, with the reason that findings remain (`US_PHONE_NUMBER`).

Clearing the phone as well, so the after string is `Mail the desk about the invoice.`, leaves both remaining and new empty. With both scans marked reopened and rescanned, that second pair is `VERIFIED`. The diff page still does not create a download for it.

## Limitations

- Text rules only. Image GPS and PDF metadata types exist in the broader ruleset and are not what this textarea path scans.
- A type that matched twice is one entry in the type list. The count fields are what show the repeats.
- `VERIFIED` here means the type sets passed this function. It does not mean a person reviewed the file.

## Reference Standards

The ruleset is the site’s own pattern list. No external identifier standard was re-read. Status: pending.

## Online Calculator

Compare the two mail sentences on the production diff page:

https://privacyfilelab.com/metadata-diff

## Related Formulas

- [Sensitive text pattern redaction](sensitive-text-redaction.md)
- [Local SHA-256 file digest](sha256-file-digest.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PrivacyFileLab metadata diff |
| Evidence | Production `diffMetadata` → `verifyCleanScans` 1.0.0; email and US-phone regexes matched the sample |
| Method | Set difference on the finding types those regexes emit |
| Example result | Removed EMAIL_ADDRESS, remaining US_PHONE_NUMBER, status VERIFICATION_FAILED |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
