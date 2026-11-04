# Kilowatt to mechanical horsepower

## Overview

The kW-to-hp calculator converts a positive power in kilowatts into horsepower. The English page uses an approximate mechanical horsepower. The zh-CN page of the same component uses metric horsepower (PS) and does not apply the mechanical factor.

Production component `KwToHpCalculator` (`BACKLOG-025`, dataset `nist-fs376b-rounded-v1`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/kw-to-hp/.

## Formula

English locale:

$$
\mathrm{hp} \approx \frac{P_{\mathrm{kW}} \times 1000}{745.6999}
$$

zh-CN locale:

$$
\mathrm{PS} = \frac{P_{\mathrm{kW}} \times 1000}{735.49875}
$$

The constants in the bundle are `MECHANICAL_HORSEPOWER_W = 745.6999` and `METRIC_HORSEPOWER_W = 735.49875`. Power must be finite and greater than 0. The result must be finite and positive.

The English assumptions say the published rounded factor is approximate, not exact, and that the tool does not infer whether the kilowatts are electrical input or shaft output.

## Variables

| Symbol | Engine field | Unit |
|---|---|---|
| \(P_{\mathrm{kW}}\) | `powerKw` | kW |
| hp or PS | metric key depends on locale | mechanical hp (approx.) or PS |

## Engineering Principles

One mechanical horsepower in the US customary definition used by NIST is the power of 550 foot pounds-force per second. NIST Federal Standard 376B prints the conversion as 745.699 9 watt per horsepower (section 5.2.13). Dividing watts by that factor recovers horsepower. Metric horsepower is a different unit. Federal Standard 376B section 4.3.3 lists “metric horsepower” among units that shall not be used; the zh-CN UI says PS is not a Chinese legal unit and is only a comparison.

## Worked Example

English page, \(P = 7.5\,\mathrm{kW}\).

$$
\mathrm{hp} = 7500 / 745.6999 = 10.057665288\ldots
$$

Result: **10.05766529… mechanical hp (approx.)**.

Same kilowatts on the zh-CN path:

$$
\mathrm{PS} = 7500 / 735.49875 = 10.19716213\ldots
$$

Boundary: \(P \le 0\) is rejected. The two factors are not interchangeable; a document that quotes this tool must say which locale produced the number.

## Limitations

- No motor efficiency, service factor, or current.
- English output is labeled approximate because 745.6999 is a rounded published factor.
- The tool does not convert electric horsepower at 746 W. NIST lists that as a separate row (“horsepower, electric”).

## Reference Standards

Verified from the PDF, not only from the tool:

- NIST / Fed. Std. 376B, section 5.2.13 Power: “horsepower (550 foot pounds-force per second) → watt, multiply by 745.699 9.” File fetched 2026-11-04 from https://www.nist.gov/system/files/documents/2017/05/09/fs376-b.pdf (the tool’s `https://www.nist.gov/document/fs376-bpdf` link redirects there). Tool metadata `licenseStatus` is `review-required`.
- The same standard, section 4.3.3, says metric horsepower shall not be used. The 735.49875 W factor is in the zh-CN code path only. A standards citation for that exact decimal is **pending**.

## Online Calculator

https://powerengineerlab.com/calculators/kw-to-hp/

Inventory tool ID: `kw-to-hp`.

## Related Formulas

- [AC machine synchronous speed](synchronous-speed.md)
- [Induction-motor slip](induction-motor-slip.md)
- [Sinusoidal power triangle](power-triangle.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `kw-to-hp` (`BACKLOG-025`) |
| Evidence | Bundle constants 745.6999 and 735.49875; NIST FS 376B PDF page for 745.699 9 W |
| Method | `7500/745.6999` and `7500/735.49875` |
| Example result | 10.05766529… mechanical hp for 7.5 kW on the English path |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
