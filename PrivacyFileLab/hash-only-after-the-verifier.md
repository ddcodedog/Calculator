# Hash the text the verifier accepted

## Order

Redact, then the clean-file check, then a digest of the text that check would let you download. A digest of the before-text does not prove the after-text. A digest by itself does not prove a redaction happened.

## Before and after

Before:

`Ping nora@example.com about dock 4.`

After, which is the file you claim to have saved:

`Ping the clerk about dock 4.`

The redactor’s email pattern matches `nora@example.com`. The phone pattern does not match the after-text. Replacement is the literal phrase you choose; “the clerk” is that phrase. The tool does not claim the sentence still means the same thing.

## Verifier

`verifyCleanScans` 1.0.0, reopened true, rescanned true. Types before: `EMAIL_ADDRESS`. Types after: none.

- Removed: `EMAIL_ADDRESS`.
- Remaining: empty.
- New: empty.

Status `VERIFIED`. A download is allowed, and the blob is the after-text, not the before-text. A LOW new type would not have failed this function. A remaining type would have. This after-text has neither.

## Digest of the download, not of the inbox copy

SHA-256 over the UTF-8 bytes of the after-text (28 bytes):

`31f169f998562b138e91b8c3a86426bb173ccd967610568c31040e890055390a`

SHA-256 of the before-text (35 bytes) is different:

`964e229f170073271c015b90776ccaa2de19921690933ffe42e644b3468a5e03`

Publishing the second digest next to the first file does not show that the email is gone. It shows that you hashed a different string. The hash page does not open the verifier. You have to bring it the string the verifier already accepted.

## What this is not

- Not a scan of a photo, a PDF, or an upload to another service. Those guides on the site are about other files.
- Not a guarantee that “the clerk” hides the person. The email characters are absent from the after-text. That is the claim.
- A matching pair of digests only says the bytes match. It does not re-run the regex.

## Tools

- Replace: https://privacyfilelab.com/text-redactor
- Accept or refuse: https://privacyfilelab.com/clean-file-verifier
- Digest: https://privacyfilelab.com/hash

## Online Calculator

Hash the after-text only after the verifier says `VERIFIED`:

https://privacyfilelab.com/hash

## Related Formulas

- [Sensitive text pattern redaction](sensitive-text-redaction.md)
- [When the clean-file verifier allows a download](clean-file-verifier-status.md)
- [Local SHA-256 file digest](sha256-file-digest.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Email and phone regexes; `verifyCleanScans` 1.0.0; SHA-256 of UTF-8 |
| Evidence | Python `re` on both sentences; Python `hashlib.sha256` of the UTF-8 bytes |
| Not done | No browser session, no file download, no photo or PDF |
| Dedup scope | AI-upload, EXIF, and PDF metadata guides, read 2026-11-10. Not a web-wide scan |
| Example result | `VERIFIED`; after-text digest `31f169f9…055390a` |
| Date | 2026-11-10 |
| Status | VERIFIED |
