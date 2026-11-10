# Chromatic dispersion coefficient D(λ)

Simplified Chinese edition: [色度色散系数 D(λ)](chromatic-dispersion.zh-CN.md).

## Overview

The Chromatic Dispersion Calculator evaluates the G.652-style dispersion coefficient, or a manually entered coefficient, then accumulates it over length, subtracts compensation, and compares the residual with a tolerance. It also reports a length window and a spectral-width pulse-broadening term.

Engine: `https://netengineerlab.com/tools/chromatic-dispersion-calculator/js/engine.js` (`NELChromaticDispersionEngine`), fetched 2026-11-04.

## Formula

Model mode:

$$
D(\lambda) = \frac{S_0}{4}\left(\lambda - \frac{\lambda_0^{4}}{\lambda^{3}}\right)
$$

with \(\lambda\) and \(\lambda_0\) in nm and \(S_0\) in ps/(nm²·km). Manual mode uses the entered \(D\) instead.

$$
\mathrm{CD}_{\mathrm{fiber}} = D \, L, \qquad \mathrm{CD}_{\mathrm{res}} = \mathrm{CD}_{\mathrm{fiber}} - C
$$

$$
M_{\mathrm{CD}} = T - \lvert \mathrm{CD}_{\mathrm{res}} \rvert, \qquad u = 100\,\frac{\lvert \mathrm{CD}_{\mathrm{res}} \rvert}{T}
$$

$$
\tau = \lvert \mathrm{CD}_{\mathrm{res}} \rvert \, \Delta\lambda
$$

Length window for \(\lvert D L - C \rvert \le T\), when \(D \ne 0\):

$$
L_{\min} = \max\left(0,\ \frac{C\,\mathrm{sign}(D) - T}{\lvert D \rvert}\right), \quad
L_{\max} = \frac{T + C\,\mathrm{sign}(D)}{\lvert D \rvert}
$$

Status is `failed` if \(M_{\mathrm{CD}} < 0\), else `warning` if \(u > 80\), else `healthy`.

Display rounding in the engine: \(D\) to 3 decimal places, accumulated and residual CD and margin to 1 decimal place, lengths to 2 decimal places.

## Variables

| Symbol | Engine field | Unit | Constraint in model mode |
|---|---|---|---|
| \(\lambda\) | `wavelength` | nm | 1200 to 1700 |
| \(\lambda_0\) | `lambda0` | nm | 1200 to 1700 |
| \(S_0\) | `s0` | ps/(nm²·km) | \(0 < S_0 \le 0.2\) |
| \(D\) | `manualD` in manual mode | ps/(nm·km) | absolute value \(\le 50\) |
| \(L\) | `lengthKm` | km | \(0 < L \le 20000\) |
| \(C\) | `compensation` | ps/nm | finite |
| \(T\) | `tolerance` | ps/nm | \(> 0\) |
| \(\Delta\lambda\) | `spectralWidth` | nm | \(\ge 0\) |

## Engineering Principles

The coefficient changes sign at the zero-dispersion wavelength. Compensation is subtracted as a ps/nm number; the sign of \(D\) decides whether a positive \(C\) reduces or increases the residual. Pulse broadening here is the product of residual dispersion and spectral width, a first-order estimate, not a full receiver penalty.

## Worked Example

Model mode: \(\lambda = 1550\,\mathrm{nm}\), \(\lambda_0 = 1310\,\mathrm{nm}\), \(S_0 = 0.092\,\mathrm{ps/(nm^2\cdot km)}\), \(L = 80\,\mathrm{km}\), \(C = 0\), \(T = 1600\,\mathrm{ps/nm}\), \(\Delta\lambda = 0.1\,\mathrm{nm}\).

1. \(1310^{4} / 1550^{3} = 790.190139\ldots\)
2. \(D = (0.092/4) \times (1550 - 790.190139\ldots) = 17.4606188\ldots\,\mathrm{ps/(nm\cdot km)}\). Display **17.461**.
3. Fiber CD \(= 1396.8495\ldots\,\mathrm{ps/nm}\). Display **1396.8**. Residual equals fiber CD. Margin \(= 1600 - 1396.8495\ldots = 203.150\ldots\,\mathrm{ps/nm}\). Display **203.2**.
4. Used fraction \(= 87.303\ldots\%\). Because this is above 80% and the margin is positive, status is **warning**.
5. Broadening \(= 139.685\ldots\,\mathrm{ps}\). Display **139.68**.
6. \(L_{\max} = 1600 / 17.4606188\ldots = 91.635\ldots\,\mathrm{km}\). Display **91.64 km**. \(L_{\min} = 0\).

Boundary: the same link with tolerance \(800\,\mathrm{ps/nm}\) has a negative margin and status **failed**. Manual mode with \(D = 0\) and \(\lvert C \rvert \le T\) reports maximum length as unbounded in the display logic.

## Limitations

- The model is the standard single-mode slope form. It is not a G.655 dispersion map.
- Slope \(S_0\) is constant. There is no measured \(D(\lambda)\) table.
- Tolerance is an input, not a transceiver catalogue.
- Wavelength and zero-dispersion wavelength are in nanometres inside the powers; do not pass metres.

## Reference Standards

The production page cites, and the engine comment states, the same coefficient formula:

- ITU-T G.652: https://www.itu.int/rec/T-REC-G.652/en — page text points at equation (6-1), \(D(\lambda) = (S_0/4)(\lambda - \lambda_0^4/\lambda^3)\), and at \(\lambda_0\) and \(S_0\) limits in the G.652 tables. This library verified the expression in the engine, not the ITU PDF.
- ITU-T G.650.1: https://www.itu.int/rec/T-REC-G.650.1/en
- ITU-T G.691: https://www.itu.int/rec/T-REC-G.691/en
- ITU-T G.655: https://www.itu.int/rec/T-REC-G.655/en — the page says to use a datasheet \(D\) for these fibres (manual mode).

## Online Calculator

https://netengineerlab.com/tools/chromatic-dispersion-calculator/

Inventory tool ID: `chromatic-dispersion-calculator`.

## Related Formulas

- [Single-span fiber link loss](fiber-link-loss.md)
- [Optical link power budget](optical-power-budget.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `chromatic-dispersion-calculator` |
| Evidence | Production `js/engine.js` function `coefficient` and `calculate` |
| Method | Python evaluation of \((S_0/4)(\lambda - \lambda_0^4/\lambda^3)\) and the residual tests |
| Example result | \(D = 17.4606188\ldots\) ps/(nm·km); display 17.461; 80 km CD display 1396.8 ps/nm; status warning at 1600 ps/nm tolerance |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
