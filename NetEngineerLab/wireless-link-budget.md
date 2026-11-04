# Wireless free-space link budget

## Overview

The wireless calculator uses a free-space path loss with frequency in gigahertz and distance in kilometres, then a first-Fresnel radius at a user-chosen obstacle position.

## Formula

$$
L_{fs} = 92.45 + 20\log_{10}(d_{km}) + 20\log_{10}(f_{GHz})
$$

$$
EIRP = P_{tx} - L_{tx} + G_{tx}
$$

$$
P_{rx} = EIRP + G_{rx} - L_{rx} - L_{extra} - L_{fs}
$$

$$
r = 17.32\sqrt{d_1 d_2 / (f_{GHz}\, d)}
$$

\(d_1\) is distance times the obstacle position in percent, divided by 100. \(d_2 = d - d_1\). The script’s clearance check compares the entered clearance with \(0.6 r\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(d\) | Path length | km |
| \(f\) | Frequency | GHz |
| \(P_{tx}\) | Transmit power | dBm |
| \(L_{tx}, L_{rx}\) | Cable and connector losses | dB |
| \(G_{tx}, G_{rx}\) | Antenna gains | dBi |
| \(r\) | First-Fresnel radius | m |

## Engineering Principles

The constant 92.45 matches a free-space expression written for kilometres and gigahertz. It is a literal in the script. The Fresnel constant 17.32 is also a literal. Neither constant was re-derived from a standards PDF for this page.

## Worked Example

Defaults: 5 km, 5.8 GHz, transmit 20 dBm, transmit cable 1 dB, transmit gain 24 dBi, receive gain 24 dBi, receive cable 1 dB, extra loss 2 dB, sensitivity −75 dBm, obstacle at 50%, clearance 8 m.

$$
L_{fs} = 92.45 + 20\log_{10}(5) + 20\log_{10}(5.8) = 121.69796\ \text{dB}
$$

EIRP is \(20 - 1 + 24 = 43\) dBm. Received power is \(43 + 24 - 1 - 2 - 121.69796 = -57.69796\) dBm. Margin over −75 dBm is 17.30204 dB.

Obstacle distances are 2.5 km and 2.5 km. Radius is 8.040608143 m. Sixty percent of that radius is 4.824364886 m. The entered 8 m clearance is above that value.

Boundary: distance or frequency of 0 is rejected because the logarithms are undefined.

## Limitations

Free-space loss ignores terrain, gas attenuation, and rain. The 0.6 factor is the script’s clearance fraction, not a value taken from an opened planning guide.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/wireless-link-budget-calculator/

## Related Formulas

- [Optical link power budget](optical-power-budget.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `wireless-link-budget-calculator` |
| Evidence | Production `js/engine.js` constants 92.45 and 17.32, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | FSPL 121.69796 dB, receive −57.69796 dBm, Fresnel radius 8.040608143 m |
| Boundary | zero distance or frequency is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
