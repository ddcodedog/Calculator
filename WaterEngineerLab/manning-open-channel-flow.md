# Manning open-channel discharge

## Overview

The Manning Open Channel Flow Calculator computes area, wetted perimeter, hydraulic radius, mean velocity, and discharge for a rectangular or trapezoidal channel at a known depth. A second mode solves normal depth by bisection so that the same Manning discharge matches a target flow.

Production module in the manning-open-channel-flow page bundle (`FORMULA-TOOL007-MANNING-OPEN-CHANNEL-001`, engine version 1.0.0), fetched 2026-11-04 from https://waterengineerlab.com/tools/manning-open-channel-flow/.

## Formula

Rectangular channel, bottom width \(b\), depth \(y\):

$$
A = b y, \qquad P = b + 2y, \qquad R = A/P
$$

Trapezoidal channel, side slope \(z\) horizontal over 1 vertical:

$$
A = y\,(b + z y), \qquad P = b + 2 y \sqrt{1+z^{2}}, \qquad R = A/P
$$

SI Manning equation used for both unit systems after conversion:

$$
V = \frac{1}{n} R^{2/3} S^{1/2}, \qquad Q = A V
$$

\(S\) is the dimensionless bed slope (m/m or ft/ft). US entries are converted before this equation: feet × 0.3048 → metres, cubic feet per second × 0.028316846592 → m³/s. Manning \(n\) is not rescaled, and the 1.486 foot-second coefficient is **not** used. Display back to US units multiplies velocity by 3.280839895013123 and discharge by 35.31466672148859.

Normal-depth mode evaluates \(Q(y)\) with the formulas above. The bracket starts at \(10^{-9}\,\mathrm{m}\) and \(\max(0.1,\ b)\), doubles the upper end at most 80 times until \(Q\) exceeds the target, then bisects at most 100 times until \(\lvert Q-Q_{\mathrm{target}}\rvert / Q_{\mathrm{target}} \le 10^{-10}\).

## Variables

| Symbol | Meaning | Unit inside the Manning call |
|---|---|---|
| \(b\) | bottom width | m |
| \(y\) | depth | m |
| \(z\) | side slope, horizontal:vertical | 1 |
| \(S\) | bed slope | m/m |
| \(n\) | Manning \(n\) | s·m^(−1/3) in the SI form |
| \(V\) | mean velocity | m/s |
| \(Q\) | discharge | m³/s |

The page validation requires Manning \(n\) in \((0,\ 0.2]\). Width, depth, and slope must be finite and \(> 0\).

## Engineering Principles

Steady uniform flow is assumed: the depth used for a known-depth run is the normal depth only if the channel is long and the slope and roughness are those of that uniform flow. The calculator does not solve gradually varied flow, critical depth, or freeboard. Because US geometry is converted to metres and then passed through \(1/n\), a hand calculation that uses \(1.486/n\) with areas in square feet will not match this tool.

## Worked Example

Known depth, rectangular, SI: \(b = 2\,\mathrm{m}\), \(y = 1\,\mathrm{m}\), \(S = 0.001\), \(n = 0.013\).

1. \(A = 2\,\mathrm{m^2}\), \(P = 4\,\mathrm{m}\), \(R = 0.5\,\mathrm{m}\).
2. \(V = (1/0.013) \times 0.5^{2/3} \times \sqrt{0.001} = 1.53239238\ldots\,\mathrm{m/s}\).
3. \(Q = 3.06478476\ldots\,\mathrm{m^3/s}\).

Result: velocity **1.532 m/s** and discharge **3.065 m³/s** when rounded to three decimals. The engine keeps the full double.

Normal-depth boundary: ask for that same discharge. The bisection returns depth **1.00000000003… m** after the relative tolerance test, which rounds to the input depth of 1 m.

A trapezoid with \(z = 0\) uses \(A = y b\) and \(P = b + 2y\), the same geometry as the rectangle.

US conversion check, not a second Manning formula: 10 ft width → \(3.048\,\mathrm{m}\) before \(V\) is computed.

## Limitations

- Prismatic rectangle or trapezoid only.
- One roughness. No composite \(n\).
- No entrance, bend, or culvert loss.
- Source ids `SRC-MANNING-OPEN-CHANNEL-FHWA-TOOL007-001` and `SRC-PROJECT-METHOD-TOOL007-001` have no URL in the bundle.

## Reference Standards

**Pending.** The formula id refers to a Manning open-channel method and an FHWA-tagged source id, but the fetched bundle does not contain an FHWA or textbook URL. The \(1/n\) equation and the US conversion factors above are what the code runs.

## Online Calculator

https://waterengineerlab.com/tools/manning-open-channel-flow/

Inventory tool ID: `TOOL-007`. The inventory URL with a trailing slash redirects to this path.

## Related Formulas

- [Rational-method peak runoff](rational-method-peak-runoff.md)
- [Darcy-Weisbach major pipe headloss](darcy-weisbach-pipe-headloss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-007` |
| Evidence | Page bundle functions for geometry, \(V=(1/n)R^{2/3}S^{1/2}\), US factors 0.3048 and 0.028316846592, and the bisection loop |
| Method | Python evaluation of the rectangle and a reimplementation of the bisection |
| Example result | 1.53239238… m/s and 3.06478476… m³/s; normal depth returns to 1 m |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
