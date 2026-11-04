# Pump head and hydraulic power

## Overview

Total dynamic head is the sum of static, pipe, and local heads. Hydraulic power multiplies that head by density, flow, and 9.80665.

## Formula

$$
H = H_{static} + H_{pipe} + H_{local}
$$

$$
K = (H_{pipe}+H_{local}) / Q^2
$$

$$
P_{hyd} = 9.80665\, \rho\, Q\, H
$$

$$
P_{in} = P_{hyd} / (\eta_{pump}\, \eta_{motor})
$$

The curve coefficient \(K\) is stored for a system curve. It is not required to compute \(P_{hyd}\) at the entered point.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Flow | m³/s |
| \(H\) | Head terms | m |
| \(\rho\) | Density | kg/m³ |
| \(\eta\) | Efficiencies | fraction |

## Engineering Principles

Heads are entered, not solved from fittings, on this page. Power uses standard gravity 9.80665 m/s². Both efficiencies must be in (0, 1].

## Worked Example

Defaults: flow 0.01 m³/s, static 12 m, pipe 4 m, local 2 m, density 998 kg/m³, pump efficiency 0.7, motor efficiency 0.9.

$$
H = 18\ \text{m}
$$

$$
P_{hyd} = 9.80665 \times 998 \times 0.01 \times 18 = 1761.666606\ \text{W}
$$

$$
P_{in} = 1761.666606 / (0.7 \times 0.9) = 2796.2962\ \text{W}
$$

$$
K = 6 / 0.01^2 = 60000\ \text{s}^2/\text{m}^5
$$

Boundary: zero flow is rejected. If both loss heads are 0, \(K = 0\) and head equals the static head. The page warns when a curve is requested without the loss terms that define \(K\); the single-point power above does not need that curve.

## Limitations

Entered heads are not a Darcy solution. The chilled-water page calls this same power function after it has computed heads.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/pump-sizing-system-curve/

## Related Formulas

- [Chilled-water flow and plant power](chilled-water-flow.md)
- [Darcy pipe pressure drop](pipe-darcy-pressure-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `pump-sizing-system-curve` |
| Evidence | Production pump function, g = 9.80665, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | head 18 m, hydraulic 1761.666606 W, input 2796.2962 W |
| Boundary | zero flow is rejected; zero losses leave K = 0 |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
