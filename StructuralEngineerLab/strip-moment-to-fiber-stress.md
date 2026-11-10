# A 5 m strip’s moment, then the fiber stress

Locale: en

## Order

Geometry first, so the section modulus exists before the moment does. Then a simply supported uniform load on a 5 m span. Then \(\sigma = M/S\). Deflection is not required for that stress, and Euler buckling is a different check on a different demand.

## Rectangle

Width \(b = 80\,\mathrm{mm}\), depth \(h = 160\,\mathrm{mm}\), strong axis about the width.

$$
I_x = \frac{b h^{3}}{12} = 2.730667\times 10^{-5}\,\mathrm{m^4}
$$

$$
S_x = \frac{I_x}{h/2} = \frac{b h^{2}}{6} = 3.413333\times 10^{-4}\,\mathrm{m^3}
$$

The section tool’s centroid for this solid rectangle is at mid-depth. \(S_x\) is what the bending-stress tool accepts in section-modulus mode.

## Moment the beam page would return

Span 5 m, uniform load 3.2 kN/m over the whole span, simple supports.

$$
M_{\max} = \frac{wL^{2}}{8} = \frac{3.2\times 25}{8} = 10\,\mathrm{kN\cdot m}
$$

Reactions are \(wL/2 = 8\,\mathrm{kN}\) each. Those reactions do not enter \(\sigma = M/S\). They would enter a shear check, which this pair of tools is not doing.

## Stress

$$
\sigma_{\mathrm{bottom}} = \frac{10\times 1000}{3.413333\times 10^{-4}} = 2.9296875\times 10^{7}\,\mathrm{Pa} = 29.297\,\mathrm{MPa}
$$

The sign convention on the stress tool: positive moment tensions the bottom fiber and compresses the top, so \(\sigma_{\mathrm{top}} = -29.297\,\mathrm{MPa}\). The governing magnitude is 29.297 MPa. That is elastic flexure. It is not an allowable and not a utilization.

## What a 10% load change does

Raise the uniform load from 3.2 to 3.52 kN/m and the moment becomes 11 kN·m, so the stress becomes 32.226 MPa. The section modulus does not change. Raise the depth and \(S_x\) changes with \(h^{2}\) while the moment stays 10 kN·m. The two tools meet only at \(M\) in newton-metres and \(S\) in cubic metres. A moment left in kN·m and a modulus left in cm³ will be off by \(10^{9}\) if you skip the tool’s unit factors (\(1\,\mathrm{kN\cdot m} = 1000\,\mathrm{N\cdot m}\), \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\)).

## Limits

- Elastic, one axis, no shear lag, no lateral buckling.
- Self-weight is inside the 3.2 kN/m only if you already included it there.
- The simply-supported guide on the site and the bending-stress guide each have their own numerical examples. This 80 mm × 160 mm strip at 3.2 kN/m is not those examples.
- No design code was opened. 29.297 MPa is not a pass.

## Tools

- Section: https://structuralengineerlab.com/tools/moment-of-inertia-calculator/
- Beam moment: https://structuralengineerlab.com/tools/beam-analysis-calculator/
- Stress: https://structuralengineerlab.com/tools/beam-bending-stress-calculator/

## Online Calculator

The stress page is where \(M\) and \(S\) meet:

https://structuralengineerlab.com/tools/beam-bending-stress-calculator/

## Related Formulas

- [Centroidal area and section modulus](section-properties.md)
- [Full uniform load on a simple span](simply-supported-uniform-load.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Rectangle \(I\) and \(S\); simple-beam \(wL^{2}/8\); \(\sigma = M/S\) |
| Evidence | Python replay. Beam moment also matches the production solver identity used for the uniform-load note. No browser session |
| Dedup scope | Structural guides for bending stress, simply supported beams, and section modulus were read 2026-11-10. Not a web-wide scan |
| Example result | \(S_x = 3.413\times 10^{-4}\,\mathrm{m^3}\), \(M = 10\,\mathrm{kN\cdot m}\), 29.297 MPa |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |