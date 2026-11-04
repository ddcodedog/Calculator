# Manning full-flow pipe diameter

## Overview

Required diameter is the full-pipe Manning relation solved for \(D\). A selected diameter is checked with the same full-flow equation.

## Formula

Full-pipe area and hydraulic radius:

$$
A = \pi D^2/4,\quad R = D/4
$$

$$
Q = (1/n)\, A\, R^{2/3}\, \sqrt{S}
$$

Solving for diameter:

$$
D = \left(Q / \left[(1/n)(\pi/4)(1/4)^{2/3}\sqrt{S}\right]\right)^{3/8}
$$

Capacity status compares the design flow with \(Q\) at the selected diameter. Velocity is \(Q/A\) at that diameter.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Design flow | m³/s |
| \(n\) | Manning coefficient | s/m^(1/3) |
| \(S\) | Slope | m/m |
| \(D\) | Diameter | m |

## Engineering Principles

The section is full. The script states that it does not apply a hidden velocity or utilization limit; utilization is the ratio of design flow to full-flow capacity and is reported, not used to resize the pipe.

## Worked Example

SI defaults: design flow 1.1111111111 m³/s, slope 0.01, \(n = 0.013\), selected diameter 1.2 m.

Required diameter is 0.7494524927 m. At 1.2 m the full-flow capacity is 3.898730279 m³/s and the velocity is 3.44723442 m/s. Hydraulic utilization is \(1.1111111111 / 3.898730279 = 0.2849930699\).

Boundary: leaving the selected diameter blank is the sizing-only path and still returns the required diameter. Slope 0 or \(n \le 0\) is rejected because the Manning product would not yield a positive capacity.

## Limitations

Partial-flow depth is not solved. The open-channel Manning page on this site is the same \(1/n\) product for a channel the user describes, not this circular inversion.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/storm-drain-pipe-capacity-sizing/

## Related Formulas

- [Manning open-channel discharge](manning-open-channel-flow.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-005` |
| Evidence | Production full-flow inversion, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | required D 0.7494524927 m; 1.2 m carries 3.898730279 m³/s |
| Boundary | zero slope is rejected; blank selected diameter skips the capacity check |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
