# Polarization-mode dispersion budget

## Overview

The PMD calculator combines a fiber coefficient and a count of discrete components into one mean differential group delay, then compares it with a fraction of the symbol period.

## Formula

$$
DGD = \sqrt{(PMD\sqrt{L})^2 + N\,pmd_c^2}
$$

$$
T_{symbol} = 1000 / B
$$

$$
DGD_{allow} = T_{symbol} \times (tol/100)
$$

\(DGD\) and the symbol period are in picoseconds when PMD is in ps/√km, component DGD is in ps, length is in km, and \(B\) is in Gbaud. The ratio reported by the page is \(DGD / DGD_{allow}\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(PMD\) | Fiber PMD coefficient | ps/√km |
| \(L\) | Length | km |
| \(N, pmd_c\) | Component count and each component’s mean DGD | count, ps |
| \(B\) | Symbol rate | Gbaud |
| \(tol\) | Allowed fraction of the symbol | percent |

## Engineering Principles

The fiber term is a square-root length law. Components add as a root-sum-square, not as a linear sum. A comment in the script names ITU-T G.650.2 and IEC TR 61282-3. Those texts were not opened. The numerical limit is the user’s tolerance percent.

## Worked Example

Defaults: 0.2 ps/√km, 80 km, 4 components at 0.1 ps, 10.3125 Gbaud, tolerance 10%.

$$
DGD = \sqrt{(0.2\sqrt{80})^2 + 4(0.1)^2} = \sqrt{3.24} = 1.8\ \text{ps}
$$

Symbol period is \(1000/10.3125 = 96.96969697\) ps. Ten percent of that is 9.696969697 ps. The ratio is \(1.8/9.696969697 = 0.185625\).

Boundary: zero length and zero components give DGD 0. A non-positive symbol rate is rejected because the period division is undefined.

## Limitations

Mean DGD is not an outage probability. The script does not apply a Maxwellian tail or a maximum-to-mean ratio unless the user compares the ratio with the separate max-ratio field. That field is a check threshold, not part of the DGD equation.

## Reference Standards

ITU-T G.650.2 and IEC TR 61282-3 are named in a code comment and were not opened. Reference standards are pending.

## Online Calculator

https://netengineerlab.com/tools/pmd-budget-calculator/

## Related Formulas

- [Chromatic dispersion coefficient D(λ)](chromatic-dispersion.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `pmd-budget-calculator` |
| Evidence | Production `js/engine.js` root-sum-square DGD, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | mean DGD 1.8 ps, allowed 9.696969697 ps, ratio 0.185625 |
| Boundary | zero length and zero components give DGD 0 |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
