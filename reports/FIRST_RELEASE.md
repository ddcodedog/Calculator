# First release strategy (GATE 7)

Release 1 of this library is the formula set already checked in [FORMULA_VERIFICATION.md](FORMULA_VERIFICATION.md). GATE 5–8 does not add formula pages.

## In this release

Published formula topics: 25.

| Site | Document | Tool ID |
|------|----------|---------|
| NetEngineerLab | [Single-span fiber link loss](../NetEngineerLab/fiber-link-loss.md) | `fiber-loss` |
| NetEngineerLab | [Optical link power budget](../NetEngineerLab/optical-power-budget.md) | `optical-power-budget` |
| NetEngineerLab | [Fiber propagation delay and RTT](../NetEngineerLab/fiber-propagation-latency.md) | `fiber-latency-calculator` |
| NetEngineerLab | [Chromatic dispersion coefficient D(λ)](../NetEngineerLab/chromatic-dispersion.md) | `chromatic-dispersion-calculator` |
| NetEngineerLab | [OSPF interface cost](../NetEngineerLab/ospf-interface-cost.md) | `ospf-cost-calculator` |
| NetEngineerLab | [STP port path cost](../NetEngineerLab/stp-path-cost.md) | `stp-path-cost-calculator` |
| PowerEngineerLab | [DC Ohm’s law](../PowerEngineerLab/ohms-law.md) | `ohms-law` |
| PowerEngineerLab | [Sinusoidal power triangle](../PowerEngineerLab/power-triangle.md) | `power-triangle` |
| PowerEngineerLab | [Ideal inductive reactance](../PowerEngineerLab/inductive-reactance.md) | `inductive-reactance` |
| PowerEngineerLab | [Ideal capacitive reactance](../PowerEngineerLab/capacitive-reactance.md) | `capacitive-reactance` |
| PowerEngineerLab | [Resistive voltage divider](../PowerEngineerLab/voltage-divider.md) | `voltage-divider` |
| PowerEngineerLab | [Transformer full-load current](../PowerEngineerLab/transformer-full-load-current.md) | `transformer-full-load-current` |
| PowerEngineerLab | [AC machine synchronous speed](../PowerEngineerLab/synchronous-speed.md) | `synchronous-speed` |
| PowerEngineerLab | [Induction-motor slip](../PowerEngineerLab/induction-motor-slip.md) | `motor-slip` |
| PowerEngineerLab | [Kilowatt to mechanical horsepower](../PowerEngineerLab/kilowatt-to-horsepower.md) | `kw-to-hp` |
| StructuralEngineerLab | [Euler elastic column buckling load](../StructuralEngineerLab/euler-column-buckling.md) | `TOOL-004` |
| StructuralEngineerLab | [Elastic beam bending stress](../StructuralEngineerLab/beam-bending-stress.md) | `TOOL-003` |
| StructuralEngineerLab | [Centroidal area and section modulus](../StructuralEngineerLab/section-properties.md) | `TOOL-008` |
| WaterEngineerLab | [Manning open-channel discharge](../WaterEngineerLab/manning-open-channel-flow.md) | `TOOL-007` |
| WaterEngineerLab | [Rational-method peak runoff](../WaterEngineerLab/rational-method-peak-runoff.md) | `TOOL-003` |
| WaterEngineerLab | [Darcy-Weisbach major pipe headloss](../WaterEngineerLab/darcy-weisbach-pipe-headloss.md) | `TOOL-010` |
| HVACEngineerLab | [Duct friction and local pressure drop](../HVACEngineerLab/duct-friction-pressure-drop.md) | `duct-airflow-design` |
| DIYCalcLab | [Concrete slab volume and bag count](../DIYCalcLab/concrete-slab-volume.md) | `concrete-slab` |
| DIYCalcLab | [Roof pitch and slope factor](../DIYCalcLab/roof-pitch.md) | `roof-pitch` |
| DIYCalcLab | [Board-foot lumber volume](../DIYCalcLab/board-foot.md) | `board-foot` |

