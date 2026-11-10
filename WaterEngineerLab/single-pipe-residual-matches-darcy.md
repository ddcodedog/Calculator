# One pipe: the residual is the Darcy loss. A second pipe is not.

## When the two tools are the same subtraction

The Darcy tool reports major headloss for one full pipe. The tree planner reports residual head at a node as upstream residual head, plus upstream elevation, minus node elevation, minus the incoming pipe’s major loss. With a single pipe and no extra nodes, those sentences describe one subtraction. With a second pipe, the Darcy page no longer sees the downstream flow, and you cannot keep pasting the first \(h_f\).

## Shared pipe

Flow 0.008 m³/s, diameter 0.08 m, length 60 m, \(f = 0.022\). Both tools use \(g = 9.80665\,\mathrm{m/s^2}\) through the constant 19.6133.

$$
A = \pi\times 0.08^{2}/4 = 0.00502655\,\mathrm{m^2}
$$

$$
V = 1.59155\,\mathrm{m/s}, \qquad h_f = 0.022\times\frac{60}{0.08}\times\frac{V^{2}}{19.6133} = 2.13095\,\mathrm{m}
$$

That \(h_f\) is the whole Darcy-tool result. Velocity head is not in it.

## The one-node tree

Source pressure 250 kPa, source elevation 20 m, node elevation 22 m, node demand 0.008 m³/s, one pipe with the numbers above. Source pressure head:

$$
h_p = 250000/9806.65 = 25.4929\,\mathrm{m}
$$

Residual head at the node:

$$
25.4929 + 20 - 22 - 2.13095 = 21.3620\,\mathrm{m}
$$

Pressure back at density 1000 kg/m³ is \(1000\times 21.3620\times 9.80665 = 209.49\,\mathrm{kPa}\). The elevation change and the Darcy loss both came off the source head. Nothing else did. Velocity head is still absent, on purpose: the tree tool says it does not include it.

## Where the identity stops

Add a downstream node that demands another 0.008 m³/s. The first pipe’s flow becomes 0.016 m³/s, not 0.008. Velocity doubles and \(h_f\) quadruples if \(f\) and diameter stay put, because headloss follows \(V^{2}\). The single-pipe Darcy result of 2.131 m is then the wrong subtraction for the first segment. The tree tool accumulates demand before it computes \(h_f\). The Darcy tool will not do that accumulation for you.

A negative residual is still reported. Raising the node by another 25 m would drive this example’s 21.36 m residual negative. The tool does not clamp it to zero and does not call the result a code pass. A typed minimum pressure is only a comparison with the number you typed.

## Limits

- Major loss only. No fittings, no pump, no loop.
- \(f\) is an input on both pages.
- Density 1000 kg/m³ is the tree tool’s constant. A different fluid breaks the 9806.65 conversion.

## Tools

- One pipe: https://waterengineerlab.com/tools/water-pipe-flow-headloss/
- Tree residual: https://waterengineerlab.com/tools/water-distribution-network-preliminary-planner

The published tree demo is 350 kPa and two nodes. This note uses 250 kPa and shows the one-pipe case before the second demand appears.

## Online Calculator

The residual, once a second node exists, belongs on the tree page:

https://waterengineerlab.com/tools/water-distribution-network-preliminary-planner

## Related Formulas

- [Darcy-Weisbach major pipe headloss](darcy-weisbach-pipe-headloss.md)
- [Single-source tree residual head](tree-network-residual-head.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Darcy and tree both use \(h_f = f(L/D)V^{2}/19.6133\); tree residual adds elevation and source head |
| Evidence | Python replay of that shared expression and the one-node residual. No browser session |
| Dedup scope | Water learn pages read 2026-11-10 do not walk this one-pipe identity. Not a web-wide scan |
| Example result | \(h_f = 2.131\,\mathrm{m}\), residual 21.362 m (209.49 kPa) |
| Date | 2026-11-10 |
| Status | VERIFIED |
