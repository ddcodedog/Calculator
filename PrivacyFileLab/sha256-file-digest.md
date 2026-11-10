# Local SHA-256 file digest

Locale: en

## Direct Answer

The hash tool reads a file in the browser, runs SHA-256 over those bytes, and prints the digest as lowercase hex with no separators. The page states that the file stays in the browser and that the hash is not sent to analytics. This note checks the digest function against known byte strings. It does not claim a particular file was clicked in a browser session.


## Overview

`sha256File` in the production hash chunk, read 2026-11-07, copies the bytes, calls `crypto.subtle.digest("SHA-256")`, and returns `algorithm: SHA-256`, the hex digest, `bytes` equal to `byteLength`, and version `1.0.0` (https://privacyfilelab.com/hash).
## Formula

SHA-256 is the digest named in that call. For an input of \(n\) bytes the tool reports `bytes: n` and a 64-character hex string. There is no salt and no HMAC in this function. The empty input is a defined case: zero bytes still have a digest.

## Variables

| Name | Meaning |
|---|---|
| Input | The file bytes passed to `sha256File` |
| `bytes` | `byteLength` of that copy |
| `hash` | Lowercase hex, 64 characters |

## Engineering Principles

The digest is a function of the bytes, not of the file name. `abc` as UTF-8 is the three bytes `61 62 63`. The same three characters in UTF-16 would be a different digest, and this function does not transcode. Changing one bit changes the digest; the tool does not offer a “close enough” comparison.

## Worked Example

UTF-8 `abc` (3 bytes):

```
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

Empty input (0 bytes):

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Both were computed with Python `hashlib.sha256` on those byte strings, which is the same SHA-256 input the browser call is specified to hash. The tool would report `bytes` 3 and `bytes` 0 respectively.

Boundary: a different length is a different input. The three bytes `abd` do not produce the `abc` digest. The function does not accept a hex string in place of the file; the page hashes the selected bytes.

## Limitations

- SHA-256 identifies bytes. It does not, by itself, prove who created the file or that the file is safe to open.
- No keyed hash. Anyone who has the file can recompute the digest.
- Version `1.0.0` is the field in this chunk, not a statement about collision resistance beyond the algorithm name.

## Reference Standards

FIPS 180-4 defines SHA-256. The PDF was not re-read for this note; the examples are the standard empty-string and `abc` digests, recomputed locally. Status: pending.
## Online Calculator

Select a file on the hash page to run the same browser digest:

https://privacyfilelab.com/hash

## Related Formulas

- [Sensitive text pattern redaction](sensitive-text-redaction.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PrivacyFileLab hash page, `sha256File` |
| Evidence | Production `crypto.subtle.digest("SHA-256")`, lowercase hex, byte length, version 1.0.0 |
| Method | Recomputed SHA-256 of UTF-8 `abc` and of the empty input locally |
| Example result | 64-hex digests above, lengths 3 and 0 |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |