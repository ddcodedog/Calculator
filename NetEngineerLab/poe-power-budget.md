# PoE switch power budget

## Overview

The PoE power-budget page grosses each device up for cable loss, then applies a headroom factor to the group. It does not solve voltage drop.

## Formula

$$
P_{source} = P_{device} / (1 - \ell)
$$

$$
P_{required} = P_{source} \times N \times (1 + h)
$$

\(\ell\) and \(h\) are the cable-loss and headroom fields after the percent values are divided by 100. A stored class table lists PSE and PD watts: af 15.4 and 12.95, at 30 and 25.5, bt type 3 60 and 51, bt type 4 90 and 71.3. The arithmetic above uses the watts the user enters, not that table, unless the user types those watts.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P_{device}\) | Power at the device | W |
| \(\ell\) | Cable-loss fraction | fraction |
| \(N\) | Device count | count |
| \(h\) | Headroom fraction | fraction |
| \(P_{switch}\) | Switch budget used only for the comparison | W |

## Engineering Principles

Cable loss is a single fraction, so source power is device power divided by what remains after that fraction. Headroom multiplies the group. The page preset for cameras fills switch budget 160 W, 8 ports, 8 devices, 12.95 W, 10% cable loss, 20% headroom, and the af label.

## Worked Example

Camera preset:

$$
P_{source} = 12.95 / 0.90 = 14.38888889\ \text{W}
$$

$$
P_{required} = 14.38888889 \times 8 \times 1.20 = 138.1333333\ \text{W}
$$

Against a 160 W budget the unused power is \(160 - 138.1333333 = 21.86666667\) W.

Boundary: cable loss of 100% makes the denominator zero and is rejected. Zero devices give a required power of 0 W.

## Limitations

This is not the quadratic pair-drop model. Class watts in the table were not checked against an IEEE PDF. Port count is not in the power product; device count is.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/poe-power-budget-calculator/

## Related Formulas

- [PoE pair voltage drop](poe-voltage-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `poe-power-budget-calculator` |
| Evidence | Production page script, camera preset and source-per-device division, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 14.38888889 W per device, 138.1333333 W required |
| Boundary | 100% cable loss is rejected; zero devices require 0 W |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
