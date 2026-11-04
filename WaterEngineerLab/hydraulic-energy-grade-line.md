# Hydraulic and energy grade lines

## Overview

Hydraulic grade is elevation plus pressure head. Energy grade adds velocity head. The balance residual is upstream energy grade, minus the supplied loss, minus downstream energy grade.

## Formula

$$
h_v = V^2 / 19.6133
$$

$$
HGL = z + h_p
$$

$$
EGL = HGL + h_v
$$

$$
r = EGL_{up} - h_L - EGL_{down}
$$

The constant 19.6133 is \(2 \times 9.80665\). A residual within \(10^{-6}\) m of zero is reported as balanced.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(z\) | Elevation | m |
| \(h_p\) | Pressure head | m |
| \(V\) | Velocity | m/s |
| \(h_L\) | Supplied head loss | m |

## Engineering Principles

Every head is an input. The page does not compute friction. The same 19.6133 constant is used by the Darcy head-loss page when the user supplies \(f\).

## Worked Example

SI defaults: upstream elevation 100 m, pressure head 8 m, velocity 2 m/s; downstream elevation 98 m, pressure head 8.1 m, velocity 2.2 m/s; head loss 0.3 m.

Upstream velocity head is 0.2039432426 m. Downstream velocity head is 0.2467713235 m. Upstream HGL is 108 m and EGL is 108.2039432 m. Downstream HGL is 106.1 m and EGL is 106.3467713 m.

$$
r = 108.2039432 - 0.3 - 106.3467713 = 1.557171919\ \text{m}
$$

The residual is far above \(10^{-6}\) m, so the grade lines are not balanced.

Boundary: equal EGLs and zero loss give a residual of 0 and the balanced status. A non-finite velocity is rejected.

## Limitations

The check does not say which head should change. It only reports the residual of the numbers supplied.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/hydraulic-energy-grade-helper/

## Related Formulas

- [Darcy-Weisbach major pipe headloss](darcy-weisbach-pipe-headloss.md)
- [Residual pressure from a head balance](residual-pressure-head.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-009` |
| Evidence | Production grade-line function, divisor 19.6133, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | residual 1.557171919 m, not balanced |
| Boundary | matching EGLs and zero loss are balanced |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
