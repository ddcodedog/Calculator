# Put the axial load over Euler. Leave the moment out.

Locale: en

## Two demands, two families

The same 80 mm × 160 mm rectangle that produced a 10 kN·m strip moment can also be asked to stand as a 4.5 m pinned column. The utilization tool will divide a demand by an allowable **in one family**. Force over force is legal. A bending stress over an Euler load is not, and the page rejects cross-dimension comparisons.

## Euler load you might type as the allowable

\(E = 200\,\mathrm{GPa}\), \(K = 1\), \(L = 4.5\,\mathrm{m}\). Strong-axis \(I_x = 2.730667\times 10^{-5}\,\mathrm{m^4}\):

$$
P_{\mathrm{cr},x} = \frac{\pi^{2} E I_x}{(KL)^{2}} = 2661.8\,\mathrm{kN}
$$

Weak-axis \(I_y = h b^{3}/12 = 6.826667\times 10^{-6}\,\mathrm{m^4}\):

$$
P_{\mathrm{cr},y} = 665.45\,\mathrm{kN}
$$

The column tool uses the \(I\) you select. It does not automatically take the smaller one. Euler stress needs an area; this note stops at load because the utilization example below is in the force family.

## Utilization, force family only

Service demand typed as 40 kN. If the allowable you type is the strong-axis Euler load:

$$
U = 40/2661.8 = 0.01503, \qquad 100U = 1.503\%
$$

If you type the weak-axis load instead:

$$
U = 40/665.45 = 0.06011, \qquad 100U = 6.011\%
$$

The tool’s labels are “below,” “equal to,” or “above” the allowable **you** supplied. The live guide states that those words are not pass, fail, safe, unsafe, or code compliance. 40 kN under 665 kN is a small ratio. It is not a certification that the column is adequate, because \(K\), imperfections, and the elastic limit were not reviewed.

## The moment stays outside

The strip’s 29.297 MPa is a stress. Dividing 29.297 by 2661.8 mixes MPa with kN. The utilization page is built to reject that pair. Dividing 10 kN·m by 2661.8 kN produces a length, not a utilization. The moment belongs on the bending-stress page with \(S_x\). The 40 kN belongs here with an Euler load in kilonewtons, and only after you have decided which axis \(I\) refers to.

Using \(I_x\) as the allowable when the weak axis is unbraced makes the ratio look about four times more comfortable (1.5% instead of 6.0%). That is a modeling choice, not a second formula.

## Limits

- Ideal elastic Euler, centroidal axial load, constant \(E\) and \(I\), typed \(K\).
- 40 kN is an assumed service load for the ratio. It is not the 8 kN beam reaction from the strip, and those reactions are not column loads unless the framing actually delivers them that way.
- No steel grade, no curve, no interaction formula for combined axial and moment.

## Tools

- Column load: https://structuralengineerlab.com/tools/column-euler-buckling-calculator/
- Ratio: https://structuralengineerlab.com/tools/user-defined-utilization-calculator/
- Moment and stress, kept separate: https://structuralengineerlab.com/tools/beam-bending-stress-calculator/

## Online Calculator

Type 40 kN over the Euler load you actually mean:

https://structuralengineerlab.com/tools/user-defined-utilization-calculator/

## Related Formulas

- [Euler elastic column buckling load](euler-column-buckling.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Euler \(P=\pi^{2}EI/(KL)^{2}\) from the column calculator; utilization = demand/allowable from the live guide text |
| Evidence | Python for both inertias and both loads. Guide sentence read 2026-11-10. The utilization page was not clicked |
| Dedup scope | Utilization guide, Euler guide, and bending-stress guide. Not a web-wide scan |
| Example result | 2661.8 kN or 665.45 kN; 40 kN gives 1.503% or 6.011% |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |