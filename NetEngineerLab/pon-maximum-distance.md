# PON maximum optical distance

## Overview

The PON distance calculator uses the same loss terms as the splitter page and solves for the longest fiber that still leaves the requested margin.

## Formula

$$
L_{fixed} = N_s a_s + N_c a_c + (s_1+s_2+s_3) + L_{other}
$$

$$
L_{fiber,allow} = (P_{tx} - P_{sens}) - L_{fixed} - M
$$

$$
L_{optical} = L_{fiber,allow} / \alpha
$$

$$
L_{effective} = \min(L_{optical}, L_{system})
$$

The limiter is optical when the fiber allowance is shorter than the entered system reach, and system when the reach is shorter.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P_{tx}\) | Transmit level | dBm |
| \(P_{sens}\) | Receiver sensitivity | dBm |
| \(\alpha\) | Attenuation | dB/km |
| \(M\) | Margin held back from the fiber | dB |
| \(L_{system}\) | Entered system reach | km |

## Engineering Principles

Distance is linear in the leftover decibels. The script refuses a non-positive attenuation because the division would not be a length. The same ratio table used by the splitter page converts each stage loss into a ratio for the ideal-loss display; the length itself uses the entered decibel losses.

## Worked Example

Defaults: transmit 1.5 dBm, sensitivity −27 dBm, stages 10.5 dB and 10.5 dB, six splices at 0.10 dB, four connectors at 0.30 dB, margin 3 dB, attenuation 0.30 dB/km, system reach 20 km.

Fixed loss is \(10.5+10.5+0.6+1.2 = 22.8\) dB. The raw window is 28.5 dB. Fiber allowance is \(28.5 - 22.8 - 3 = 2.7\) dB. Optical maximum is \(2.7 / 0.30 = 9\) km. Effective maximum is 9 km and the limiter is optical, because 9 is below the 20 km reach.

Boundary: if system reach is entered as 5 km with the same optics, effective maximum becomes 5 km and the limiter is the system reach. Attenuation of 0 is rejected.

## Limitations

The result is an attenuation budget, not a dispersion or splitter-uniformity limit. Overload is reported from the same receive-level arithmetic as the splitter page and does not change the length formula.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/pon-distance/

## Related Formulas

- [PON splitter and link loss budget](pon-splitter-loss.md)
- [Single-span fiber link loss](fiber-link-loss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `pon-distance` |
| Evidence | Production `js/engine.js` optical-maximum division, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | fiber allowance 2.7 dB, optical maximum 9 km, limiter optical |
| Boundary | a 5 km system reach becomes the limiter; zero attenuation is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
