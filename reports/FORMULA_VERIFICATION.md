# Formula verification — GATE 4, batch 1

- Date: 2026-11-04
- Doc version on each topic: 1.0.0
- Machine-readable copy: [FORMULA_VERIFICATION.json](FORMULA_VERIFICATION.json)

`VERIFIED` in this report means all of the following:

1. The formula was read from the production calculator’s JavaScript on 2026-11-04, not written from a generic textbook memory.
2. Units in the document match the conversions in that code.
3. At least one normal example was recomputed in Python from those expressions.
4. A boundary case was evaluated where the code defines one (domain reject, zero, clamp, or a second regime).

It does **not** mean a design code PDF was re-audited. Where a standard URL is missing or the PDF body was not checked, the topic says **pending** in Reference Standards even though the arithmetic is `VERIFIED`.

The inventory local paths (`D:\...`) were not available. The only other public `ddcodedog` repository, `fiber-loss-calculator`, is a different page and was not used.

## Batch count

| Site | Topics | Tool IDs |
|---|---:|---|
| NetEngineerLab | 6 | `fiber-loss`, `optical-power-budget`, `fiber-latency-calculator`, `chromatic-dispersion-calculator`, `ospf-cost-calculator`, `stp-path-cost-calculator` |
| PowerEngineerLab | 9 | `ohms-law`, `power-triangle`, `inductive-reactance`, `capacitive-reactance`, `voltage-divider`, `transformer-full-load-current`, `synchronous-speed`, `motor-slip`, `kw-to-hp` |
| StructuralEngineerLab | 3 | `TOOL-004`, `TOOL-003`, `TOOL-008` |
| WaterEngineerLab | 3 | `TOOL-007`, `TOOL-003`, `TOOL-010` |
| HVACEngineerLab | 1 | `duct-airflow-design` |
| DIYCalcLab | 3 | `concrete-slab`, `roof-pitch`, `board-foot` |
| **Total** | **25** | |

No count shortfall. The rest of the 375 inventory rows are out of this batch on purpose.

## Verified topics

| Document | Example recomputed | Boundary checked |
|---|---|---|
| [Single-span fiber link loss](../NetEngineerLab/fiber-link-loss.md) | 10 km × 0.25 dB/km + splices + connectors + 21 dB splitter = 25.30 dB physical, 28.30 dB design | Available budget 28 dB → failed; zero length drops only fiber loss |
| [Optical link power budget](../NetEngineerLab/optical-power-budget.md) | Design loss 11.40 dB, remaining 17.60 dB | Overload threshold −8 dBm fails while sensitivity margin stays positive |
| [Fiber propagation delay and RTT](../NetEngineerLab/fiber-propagation-latency.md) | 100 km, \(n_g=1.468\), \(c=299792.458\) km/s → 489.672 µs one way | Route factor &lt; 1 and \(n_g\) outside 1…1.6 rejected; 1500-byte serialization = 24 µs for 2 hops at 1 Gbit/s |
| [Chromatic dispersion coefficient D(λ)](../NetEngineerLab/chromatic-dispersion.md) | \(D(1550)=17.46062\ldots\) ps/(nm·km); 80 km → 1396.8 ps/nm displayed | Tolerance 800 ps/nm fails |
| [OSPF interface cost](../NetEngineerLab/ospf-interface-cost.md) | Reference 100000 Mbit/s, ceil: 1G→100, 10G→10, 100M→1000 | Faster than reference clamps to cost 1; override outside 1…65535 errors |
| [STP port path cost](../NetEngineerLab/stp-path-cost.md) | Long: 2000+2000 vs 20000. Short: 2+2 vs 4, tie | Short method rejects 100 Gbit/s |
| [DC Ohm’s law](../PowerEngineerLab/ohms-law.md) | 12 V / 6 Ω = 2 A, 24 W | \(R=0\) rejected; \(V=0\) yields 0 A |
| [Sinusoidal power triangle](../PowerEngineerLab/power-triangle.md) | 3 kW and 4 kvar → 5 kVA, pf 0.6, 53.130° | Zero power makes pf and angle null; negative \(P\) rejected |
| [Ideal inductive reactance](../PowerEngineerLab/inductive-reactance.md) | \(2\pi\cdot 60\cdot 0.1 = 37.69911\ldots\) Ω | \(f=0\) → 0 Ω |
| [Ideal capacitive reactance](../PowerEngineerLab/capacitive-reactance.md) | \(1/(2\pi\cdot 60\cdot 100\,\mu\mathrm{F}) = 26.52582\ldots\) Ω | \(f=0\) → null (open circuit) |
| [Resistive voltage divider](../PowerEngineerLab/voltage-divider.md) | 12 V, 1 kΩ/1 kΩ, 1 kΩ load → 4 V loaded, 6 V open, 8 mA | No load → 6 V and 6 mA |
| [Transformer full-load current](../PowerEngineerLab/transformer-full-load-current.md) | 100 kVA, 480 V, three-phase → 120.2813… A | Single-phase 10 kVA / 240 V → 41.666… A; \(V\le 0\) rejected |
| [AC machine synchronous speed](../PowerEngineerLab/synchronous-speed.md) | 60 Hz, 4 poles → 1800 r/min | 400 Hz and 2 poles accepted; odd pole count rejected |
| [Induction-motor slip](../PowerEngineerLab/induction-motor-slip.md) | 1750 r/min on 1800 r/min field → slip \(1/36\) | Slip 0 at synchronous speed; rotor above \(2n_s\) rejected |
| [Kilowatt to mechanical horsepower](../PowerEngineerLab/kilowatt-to-horsepower.md) | 7.5 kW → 10.05767… hp using 745.6999 W | zh-CN path uses 735.49875 and is a different unit; \(P\le 0\) rejected |
| [Euler elastic column buckling load](../StructuralEngineerLab/euler-column-buckling.md) | 200 GPa, 100 cm⁴, \(K=1\), \(L=3\) m → 219324.5 N | \(K=2\) divides the load by 4; omitted area skips stress |
| [Elastic beam bending stress](../StructuralEngineerLab/beam-bending-stress.md) | 10 kN·m / 200 cm³ = 50 MPa | Zero moment → 0; negative moment flips fiber signs |
| [Centroidal area and section modulus](../StructuralEngineerLab/section-properties.md) | 0.1 m × 0.2 m rectangle, \(I_x=bh^3/12\) | Hollow circle with inner diameter ≥ outer is rejected |
| [Manning open-channel discharge](../WaterEngineerLab/manning-open-channel-flow.md) | \(b=2\) m, \(y=1\) m, \(S=0.001\), \(n=0.013\) → 1.532 m/s, 3.065 m³/s | Bisection recovers depth 1 m for that discharge. US inputs are converted with 0.3048 and then use \(1/n\), not 1.486 |
| [Rational-method peak runoff](../WaterEngineerLab/rational-method-peak-runoff.md) | 10 ha, \(C=0.8\), 50 mm/h → \(10/9\) m³/s | US acre and in/h factors checked; \(C>1\) rejected |
| [Darcy-Weisbach major pipe headloss](../WaterEngineerLab/darcy-weisbach-pipe-headloss.md) | 0.01 m³/s, \(D=0.1\) m, \(L=100\) m, \(f=0.02\) → \(h_f=1.653\) m | \(f=0\) rejected. Constant 19.6133 is \(2\times 9.80665\) |
| [Duct friction and local pressure drop](../HVACEngineerLab/duct-friction-pressure-drop.md) | 0.5 m³/s, 0.3 m round, 20 m, \(K=0.5\) → 54.251 Pa | 0.005 m³/s in a 0.5 m duct uses \(f=64/\mathrm{Re}\) |
| [Concrete slab volume and bag count](../DIYCalcLab/concrete-slab-volume.md) | 10 ft × 10 ft × 4 in, 10% waste, 80 lb bags → 62 bags | 0% waste → 56 bags; zero thickness → 0 bags |
| [Roof pitch and slope factor](../DIYCalcLab/roof-pitch.md) | 6 in in 12 in → 6/12, 26.565°, factor \(\sqrt{1.25}\) | Angle 0° → factor 1; angle above 80° is clamped |
| [Board-foot lumber volume](../DIYCalcLab/board-foot.md) | 2×6×8 ft × 10 = 80 BF | Zero thickness → 0. 1 BF = \(144\times(0.0254)^3\) m³ |

## Standards evidence beyond the formula code

| Topic | What was checked outside the calculator |
|---|---|
| Kilowatt to horsepower | NIST Fed. Std. 376B PDF (https://www.nist.gov/system/files/documents/2017/05/09/fs376-b.pdf), section 5.2.13: horsepower (550 ft·lbf/s) multiplies by 745.699 9 to give watts. Text extracted 2026-11-04. The metric 735.49875 factor is only in the zh-CN code path; FS 376B lists metric horsepower as a unit not to be used and does not print 735.49875. |
| Ohm’s law | OpenStax URL in the bundle returns HTTP 200. Page body was not transcribed. |
| Fiber loss, chromatic dispersion, STP | Production HTML cites ITU or IEEE URLs. Those PDFs were not re-read. The engines match the formulas the pages state. |
| All other topics | No resolvable standard URL in the calculation script, or only an internal source id. Marked pending in the topic. |

## Deferred on purpose

These were looked at far enough to see that a honest page would be longer than a closed formula, or that the public bundle did not expose a single equation cleanly enough for this batch. They are **not** `VERIFIED` and have no topic file.

| Tool | Why it is not in batch 1 |
|---|---|
| PowerEngineerLab `voltage-drop-cable-sizing` | Several resistance models and grouping factors in one large chunk. Easy to mis-state a branch. |
| StructuralEngineerLab simply-supported beam tools | Singularity / EI integration rather than one closed form. Not extracted line by line. |
| HVACEngineerLab psychrometric and plant planners | Shared engines plus a PsychroLib adapter. Not reduced to one checked equation here. |
| NetEngineerLab PoE voltage drop | Quadratic loop solution is in `engine.js` and could be a later topic. Left out so this batch stayed on formulas that are short enough to recompute in full. |
| NetEngineerLab bandwidth and MTU tools | Unit tables and overhead libraries, not a single engineering formula. |
| DIYCalcLab remaining material calculators | Same bundle pattern as the three that were published. Not all 40 were read. |
| AIMarkTool, PCDog, DataFileLab, DevEngineerLab, PrivacyFileLab | Outside the requested first-batch sites, and mostly non-formula tools. |

## Reproduction

Python 3, standard library `math` only, using the constants copied from the bundles (`Math.PI`, 0.3048, 0.0254, 9.80665, 299792.458, 745.6999, Manning \(1/n\), rational-method scale factors, duct \(f\) branches). Results are recorded in the topic files. No production POST endpoint was required; the calculators run in the browser from these scripts.

## Tool notes added 2026-11-07

Twenty-two topic files were added after batch 1. The machine-readable list in [FORMULA_VERIFICATION.json](FORMULA_VERIFICATION.json) is the full set. `countVerified` counts rows whose status is `VERIFIED` only.

| Site | Topics added | Status |
|---|---:|---|
| NetEngineerLab | bandwidth transfer time, MTU/MSS | VERIFIED |
| PowerEngineerLab | transformer turns ratio, same-interval load factor | VERIFIED |
| HVACEngineerLab | cooling/heating load components, psychrometric process | VERIFIED |
| WaterEngineerLab | catchment runoff summary, tree residual head | VERIFIED |
| StructuralEngineerLab | cantilever tip case, simply supported midspan case | REVIEW_REQUIRED |
| DIYCalcLab | fence quantities, rebar grid | VERIFIED |
| AIMarkTool | ROAS, order-value LTV/CAC | VERIFIED |
| DataFileLab | CSV frequency, encoding detection | VERIFIED |
| DevEngineerLab | Unix timestamp, integer base conversion | VERIFIED |
| PCDog | IPv4 longest prefix, static-route command text | VERIFIED |
| PrivacyFileLab | local SHA-256, text-pattern redaction | VERIFIED |

The two structural pages recompute the closed form printed on the public guide. The page script confirms the support conditions. The general EI integrator was not extracted line by line, so those two rows stay `REVIEW_REQUIRED`. Batch 1’s deferred list above is the historical scope note; it is not a claim that those later files are absent.

AIMarkTool results were checked with the production POST API. The other new pages were recomputed from production JavaScript or, for the beam closed forms, from the published guide identity. Non-formula tools are documented as the algorithm or input-output rule they actually implement.

## Original tool notes added 2026-11-08

Nineteen topic files were added from tools that were not already written up on main and were not the same formulas as unmerged PR 4. Examples were newly chosen and recomputed. `countVerified` is 64 because the two earlier structural rows remain `REVIEW_REQUIRED`. HVAC has no new file: its 13 English sitemap tools are already on main or in that PR. Water has one new file. The stormwater planner’s executed diameter path repeats the Manning relation already proposed in PR 4, so a second water note was not written.

| Site | Topics added | Status |
|---|---:|---|
| NetEngineerLab | DNS TTL baseline, switch-uplink baseline | VERIFIED |
| PowerEngineerLab | demand factor, appliance period energy | VERIFIED |
| HVACEngineerLab | none | gap of 2 |
| WaterEngineerLab | site-drainage scenario score | VERIFIED, gap of 1 |
| StructuralEngineerLab | off-center point load, full uniform load | VERIFIED from `solver.js` |
| DIYCalcLab | modular brick count, blown-fiberglass bags | VERIFIED |
| AIMarkTool | funnel counts, equal-group sample size | VERIFIED via production POST |
| DataFileLab | blank-record removal, row-number column | VERIFIED |
| DevEngineerLab | grapheme wrap, text size counts | VERIFIED |
| PCDog | backing-pixel estimate, refresh-interval summary | VERIFIED from production JS, not a browser run |
| PrivacyFileLab | metadata type diff, clean-file verifier status | VERIFIED |

## Cross-tool topics added 2026-11-10

Twenty-two topic files, two per site, each built around one decision and at least two tools on that same site. They do not replace the single-tool notes above, and the two structural `REVIEW_REQUIRED` rows are unchanged. `countVerified` is 86.

| Site | Topics added | What the pair decides |
|---|---|---|
| NetEngineerLab | cutover wait versus fiber delay; on-wire bytes at the safe uplink | Minutes of DNS cache are not a fiber RTT. Header bytes, safe uplink, and transfer time stay in that order. |
| PowerEngineerLab | three shop ratios; divider is not a winding | Load factor and demand factor are not multiplied. A divider tap is not a transformer secondary. |
| HVACEngineerLab | mass flow into duct velocity; latent sign is not condensate | Specific volume can become a duct flow. Watts are not pascals. A positive latent term is moisture added. |
| WaterEngineerLab | ditch capacity versus lot peak; one-pipe residual matches Darcy | Rational peak is compared with Manning capacity. One pipe’s Darcy loss is the tree residual only until a second demand appears. |
| StructuralEngineerLab | strip moment to fiber stress; axial ratio beside Euler | \(M/S\) uses the strip moment. Utilization is force over an Euler load, not stress over kilonewtons. |
| DIYCalcLab | 18 by 9 slab and mat; rafter length into board feet | One pad feeds bags and a rebar mat. Pitch length is the board-foot length, and nominal and dressed are alternative bills. |
| AIMarkTool | one count, two ratios; planned sample versus arrivals | Production POST on 2026-11-10. ROAS and LTV/CAC match only for this one-purchase case. 8155 planned visitors are not the 40 already counted. |
| DataFileLab | encoding, blank row, then city tally; do not tally the row number | Order of the three file tools changes the city bucket. The inserted row-number column is not a city. |
| DevEngineerLab | wrap then recount; one integer, two tools | Wrap changes lines and not tokens. The same digits are a UTC instant in one tool and hex in the other. |
| PCDog | longer prefix then the route command; pixels beside frame time | The /24 wins, then the Linux template prints that prefix. Backing-store pixels are not multiplied by hertz. No `requestAnimationFrame` run. |
| PrivacyFileLab | hash only after the verifier; a different digest on a failed diff | SHA-256 of the accepted after text. A remaining US phone stays `VERIFICATION_FAILED` even if the digest changed. No browser download. |

Live guide, case, and topic pages closest to these decisions were read on 2026-11-10 so the datasets would not repeat those pages. That reading is not a web-wide similarity scan. Non-English site locales were not read in full.

## Calculation status and standards status (2026-11-10)

`status` in the table above remains the calculation status. It is not a standards verdict.

| Status field | Meaning on 2026-11-10 |
|---|---|
| Calculation status | `VERIFIED` for 86 topics whose arithmetic was recomputed from the production engine or the published identity. `REVIEW_REQUIRED` for the two structural notes whose general EI integrator was not line-traced. |
| Standards status | `VERIFIED` for one topic, kilowatt to horsepower, after Fed. Std. 376B section 5.2.13 was read again on 2026-11-10. `PENDING` for the other 87. `NOT_APPLICABLE` for none. |

The mechanical horsepower factor 745.699 9 W is the standards claim. The metric factor 735.49875 is still only a code constant. OpenStax section 9.4 was read on 2026-11-10 and does state I = V/R, but the fetched page has no ISBN, so Ohm's law stays `PENDING`. The two beam notes were recomputed again and stay `REVIEW_REQUIRED`.
