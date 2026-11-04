# Formula verification — GATE 4

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

## Batch 1 count

These 25 topics were the first release. Batch 2 is below.

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

## Batch 2 count

Date: 2026-11-04. Each topic was read from the production script and recomputed in Python. Reference standards stay pending except the RC page, whose OpenStax URL returned HTTP 200 and whose body was not transcribed.

| Site | New topics | Tool IDs |
|---|---:|---|
| NetEngineerLab | 10 | `pue-data-center-energy-efficiency`, `ethernet-serialization-delay-calculator`, `subnet-calculator`, `pmd-budget-calculator`, `poe-power-budget-calculator`, `poe-voltage-drop-calculator`, `pon-distance`, `pon-splitter-loss`, `all-reduce-traffic-estimator`, `wireless-link-budget-calculator` |
| PowerEngineerLab | 10 | `ac-power`, `battery-charging-time`, `battery-runtime`, `conductor-resistance`, `electrical-efficiency`, `motor-current`, `power-factor-correction`, `rc-time-constant`, `series-parallel-resistance`, `motor-torque` |
| HVACEngineerLab | 10 | `chilled-water-system-planner`, `condensate-drain-planner`, `data-center-cooling-planner`, `fan-selection-system-curve`, `hvac-energy-operating-cost-analyzer`, `building-energy-benchmark`, `outdoor-air-ventilation-planner`, `pipe-flow-pressure-drop`, `thermal-comfort-pmv-planner`, `pump-sizing-system-curve` |
| WaterEngineerLab | 9 | `TOOL-016`, `TOOL-011`, `TOOL-002`, `TOOL-009`, `TOOL-018`, `TOOL-004`, `TOOL-005`, `TOOL-013`, `TOOL-012` |
| StructuralEngineerLab | 4 | `TOOL-009`, `TOOL-002`, `TOOL-012`, `TOOL-010` |
| DIYCalcLab | 10 | `cubic-yard`, `deck-board`, `drywall`, `gravel`, `paint`, `mulch`, `sonotube`, `square-footage`, `stair`, `tile` |
| **Total** | **53** | |

Shortfall against 10 per site: Water 9, Structural 4. Reasons are in “Deferred on purpose”.

| Document | Example recomputed | Boundary checked |
|---|---|---|
| [Data center power usage effectiveness](../NetEngineerLab/data-center-pue.md) | PUE 1.428571429, facility 4380000 kWh/year, non-IT cost 157680 | zero IT power is rejected |
| [Ethernet serialization delay](../NetEngineerLab/ethernet-serialization-delay.md) | 1214.4 ns per hop, 3643.2 ns for 3 hops, wire 1230.4 ns | 1 hop equals the frame time; zero rate is rejected |
| [IPv4 subnet size](../NetEngineerLab/ipv4-subnet.md) | 192.168.10.20/26 → network 192.168.10.0, usable 62, broadcast 192.168.10.63 | /31 reports 2 usable hosts; prefix outside 0–32 is rejected |
| [Polarization-mode dispersion budget](../NetEngineerLab/pmd-budget.md) | mean DGD 1.8 ps, allowed 9.696969697 ps, ratio 0.185625 | zero length and zero components give DGD 0 |
| [PoE switch power budget](../NetEngineerLab/poe-power-budget.md) | 14.38888889 W per device, 138.1333333 W required | 100% cable loss is rejected; zero devices require 0 W |
| [PoE pair voltage drop](../NetEngineerLab/poe-voltage-drop.md) | loop 8.07768614 ohm, current 0.2921402254 A, end voltage 45.64018295 V | negative discriminant returns overload; pairs must be 2 or 4 |
| [PON maximum optical distance](../NetEngineerLab/pon-maximum-distance.md) | fiber allowance 2.7 dB, optical maximum 9 km, limiter optical | a 5 km system reach becomes the limiter; zero attenuation is rejected |
| [PON splitter and link loss budget](../NetEngineerLab/pon-splitter-loss.md) | physical 25.3 dB, design 28.3 dB, remaining 3.7 dB, status healthy | zero distance drops the 2.5 dB fiber term; unknown splitter loss is rejected |
| [Ring all-reduce traffic and time](../NetEngineerLab/ring-all-reduce.md) | 1.75 times 1.4e10 bytes, bandwidth time 0.6125 s, latency 70 µs | N = 1 gives a zero factor; zero link rate is rejected |
| [Wireless free-space link budget](../NetEngineerLab/wireless-link-budget.md) | FSPL 121.69796 dB, receive −57.69796 dBm, Fresnel radius 8.040608143 m | zero distance or frequency is rejected |
| [AC apparent real and reactive power](../PowerEngineerLab/ac-power.md) | S 6928.20323 VA, P 5542.562584 W, Q 4156.921938 var | power factor 1 gives Q = 0; power factor 0 is rejected |
| [Battery charging time](../PowerEngineerLab/battery-charging-time.md) | 4 h | taper 1 gives 3.333333333 h; zero current is rejected |
| [Battery energy and runtime](../PowerEngineerLab/battery-runtime.md) | 864 Wh and 8.64 h | efficiency 1 gives 960 Wh; zero load is rejected |
| [Conductor resistance and temperature](../PowerEngineerLab/conductor-resistance.md) | R20 0.172 ohm, R70 0.205798 ohm | temperature 20 °C returns R20; zero area is rejected |
| [Electrical efficiency and loss](../PowerEngineerLab/electrical-efficiency.md) | 0.85 and 150 W from 1000 W and 850 W | equal powers give eta 1; output above input is rejected |
| [Three-phase motor line current](../PowerEngineerLab/motor-line-current.md) | 14.15074189 A running, 84.90445135 A start, 17.90068849 A planned | margin 0 and service factor 1 leave I unchanged; eta or pf of 0 is rejected |
| [Power-factor correction kvar](../PowerEngineerLab/power-factor-correction.md) | 7500 var and 49.73591972 µF per branch | equal power factors give 0 var; leading load is rejected |
| [Series RC time constant](../PowerEngineerLab/rc-time-constant.md) | tau 1 s, charge voltage 6.321205588 V | discharge of the same RC is 3.678794412 V; non-positive R or C is rejected |
| [Series and parallel resistance](../PowerEngineerLab/series-parallel-resistance.md) | series 10+20+30 = 60 ohm | parallel of the same three is 5.454545455 ohm; R ≤ 0 is rejected |
| [Shaft torque from power and speed](../PowerEngineerLab/shaft-torque.md) | 53.0516477 N·m and 39.1288873 lbf·ft | zero speed is rejected |
| [Chilled-water flow and plant power](../HVACEngineerLab/chilled-water-flow.md) | 4.79427755 L/s, head 10.34144413 m, plant 18181.81818 W | zero water temperature rise is rejected |
| [Condensate from latent cooling load](../HVACEngineerLab/condensate-from-latent-load.md) | 14.69387755 L/h base, 18.36734694 L/h design | safety factor 1 removes the multiplier; k < 1 is rejected |
| [Data-center sensible cooling airflow](../HVACEngineerLab/data-center-sensible-airflow.md) | 99.40357853 kg/s and 82.83631544 m³/s; plant 200 kW | zero temperature rise is rejected; SHF changes heat and unit count, not airflow |
| [Fan air power and input](../HVACEngineerLab/fan-air-power.md) | 500 Pa and 1000 W air, 1709.401709 W input | zero flow is rejected; zero loss leaves static pressure only |
| [HVAC cooling electrical energy](../HVACEngineerLab/hvac-cooling-energy-cost.md) | 35000 kWh and cost 4200, peak 30 kW | load factor 0 leaves auxiliary energy only; blank demand rate omits demand cost |
| [Site energy use intensity](../HVACEngineerLab/illustrative-site-eui.md) | EUI 140, bin label 50 | EUI 80 labels 25; EUI just above 140 labels 75 |
| [Outdoor-air ventilation flow](../HVACEngineerLab/outdoor-air-ventilation-flow.md) | required 0.11 m³/s, CO₂ balance 0.1724137931 m³/s | equal CO₂ concentrations are rejected |
| [Darcy pipe pressure drop](../HVACEngineerLab/pipe-darcy-pressure-drop.md) | Re 89209.74149, f 0.01846758679, total head 4.98593713 m | Re below 2300 uses f = 64/Re; zero diameter is rejected |
| [Predicted mean vote](../HVACEngineerLab/pmv-ppd.md) | PMV −0.2137764882, PPD 5.947912698% | relative humidity 101 is rejected |
| [Pump head and hydraulic power](../HVACEngineerLab/pump-tdh-hydraulic-power.md) | head 18 m, hydraulic 1761.666606 W, input 2796.2962 W | zero flow is rejected; zero losses leave K = 0 |
| [Area-weighted runoff coefficient](../WaterEngineerLab/composite-runoff-coefficient.md) | C = 0.45 | zero total area is rejected |
| [Darcy required pipe diameter](../WaterEngineerLab/darcy-required-pipe-diameter.md) | required diameter 0.1832491273 m | zero allowable head or zero f is rejected |
| [Design-storm rainfall depth](../WaterEngineerLab/design-storm-rainfall-depth.md) | 50 mm | zero duration gives zero depth |
| [Hydraulic and energy grade lines](../WaterEngineerLab/hydraulic-energy-grade-line.md) | residual 1.557171919 m, not balanced | matching EGLs and zero loss are balanced |
| [Log-log IDF intensity](../WaterEngineerLab/idf-log-log-interpolation.md) | 25.36833891 mm/h and 12.68416945 mm | a corner query returns that corner; a non-positive intensity is rejected |
| [Kirpich time of concentration](../WaterEngineerLab/kirpich-time-of-concentration.md) | 7.104302235 min | slope outside (0, 1] is rejected; slope 1 removes the slope power |
| [Manning full-flow pipe diameter](../WaterEngineerLab/manning-storm-drain-diameter.md) | required D 0.7494524927 m; 1.2 m carries 3.898730279 m³/s | zero slope is rejected; blank selected diameter skips the capacity check |
| [Pump duty head and power](../WaterEngineerLab/pump-duty-head-power.md) | 25 m, 12258.3125 W hydraulic, 16344.41667 W shaft | efficiency 1 returns hydraulic power; non-positive head is rejected |
| [Residual pressure from a head balance](../WaterEngineerLab/residual-pressure-head.md) | 10.59148639 m and 103.867 kPa, above the 100 kPa minimum | a blank minimum skips the comparison |
| [Elastic section modulus](../StructuralEngineerLab/elastic-section-modulus.md) | Sx 0.005333333333 m³, Sy 0.002666666667 m³ | a zero fiber distance is rejected with the geometry |
| [Geometric section properties](../StructuralEngineerLab/geometric-section-properties.md) | A 0.08 m², Ix 0.001066666667 m⁴, Sx 0.005333333333 m³ | zero diameter and a hollow circle with no wall are rejected |
| [Section normal stress at four script points](../StructuralEngineerLab/section-normal-stress.md) | bottom +1.875 MPa, top and both side points −1.875 MPa | zero loads give zero stress; side levers are the script values, not mid-depth offsets |
| [User-defined demand over allowable](../StructuralEngineerLab/user-defined-utilization.md) | 0.8 | zero demand returns 0; zero allowable is rejected; the ratio is not capped |
| [Rectangular prism volume](../DIYCalcLab/cubic-yard.md) | 50 ft³, 1.851851852 yd³, 1.41584233 m³ | zero depth gives zero volume |
| [Deck board count](../DIYCalcLab/deck-board-count.md) | 26 rows, 416 ft, 29 boards, 13 joists | zero waste returns 26 boards |
| [Drywall sheet count](../DIYCalcLab/drywall-sheets.md) | 493 ft² and 17 sheets | 0% waste gives 16 sheets |
| [Gravel volume and mass](../DIYCalcLab/gravel-tonnage.md) | 1.486634446 m³, 2.378615114 t, 2.621974344 short tons | zero waste removes the 5% factor |
| [Interior wall paint quantity](../DIYCalcLab/interior-paint.md) | 334 ft² net, 7.224728776 L, displayed as 2 gal | zero coats give zero volume; three leftover quarts display as an extra gallon |
| [Mulch bed volume](../DIYCalcLab/mulch-volume.md) | 25 ft³ and 13 bags | 10% extra yields 14 bags; zero depth yields zero |
| [Round column concrete volume](../DIYCalcLab/sonotube-concrete.md) | 0.3914239878 m³ with waste, 24 bags of 80 lb | 0% waste drops the 10% factor; zero diameter gives zero bags |
| [Plan area](../DIYCalcLab/square-footage.md) | 120 ft² and 11.1483648 m² | a zero side is zero area; count below 1 is raised to 1 |
| [Stair rise and run](../DIYCalcLab/stair-geometry.md) | 14 risers at 7.714285714 in, run 10.83333333 ft, angle 37.64762064° | a riser above the stored code maximum is flagged; the geometry still uses the typed maximum |
| [Tile count with joints](../DIYCalcLab/tile-quantity.md) | 78.35901796 tiles, buy 87, 9 boxes | explicit 0% waste buys 79 tiles |
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

