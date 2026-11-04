# Darcy required pipe diameter

## Overview

Required diameter is the Darcy-Weisbach equation solved for \(D\) with a user friction factor and an allowable major head loss.

## Formula

$$
D = \left(\frac{8 f L Q^2}{9.80665\,\pi^2 h_{allow}}\right)^{0.2}
$$

A selected diameter can be checked with the same major-loss expression used on the head-loss page, \(h_f = f (L/D) V^2 / 19.6133\), with \(V = Q/(\pi D^2/4)\). The status is about that major-loss allowance only.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Flow | m³/s |
| \(L\) | Length | m |
| \(f\) | Darcy friction factor | dimensionless |
| \(h_{allow}\) | Allowable major head loss | m |

## Engineering Principles

Friction factor is an input. Nothing in this inversion computes Reynolds number. Gravity is 9.80665, so \(2g = 19.6133\), which is why the selected-pipe check matches the other Darcy page.

## Worked Example

SI defaults: flow 0.05 m³/s, length 100 m, \(f = 0.02\), allowable head loss 2 m, selected diameter 0.2 m.

$$
D = 0.1832491273\ \text{m}
$$

The selected 0.2 m diameter is above that continuous minimum. The page can leave the selected diameter blank and return only the required diameter.

Boundary: allowable head loss of 0 is rejected. A friction factor of 0 is rejected.

## Limitations

Minor losses are outside this diameter. The HVAC pipe page estimates \(f\) from Reynolds number; this page does not.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/pipe-diameter-sizing/

## Related Formulas

- [Darcy-Weisbach major pipe headloss](darcy-weisbach-pipe-headloss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-011` |
| Evidence | Production diameter inversion, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | required diameter 0.1832491273 m |
| Boundary | zero allowable head or zero f is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
