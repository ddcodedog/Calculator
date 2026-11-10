# PrivacyFileLab Formula & Technical Topics

[← Back to repository README](../README.md)

## Domain

Published notes cover a local SHA-256 file digest, sensitive-text pattern redaction, the clean-file verifier’s download gate, and which sensitive-text types a metadata diff still sees. Two further notes hash only the text the verifier accepted, and keep a new digest from clearing a phone number the diff still reports. The tools run in the browser on the production site below.

**Production site:** [https://privacyfilelab.com](https://privacyfilelab.com)

## Topic index

Published topics: 6

Checked against the production page, script, or API on 2026-11-07. These are algorithm or input-output notes where the tool is not a physics formula. Status labels are defined in [FORMULA_VERIFICATION.md](../reports/FORMULA_VERIFICATION.md).

| Status | Document | Tool |
|--------|----------|------|
| VERIFIED | [Local SHA-256 file digest](sha256-file-digest.md) | `hash` |
| VERIFIED | [Sensitive text pattern redaction](sensitive-text-redaction.md) | `text-redactor` |
| VERIFIED | [Which sensitive-text types disappeared](metadata-finding-type-diff.md) | `metadata-diff` |
| VERIFIED | [When the clean-file verifier allows a download](clean-file-verifier-status.md) | `clean-file-verifier` |
| VERIFIED | [Hash the text the verifier accepted](hash-only-after-the-verifier.md) | `hash` |
| VERIFIED | [A new digest does not clear a phone the diff still sees](different-digest-failed-diff.md) | `metadata-diff` |

## Online calculators

Each published topic links to its own production tool. This index does not list every tool on the site.

## Contribution

See [CONTRIBUTING.md](../CONTRIBUTING.md). Do not invent formulas, standards, or tool URLs.

## Other domains

The other ten calculator sites have their own indexes:
- [NetEngineerLab](../NetEngineerLab/README.md) — https://netengineerlab.com
- [PCDog](../PCDog/README.md) — https://pcdog.com
- [AIMarkTool](../AIMarkTool/README.md) — https://aimarktool.com
- [PowerEngineerLab](../PowerEngineerLab/README.md) — https://powerengineerlab.com
- [HVACEngineerLab](../HVACEngineerLab/README.md) — https://hvacengineerlab.com
- [DataFileLab](../DataFileLab/README.md) — https://datafilelab.com
- [WaterEngineerLab](../WaterEngineerLab/README.md) — https://waterengineerlab.com
- [StructuralEngineerLab](../StructuralEngineerLab/README.md) — https://structuralengineerlab.com
- [DevEngineerLab](../DevEngineerLab/README.md) — https://devengineerlab.com
- [DIYCalcLab](../DIYCalcLab/README.md) — https://diycalclab.com

Local digests, redaction, and file checks. This index does not reuse another site's tools.
