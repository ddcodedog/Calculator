# Refresh estimate from a list of frame intervals

## Overview

The refresh-rate test summarizes frame intervals the browser already collected. It does not read the monitor’s EDID refresh. Given at least 20 positive finite intervals, it drops long outliers, takes a median, and converts that median to hertz. The score that sits beside the hertz value is a penalty on jitter, long frames, and the outlier fraction. It is not a pass/fail from a display specification.

The summary function in chunk `38jyx3t4_ei-3.js`, measurement prefix `measurement.display.refresh-rate-test`, was read on 2026-11-08. The intervals below are an assumed sample, long enough to pass the 20-interval gate and short enough to show the low-confidence branch. No `requestAnimationFrame` loop was run.

## Formula

Keep finite intervals greater than 0. If fewer than 20 remain, hertz, median, p95, jitter, long-frame percent, and score are null and confidence is `low`.

Median \(m_0\) is the middle value after sorting, or the mean of the two middle values when the count is even. The outlier fence is \(\max(3 m_0,\; m_0+12)\) milliseconds. Intervals above the fence are counted as outliers and removed. If fewer than 20 remain, the same null result is returned.

On the kept list, median \(m\), then

$$
f = \mathrm{Number}\big((1000/m).\mathrm{toFixed}(1)\big)
$$

P95 uses index \(\min(n-1,\;\max(0,\;\lceil 0.95 n\rceil-1))\) on the sorted kept list. Jitter is the median of \(|x-m|\). A long frame is a kept interval greater than \(1.5 m\), and the long-frame percent is that count over \(n\), times 100, passed through `toFixed(2)`. Outlier fraction \(p\) is outliers divided by the pre-fence count. Confidence is `high` when \(n\ge 110\) and \(p\le 0.05\), `medium` when \(n\ge 60\) and \(p\le 0.15\), otherwise `low`. The score is

$$
\mathrm{clamp}\Big(\mathrm{round}\big(100-\min(35,12 j)-\min(45,4 c)-\min(20,100 p)\big),\; 0,\; 100\Big)
$$

where \(j\) is jitter in milliseconds and \(c\) is the long-frame percent.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| intervals | Positive frame deltas | ms |
| median | Median of kept deltas | ms |
| estimatedHz | 1000 divided by that median | Hz |
| long-frame percent | Share above 1.5 medians | % |
| score | Penalty score | 0–100 |

## Engineering Principles

A steady 16.6 ms median is about 60 Hz only after the 1000/median rounding. Four slower frames in a 24-frame list can leave the median, and therefore the hertz value, on the fast cluster, while the long-frame term still cuts the score. Confidence stays low until the kept count reaches 60, so a tidy 24-frame sample is still a low-confidence estimate.

## Worked Example

Twenty intervals of 16.6 ms and four intervals of 40 ms. All are positive and finite.

1. Median of the 24 values is 16.6 ms. Fence = \(\max(49.8,\; 28.6) = 49.8\) ms. The 40 ms values stay. Outliers = 0.
2. Kept median = 16.6 ms. Estimated rate = \(\mathrm{Number}((1000/16.6).\mathrm{toFixed}(1)) = 60.2\) Hz.
3. P95 index = \(\lceil 0.95\times 24\rceil-1 = 22\). Sorted index 22 is 40 ms.
4. Absolute deviations are twenty zeros and four values of 23.4. Their median is 0, so jitter is 0.
5. Long-frame threshold = \(1.5\times 16.6 = 24.9\) ms. Four frames qualify. Percent = \(4/24\times 100 = 16.666\ldots\), stored as 16.67.
6. Score = \(\mathrm{round}(100-\min(45,\;4\times 16.666\ldots)) = \mathrm{round}(55) = 55\). Kept count 24 is below 60, so confidence is `low`.

A list of 19 positive intervals returns null hertz and confidence `low` without a score. That gate is the reason this example uses 24.

## Limitations

- The sampler that produces the intervals was not run. Feeding these 24 numbers through the summary is the check.
- Score weights 12, 4, and the 35/45/20 caps are the function’s constants, not a published display standard.
- A hidden tab or an aborted signal is handled before this summary and can return a partial result with null hertz.

## Reference Standards

No VESA timing document is referenced in the summary function. Status: pending.

## Online Calculator

The refresh-rate test collects its own intervals and then runs this summary:

https://pcdog.com/tools/refresh-rate-test

## Related Formulas

- [IPv4 longest prefix match](ipv4-longest-prefix-match.md)
- [IPv4 static route commands](ipv4-static-route-commands.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PCDog refresh-rate test summary |
| Evidence | Production median, fence \(\max(3m, m+12)\), p95 index, long-frame threshold \(1.5m\), and score expression |
| Method | Node replay of that function on 20×16.6 ms and 4×40 ms |
| Example result | 60.2 Hz, p95 40 ms, long frames 16.67%, score 55, confidence low |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
