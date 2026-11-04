# Fan air power and input

## Overview

Fan air power is volume flow times the sum of static pressure and path loss. Input power divides by fan and motor efficiency.

## Formula

$$
\Delta p = p_{static} + p_{loss}
$$

$$
K = p_{loss} / Q^2
$$

$$
P_{air} = Q\, \Delta p
$$

$$
P_{in} = P_{air} / (\eta_{fan}\, \eta_{motor})
$$

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Airflow | m³/s |
| \(p\) | Pressure | Pa |
| \(\eta\) | Efficiencies | fraction |

## Engineering Principles

Air power in watts equals m³/s times pascals. The loss coefficient is the loss at this flow divided by flow squared. Density is not in this product.

## Worked Example

Defaults: 2 m³/s, static 300 Pa, loss 200 Pa, fan efficiency 0.65, motor efficiency 0.9.

$$
\Delta p = 500\ \text{Pa}
$$

$$
P_{air} = 1000\ \text{W}
$$

$$
P_{in} = 1000/(0.65\times 0.9) = 1709.401709\ \text{W}
$$

$$
K = 200/4 = 50\ \text{Pa·s}^2/\text{m}^6
$$

Boundary: zero airflow is rejected. Loss of 0 Pa leaves air power equal to flow times static pressure only.

## Limitations

This is not a fan-curve intersection. The pressure terms are inputs. Compressibility and density changes are outside the product.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/fan-selection-system-curve/

## Related Formulas

- [Duct friction and local pressure drop](duct-friction-pressure-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `fan-selection-system-curve` |
| Evidence | Production fan function, Pair = Q Δp, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 500 Pa and 1000 W air, 1709.401709 W input |
| Boundary | zero flow is rejected; zero loss leaves static pressure only |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
