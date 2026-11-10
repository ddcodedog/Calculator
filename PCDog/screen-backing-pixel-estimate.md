# Estimated backing pixels from the screen API

Locale: en

## Direct Answer

The screen-information test reads the browser’s screen size and device-pixel ratio, then estimates a backing-pixel width and height. The production page says browser screen APIs usually report CSS coordinates rather than raw EDID pixels, and it labels the backing-pixel calculation as an estimate. This note does not claim a measured diagonal or a monitor model. Those are not available from the fields below (https://pcdog.com/tools/screen-information).


## Overview

The collector in chunk `38jyx3t4_ei-3.js`, test `test.display.screen-information` version 2.4.4, was read on 2026-11-08. No browser tab was driven. The example uses assumed reports from `screen.width`, `screen.height`, and `devicePixelRatio`.
## Formula

The collector stores

$$
r = \mathrm{devicePixelRatio} \text{ or } 1 \text{ when that value is missing}
$$

The displayed estimates are

$$
W_{\mathrm{est}} = \mathrm{round}(W_{\mathrm{screen}}\times r), \qquad H_{\mathrm{est}} = \mathrm{round}(H_{\mathrm{screen}}\times r)
$$

`round` is JavaScript `Math.round`. Color depth is copied when it is finite and is null otherwise. Those fields are measurements from the browser, not inputs you type into a formula form. The arithmetic itself is the two products above.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| screenWidth | `screen.width` | CSS px |
| screenHeight | `screen.height` | CSS px |
| devicePixelRatio | `window.devicePixelRatio`, or 1 | 1 |
| Estimated width, height | Rounded products | backing px |

## Engineering Principles

A ratio of 1.25 on a 1920 by 1080 CSS screen is 2400 by 1350 after rounding. That product can match a panel’s framebuffer and can also disagree with it, which is why the page calls it an estimate. A missing ratio must not be treated as zero: the code substitutes 1, and the estimate then equals the CSS size. Multiplying by a ratio you hoped the monitor had, instead of the ratio the browser reported, is a different calculation.

## Worked Example

Assumed browser report: `screen.width` 1920, `screen.height` 1080, `devicePixelRatio` 1.25. These values were not read from a machine in this check.

1. Width = \(\mathrm{round}(1920\times 1.25) = \mathrm{round}(2400) = 2400\).
2. Height = \(\mathrm{round}(1080\times 1.25) = \mathrm{round}(1350) = 1350\).

If `devicePixelRatio` is missing, \(r=1\) and both estimates stay 1920 and 1080. A ratio of 1.5 on a 1366 by 768 CSS screen gives \(\mathrm{round}(2049)=2049\) and \(\mathrm{round}(1152)=1152\). The runtime returns `unsupported` when `screen` or `navigator` is missing, and it does not invent those products.

## Limitations

- CSS pixels times a ratio are not an EDID native mode.
- Color gamut and HDR in the same payload are media-query booleans, not this multiplication.
- Refresh rate is sampled by a different function in the same test and is documented separately.
- No diagonal, pitch, or model string is computed.

## Reference Standards

The CSSOM view definition of `devicePixelRatio` was not re-read. Status: pending.
## Online Calculator

Open the screen-information test; the estimate appears after the browser reports a size and a ratio:

https://pcdog.com/tools/screen-information

## Related Formulas

- [IPv4 longest prefix match](ipv4-longest-prefix-match.md)
- [IPv4 static route commands](ipv4-static-route-commands.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PCDog `test.display.screen-information` 2.4.4 |
| Evidence | Production `Math.round(screenWidth * devicePixelRatio)` and the `|| 1` fallback |
| Method | Node `Math.round` on the assumed 1920×1080 at 1.25 |
| Example result | 2400 by 1350 backing pixels |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |