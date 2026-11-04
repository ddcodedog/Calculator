# Induction-motor slip

## Overview

The Motor Slip Calculator computes synchronous speed, per-unit slip, percent slip, and slip frequency from frequency, pole count, and rotor speed.

Production function in the motor-slip page bundle (`BACKLOG-071`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/motor-slip/. The bundle lists https://www.engineeringtoolbox.com/electrical-motor-slip-d_652.html among its page strings.

## Formula

$$
n_s = \frac{120\, f}{p}
$$

$$
s = \frac{n_s - n_r}{n_s}, \qquad s_{\%} = 100\, s, \qquad f_{\mathrm{slip}} = s\, f
$$

Domain:

- \(0 < f \le 400\,\mathrm{Hz}\)
- \(p\) even integer from 2 through 20
- \(0 \le n_r \le 2 n_s\)

Negative slip is allowed inside that rotor-speed range. The warning text says negative slip means the rotor is faster than the field and is not a generating-mode or overspeed approval.

## Variables

| Symbol | Engine field | Unit |
|---|---|---|
| \(f\) | `frequencyHz` | Hz |
| \(p\) | `poles` | count |
| \(n_r\) | `rotorSpeedRpm` | r/min |
| \(n_s\) | `synchronousSpeedRpm` | r/min |
| \(s\) | `slip` | 1 |
| \(s_{\%}\) | `slipPercent` | % |
| \(f_{\mathrm{slip}}\) | `slipFrequencyHz` | Hz |

## Engineering Principles

Slip is the normalized difference between field speed and rotor speed. Slip frequency is that fraction of the stator frequency and is the frequency of the rotor currents in the simple induction-machine model. Percent slip is 100 times per-unit slip, not a separate definition. The same pole and frequency limits as the synchronous-speed tool apply.

## Worked Example

\(f = 60\,\mathrm{Hz}\), \(p = 4\), \(n_r = 1750\,\mathrm{r/min}\).

1. \(n_s = 1800\,\mathrm{r/min}\).
2. \(s = (1800-1750)/1800 = 0.027777\ldots\)
3. \(s_{\%} = 2.7777\ldots\%\)
4. \(f_{\mathrm{slip}} = 0.027777\ldots \times 60 = 1.6666\ldots\,\mathrm{Hz}\)

Result: synchronous speed **1800 r/min**, slip **1/36**, slip frequency **5/3 Hz**.

Boundary: \(n_r = 1800\) gives slip **0**. \(n_r = 1850\) gives \(s = -0.027777\ldots\) and the negative-slip warning. \(n_r = 3601\) is above \(2 n_s\) and is rejected. \(n_r < 0\) is rejected.

## Limitations

- Does not diagnose broken bars, overload, or permission to run. The warnings say that explicitly.
- No load torque, current, or temperature.
- Rotor speed is an input, not estimated from slip.

## Reference Standards

The page bundle contains the Engineering Toolbox motor-slip URL above. This library did not re-fetch that article’s text in the verification pass, so the external article remains **pending** as a standards citation. The equations were taken from the calculation function, whose assumptions state the same three relations.

## Online Calculator

https://powerengineerlab.com/calculators/motor-slip/

Inventory tool ID: `motor-slip`.

## Related Formulas

- [Synchronous speed](synchronous-speed.md)
- [Kilowatt to horsepower](kilowatt-to-horsepower.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `motor-slip` (`BACKLOG-071`) |
| Evidence | Production bundle assignments for `n`, `t`, `s`, and `a` (synchronous speed, per-unit slip, percent, slip frequency) |
| Method | Exact fractions for the 1750 r/min case and the zero-slip and overspeed bounds |
| Example result | \(s = 1/36\), slip frequency \(5/3\) Hz, synchronous speed 1800 r/min |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
