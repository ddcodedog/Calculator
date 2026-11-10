# Formula standards audit

- Date: 2026-11-10
- Calculation status and standards status are separate.
- Standards status was not set to VERIFIED from a generic webpage, a homepage, or an unread PDF link.
- Machine-readable copy: [FORMULA_STANDARDS_AUDIT.json](FORMULA_STANDARDS_AUDIT.json).

## Read in this round

### Fed. Std. 376B — kilowatt to horsepower

- File: https://www.nist.gov/system/files/documents/2017/05/09/fs376-b.pdf (HTTP 200, 301517 bytes, `application/pdf`).
- Identity: extracted page text says Fed-Std-376B / Fed. Std. 376B. The cover page did not yield a title beyond the roman numeral page label.
- Foreword: the General Services Administration authorized use. NIST hosts this copy.
- Section 1 scope: preferred metric units recommended for Federal Government use.
- Section 5.2.13 Power: horsepower converts to watt by 745.699 9.
- Section 4.3.3: metric horsepower is listed with units that shall not be used.
- 735.49875 does not appear in the extracted text. It stays a calculator constant, not a standards result.
- A publication day was not printed on the extracted front pages. The `2017/05/09` segment of the URL was not copied as the standard's date.
- Section 2 cites ANSI/IEEE Std 268-1992. That document was not opened in this round.
- Standards status: VERIFIED for the mechanical horsepower factor only.

### OpenStax University Physics Volume 2, section 9.4 — Ohm's law

- URL fetched HTTP 200 on 2026-11-10: https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- The page says current is proportional to applied voltage and uses I = V/R in the example.
- No ISBN or numbered edition was in the extracted text, so the version is not pinned.
- Standards status remains PENDING.

## Structural calculation recheck

Both notes stay calculation `REVIEW_REQUIRED`. The closed forms were recomputed on 2026-11-10:

- Cantilever tip: 10 kN, 4 m, 200 GPa, 8e-6 m⁴ → 40 kN·m and 0.133333 m. The public HTML contains the tip relation. The 2026-11-07 formula ids were not found as text in that fetch. The general EI integrator was not line-traced.
- Simply supported midspan: 12 kN, 6 m, same EI → 0.03375 m (33.75 mm). Zero end deflection is the support boundary v(0) = v(L) = 0. The integrator was not line-traced.

Hibbeler and Roark editions are still not pinned. Standards status PENDING.

## All other topics

The historical `standards` string is unchanged in [FORMULA_VERIFICATION.json](FORMULA_VERIFICATION.json). Those strings already say the PDF, RFC, or textbook body was not read, or that no standard URL was in the engine. They stay PENDING. Bodies that were not opened include ITU-T, IEEE 802.1, IEC, ASHRAE, ACI, AISC, and AWWA. A link to one of those sites was not treated as a reading.

Pending topics: 87. Verified topics: 1. Not applicable: 0.

