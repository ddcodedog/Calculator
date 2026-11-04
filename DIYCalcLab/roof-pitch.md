# Roof pitch and slope factor

## Overview

The Roof Pitch calculator converts a rise and a run, or a roof angle, into a pitch in the form \(x/12\), a slope angle, a percent grade, and a pitch factor. If a building span is entered, it also estimates ridge height and common-rafter line length.

Production module `roof-pitch` (`pitchFrom`, `angleOf`, and `pitchFactor` from the roofing module), fetched 2026-11-04 from https://diycalclab.com/roofing/roof-pitch-calculator/.

## Formula

Rise-and-run mode, after both lengths are converted to metres (the ratio is dimensionless):

$$
p = 12 \frac{\mathrm{rise}}{\mathrm{run}} \quad (\mathrm{run} > 0)
$$

Angle mode, with the typed angle clamped to 0…80 degrees:

$$
p = 12 \tan \theta
$$

$$
\theta = \arctan(p/12), \qquad g = 100\, p/12, \qquad k = \sqrt{1 + (p/12)^{2}}
$$

Optional gable geometry, span and overhang converted to metres:

$$
h_{\mathrm{ridge}} = \frac{\mathrm{span}}{2} \cdot \frac{p}{12}, \qquad L_{\mathrm{rafter}} = \left(\frac{\mathrm{span}}{2} + \mathrm{overhang}\right) k
$$

Imperial display divides metres by 0.3048 for feet and by 0.0254 for inches. The nominal label rounds \(p\) to the nearest 0.5 for a “\(n/12\)” phrase; the primary numeric pitch keeps the calculated value.

Slope class from the pitch number: below 2, “flat / low slope”; below 4, “low slope”; through 9, “conventional”; above 9, “steep.”

## Variables

| Name | Field | Imperial | Metric |
|---|---|---|---|
| Mode | `mode` | `rise-run` or `angle` | same |
| Rise, run | `rise`, `run` | inches (depth fields) | centimetres |
| Angle | `angle` | degrees, 0 to 80 | same |
| Span | `width` | feet | metres |
| Overhang | `overhang` | feet | metres |

## Engineering Principles

Pitch \(p/12\) is the vertical rise over a 12-unit horizontal run. The pitch factor is the secant of the roof angle, \(\sqrt{1+\mathrm{rise}^{2}/\mathrm{run}^{2}}\), and multiplies a horizontal plan length to get the slope length. Ridge height uses half the span because the module treats the span as wall-to-wall for a symmetric gable. It does not add a birdsmouth or a ridge-board thickness.

## Worked Example

Rise 6 in, run 12 in. Span 24 ft, overhang 0.

1. \(p = 12 \times 6/12 = 6\). Pitch **6/12** (the nominal half-step label is also 6/12).
2. \(\theta = \arctan(0.5) = 26.56505118\ldots^\circ\).
3. Grade \(= 50\%\).
4. \(k = \sqrt{1.25} = 1.1180339887\ldots\)
5. Half span \(= 12\,\mathrm{ft}\). Ridge height \(= 6\,\mathrm{ft}\). Rafter line length \(= 12 k = 13.41640786\ldots\,\mathrm{ft}\).

Result: **6/12**, angle **26.565°**, factor **1.11803**, ridge **6 ft**, rafter **13.416 ft**.

Boundary: angle mode at 0° gives pitch 0, factor 1, and the low-slope warning. An entered angle above 80° is clamped to 80° before the tangent. Run 0 in rise-run mode yields pitch 0. Pitch below 2 adds the page warning that asphalt shingles are not allowed and cites IRC R905.2.2 in that warning string. Pitch above 21 adds a steep-slope fastening warning. Those sentences are UI warnings, not calculations.

## Limitations

- Symmetric gable geometry only when span is used. Hip lengths and valleys are not computed here.
- Rafter length is the hypotenuse of half-span plus overhang. It is not a cut length.
- The IRC sentence is a warning string in the module. This library did not fetch the IRC text.

## Reference Standards

The module’s low-slope warning names IRC R905.2.2. No IRC URL is in the script, so the code citation is **pending** as a verified standard text. The pitch, angle, and factor formulas are from `roof-pitch` and `pitchFactor`.

## Online Calculator

https://diycalclab.com/roofing/roof-pitch-calculator/

Inventory tool ID: `roof-pitch`.

## Related Formulas

- [Concrete slab volume and bag count](concrete-slab-volume.md)
- [Board-foot lumber volume](board-foot.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `roof-pitch` |
| Evidence | `pitchFrom`, `angleOf` in `roof-pitch.*.js`, and `pitchFactor = sqrt(1+(p/12)^2)` in the roofing module |
| Method | Python `atan(0.5)` and `sqrt(1.25)` for the 6-in-12 case |
| Example result | 6/12, 26.565°, factor 1.118034, rafter 13.416 ft on a 24 ft span |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