Five domain folders have no topic file: AIMarkTool, DataFileLab, DevEngineerLab, PCDog, PrivacyFileLab. Their READMEs say `Published topics: 0`.

## Deferred topics

A tool listed below has an inventory row and no formula page. That is a scope decision. It is not a claim that the tool is wrong, and it is not a placeholder article.

Some tools were opened during batch 1 and then left out for a specific reason. Those notes stay in [FORMULA_VERIFICATION.md](FORMULA_VERIFICATION.md) under “Deferred on purpose” (voltage-drop cable sizing, simply-supported beam tools, HVAC psychrometric and plant planners, PoE voltage drop, bandwidth and MTU tools, the unread DIYCalcLab calculators, and the five non-batch sites).

### NetEngineerLab

Inventory tools: 46. Published: 6. Deferred: 40.

| Tool ID | Name |
|---------|------|
| `pon-splitter-loss` | PON Splitter Loss Calculator |
| `onu-rx-power` | ONU RX Power Diagnosis |
| `pon-distance` | PON Maximum Distance Calculator |
| `otdr-event` | OTDR Event Analyzer |
| `mtu-calculator` | MTU & MSS Calculator |
| `subnet-calculator` | IP Subnet Calculator |
| `bandwidth-calculator` | Bandwidth & Transfer Time Calculator |
| `48v-battery-runtime` | -48V Telecom Battery Runtime Calculator |
| `ipv6-nat-planner` | IPv6 & NAT Planning Calculator |
| `wifi-coverage-capacity-planner` | Wi-Fi Coverage & Capacity Planner |
| `poe-power-budget-calculator` | PoE Power Budget Calculator |
| `sfp-qsfp-compatibility-calculator` | SFP & QSFP Compatibility Checker |
| `wireless-link-budget-calculator` | Wireless Link Budget Calculator |
| `poe-voltage-drop-calculator` | Ethernet Cable PoE Voltage Drop Calculator |
| `network-rack-power-cooling-calculator` | Network Rack Power & Cooling Calculator |
| `vlan-ip-capacity-planner` | VLAN & IP Subnet Capacity Planner |
| `switch-uplink-oversubscription-calculator` | Switch Uplink Bandwidth & Oversubscription Calculator |
| `dns-ttl-propagation-calculator` | DNS TTL & Propagation Time Calculator |
| `acl-generator-validator` | Multi-Vendor ACL Generator & Validator |
| `network-change-planner-mop-generator` | Network Change Planner & MOP Generator |
| `pue-data-center-energy-efficiency` | PUE & Data Center Energy Efficiency Analyzer |
| `telecom-solar-battery-sizing-calculator` | Telecom Solar Power & Battery Sizing Calculator |
| `generator-fuel-runtime-calculator` | Generator Fuel Consumption & Runtime Calculator |
| `telecom-rectifier-dc-power-sizing` | Telecom Rectifier & DC Power System Sizing Calculator |
| `telecom-ac-dc-breaker-sizing` | Telecom AC/DC Power Capacity & Breaker Sizing Calculator |
| `ups-capacity-battery-runtime-calculator` | UPS Capacity & Battery Backup Runtime Calculator |
| `data-center-cooling-load-calculator` | Data Center Cooling Load & Precision AC Capacity Calculator |
| `dc-plant-efficiency-load-sharing` | DC Plant Efficiency & Rectifier Load-Sharing Analyzer |
| `data-center-airflow-containment-planner` | Data Center Airflow & Hot-Aisle Containment Planner |
| `generator-ups-transfer-ride-through-planner` | Generator + UPS Transfer & Ride-Through Planner |
| `transmission-ring-optimization-risk-analyzer` | Transmission Ring Optimization & Protection Risk Analyzer |
| `olt-dual-uplink-transport-mse-planner` | OLT Dual-Uplink Capacity, Transport Channel & MSE Port Planner |
| `data-center-network-convergence-fabric-capacity-planner` | Data Center Network Convergence & Fabric Capacity Planner |
| `network-risk-hidden-hazard-assessment-generator` | Network Risk & Hidden-Hazard Assessment Generator |
| `odf-odn-resource-planner` | ODF / ODN Fiber Resource & Split Planning Planner |
| `network-capacity-forecast-planner` | Network Capacity Forecast Planner |
| `engineering-report-batch-export-center` | Engineering Report & Batch Export Center |
| `pmd-budget-calculator` | PMD Budget Calculator |
| `ethernet-serialization-delay-calculator` | Ethernet Serialization Delay Calculator |
| `all-reduce-traffic-estimator` | All-Reduce Traffic Estimator |

