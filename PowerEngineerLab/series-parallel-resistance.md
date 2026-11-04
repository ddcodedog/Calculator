# Series and parallel resistance

## Overview

Series resistance is the sum of the entered values. Parallel resistance is the reciprocal of the sum of reciprocals. A non-positive resistance is rejected.

## Formula

Series:

$$
R = R_1 + R_2 + \cdots + R_n
$$

Parallel:

$$
R = \left(\sum_i 1/R_i\right)^{-1}
$$

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(R_i\) | Branch resistance | ohm |

## Engineering Principles

Every entered value must be greater than zero. The parallel form is undefined at zero, and the script rejects zero rather than returning infinity. One resistor is valid in either topology and returns that resistor.

## Worked Example

Load example: series, 10 ohm, 20 ohm, and 30 ohm.

$$
R = 60\ \Omega
$$

Boundary: the same three values in parallel:

$$
R = (1/10 + 1/20 + 1/30)^{-1} = (0.1+0.05+0.03333333333)^{-1} = 5.454545455\ \Omega
$$

A listed resistance of 0 ohm or a negative resistance is rejected.

## Limitations

The page does not solve a bridge or a network with both series and parallel parts in one entry. The user picks one topology for the whole list.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/series-parallel-resistance/

## Related Formulas

- [DC Ohm’s law](ohms-law.md)
- [Resistive voltage divider](voltage-divider.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `series-parallel-resistance` (`TOOL-002`) |
| Evidence | Production chunk `0m1-f0p8swouv.js`, sum and reciprocal sum, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | series 10+20+30 = 60 ohm |
| Boundary | parallel of the same three is 5.454545455 ohm; R ≤ 0 is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
