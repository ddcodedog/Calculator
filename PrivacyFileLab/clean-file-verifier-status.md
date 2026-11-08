# When the clean-file verifier allows a download

## Overview

The clean-file verifier scans the before text and the after text in the browser, then runs the same `verifyCleanScans` function version 1.0.0 that the metadata diff uses. The extra behavior on this page is the download: a `verified-cleaned.txt` blob is created only when the status is `VERIFIED`, and the blob is the after text. A failed comparison shows the type lists and does not create that link.

Read from the production verifier chunk on 2026-11-08. The button sets `reopened` and `rescanned` true after both local scans return. This note uses a pair that passes, and a second pair that shows a new low-severity address still passing. No file was uploaded.

## Formula

Type sets and the failure rules are the ones in `verifyCleanScans`:

- not reopened or not rescanned → `VERIFICATION_FAILED`
- any remaining type → `VERIFICATION_FAILED`
- any new finding with severity HIGH or CRITICAL → `VERIFICATION_FAILED`
- otherwise, if `reviewRequired` is set → `REVIEW_REQUIRED`
- otherwise → `VERIFIED`, and the reason text says the output was reopened and rescanned with no residual or new high-risk findings

`IPV4_ADDRESS` is severity LOW in the current ruleset. A new low-severity type is listed under new types and does not trip the high-risk clause. `EMAIL_ADDRESS` is MEDIUM. Both patterns were checked against the strings below.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| before, after | Text areas on the page | characters |
| status | VERIFIED, REVIEW_REQUIRED, or VERIFICATION_FAILED | enum |
| download | Present only for VERIFIED | the after text |

## Engineering Principles

The download gate is the status string, not a second scan. If you need the file only when the email and the phone are both gone, the after text has to produce an empty remaining set and no new high-risk type. A new documentation IP address is a new type and is still LOW, so the status can stay `VERIFIED` while the new-type line is not empty. That is easy to misread as “nothing was found.”

## Worked Example

Before: `Mail ada@example.com or 415-555-0134.`

After: `Mail the desk about the invoice.`

1. Before findings: `EMAIL_ADDRESS`, `US_PHONE_NUMBER`. After findings: none.
2. Removed: both types, sorted. Remaining: none. New: none.
3. Both scans completed, so the flags are true. Status = `VERIFIED`.
4. The page then builds a blob whose contents are the after sentence and offers it as `verified-cleaned.txt`.

Boundary: before `Mail ada@example.com about the invoice.` and after `Reach 203.0.113.10 after the note.` The email type is removed. `203.0.113.10` is a new `IPV4_ADDRESS` at severity LOW. Remaining is empty and the new type is not HIGH or CRITICAL, so status stays `VERIFIED` and a download is still offered. Replacing the after text with a string that still contains `415-555-0134` leaves `US_PHONE_NUMBER` remaining and the status becomes `VERIFICATION_FAILED` with no download.

## Limitations

- The worker scan is local. This check applied the published regexes and the status function; it did not click Verify in a browser.
- HIGH and CRITICAL patterns exist in the ruleset. This example does not include secret material to demonstrate them.
- `VERIFIED` does not mean the after text is appropriate to publish. It means this function’s type rules passed.

## Reference Standards

The status rules are the site’s verifier, version 1.0.0. No external redaction standard was re-read. Status: pending.

## Online Calculator

Run the two sentences on the production verifier:

https://privacyfilelab.com/clean-file-verifier

## Related Formulas

- [Sensitive text pattern redaction](sensitive-text-redaction.md)
- [Local SHA-256 file digest](sha256-file-digest.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PrivacyFileLab clean-file verifier |
| Evidence | Production `verifyCleanScans` 1.0.0 and the download branch that requires status VERIFIED |
| Method | Regex match plus the status function on the pass pair and the LOW IPv4 pair |
| Example result | Pass pair VERIFIED with a download of the after text; a remaining phone fails |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