### PCDog

Inventory tools: 27. Published: 0. Deferred: 27.

| Tool ID | Name |
|---------|------|
| `tool.display.backlight-bleed` | Backlight Bleed / Black Field Test |
| `tool.display.contrast-clipping` | Contrast / White & Black Clipping Test |
| `tool.display.dead-pixel` | Dead Pixel Test |
| `tool.display.frame-pacing-stutter` | Frame Pacing / Stutter Visual Test |
| `tool.display.gamma` | Gamma Test |
| `tool.display.gradient-banding` | Gradient / Banding Test |
| `tool.display.grayscale-shadow-detail` | Grayscale / Shadow Detail Test |
| `tool.display.motion-ghosting` | Motion / Ghosting Test |
| `tool.display.refresh-rate` | Refresh Rate Test |
| `tool.display.screen-information` | Screen Information Test |
| `tool.display.screen-tearing-frame-sync` | Screen Tearing / Frame Sync Visual Test |
| `tool.display.screen-uniformity` | Screen Uniformity Test |
| `tool.network.dns` | DNS Test & DNS Doctor |
| `tool.network.download-throughput` | Internet Speed Test — Browser Download Throughput |
| `tool.network.global-connectivity` | Global Doctor — Global Connectivity Test |
| `tool.network.http-connectivity` | HTTP / HTTPS Connectivity Test |
| `tool.network.ipv6` | IPv6 Test — Check IPv4 and IPv6 Connectivity |
| `tool.network.latency` | Browser Latency Test |
| `tool.network.latency-under-load` | Latency Under Load — Browser Comparison |
| `tool.network.longest-prefix-match` | Longest Prefix Match Analyzer |
| `tool.network.health` | Network Health Check |
| `tool.network.port-check` | Port Checker |
| `tool.network.stability` | Packet Loss & Stability Test |
| `tool.network.static-route-generator` | Static Route Generator |
| `tool.network.tls-certificate` | TLS / Certificate Test |
| `tool.network.traceroute-import` | Traceroute / MTR Import |
| `tool.network.websocket` | WebSocket Connectivity Test |

### AIMarkTool

Inventory tools: 32. Published: 0. Deferred: 32.

| Tool ID | Name |
|---------|------|
| `roas-calculator` | ROAS Calculator |
| `cac-ltv-calculator` | CAC / LTV Calculator |
| `marketing-budget-planner` | Marketing Budget Planner |
| `persona-builder` | Persona Builder |
| `icp-generator` | ICP Generator |
| `jtbd-generator` | JTBD Generator |
| `pain-point-analyzer` | Pain Point Analyzer |
| `voice-of-customer-analyzer` | Voice of Customer Analyzer |
| `swot-generator` | SWOT Generator |
| `positioning-generator` | Positioning Generator |
| `marketing-plan-generator` | Marketing Plan Generator |
| `campaign-planner` | Campaign Planner |
| `value-proposition-builder` | Value Proposition Builder |
| `channel-strategy-planner` | Channel Strategy Planner |
| `landing-page-audit` | Landing Page Audit |
| `cta-analyzer` | CTA Analyzer |
| `geo-readiness-checker` | GEO / AI Search Readiness Checker |
| `keyword-intent-analyzer` | Keyword Intent Analyzer |
| `seo-audit` | SEO Audit |
| `content-gap-analyzer` | Content Gap Analyzer |
| `schema-generator` | Schema Generator |
| `content-strategy-generator` | Content Strategy Generator |
| `content-calendar-generator` | Content Calendar Generator |
| `content-brief-generator` | Content Brief Generator |
| `video-script-generator` | Video Script Generator |
| `ad-copy-generator` | Ad Copy Generator |
| `email-campaign-generator` | Email Campaign Generator |
| `social-post-generator` | Social Post Generator |
| `market-research-assistant` | Market Research Assistant |
| `competitor-analyzer` | Competitor Analyzer |
| `market-opportunity-analyzer` | Market Opportunity Analyzer |
| `trend-research-planner` | Trend Research Planner |

