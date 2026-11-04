# AC machine synchronous speed

## Overview

The Synchronous Speed Calculator returns the rotating-field speed of an AC machine from supply frequency and pole count.

Production function in the synchronous-speed page bundle (`BACKLOG-070`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/synchronous-speed/.

## Formula

$$
n_s = \frac{120\, f}{p}
$$

\(n_s\) is in revolutions per minute, \(f\) in hertz, and \(p\) is the number of poles.

Accepted domain in this tool:

- \(0 < f \le 400\,\mathrm{Hz}\)
- \(p\) is an even integer from 2 through 20

## Variables

| Symbol | Engine field | Unit |
|---|---|---|
| \(f\) | `frequencyHz` | Hz |
| \(p\) | `poles` | count |
| \(n_s\) | `synchronousSpeedRpm` | r/min |

## Engineering Principles

One electrical cycle advances the field by two poles, so the mechanical revolutions per second are \(2f/p\), which is \(120f/p\) in revolutions per minute. The speed is the field speed. The result warning states that an induction motor runs below this speed and that slip is not calculated here.

## Worked Example

\(f = 60\,\mathrm{Hz}\), \(p = 4\).

$$
n_s = 120 \times 60 / 4 = 1800\,\mathrm{r/min}.
$$

Result: **1800 r/min**.

Boundary: \(f = 50\,\mathrm{Hz}\), \(p = 2\) gives **3000 r/min**. \(f = 400\,\mathrm{Hz}\), \(p = 2\) gives **24000 r/min** and is accepted. \(f = 400.1\,\mathrm{Hz}\) is rejected. \(p = 3\) is rejected because it is not an even integer. \(p = 22\) is rejected.

## Limitations

- Single supply frequency. Harmonics, pole-changing windings, and converter modulation are excluded by the assumptions text.
- Not a nameplate check and not permission to apply a motor.
- Slip, torque, and current are other tools.

## Reference Standards

No standards URL was extracted from this calculation closure. **Pending.**

## Online Calculator

https://powerengineerlab.com/calculators/synchronous-speed/

Inventory tool ID: `synchronous-speed`.

## Related Formulas

- [Induction-motor slip](induction-motor-slip.md)
- [Kilowatt to mechanical horsepower](kilowatt-to-horsepower.md)
- [Transformer full-load current](transformer-full-load-current.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `synchronous-speed` (`BACKLOG-070`) |
| Evidence | Production bundle: `120*frequencyHz/poles` and the even-pole domain |
| Method | Direct arithmetic, including the 400 Hz and odd-pole boundaries |
| Example result | 1800 r/min at 60 Hz and 4 poles |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
