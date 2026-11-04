# Residual pressure from a head balance

## Overview

Residual head is upstream pressure head, plus the elevation drop, minus the supplied head loss. Pressure is head times 9806.65.

## Formula

$$
h_p = p / 9806.65
$$

$$
h_r = h_p + z_{up} - z_{down} - h_L
$$

$$
p_r = 1000 \times h_r \times 9.80665
$$

9806.65 is \(1000 \times 9.80665\). The SI pressure input is kilopascals converted to pascals by multiplying by 1000. If a minimum residual pressure is supplied, status compares \(p_r\) with that minimum. A blank minimum is calculation-only.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(p\) | Upstream pressure | kPa in the SI form |
| \(z\) | Elevation | m |
| \(h_L\) | Supplied head loss | m |

## Engineering Principles

The loss is not computed. Static elevation change is downstream elevation minus upstream elevation, with the sign already arranged by the subtraction above.

## Worked Example

SI defaults: upstream 300 kPa, upstream elevation 100 m, downstream elevation 112 m, head loss 8 m, minimum residual 100 kPa.

Upstream pressure head is \(300000/9806.65 = 30.59148639\) m.

$$
h_r = 30.59148639 + 100 - 112 - 8 = 10.59148639\ \text{m}
$$

Residual pressure is 103867 Pa, or 103.867 kPa, which is above 100 kPa.

Boundary: clearing the minimum leaves the same residual and skips the pass/fail comparison. A residual head of 0 gives zero residual pressure.

## Limitations

The check is one supplied loss term. It is not a hydrant-flow test reduction and it does not add velocity head.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/pressure-static-residual-check/

## Related Formulas

- [Hydraulic and energy grade lines](hydraulic-energy-grade-line.md)
- [Pump duty head and power](pump-duty-head-power.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-012` |
| Evidence | Production residual-head function, divisor 9806.65, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 10.59148639 m and 103.867 kPa, above the 100 kPa minimum |
| Boundary | a blank minimum skips the comparison |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