### PowerEngineerLab

Inventory tools: 52. Published: 9. Deferred: 43.

| Tool ID | Name |
|---------|------|
| `ac-power` | Ac Power |
| `appliance-electricity-cost` | Appliance Electricity Cost |
| `appliance-replacement-payback` | Appliance Replacement Payback |
| `battery-charging-time` | Battery Charging Time |
| `battery-runtime` | Battery Runtime |
| `cable-ampacity-estimate` | Cable Ampacity Estimate |
| `cable-short-circuit-withstand` | Cable Short Circuit Withstand |
| `compressor-leak` | Compressor Leak |
| `conductor-resistance` | Conductor Resistance |
| `data-center-energy` | Data Center Energy |
| `data-center-pue` | Data Center Pue |
| `demand-factor` | Demand Factor |
| `diversity-factor` | Diversity Factor |
| `electrical-efficiency` | Electrical Efficiency |
| `energy-cost-comparison` | Energy Cost Comparison |
| `energy-project-portfolio` | Energy Project Portfolio |
| `ev-charging` | Ev Charging |
| `fan-energy` | Fan Energy |
| `generator-sizing` | Generator Sizing |
| `home-energy-use` | Home Energy Use |
| `household-load` | Household Load |
| `hvac-cost` | Hvac Cost |
| `lighting-energy-savings` | Lighting Energy Savings |
| `load-factor` | Load Factor |
| `maximum-demand` | Maximum Demand |
| `motor-current` | Motor Current |
| `motor-torque` | Motor Torque |
| `neutral-conductor-current-screen` | Neutral Conductor Current Screen |
| `power-factor-correction` | Power Factor Correction |
| `pump-energy` | Pump Energy |
| `pv-string-design-estimate` | Pv String Design Estimate |
| `rc-time-constant` | Rc Time Constant |
| `series-parallel-resistance` | Series Parallel Resistance |
| `solar-dc-current-estimate` | Solar Dc Current Estimate |
| `solar-energy-payback` | Solar Energy Payback |
| `solar-inverter-capacity-estimate` | Solar Inverter Capacity Estimate |
| `storage-capacity-planning` | Storage Capacity Planning |
| `three-phase-fault-current-estimate` | Three Phase Fault Current Estimate |
| `transformer-losses` | Transformer Losses |
| `transformer-ratio` | Transformer Ratio |
| `transformer-voltage-regulation` | Transformer Voltage Regulation |
| `ups-sizing-runtime` | Ups Sizing Runtime |
| `voltage-drop-cable-sizing` | Voltage Drop Cable Sizing |

### HVACEngineerLab

Inventory tools: 13. Published: 1. Deferred: 12.

| Tool ID | Name |
|---------|------|
| `building-energy-benchmark` | Building Energy Benchmark |
| `chilled-water-system-planner` | Chilled Water System Planner |
| `condensate-drain-planner` | Condensate Drain Planner |
| `cooling-heating-load-planner` | Cooling Heating Load Planner |
| `data-center-cooling-planner` | Data Center Cooling Planner |
| `fan-selection-system-curve` | Fan Selection System Curve |
| `hvac-energy-operating-cost-analyzer` | Hvac Energy Operating Cost Analyzer |
| `outdoor-air-ventilation-planner` | Outdoor Air Ventilation Planner |
| `pipe-flow-pressure-drop` | Pipe Flow Pressure Drop |
| `psychrometric-process-analyzer` | Psychrometric Process Analyzer |
| `pump-sizing-system-curve` | Pump Sizing System Curve |
| `thermal-comfort-pmv-planner` | Thermal Comfort Pmv Planner |

