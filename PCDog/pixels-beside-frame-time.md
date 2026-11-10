# Backing-store pixels sit beside frame time. They do not multiply.

Locale: en

## Two instruments

The screen-information page can report a backing-store size from `screen.width`, `screen.height`, and `devicePixelRatio`. The refresh-rate page summarizes intervals from `requestAnimationFrame`. A 2560×1440 panel at device pixel ratio 2 is not a frame time, and a 8.3 ms interval is not a resolution. Their product is not a bitrate and not a bandwidth this site will accept.

## Pixels, as a formula, not as this machine

Assumed inputs, not a browser reading of the computer that wrote this note:

$$
W = \operatorname{round}(2560\times 2) = 5120, \qquad H = \operatorname{round}(1440\times 2) = 2880
$$

`Math.round` is what the page uses. A missing ratio becomes 1, which would have left the size at 2560×1440. The page also reports color depth and refresh when the browser supplies them. Those fields were not read here. 5120×2880 is the arithmetic result of the assumed inputs.

## Frame times, as a formula, not as a captured trace

Twenty-two intervals of 8.3 ms and two of 20 ms, in that order, 24 kept samples. The page wants at least 20. Sorted, the median of 24 values is the average of the 12th and 13th, both 8.3 ms, so the median is 8.3 ms. The fence is \(\max(3\times 8.3,\, 8.3+12) = 24.9\,\mathrm{ms}\). Neither sample is above it, so nothing is dropped and the outlier fraction is 0. The p95 index is \(\lceil 0.95\times 24\rceil - 1 = 22\), and the sorted value there is 20 ms. Jitter is the median of \(|x-8.3|\): twenty-two zeros and two values of 11.7, so that median is 0. A long frame is anything above \(1.5\times 8.3 = 12.45\,\mathrm{ms}\): the two 20 ms samples, \(2/24 = 8.33\%\).

Score, with jitter 0 ms, long-frame percent 8.33, and outlier fraction 0:

$$
\operatorname{clamp}\!\left(\operatorname{round}(100 - \min(35, 0) - \min(45, 4\times 8.33) - \min(20, 0)),\, 0,\, 100\right) = 67
$$

Estimated rate is \(\mathrm{Number}((1000/8.3).\mathrm{toFixed}(1)) = 120.5\,\mathrm{Hz}\). Confidence is low because \(n = 24\) is under 60. The page says the score is a smoothness summary, not a hardware certification. This replay did not call `requestAnimationFrame`.

## Why the product is refused

\(5120\times 2880\times 120.5\) is a number of pixels per second only if every frame actually repaints every backing-store pixel, which neither tool measured. The bandwidth calculator on the networking site wants bytes and a rate. These two PC tools do not emit bytes. Do not paste 5120 into a bandwidth field and call it a payload.

A visual monitor checklist (dead pixels, glow, gray, cadence) is a different page. It does not compute 67.

## Limits

- Assumed geometry and assumed intervals. Not a screenshot of pcdog.org and not a trace from a panel.
- Two long frames in a 24-sample list move the score by the formula above. A real session can drop the first samples; this list did not.
- No claim about a cable, a GPU, or a refresh setting in an operating system.

## Tools

- Backing store: https://pcdog.com/tools/screen-information
- Intervals: https://pcdog.com/tools/refresh-rate-test

## Online Calculator

If you have a real panel in front of you, the pixel report is the screen page. The 5120×2880 above is the formula, not that report:

https://pcdog.com/tools/screen-information

## Related Formulas

- [Estimated backing pixels from the screen API](screen-backing-pixel-estimate.md)
- [Refresh estimate from a list of frame intervals](refresh-frame-interval-summary.md)

## Verification

| Item | Value |
|---|---|
| Source tools | `Math.round(screen × devicePixelRatio)`; refresh median, p95, fence, long-frame fraction, and score |
| Evidence | Arithmetic replay. Node was not required for `Math.round` of these integers |
| Not done | No browser, no `requestAnimationFrame`, no reading of this machine’s `screen` object |
| Dedup scope | New-monitor checklist and the older 1920×1080 / 16.6 ms notes. Not a web-wide scan |
| Example result | 5120×2880 beside 120.5 Hz, score 67, confidence low |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |