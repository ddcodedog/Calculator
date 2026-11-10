# Locale route matrix

- Verification date: 2026-11-10
- Method: live HTTP GET. A filename was not treated as a page.
- Route status counts: {"NOT_SUPPORTED": 38, "VERIFIED": 50}
- Chinese topic files were not added for sites other than NetEngineerLab. A VERIFIED route with an empty Chinese document means the production page exists and the companion note does not.
- NetEngineerLab `/zh-CN/tools/stp-path-cost-calculator/` and `/tools/stp-path-cost-calculator/zh-CN/` both returned HTTP 404. The working Chinese STP page is `/tools/stp-path-cost-calculator/zh/`.
- Spanish alternates advertised by some hreflang tags were fetched when present and are recorded as `advertisedEsUrl`. No Spanish topic files were added.

Machine-readable copy: [../config/locale-routes.json](../config/locale-routes.json).

| Website | Tool | English document | Chinese document | English status | Chinese status | Route | Chinese final language | Canonical | Hreflang |
|---|---|---|---|---:|---:|---|---|---|---|
| NetEngineerLab | `fiber-loss` | NetEngineerLab/fiber-link-loss.md | NetEngineerLab/fiber-link-loss.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `optical-power-budget` | NetEngineerLab/optical-power-budget.md | NetEngineerLab/optical-power-budget.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `fiber-latency-calculator` | NetEngineerLab/fiber-propagation-latency.md | NetEngineerLab/fiber-propagation-latency.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `chromatic-dispersion-calculator` | NetEngineerLab/chromatic-dispersion.md | NetEngineerLab/chromatic-dispersion.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `ospf-cost-calculator` | NetEngineerLab/ospf-interface-cost.md | NetEngineerLab/ospf-interface-cost.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `stp-path-cost-calculator` | NetEngineerLab/stp-path-cost.md | NetEngineerLab/stp-path-cost.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `ohms-law` | PowerEngineerLab/ohms-law.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `power-triangle` | PowerEngineerLab/power-triangle.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `inductive-reactance` | PowerEngineerLab/inductive-reactance.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `capacitive-reactance` | PowerEngineerLab/capacitive-reactance.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `voltage-divider` | PowerEngineerLab/voltage-divider.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `transformer-full-load-current` | PowerEngineerLab/transformer-full-load-current.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `synchronous-speed` | PowerEngineerLab/synchronous-speed.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `motor-slip` | PowerEngineerLab/induction-motor-slip.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `kw-to-hp` | PowerEngineerLab/kilowatt-to-horsepower.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| StructuralEngineerLab | `TOOL-004` | StructuralEngineerLab/euler-column-buckling.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `TOOL-003` | StructuralEngineerLab/beam-bending-stress.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `TOOL-008` | StructuralEngineerLab/section-properties.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| WaterEngineerLab | `TOOL-007` | WaterEngineerLab/manning-open-channel-flow.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| WaterEngineerLab | `TOOL-003` | WaterEngineerLab/rational-method-peak-runoff.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| WaterEngineerLab | `TOOL-010` | WaterEngineerLab/darcy-weisbach-pipe-headloss.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| HVACEngineerLab | `duct-airflow-design` | HVACEngineerLab/duct-friction-pressure-drop.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| DIYCalcLab | `concrete-slab` | DIYCalcLab/concrete-slab-volume.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| DIYCalcLab | `roof-pitch` | DIYCalcLab/roof-pitch.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| DIYCalcLab | `board-foot` | DIYCalcLab/board-foot.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| NetEngineerLab | `bandwidth-calculator` | NetEngineerLab/bandwidth-transfer-time.md | NetEngineerLab/bandwidth-transfer-time.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `mtu-calculator` | NetEngineerLab/mtu-mss-overhead.md | NetEngineerLab/mtu-mss-overhead.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `transformer-ratio` | PowerEngineerLab/transformer-turns-ratio.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `load-factor` | PowerEngineerLab/interval-load-factor.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| HVACEngineerLab | `cooling-heating-load-planner` | HVACEngineerLab/cooling-heating-load-components.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| HVACEngineerLab | `psychrometric-process-analyzer` | HVACEngineerLab/psychrometric-process-states.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| WaterEngineerLab | `TOOL-017` | WaterEngineerLab/catchment-runoff-summary.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| WaterEngineerLab | `water-distribution-network-preliminary-planner` | WaterEngineerLab/tree-network-residual-head.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `cantilever-beam-calculator` | StructuralEngineerLab/cantilever-tip-deflection.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `beam-deflection-calculator` | StructuralEngineerLab/simply-supported-midspan-deflection.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DIYCalcLab | `fence` | DIYCalcLab/fence-post-and-picket-count.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| DIYCalcLab | `rebar` | DIYCalcLab/slab-rebar-grid.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| AIMarkTool | `roas-calculator` | AIMarkTool/return-on-ad-spend.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| AIMarkTool | `cac-ltv-calculator` | AIMarkTool/order-value-ltv-to-cac.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| DataFileLab | `csv-frequency` | DataFileLab/csv-value-frequency.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DataFileLab | `encoding` | DataFileLab/csv-encoding-detection.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DevEngineerLab | `timestamp-converter` | DevEngineerLab/unix-timestamp-conversion.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DevEngineerLab | `number-base-converter` | DevEngineerLab/integer-base-conversion.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| PCDog | `longest-prefix-match` | PCDog/ipv4-longest-prefix-match.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PCDog | `static-route-generator` | PCDog/ipv4-static-route-commands.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PrivacyFileLab | `hash` | PrivacyFileLab/sha256-file-digest.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PrivacyFileLab | `text-redactor` | PrivacyFileLab/sensitive-text-redaction.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `dns-ttl-propagation-calculator` | NetEngineerLab/dns-ttl-cache-window.md | NetEngineerLab/dns-ttl-cache-window.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `switch-uplink-oversubscription-calculator` | NetEngineerLab/switch-uplink-safe-capacity.md | NetEngineerLab/switch-uplink-safe-capacity.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `demand-factor` | PowerEngineerLab/maximum-demand-factor.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `TOOL-011` | PowerEngineerLab/appliance-period-energy-cost.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| WaterEngineerLab | `TOOL-015` | WaterEngineerLab/site-drainage-scenario-score.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `simply-supported-beam-calculator` | StructuralEngineerLab/simply-supported-offcenter-point-load.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `TOOL-001` | StructuralEngineerLab/simply-supported-uniform-load.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DIYCalcLab | `brick` | DIYCalcLab/modular-brick-wall-count.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| DIYCalcLab | `insulation` | DIYCalcLab/blown-fiberglass-attic-bags.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| AIMarkTool | `funnel-conversion-calculator` | AIMarkTool/funnel-stage-counts.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| AIMarkTool | `ab-test-sample-size-calculator` | AIMarkTool/ab-equal-group-sample-size.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| DataFileLab | `csv-blank-rows` | DataFileLab/csv-blank-record-removal.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DataFileLab | `csv-row-numberer` | DataFileLab/csv-row-number-column.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DevEngineerLab | `TOOL-058` | DevEngineerLab/word-wrap-grapheme-width.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DevEngineerLab | `TOOL-030` | DevEngineerLab/local-text-size-counts.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| PCDog | `screen-information` | PCDog/screen-backing-pixel-estimate.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PCDog | `refresh-rate-test` | PCDog/refresh-frame-interval-summary.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PrivacyFileLab | `metadata-diff` | PrivacyFileLab/metadata-finding-type-diff.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PrivacyFileLab | `clean-file-verifier` | PrivacyFileLab/clean-file-verifier-status.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `dns-ttl-propagation-calculator` | NetEngineerLab/cutover-wait-versus-fiber-delay.md | NetEngineerLab/cutover-wait-versus-fiber-delay.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| NetEngineerLab | `bandwidth-calculator` | NetEngineerLab/on-wire-bytes-at-safe-uplink.md | NetEngineerLab/on-wire-bytes-at-safe-uplink.zh-CN.md | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `load-factor` | PowerEngineerLab/three-shop-ratios.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PowerEngineerLab | `transformer-ratio` | PowerEngineerLab/divider-is-not-a-winding.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| HVACEngineerLab | `duct-airflow-design` | HVACEngineerLab/mass-flow-into-duct-velocity.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| HVACEngineerLab | `psychrometric-process-analyzer` | HVACEngineerLab/latent-sign-is-not-condensate.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| WaterEngineerLab | `manning-open-channel-flow` | WaterEngineerLab/ditch-capacity-versus-lot-peak.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| WaterEngineerLab | `water-distribution-network-preliminary-planner` | WaterEngineerLab/single-pipe-residual-matches-darcy.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `beam-bending-stress-calculator` | StructuralEngineerLab/strip-moment-to-fiber-stress.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| StructuralEngineerLab | `user-defined-utilization-calculator` | StructuralEngineerLab/axial-ratio-beside-moment.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DIYCalcLab | `concrete-slab` | DIYCalcLab/eighteen-by-nine-slab-and-mat.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| DIYCalcLab | `board-foot` | DIYCalcLab/rafter-length-into-board-feet.md | — | 200 | 404 | NOT_SUPPORTED | en | MISMATCH | ABSENT |
| AIMarkTool | `roas-calculator` | AIMarkTool/one-count-two-ratios.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| AIMarkTool | `ab-test-sample-size-calculator` | AIMarkTool/planned-sample-versus-arrivals.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| DataFileLab | `csv-frequency` | DataFileLab/encoding-blank-then-city-tally.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DataFileLab | `csv-row-numberer` | DataFileLab/do-not-tally-the-row-number.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DevEngineerLab | `text-wrap-calculator` | DevEngineerLab/wrap-then-recount-lines.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| DevEngineerLab | `timestamp-converter` | DevEngineerLab/same-integer-two-tools.md | — | 200 | 404 | NOT_SUPPORTED | en | ABSENT | ABSENT |
| PCDog | `static-route-generator` | PCDog/keep-the-longer-prefix-then-print-it.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PCDog | `screen-information` | PCDog/pixels-beside-frame-time.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PrivacyFileLab | `hash` | PrivacyFileLab/hash-only-after-the-verifier.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |
| PrivacyFileLab | `metadata-diff` | PrivacyFileLab/different-digest-failed-diff.md | — | 200 | 200 | VERIFIED | zh-CN | MATCH | HAS_ZH_CN |

## Negative probes

| URL | HTTP | Final | Language | Title |
|---|---:|---|---|---|
| https://netengineerlab.com/zh-CN/tools/stp-path-cost-calculator/ | 404 | https://netengineerlab.com/zh-CN/tools/stp-path-cost-calculator/ | en | Page not found / NetEngineerLab |
| https://netengineerlab.com/tools/stp-path-cost-calculator/zh-CN/ | 404 | https://netengineerlab.com/tools/stp-path-cost-calculator/zh-CN/ | en | Page not found / NetEngineerLab |