### PrivacyFileLab

Inventory tools: 12. Published: 0. Deferred: 12.

| Tool ID | Name |
|---------|------|
| `T01` | Universal Privacy Scanner |
| `T02` | AI Upload Privacy Scanner |
| `T03` | PDF Privacy Scanner |
| `T04` | Photo Privacy Scanner |
| `T05` | Photo EXIF / GPS Cleaner |
| `T06` | PDF Metadata Cleaner |
| `T07` | Office Metadata Cleaner |
| `T08` | Sensitive Text Redactor |
| `T09` | Clean File Verifier |
| `T10` | Metadata Before / After Diff |
| `T11` | SHA-256 File Hash |
| `T12` | Local OCR |

### DataFileLab

Inventory tools: 43. Published: 0. Deferred: 43.

| Tool ID | Name |
|---------|------|
| `TOOL-001` | Excel / CSV Compare |
| `TOOL-002` | Data Cleaner & Profiler |
| `SEO-001` | CSV to XLSX |
| `SEO-002` | XLSX to CSV |
| `SEO-003` | CSV Deduplicator |
| `SEO-004` | CSV Delimiter Detector |
| `SEO-005` | CSV Encoding Detector |
| `TOOL-003` | CSV Repair |
| `TOOL-004` | Large CSV Viewer |
| `TOOL-005` | Schema Validator |
| `TOOL-006` | CSV Formula Safety Scanner |
| `TOOL-007` | CSV Column Extractor |
| `TOOL-008` | CSV File Splitter |
| `TOOL-009` | CSV Merger |
| `TOOL-010` | CSV Sorter |
| `TOOL-011` | CSV to JSON Converter |
| `TOOL-012` | JSON to CSV Converter |
| `TOOL-013` | CSV Row Filter |
| `TOOL-014` | CSV Transpose |
| `TOOL-015` | CSV to Markdown Table |
| `TOOL-016` | CSV Row Range Extractor |
| `TOOL-017` | CSV Header Editor |
| `TOOL-018` | CSV Value Frequency |
| `TOOL-019` | CSV Find and Replace |
| `TOOL-020` | CSV Row Sampler |
| `TOOL-021` | CSV to JSONL |
| `TOOL-022` | JSONL to CSV |
| `TOOL-023` | CSV Column Combiner |
| `TOOL-024` | CSV Column Splitter |
| `TOOL-025` | CSV to PostgreSQL INSERT |
| `TOOL-026` | CSV to HTML Table |
| `TOOL-027` | CSV Row Numberer |
| `TOOL-028` | CSV Blank Row Remover |
| `TOOL-029` | CSV Cell Trimmer |
| `TOOL-030` | CSV Empty Cell Filler |
| `TOOL-031` | CSV to XML Converter |
| `TOOL-032` | XML to CSV Converter |
| `TOOL-033` | CSV to YAML Converter |
| `TOOL-034` | YAML to CSV Converter |
| `TOOL-035` | CSV to TOML Converter |
| `TOOL-036` | TOML to CSV Converter |
| `TOOL-037` | CSV to Parquet Converter |
| `TOOL-038` | Parquet to CSV Converter |

### WaterEngineerLab

Inventory tools: 18. Published: 3. Deferred: 15.

| Tool ID | Name |
|---------|------|
| `TOOL-001` | Stormwater Drainage Design Planner |
| `TOOL-002` | Rainfall / IDF Design Storm Helper |
| `TOOL-004` | Time of Concentration Calculator |
| `TOOL-005` | Storm Drain Pipe Capacity & Sizing |
| `TOOL-006` | Detention / Storage Preliminary Sizing |
| `TOOL-008` | Culvert Capacity Preliminary Check |
| `TOOL-009` | Hydraulic Grade / Energy Grade Helper |
| `TOOL-011` | Pipe Diameter Sizing Calculator |
| `TOOL-012` | Pressure / Static Head / Residual Pressure Check |
| `TOOL-013` | Pump Duty Point Helper |
| `TOOL-014` | Water Distribution Network Preliminary Planner |
| `TOOL-015` | Site Drainage Layout / Scenario Comparator |
| `TOOL-016` | Composite Runoff Coefficient Calculator |
| `TOOL-017` | Catchment Area Breakdown & Runoff Summary |
| `TOOL-018` | IDF Curve Interpolator |

### StructuralEngineerLab

Inventory tools: 25. Published: 3. Deferred: 22.

| Tool ID | Name |
|---------|------|
| `TOOL-001` | Beam Analysis Calculator |
| `TOOL-002` | Section Properties Calculator |
| `TOOL-005` | Simply Supported Beam Calculator |
| `TOOL-006` | Cantilever Beam Calculator |
| `TOOL-007` | Beam Deflection Calculator |
| `TOOL-009` | Section Modulus Calculator |
| `TOOL-010` | User-Defined Utilization Calculator |
| `TOOL-018` | Beam Load Case Normalizer & Validator |
| `TOOL-019` | Beam Load Resultant & Centroid Calculator |
| `TOOL-020` | Beam Reaction Equilibrium Checker |
| `TOOL-023` | Beam Deflection–Curvature Consistency Validator |
| `TOOL-029` | Beam Strain Energy & Compliance Calculator |
| `TOOL-030` | Beam Virtual Work Displacement Calculator |
| `TOOL-031` | Maxwell–Betti Displacement Reciprocity Checker |
| `TOOL-032` | Single Redundant Compatibility Solver |
| `TOOL-011` | Beam Slope & Rotation Calculator |
| `TOOL-012` | Section Stress Distribution Calculator |
| `TOOL-013` | Beam Load Combination Envelope |
| `TOOL-014` | Beam Critical Location Report |
| `TOOL-015` | Beam Response Comparison Calculator |
| `TOOL-016` | Beam Design Snapshot Export |
| `TOOL-017` | Beam Review Notes & Assumption Register |

### DevEngineerLab

Inventory tools: 67. Published: 0. Deferred: 67.

| Tool ID | Name |
|---------|------|
| `TOOL-001` | JSON Formatter |
| `TOOL-002` | JSON Validator |
| `TOOL-003` | JSON Schema Validator |
| `TOOL-004` | JSON ↔ YAML Converter |
| `TOOL-005` | Base64 Encode & Decode |
| `TOOL-006` | UUID Generator |
| `TOOL-007` | Timestamp Converter |
| `TOOL-008` | Regex Tester |
| `TOOL-009` | JWT Decoder |
| `TOOL-010` | Text Diff |
| `TOOL-011` | REST API Tester |
| `TOOL-012` | HTTP Request Builder |
| `TOOL-013` | cURL Parser |
| `TOOL-014` | cURL Generator |
| `TOOL-015` | cURL → Code Converter |
| `TOOL-016` | API Response Diff |
| `TOOL-017` | OpenAPI Validator |
| `TOOL-018` | .env Validator |
| `TOOL-019` | Webhook Payload Inspector |
| `TOOL-020` | Webhook Signature Validator |
| `TOOL-021` | OpenAPI Mock Data Generator |
| `TOOL-022` | JSON → TypeScript Type Generator |
| `TOOL-023` | URL Encode & Decode |
| `TOOL-024` | Hash Generator |
| `TOOL-025` | CSV ↔ JSON Converter |
| `TOOL-026` | JSON → JSON Schema Generator |
| `TOOL-027` | JSON Escape & Unescape |
| `TOOL-028` | Integer Base Converter |
| `TOOL-029` | Query String ↔ JSON Converter |
| `TOOL-030` | Text Statistics |
| `TOOL-032` | JSON Minifier |
| `TOOL-033` | JSON Diff |
| `TOOL-034` | JSON Patch Builder |
| `TOOL-035` | JSON Pointer Resolver |
| `TOOL-036` | JSON Lines Converter |
| `TOOL-037` | JSON Merge Tool |
| `TOOL-038` | JSON Flatten & Unflatten |
| `TOOL-039` | JSON Key Sorter |
| `TOOL-040` | JSON Array Deduplicator |
| `TOOL-041` | JSON Sample Generator |
| `TOOL-042` | JSON Type Profiler |
| `TOOL-043` | JSONPath Query Tool |
| `TOOL-045` | JSON Schema Faker |
| `TOOL-046` | NDJSON Validator |
| `TOOL-048` | Text Case Converter |
| `TOOL-049` | Slug Generator |
| `TOOL-050` | Whitespace Visualizer |
| `TOOL-051` | Unicode Inspector |
| `TOOL-052` | Unicode Normalizer |
| `TOOL-053` | Character Code Explorer |
| `TOOL-054` | Line Ending Converter |
| `TOOL-055` | Text Deduplicator |
| `TOOL-056` | Text Sorter |
| `TOOL-057` | Text Columnizer |
| `TOOL-058` | Text Wrap Calculator |
| `TOOL-059` | Lorem Ipsum Generator |
| `TOOL-044` | JSON Schema to TypeScript |
| `TOOL-047` | JSON5 Converter |
| `TOOL-060` | Markdown Table Generator |
| `TOOL-061` | Markdown TOC Generator |
| `TOOL-062` | HTML to Markdown |
| `TOOL-063` | Markdown to HTML |
| `TOOL-064` | Diff Patch Generator |
| `TOOL-065` | URL Builder |
| `TOOL-066` | URL Parser |
| `TOOL-067` | URL Query Editor |
| `TOOL-068` | URL Pattern Tester |

### DIYCalcLab

Inventory tools: 40. Published: 3. Deferred: 37.

| Tool ID | Name |
|---------|------|
| `concrete-bag` | Concrete Bags |
| `paint` | Paint |
| `tile` | Tile |
| `flooring` | Flooring |
| `square-footage` | Square Footage |
| `mulch` | Mulch |
| `gravel` | Gravel |
| `drywall` | Drywall |
| `roofing` | Roofing Shingles |
| `deck-board` | Deck Boards |
| `fence` | Fence |
| `topsoil` | Topsoil |
| `paver` | Pavers |
| `brick` | Bricks |
| `stair` | Stairs |
| `wallpaper` | Wallpaper |
| `cubic-yard` | Cubic Yards |
| `feet-inches` | Feet & Inches |
| `concrete-block` | Concrete Block |
| `rebar` | Rebar |
| `sonotube` | Sonotube |
| `concrete-step` | Concrete Steps |
| `insulation` | Insulation |
| `roof-area` | Roofing |
| `siding` | Siding |
| `retaining-wall` | Retaining Wall |
| `sand` | Sand |
| `grout` | Grout |
| `thinset` | Thinset |
| `carpet` | Carpet |
| `baseboard` | Baseboard |
| `crown-molding` | Crown Molding |
| `laminate-flooring` | Laminate Flooring |
| `backsplash` | Backsplash |
| `ceiling-tile` | Drop Ceiling |
| `stain` | Deck & Fence Stain |
| `epoxy-floor` | Epoxy Floor |

Deferred inventory rows: 350. Inventory rows: 375. Published topic files: 25.

## What the next batch should do

- Read the production script for one deferred tool, recompute one example, and add one topic file. Do not generate the rest of that site in the same pass.
- Prefer the tools already named in the GATE 4 deferred table when the equation is closed-form (PoE voltage drop is the shortest known candidate).
- Leave DNS, file, OCR, and API tools as algorithm notes only when a formula page would be false.
- Fill a “Reference Standards” section only after the cited document is opened. Pending is the correct label until then.