| Document | Calculation | Standards | What the record already says |
|---|---|---|---|
| NetEngineerLab/fiber-link-loss.md | VERIFIED | PENDING | pending ITU/IEEE PDFs not re-read; URLs are on the production page |
| NetEngineerLab/optical-power-budget.md | VERIFIED | PENDING | pending |
| NetEngineerLab/fiber-propagation-latency.md | VERIFIED | PENDING | pending G.652 table fetch |
| NetEngineerLab/chromatic-dispersion.md | VERIFIED | PENDING | ITU URLs cited on page; PDF not re-read |
| NetEngineerLab/ospf-interface-cost.md | VERIFIED | PENDING | pending external RFC |
| NetEngineerLab/stp-path-cost.md | VERIFIED | PENDING | IEEE URLs on page; PDFs not re-read |
| PowerEngineerLab/ohms-law.md | VERIFIED | PENDING | OpenStax URL HTTP 200; body not transcribed |
| PowerEngineerLab/power-triangle.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/inductive-reactance.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/capacitive-reactance.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/voltage-divider.md | VERIFIED | PENDING | pending; SRC-001 url null |
| PowerEngineerLab/transformer-full-load-current.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/synchronous-speed.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/induction-motor-slip.md | VERIFIED | PENDING | Engineering Toolbox URL present; article not re-fetched |
| PowerEngineerLab/kilowatt-to-horsepower.md | VERIFIED | VERIFIED | NIST 745.6999 verified from PDF; 735.49875 code only |
| StructuralEngineerLab/euler-column-buckling.md | VERIFIED | PENDING | pending textbook source id only |
| StructuralEngineerLab/beam-bending-stress.md | VERIFIED | PENDING | pending |
| StructuralEngineerLab/section-properties.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/manning-open-channel-flow.md | VERIFIED | PENDING | pending FHWA source id has no URL |
| WaterEngineerLab/rational-method-peak-runoff.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/darcy-weisbach-pipe-headloss.md | VERIFIED | PENDING | pending |
| HVACEngineerLab/duct-friction-pressure-drop.md | VERIFIED | PENDING | pending |
| DIYCalcLab/concrete-slab-volume.md | VERIFIED | PENDING | pending |
| DIYCalcLab/roof-pitch.md | VERIFIED | PENDING | IRC citation pending |
| DIYCalcLab/board-foot.md | VERIFIED | PENDING | pending |
| NetEngineerLab/bandwidth-transfer-time.md | VERIFIED | PENDING | pending |
| NetEngineerLab/mtu-mss-overhead.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/transformer-turns-ratio.md | VERIFIED | PENDING | pending OpenStax citation not re-read |
| PowerEngineerLab/interval-load-factor.md | VERIFIED | PENDING | pending EIA glossary not re-read; chunk licenseStatus review-required |
| HVACEngineerLab/cooling-heating-load-components.md | VERIFIED | PENDING | pending EnergyPlus eng ref not re-read |
| HVACEngineerLab/psychrometric-process-states.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/catchment-runoff-summary.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/tree-network-residual-head.md | VERIFIED | PENDING | pending |
| StructuralEngineerLab/cantilever-tip-deflection.md | REVIEW_REQUIRED | PENDING | pending Hibbeler/Roark edition not pinned |
| StructuralEngineerLab/simply-supported-midspan-deflection.md | REVIEW_REQUIRED | PENDING | pending |
| DIYCalcLab/fence-post-and-picket-count.md | VERIFIED | PENDING | pending |
| DIYCalcLab/slab-rebar-grid.md | VERIFIED | PENDING | pending |
| AIMarkTool/return-on-ad-spend.md | VERIFIED | PENDING | pending |
| AIMarkTool/order-value-ltv-to-cac.md | VERIFIED | PENDING | pending; order value not gross profit |
| DataFileLab/csv-value-frequency.md | VERIFIED | PENDING | pending; splitter.js quotes not re-derived |
| DataFileLab/csv-encoding-detection.md | VERIFIED | PENDING | pending |
| DevEngineerLab/unix-timestamp-conversion.md | VERIFIED | PENDING | pending |
| DevEngineerLab/integer-base-conversion.md | VERIFIED | PENDING | pending |
| PCDog/ipv4-longest-prefix-match.md | VERIFIED | PENDING | pending |
| PCDog/ipv4-static-route-commands.md | VERIFIED | PENDING | pending; reachability not-tested |
| PrivacyFileLab/sha256-file-digest.md | VERIFIED | PENDING | pending FIPS 180-4 not re-read |
| PrivacyFileLab/sensitive-text-redaction.md | VERIFIED | PENDING | pending |
| NetEngineerLab/dns-ttl-cache-window.md | VERIFIED | PENDING | pending |
| NetEngineerLab/switch-uplink-safe-capacity.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/maximum-demand-factor.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/appliance-period-energy-cost.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/site-drainage-scenario-score.md | VERIFIED | PENDING | pending |
| StructuralEngineerLab/simply-supported-offcenter-point-load.md | VERIFIED | PENDING | pending |
| StructuralEngineerLab/simply-supported-uniform-load.md | VERIFIED | PENDING | pending |
| DIYCalcLab/modular-brick-wall-count.md | VERIFIED | PENDING | pending |
| DIYCalcLab/blown-fiberglass-attic-bags.md | VERIFIED | PENDING | pending |
| AIMarkTool/funnel-stage-counts.md | VERIFIED | PENDING | pending |
| AIMarkTool/ab-equal-group-sample-size.md | VERIFIED | PENDING | pending |
| DataFileLab/csv-blank-record-removal.md | VERIFIED | PENDING | pending |
| DataFileLab/csv-row-number-column.md | VERIFIED | PENDING | pending |
| DevEngineerLab/word-wrap-grapheme-width.md | VERIFIED | PENDING | pending |
| DevEngineerLab/local-text-size-counts.md | VERIFIED | PENDING | pending |
| PCDog/screen-backing-pixel-estimate.md | VERIFIED | PENDING | pending |
| PCDog/refresh-frame-interval-summary.md | VERIFIED | PENDING | pending |
| PrivacyFileLab/metadata-finding-type-diff.md | VERIFIED | PENDING | pending |
| PrivacyFileLab/clean-file-verifier-status.md | VERIFIED | PENDING | pending |
| NetEngineerLab/cutover-wait-versus-fiber-delay.md | VERIFIED | PENDING | pending |
| NetEngineerLab/on-wire-bytes-at-safe-uplink.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/three-shop-ratios.md | VERIFIED | PENDING | pending |
| PowerEngineerLab/divider-is-not-a-winding.md | VERIFIED | PENDING | pending |
| HVACEngineerLab/mass-flow-into-duct-velocity.md | VERIFIED | PENDING | pending |
| HVACEngineerLab/latent-sign-is-not-condensate.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/ditch-capacity-versus-lot-peak.md | VERIFIED | PENDING | pending |
| WaterEngineerLab/single-pipe-residual-matches-darcy.md | VERIFIED | PENDING | pending |
| StructuralEngineerLab/strip-moment-to-fiber-stress.md | VERIFIED | PENDING | pending |
| StructuralEngineerLab/axial-ratio-beside-moment.md | VERIFIED | PENDING | pending; labels are not code compliance |
| DIYCalcLab/eighteen-by-nine-slab-and-mat.md | VERIFIED | PENDING | pending |
| DIYCalcLab/rafter-length-into-board-feet.md | VERIFIED | PENDING | pending |
| AIMarkTool/one-count-two-ratios.md | VERIFIED | PENDING | pending |
| AIMarkTool/planned-sample-versus-arrivals.md | VERIFIED | PENDING | pending |
| DataFileLab/encoding-blank-then-city-tally.md | VERIFIED | PENDING | pending |
| DataFileLab/do-not-tally-the-row-number.md | VERIFIED | PENDING | pending |
| DevEngineerLab/wrap-then-recount-lines.md | VERIFIED | PENDING | pending |
| DevEngineerLab/same-integer-two-tools.md | VERIFIED | PENDING | pending |
| PCDog/keep-the-longer-prefix-then-print-it.md | VERIFIED | PENDING | pending |
| PCDog/pixels-beside-frame-time.md | VERIFIED | PENDING | pending |
| PrivacyFileLab/hash-only-after-the-verifier.md | VERIFIED | PENDING | pending |
| PrivacyFileLab/different-digest-failed-diff.md | VERIFIED | PENDING | pending |
