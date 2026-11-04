# Resistive voltage divider

## Overview

The Voltage Divider Calculator reports the unloaded output, the output with an optional resistive load across the lower resistor, and the current drawn from the input.

Production function `computeVoltageDivider` (`TOOL-003`, model 1.0.0) in the voltage-divider page bundle, fetched 2026-11-04 from https://powerengineerlab.com/calculators/voltage-divider/. The page’s “Load example” is 12 V, 1000 Ω, 1000 Ω, and a 1000 Ω load.

## Formula

Unloaded:

$$
V_{\mathrm{oc}} = V_{\mathrm{in}}\frac{R_2}{R_1+R_2}
$$

With a load \(R_L > 0\), the lower arm is the parallel combination

$$
R_e = \frac{R_2 R_L}{R_2+R_L}
$$

and

$$
V_{\mathrm{L}} = V_{\mathrm{in}}\frac{R_e}{R_1+R_e}, \qquad I_{\mathrm{in}} = \frac{V_{\mathrm{in}}}{R_1+R_e}
$$

If the load field is empty, \(R_e = R_2\), so the loaded and open-circuit voltages match. The code forms sums with a log-sum-exp and the quotient with \(\exp(\ln V_{\mathrm{in}}+\ln R_e-\ln(R_1+R_e))\). That is the same real function inside the finite range. Parallel combination uses the smaller resistance over one plus the resistance ratio, which equals the product-over-sum form.

\(V_{\mathrm{in}} = 0\) forces both voltages and the current to 0.

## Variables

| Symbol | Engine field | Unit | Constraint |
|---|---|---|---|
| \(V_{\mathrm{in}}\) | `vin` | V | finite, \(\ge 0\) |
| \(R_1\) | `r1` | Ω | finite, \(> 0\) (upper resistor) |
| \(R_2\) | `r2` | Ω | finite, \(> 0\) (lower resistor) |
| \(R_L\) | `loadResistance` | Ω | omitted, or finite and \(> 0\) |

## Engineering Principles

The load is assumed to be a resistance in parallel with \(R_2\) only. The result text says the divider is not assumed to drive an arbitrary external network. Input current is the current through \(R_1\), which equals the sum of the currents in \(R_2\) and \(R_L\). There is no source resistance beyond \(R_1\).

## Worked Example

Example button: \(V_{\mathrm{in}} = 12\,\mathrm{V}\), \(R_1 = 1000\,\Omega\), \(R_2 = 1000\,\Omega\), \(R_L = 1000\,\Omega\).

1. \(R_e = 1000 \parallel 1000 = 500\,\Omega\).
2. Loaded output \(= 12 \times 500/1500 = 4\,\mathrm{V}\).
3. Open-circuit output \(= 12 \times 1000/2000 = 6\,\mathrm{V}\).
4. Input current \(= 12/1500 = 0.008\,\mathrm{A}\).

Result: **4 V** loaded, **6 V** open-circuit, **0.008 A**.

Boundary: clear the load. Then \(V_{\mathrm{L}} = V_{\mathrm{oc}} = 6\,\mathrm{V}\) and \(I_{\mathrm{in}} = 0.006\,\mathrm{A}\). \(R_L = 0\) is rejected. \(V_{\mathrm{in}} = 0\) yields 0 V and 0 A.

## Limitations

- Resistive DC divider only. No frequency response.
- Both resistors must be greater than zero, so a shorted lower arm is not a supported case.
- The source record `SRC-001` in this module has `url: null`. Do not invent a textbook link for this tool.

## Reference Standards

**Pending.** The module marks `SRC-001` with a null URL. The formula above is the one printed by the page (“Vout = Vin × Re / (R1 + Re)”) and computed in `computeVoltageDivider`.

## Online Calculator

https://powerengineerlab.com/calculators/voltage-divider/

Inventory tool ID: `voltage-divider`.

## Related Formulas

- [DC Ohm’s law](ohms-law.md)
- [Ideal capacitive reactance](capacitive-reactance.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `voltage-divider` (`TOOL-003`) |
| Evidence | `computeVoltageDivider` and the page formula string, 2026-11-04 |
| Method | Parallel combination and divider equation on the load-example values |
| Example result | 4 V loaded, 6 V open-circuit, 8 mA |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
