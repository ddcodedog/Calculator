# A new digest does not clear a phone the diff still sees

Locale: en

## The failure

The metadata diff and the clean-file verifier are the same comparison. They do not hash. The hash page will digest any string you paste, including a string the comparison has already refused. A changed digest is evidence the bytes changed. It is not a `VERIFIED` status.

## Texts

Before:

`Ping nora@example.com about dock 4 at 415-555-0198.`

After:

`Ping the clerk about dock 4 at 415-555-0198.`

The email pattern matches `nora@example.com` and does not match the after text. The US-phone pattern matches `415-555-0198` in both. Types before: `EMAIL_ADDRESS`, `US_PHONE_NUMBER`. Types after: `US_PHONE_NUMBER`.

## Comparison

Reopened true, rescanned true.

- Removed: `EMAIL_ADDRESS`.
- Remaining: `US_PHONE_NUMBER`.
- New: empty.

`VERIFICATION_FAILED`, because a remaining type fails `verifyCleanScans` 1.0.0 even when nothing new appeared. Download stays off. The diff page shows the same failure and still does not produce a file. A new type fails this function only when its severity is HIGH or CRITICAL. A US phone in the published ruleset is not that case, so this note does not pretend a brand-new phone number is what failed. The phone was already in the before text and is still in the after text.

If the rescan flag is false, the function fails even when the after-text is empty of matches. That flag was true here. The failure is the phone that remains, not a skipped scan.

## Digest anyway

SHA-256 of the after-text UTF-8 (44 bytes):

`0b2ccca6e82f74b79793718f858b999c776d04d54380afcb770e3dcd46c3fc7a`

It differs from the digest of `Ping the clerk about dock 4.` You can see the bytes changed. You still do not have a download, and you should not attach this digest to a ticket as “clean.” The hash page never saw the finding list.

## What would be a different check

Removing the phone characters and re-running the comparison could return `VERIFIED`. This note does not do that second edit, because the point is the failed state. Photo GPS and PDF metadata are other guides and other finding types. They were not run.

## Tools

- Comparison that refuses the download: https://privacyfilelab.com/metadata-diff
- Same function under the verifier name: https://privacyfilelab.com/clean-file-verifier
- Digest, which will not repair the status: https://privacyfilelab.com/hash

## Online Calculator

The page that records the failure is the diff:

https://privacyfilelab.com/metadata-diff

## Related Formulas

- [Which sensitive-text types disappeared](metadata-finding-type-diff.md)
- [When the clean-file verifier allows a download](clean-file-verifier-status.md)
- [Local SHA-256 file digest](sha256-file-digest.md)

## Verification

| Item | Value |
|---|---|
| Source tools | `verifyCleanScans` 1.0.0 remaining-type rule; SHA-256 of UTF-8 |
| Evidence | Same US-phone shape as the published `415-555-0134` example, present in both sentences; Python `hashlib.sha256` of the after text |
| Not done | No browser session and no claim that a file was cleaned |
| Dedup scope | Same privacy guides as the companion note; this one is the failed phone case. Not a web-wide scan |
| Example result | `VERIFICATION_FAILED`; digest `0b2ccca6…c3fc7a` is not a pass |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |