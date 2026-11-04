# Shaft torque from power and speed

## Overview

Torque is mechanical power divided by angular speed. The page also divides newton-metres by the constant 1.3558179483314003 to show pound-force feet.

## Formula

$$
\omega = 2\pi n / 60
$$

$$
T = P / \omega
$$

$$
T_{lbf\cdot ft} = T / 1.3558179483314003
$$

\(P\) is kilowatts times 1000. \(n\) is revolutions per minute. The English default power is 10 kW and the English default speed is 1800 r/min.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P\) | Shaft power | W |
| \(n\) | Rotational speed | r/min |
| \(T\) | Torque | N·m |

## Engineering Principles

The conversion constant is the literal in the chunk. It matches the pound-force-foot factor used by the structural utilization tool on this site’s sibling page, but this page does not import that tool. Speed must be positive.

## Worked Example

English defaults, 10 kW at 1800 r/min:

$$
\omega = 2\pi \times 1800/60 = 188.4955592\ \text{rad/s}
$$

$$
T = 10000 / 188.4955592 = 53.0516477\ \text{N·m}
$$

$$
T_{lbf\cdot ft} = 39.1288873
$$

Boundary: speed 0 is rejected. Doubling the speed at the same power halves the torque.

## Limitations

The result is steady torque at the stated speed. It is not a breakdown torque or a duty-cycle rms torque.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/motor-torque/

## Related Formulas

- [Three-phase motor line current](motor-line-current.md)
- [Kilowatt to mechanical horsepower](kilowatt-to-horsepower.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `motor-torque` (script id `BACKLOG-072`) |
| Evidence | Production chunk `02p8akv3gdoyn.js`, English defaults 10 kW and 1800 r/min, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 53.0516477 N·m and 39.1288873 lbf·ft |
| Boundary | zero speed is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
