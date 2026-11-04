# Conductor resistance and temperature

## Overview

Resistance at 20 °C is resistivity times length over area. Resistance at another temperature multiplies by a linear coefficient.

## Formula

$$
R_{20} = \rho_{20} L / A
$$

$$
R_T = R_{20}[1 + \alpha (T-20)]
$$

Area is entered in square millimetres and multiplied by \(10^{-6}\) to square metres. The reference temperature in the difference is 20 °C.

## Variables

| Symbol | Meaning | Unit in the product |
|---|---|---|
| \(\rho_{20}\) | Resistivity at 20 °C | ohm·m |
| \(L\) | Length | m |
| \(A\) | Area | m² after conversion |
| \(\alpha\) | Temperature coefficient | 1/°C |
| \(T\) | Conductor temperature | °C |

## Engineering Principles

The script does not look up copper or aluminum by name for the arithmetic. A teaching example supplies \(\rho\) and \(\alpha\). The linear model can produce a non-positive resistance if \(\alpha(T-20)\) is −1 or lower; that result is outside the usual metal range and should be read as the formula output, not as a material limit.

## Worked Example

Teaching-copper example in the page: length 100 m, area 10 mm², \(\rho_{20} = 1.72\times 10^{-8}\) ohm·m, \(\alpha = 0.00393\) per °C, temperature 70 °C.

$$
R_{20} = 1.72\times 10^{-8} \times 100 / 10^{-5} = 0.172\ \Omega
$$

$$
R_{70} = 0.172[1 + 0.00393\times 50] = 0.172 \times 1.1965 = 0.205798\ \Omega
$$

Boundary: at 20 °C the factor is 1 and \(R_T = R_{20}\). Area of 0 is rejected.

## Limitations

The coefficient is constant. It is not a tabulated resistivity curve. The example values are the ones stored on the example button, not a claim that every copper datasheet prints 1.72×10⁻⁸.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/conductor-resistance/

## Related Formulas

- [PoE pair voltage drop](../NetEngineerLab/poe-voltage-drop.md)
- [DC Ohm’s law](ohms-law.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `conductor-resistance` (`TOOL-007`) |
| Evidence | Production chunk `03c90g4jdm08z.js`, R20 and linear temperature factor, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | R20 0.172 ohm, R70 0.205798 ohm |
| Boundary | temperature 20 °C returns R20; zero area is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
