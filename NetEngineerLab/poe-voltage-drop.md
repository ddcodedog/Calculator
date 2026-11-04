# PoE pair voltage drop

## Overview

The PoE voltage-drop calculator solves the quadratic that remains when cable power is load power divided by efficiency and both conductors of each pair carry the current.

## Formula

Conductor resistance per kilometre at temperature \(T\):

$$
R = R_{20}[1 + 0.00393(T-20)]
$$

Loop resistance for the selected pair count:

$$
R_{loop} = 2 R (L/1000) / N_{pairs} + R_{contact}
$$

With cable power \(P = P_{load}/\eta\):

$$
I = \frac{V_s - \sqrt{V_s^2 - 4 R_{loop} P}}{2 R_{loop}}
$$

$$
V_{end} = V_s - I R_{loop}
$$

\(R_{20}\) for AWG 22 through 26 is 52.96, 66.79, 84.22, 106.2, and 133.9 ohm/km. Pair count must be 2 or 4. If the discriminant is negative the script returns overload and the maximum power \(V_s^2/(4 R_{loop})\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(L\) | One-way cable length | m |
| \(V_s\) | Source voltage | V |
| \(P_{load}\) | Device load | W |
| \(\eta\) | Efficiency entered as a percent, divided by 100 | fraction |
| \(R_{contact}\) | Extra series resistance | ohm |
| \(V_{min}\) | Comparison threshold, not used inside \(I\) | V |

## Engineering Principles

The temperature coefficient 0.00393 per °C is the value in the script, applied to the AWG table rather than to a resistivity the user types. The smaller root of the quadratic is the operating current. End voltage is compared with the minimum only after the current exists. Class wattages stored beside the formula are 15.4, 30, 60, and 90 W for the labels 802.3af, 802.3at, 802.3bt-60, and 802.3bt-90. Those labels are not a reading of the IEEE PDF.

## Worked Example

Defaults from the form: 90 m, 48 V, 12 W, AWG 24, 2 pairs, 30 °C, 0.2 ohm contact, 90% efficiency, 44 V minimum.

$$
R = 84.22[1 + 0.00393(10)] = 87.529846\ \Omega/\text{km}
$$

$$
R_{loop} = 2(87.529846)(0.090)/2 + 0.2 = 8.07768614\ \Omega
$$

Cable power is \(12/0.9 = 13.33333333\) W. Current is 0.2921402254 A. End voltage is 45.64018295 V, which is also cable power divided by current. That is above 44 V.

Boundary: a load large enough to make \(V_s^2 - 4 R_{loop} P\) negative is rejected as overload. Pair counts other than 2 or 4 are rejected. Efficiency above 100% is rejected.

## Limitations

The AWG table is a single 20 °C column in the script. Contact resistance is a user constant, not a connector model. The class wattages are labels in the same file and were not checked against IEEE 802.3.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/poe-voltage-drop-calculator/

## Related Formulas

- [PoE switch power budget](poe-power-budget.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `poe-voltage-drop-calculator` |
| Evidence | Production `js/engine.js` loopR and quadratic current, fetched 2026-11-04. Form defaults read from the live page the same day. |
| Method | Direct evaluation of the expressions above |
| Example result | loop 8.07768614 ohm, current 0.2921402254 A, end voltage 45.64018295 V |
| Boundary | negative discriminant returns overload; pairs must be 2 or 4 |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
