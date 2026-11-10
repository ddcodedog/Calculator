# Does the ditch pass the lot peak?

## Pass rule used here

The rational-method tool produces a peak in cubic metres per second. The Manning tool produces a channel capacity in the same unit when you give it a depth. The ditch passes **this** check only when Manning \(Q\) is at least the rational \(Q\). The runoff coefficient and Manning \(n\) are not added, and neither tool certifies a permit.

## Lot peak

Catchment 1.5 ha, \(C = 0.55\), intensity 40 mm/h. The SI conversion inside the rational tool is area × 10,000 and intensity divided by \(3.6\times 10^{6}\):

$$
Q_{\mathrm{peak}} = 0.55\times\frac{40}{3.6\times 10^{6}}\times 15000 = 0.0916667\,\mathrm{m^3/s}
$$

No time of concentration is computed. The 40 mm/h is an input, not a lookup.

## Ditch at the depth you are willing to see

Rectangle, bottom 0.60 m, depth 0.40 m, slope 0.002, \(n = 0.015\). SI Manning with \(1/n\), not 1.486:

$$
A = 0.24\,\mathrm{m^2},\quad R = 0.24/1.4 = 0.171429\,\mathrm{m}
$$

$$
Q_{\mathrm{ditch}} = 0.24\times\frac{1}{0.015}\times 0.171429^{2/3}\times\sqrt{0.002} = 0.220813\,\mathrm{m^3/s}
$$

Spare at this depth = \(0.220813 - 0.091667 = 0.129146\,\mathrm{m^3/s}\). The inequality holds. Velocity in the ditch is 0.920 m/s.

## The slope that reverses the answer

Same section, slope 0.0002, which is ten times flatter. Discharge scales with \(\sqrt{S}\), so capacity becomes 0.069827 m³/s. That is **below** 0.091667 m³/s. The lot peak did not change. The pass became a fail because the channel input changed. Freeboard, inlets, and tailwater are still unchecked either way.

## What must not be mixed

- Do not add \(C = 0.55\) to \(n = 0.015\).
- Do not type the rational peak into Manning as a roughness.
- Do not treat the spare 0.129 m³/s as storage volume. The site-drainage comparator would want pipe length, excavation, and outfalls, which this pair does not have.
- A US hand formula \(Q = CiA\) in cfs is a different arrangement. This comparison stayed in the SI product both tools actually run.

## Limits

- One catchment, one intensity, one prismatic rectangle, uniform flow.
- \(C\) and \(n\) are typed. No land-use table and no FHWA chart was opened.
- Passing this inequality is not a drainage approval.

## Tools

- Peak: https://waterengineerlab.com/tools/rational-method-peak-runoff/
- Capacity: https://waterengineerlab.com/tools/manning-open-channel-flow/

The learn page “check storm drain capacity” works a 1.2 m pipe. This note is an open ditch and a 1.5 ha lot, and it stops at the inequality.

## Online Calculator

After the peak exists, the capacity page is the one that can fail the slope:

https://waterengineerlab.com/tools/manning-open-channel-flow/

## Related Formulas

- [Rational-method peak runoff](rational-method-peak-runoff.md)
- [Manning open-channel discharge](manning-open-channel-flow.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Rational \(Q=CiA\) after SI conversion; Manning \(Q=A(1/n)R^{2/3}S^{1/2}\) |
| Evidence | Python replay of both production formulas. No browser session |
| Dedup scope | Water learn pages for rational method, Manning storm-drain check, and the reviewable-calculations page, read 2026-11-10. Not a web-wide scan |
| Example result | 0.091667 m³/s versus 0.220813 m³/s at slope 0.002; fail at slope 0.0002 |
| Date | 2026-11-10 |
| Status | VERIFIED |
