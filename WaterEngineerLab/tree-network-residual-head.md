# Single-source tree residual head

## Overview

The distribution-network planner checks one source feeding a tree: every node has one incoming pipe, the graph is connected, and there are no loops. Flow in each pipe is the downstream demand. Headloss on that pipe uses Darcy-Weisbach with the friction factor you type. Residual pressure at each node is source head minus elevation change minus those losses. It does not run EPANET, and it does not decide whether a code minimum is met beyond comparing the number you typed.

Production planner chunk, read 2026-11-07. Segment count must equal node count. The demo topology is SOURCE → A → B (https://waterengineerlab.com/tools/water-distribution-network-preliminary-planner).

## Formula

Accumulated flow is own demand plus every downstream accumulated flow. Velocity and major headloss, with \(D\) and \(L\) in metres and \(Q\) in m³/s:

$$
V = \frac{Q}{\pi D^{2}/4}, \qquad h_f = \frac{L}{D}\,f\,\frac{V^{2}}{19.6133}
$$

\(19.6133 = 2\times 9.80665\). Pressure head and pressure use density 1000 kg/m³:

$$
h_p = \frac{P}{9806.65}, \qquad P = 1000\,h\,9.80665
$$

Node residual head = upstream residual head + upstream elevation − node elevation − \(h_f\) of the incoming pipe. The source residual head is the source pressure head, and the source elevation is the starting elevation. Velocity head is not included. A negative residual is reported rather than clamped.

## Variables

SI demo values:

| Node or pipe | Inputs |
|---|---|
| Source | 350 kPa, elevation 100 m, minimum residual to compare 100 kPa |
| Node A | demand 0.02 m³/s, elevation 103 m |
| Node B | demand 0.01 m³/s, elevation 106 m |
| SOURCE → A | length 100 m, diameter 0.20 m, \(f = 0.02\) |
| A → B | length 120 m, diameter 0.15 m, \(f = 0.025\) |

US entry is converted with 1 ft = 0.3048 m, 1 psi = 6894.757293168 Pa, 1 ft³/s = 0.028316846592 m³/s, and 1 in = 0.0254 m. The demo below stays in SI.

## Engineering Principles

Because the graph is a tree, each pipe has one flow and that flow is known from the demands. A loop would split flow, and this tool refuses loops instead of guessing a split. Residual pressure is a hydraulic check against the minimum you supply. Clearing that minimum is not a permit result.

## Worked Example

1. Flow A→B = demand B = 0.01 m³/s. Flow SOURCE→A = 0.02 + 0.01 = 0.03 m³/s.
2. \(V_1 = 0.03/(\pi\times 0.2^{2}/4) = 0.954930\,\mathrm{m/s}\). \(h_{f1} = (100/0.2)\times 0.02\times V_1^{2}/19.6133 = 0.464935\,\mathrm{m}\).
3. \(V_2 = 0.565884\,\mathrm{m/s}\). \(h_{f2} = (120/0.15)\times 0.025\times V_2^{2}/19.6133 = 0.326539\,\mathrm{m}\).
4. Source pressure head = \(350000/9806.65 = 35.6901\,\mathrm{m}\).
5. Residual head at A = \(35.6901 + 100 - 103 - 0.464935 = 32.2251\,\mathrm{m}\), which is 316.02 kPa.
6. Residual head at B = \(32.2251 + 103 - 106 - 0.326539 = 28.8986\,\mathrm{m}\), which is 283.40 kPa.
7. Both sit above the typed 100 kPa minimum.

Boundary: a second incoming pipe, a disconnected node, or a segment count that is not the node count is rejected. Dropping the source pressure until a residual goes negative still returns the negative head; it does not hide the node.

## Limitations

- Tree only. No loops, pumps, tanks, or minor losses.
- \(f\) is an input. The tool does not solve Colebrook.
- Fixed density 1000 kg/m³ and no velocity head.
- “Above the minimum” is a comparison with the typed value.

## Reference Standards

Darcy-Weisbach with \(2g = 19.6133\) is the expression in the production chunk, the same constant used by the single-pipe headloss topic. No pipe-design code was re-read. Status: pending.
## Online Calculator

The SOURCE → A → B demo is the SI starting point:

https://waterengineerlab.com/tools/water-distribution-network-preliminary-planner

## Related Formulas

- [Catchment breakdown and peak runoff sum](catchment-runoff-summary.md)
- [Darcy-Weisbach major pipe headloss](darcy-weisbach-pipe-headloss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab distribution-network preliminary planner |
| Evidence | Production accumulated-demand walk, \(h_f=(L/D)f V^{2}/19.6133\), and residual head with \(P/9806.65\) |
| Method | Recomputed the default SOURCE → A → B SI case in Python |
| Example result | Residuals 316.02 kPa at A and 283.40 kPa at B |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