These still have no topic file. They are not `VERIFIED`.

| Tool | Why there is no page |
|---|---|
| PowerEngineerLab `voltage-drop-cable-sizing` | Several resistance models and grouping factors in one large chunk. |
| StructuralEngineerLab beam solvers (`TOOL-001`, `TOOL-005`, `TOOL-006`, `TOOL-007`, `TOOL-011`, `TOOL-013` through `TOOL-017`) | Singularity or EI integration, or a report wrapped around that integration. Not a single closed form. |
| StructuralEngineerLab `TOOL-018`, `TOOL-019`, `TOOL-020`, `TOOL-023`, `TOOL-029` through `TOOL-032` | Inventory URLs returned HTTP 404 on 2026-11-04, so they were not linked. |
| HVACEngineerLab `psychrometric-process-analyzer` | Shared psychrometric library rather than one equation extracted and recomputed here. |
| HVACEngineerLab `cooling-heating-load-planner` | A load planner with many internal branches, not one closed form. |
| WaterEngineerLab `TOOL-006`, `TOOL-008` | Inventory URLs returned HTTP 404 on 2026-11-04. |
| WaterEngineerLab `TOOL-001`, `TOOL-014`, `TOOL-015`, `TOOL-017` | Planners or weighted comparisons wrapped around formulas that already have pages. |
| NetEngineerLab bandwidth and MTU tools | Unit tables and overhead libraries, not a single engineering formula. |
| NetEngineerLab generators, scanners, and the remaining planners | No single closed-form equation was taken from the production script for a topic page. |
| DIYCalcLab calculators not in the published list | Modules exist, and they were not all read. Unpublished ones have no page. |
| AIMarkTool, PCDog, DataFileLab, DevEngineerLab, PrivacyFileLab | Outside this request. Mostly non-formula tools. |

## Reproduction

Python 3, standard library `math` only, using the constants copied from the bundles (`Math.PI`, 0.3048, 0.0254, 9.80665, 299792.458, 745.6999, Manning \(1/n\), rational-method scale factors, duct \(f\) branches). Results are recorded in the topic files. No production POST endpoint was required; the calculators run in the browser from these scripts.
