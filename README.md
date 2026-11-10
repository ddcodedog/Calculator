# Calculator — Engineering Formula Library

Worked formulas, units, and numerical examples for eleven engineering calculator sites: network design, PC routing and display timing, marketing measurement, electrical power, HVAC loads and airflow, local file privacy, CSV inspection, water and drainage, structural members, developer text and time utilities, and DIY quantities.

Each published note names the relation it uses, a case you can recompute, the limits of that model, and the live calculator on the product site. A `VERIFIED` label means that note was checked against the production source and an example. Notes that have not been checked that way keep their recorded label.

**Repository:** https://github.com/ddcodedog/Calculator

---

## 1. Introduction

Engineering teams and learners often need:

- Clear formulas with units and assumptions
- Worked numerical examples
- Pointers to the matching online calculator

This library collects that material per domain site. The notes are in English and are tied to real tools registered in the GATE 1 inventory. The twelve NetEngineerLab notes also have Simplified Chinese editions. Those editions are the same topics, linked from [NetEngineerLab/README.md](NetEngineerLab/README.md) and from each English note, and they are not an extra count.

**Hard rules**

- No batch generation of fake formulas, invented standards, or invented tool links
- DNS / file / OCR / API tools get algorithm or protocol docs — not forced math formulas
- Relative Markdown links must resolve on GitHub

---

## 2. Domain entry points (11 sites)

| Domain | Folder | Published topics | Production site |
|--------|--------|------------------|-----------------|
| NetEngineerLab | [NetEngineerLab/](NetEngineerLab/) | 12 | https://netengineerlab.com |
| PCDog | [PCDog/](PCDog/) | 6 | https://pcdog.com |
| AIMarkTool | [AIMarkTool/](AIMarkTool/) | 6 | https://aimarktool.com |
| PowerEngineerLab | [PowerEngineerLab/](PowerEngineerLab/) | 15 | https://powerengineerlab.com |
| HVACEngineerLab | [HVACEngineerLab/](HVACEngineerLab/) | 5 | https://hvacengineerlab.com |
| PrivacyFileLab | [PrivacyFileLab/](PrivacyFileLab/) | 6 | https://privacyfilelab.com |
| DataFileLab | [DataFileLab/](DataFileLab/) | 6 | https://datafilelab.com |
| WaterEngineerLab | [WaterEngineerLab/](WaterEngineerLab/) | 8 | https://waterengineerlab.com |
| StructuralEngineerLab | [StructuralEngineerLab/](StructuralEngineerLab/) | 9 | https://structuralengineerlab.com |
| DevEngineerLab | [DevEngineerLab/](DevEngineerLab/) | 6 | https://devengineerlab.com |
| DIYCalcLab | [DIYCalcLab/](DIYCalcLab/) | 9 | https://diycalclab.com |

Each folder README is the topic index for that site. The count is the number of topic files in that folder. Deferred inventory rows stay listed in [reports/FIRST_RELEASE.md](reports/FIRST_RELEASE.md), not as extra pages.

---

## 3. Formula knowledge-base navigation

Published formula topics: 88

1. Open a domain folder from the table above.
2. Read that domain’s README topic index.
3. Open a topic file for Overview, Formula, Variables, Principles, Worked Example, Limitations, Standards, Online Calculator, Related Formulas, and Verification.
4. Cross-check status in [reports/FORMULA_VERIFICATION.md](reports/FORMULA_VERIFICATION.md).

Audit inventory (375 registered tools): [reports/GATE1_TOOL_INVENTORY.md](reports/GATE1_TOOL_INVENTORY.md), [reports/GATE1_TOOL_INVENTORY.json](reports/GATE1_TOOL_INVENTORY.json).

Chinese outreach drafts keyed by site live under [promo/zh/](promo/zh/README.md). They are not formula topics, are not counted above, and are outside the verified-topic checks.

### NetEngineerLab

- [Single-span fiber link loss](NetEngineerLab/fiber-link-loss.md)
- [Optical link power budget](NetEngineerLab/optical-power-budget.md)
- [Fiber propagation delay and RTT](NetEngineerLab/fiber-propagation-latency.md)
- [Chromatic dispersion coefficient D(λ)](NetEngineerLab/chromatic-dispersion.md)
- [OSPF interface cost](NetEngineerLab/ospf-interface-cost.md)
- [STP port path cost](NetEngineerLab/stp-path-cost.md)
- [File transfer time from link rate](NetEngineerLab/bandwidth-transfer-time.md)
- [MTU, MSS, and encapsulation overhead](NetEngineerLab/mtu-mss-overhead.md)
- [DNS TTL window before a record change](NetEngineerLab/dns-ttl-cache-window.md)
- [Access-switch demand against uplink headroom](NetEngineerLab/switch-uplink-safe-capacity.md)
- [A cutover wait is not a fiber round trip](NetEngineerLab/cutover-wait-versus-fiber-delay.md)
- [Header bytes, then the safe uplink, then the clock](NetEngineerLab/on-wire-bytes-at-safe-uplink.md)

Simplified Chinese editions of those twelve topics. They are not additional formula counts:

- [单段光纤链路损耗](NetEngineerLab/fiber-link-loss.zh-CN.md)
- [光链路功率预算](NetEngineerLab/optical-power-budget.zh-CN.md)
- [光纤传播时延与往返时间](NetEngineerLab/fiber-propagation-latency.zh-CN.md)
- [色度色散系数 D(λ)](NetEngineerLab/chromatic-dispersion.zh-CN.md)
- [OSPF 接口开销](NetEngineerLab/ospf-interface-cost.zh-CN.md)
- [STP 端口路径开销](NetEngineerLab/stp-path-cost.zh-CN.md)
- [由链路速率得到的文件传输时间](NetEngineerLab/bandwidth-transfer-time.zh-CN.md)
- [MTU、MSS 与封装开销](NetEngineerLab/mtu-mss-overhead.zh-CN.md)
- [记录变更前的 DNS TTL 窗口](NetEngineerLab/dns-ttl-cache-window.zh-CN.md)
- [接入交换机需求与上行余量](NetEngineerLab/switch-uplink-safe-capacity.zh-CN.md)
- [割接等待不是光纤往返时延](NetEngineerLab/cutover-wait-versus-fiber-delay.zh-CN.md)
- [先把报头算进字节，再取安全上行，最后算时间](NetEngineerLab/on-wire-bytes-at-safe-uplink.zh-CN.md)

### PowerEngineerLab

- [DC Ohm’s law](PowerEngineerLab/ohms-law.md)
- [Sinusoidal power triangle](PowerEngineerLab/power-triangle.md)
- [Ideal inductive reactance](PowerEngineerLab/inductive-reactance.md)
- [Ideal capacitive reactance](PowerEngineerLab/capacitive-reactance.md)
- [Resistive voltage divider](PowerEngineerLab/voltage-divider.md)
- [Transformer full-load current](PowerEngineerLab/transformer-full-load-current.md)
- [AC machine synchronous speed](PowerEngineerLab/synchronous-speed.md)
- [Induction-motor slip](PowerEngineerLab/induction-motor-slip.md)
- [Kilowatt to mechanical horsepower](PowerEngineerLab/kilowatt-to-horsepower.md)
- [Ideal transformer turns and voltage ratio](PowerEngineerLab/transformer-turns-ratio.md)
- [Same-interval load factor](PowerEngineerLab/interval-load-factor.md)
- [Demand factor from maximum and connected load](PowerEngineerLab/maximum-demand-factor.md)
- [Appliance energy over a stated duty](PowerEngineerLab/appliance-period-energy-cost.md)
- [Three readings from one heater shop](PowerEngineerLab/three-shop-ratios.md)
- [Do not feed a divider tap into a winding](PowerEngineerLab/divider-is-not-a-winding.md)

### StructuralEngineerLab

- [Euler elastic column buckling load](StructuralEngineerLab/euler-column-buckling.md)
- [Elastic beam bending stress](StructuralEngineerLab/beam-bending-stress.md)
- [Centroidal area and section modulus](StructuralEngineerLab/section-properties.md)
- [Cantilever tip load and deflection](StructuralEngineerLab/cantilever-tip-deflection.md)
- [Simply supported midspan deflection](StructuralEngineerLab/simply-supported-midspan-deflection.md)
- [Off-center point load on a simple span](StructuralEngineerLab/simply-supported-offcenter-point-load.md)
- [Full uniform load on a simple span](StructuralEngineerLab/simply-supported-uniform-load.md)
- [A 5 m strip’s moment, then the fiber stress](StructuralEngineerLab/strip-moment-to-fiber-stress.md)
- [Put the axial load over Euler. Leave the moment out.](StructuralEngineerLab/axial-ratio-beside-moment.md)

### WaterEngineerLab

- [Manning open-channel discharge](WaterEngineerLab/manning-open-channel-flow.md)
- [Rational-method peak runoff](WaterEngineerLab/rational-method-peak-runoff.md)
- [Darcy-Weisbach major pipe headloss](WaterEngineerLab/darcy-weisbach-pipe-headloss.md)
- [Catchment breakdown and peak runoff sum](WaterEngineerLab/catchment-runoff-summary.md)
- [Single-source tree residual head](WaterEngineerLab/tree-network-residual-head.md)
- [Weighted score for two drainage layouts](WaterEngineerLab/site-drainage-scenario-score.md)
- [Does the ditch pass the lot peak?](WaterEngineerLab/ditch-capacity-versus-lot-peak.md)
- [One pipe: the residual is the Darcy loss. A second pipe is not.](WaterEngineerLab/single-pipe-residual-matches-darcy.md)

### HVACEngineerLab

- [Duct friction and local pressure drop](HVACEngineerLab/duct-friction-pressure-drop.md)
- [Cooling and heating load components](HVACEngineerLab/cooling-heating-load-components.md)
- [Psychrometric process between two states](HVACEngineerLab/psychrometric-process-states.md)
- [The coil’s volume flow can enter the duct tool. Its watts cannot.](HVACEngineerLab/mass-flow-into-duct-velocity.md)
- [A positive latent term is not condensate](HVACEngineerLab/latent-sign-is-not-condensate.md)

### DIYCalcLab

- [Concrete slab volume and bag count](DIYCalcLab/concrete-slab-volume.md)
- [Roof pitch and slope factor](DIYCalcLab/roof-pitch.md)
- [Board-foot lumber volume](DIYCalcLab/board-foot.md)
- [Fence posts, rails, and pickets](DIYCalcLab/fence-post-and-picket-count.md)
- [Slab rebar grid count](DIYCalcLab/slab-rebar-grid.md)
- [Modular bricks for a wall with one opening](DIYCalcLab/modular-brick-wall-count.md)
- [Blown-fiberglass bags for an attic top-up](DIYCalcLab/blown-fiberglass-attic-bags.md)
- [One 18 by 9 ft pad, then the steel that sits in it](DIYCalcLab/eighteen-by-nine-slab-and-mat.md)
- [The pitch tool’s rafter length is the board-foot length](DIYCalcLab/rafter-length-into-board-feet.md)

### AIMarkTool

- [Return on ad spend](AIMarkTool/return-on-ad-spend.md)
- [Order-value LTV to CAC](AIMarkTool/order-value-ltv-to-cac.md)
- [Successive funnel counts from stage percents](AIMarkTool/funnel-stage-counts.md)
- [Equal-group sample size for an absolute rate lift](AIMarkTool/ab-equal-group-sample-size.md)
- [Forty customers, then a ratio that sometimes equals ROAS](AIMarkTool/one-count-two-ratios.md)
- [Eight thousand planned visitors are not the forty you already have](AIMarkTool/planned-sample-versus-arrivals.md)

### DataFileLab

- [CSV value frequency counts](DataFileLab/csv-value-frequency.md)
- [CSV encoding detection](DataFileLab/csv-encoding-detection.md)
- [Dropping CSV records whose cells are all empty](DataFileLab/csv-blank-record-removal.md)
- [A leading row-number column](DataFileLab/csv-row-number-column.md)
- [Label the bytes, drop the empty record, then tally the city](DataFileLab/encoding-blank-then-city-tally.md)
- [Number the kept rows. Do not frequency-count that new column.](DataFileLab/do-not-tally-the-row-number.md)

### DevEngineerLab

- [Unix timestamp conversion](DevEngineerLab/unix-timestamp-conversion.md)
- [Integer base conversion](DevEngineerLab/integer-base-conversion.md)
- [Word wrap at a grapheme width](DevEngineerLab/word-wrap-grapheme-width.md)
- [Local counts of code points, graphemes, and lines](DevEngineerLab/local-text-size-counts.md)
- [Wrap the relay note, then count again](DevEngineerLab/wrap-then-recount-lines.md)
- [One integer, a clock in one tool and hex in the other](DevEngineerLab/same-integer-two-tools.md)

### PCDog

- [IPv4 longest prefix match](PCDog/ipv4-longest-prefix-match.md)
- [IPv4 static route commands](PCDog/ipv4-static-route-commands.md)
- [Estimated backing pixels from the screen API](PCDog/screen-backing-pixel-estimate.md)
- [Refresh estimate from a list of frame intervals](PCDog/refresh-frame-interval-summary.md)
- [Keep the longer prefix, then print that route](PCDog/keep-the-longer-prefix-then-print-it.md)
- [Backing-store pixels sit beside frame time. They do not multiply.](PCDog/pixels-beside-frame-time.md)

### PrivacyFileLab

- [Local SHA-256 file digest](PrivacyFileLab/sha256-file-digest.md)
- [Sensitive text pattern redaction](PrivacyFileLab/sensitive-text-redaction.md)
- [Which sensitive-text types disappeared](PrivacyFileLab/metadata-finding-type-diff.md)
- [When the clean-file verifier allows a download](PrivacyFileLab/clean-file-verifier-status.md)
- [Hash the text the verifier accepted](PrivacyFileLab/hash-only-after-the-verifier.md)
- [A new digest does not clear a phone the diff still sees](PrivacyFileLab/different-digest-failed-diff.md)

---


## Formula search index

Published formula topics: the count above is English topic files only. `*.zh-CN.md` companions are the same topics in Simplified Chinese.

Machine-readable indexes:

- [indexes/topics.json](indexes/topics.json) — one row per English topic, with tool id, Chinese companion, and both statuses
- [indexes/verification-index.json](indexes/verification-index.json) — calculation status, standards status, and the evidence fields
- [config/locale-routes.json](config/locale-routes.json) — production English and Chinese URLs checked on 2026-11-10
- [llms.txt](llms.txt) — a short map for automated readers. It does not claim inclusion in any search or answer engine

Each site block below is that site's topic list. The per-site index is the folder README.

## English and Chinese entries

English is the source text. Simplified Chinese companions exist for the twelve NetEngineerLab topics and stay in the same directory as `*.zh-CN.md`. They are linked from [NetEngineerLab/README.md](NetEngineerLab/README.md). A Chinese file is not an extra English topic.

Other production sites do have live localized pages. Those URLs were probed and recorded in [reports/LOCALE_ROUTE_MATRIX.md](reports/LOCALE_ROUTE_MATRIX.md). This round does not add Chinese topic files for them.

## Verification method

A calculation `VERIFIED` row means the formula, units, one worked example, and a boundary case were checked against the production calculator, as recorded in [reports/FORMULA_VERIFICATION.md](reports/FORMULA_VERIFICATION.md). It does not mean a design-code PDF was re-audited.

Standards status is separate. `PENDING` means the cited standard text and version were not both checked. One mechanical-horsepower factor is `VERIFIED` from Fed. Std. 376B. The audit is [reports/FORMULA_STANDARDS_AUDIT.md](reports/FORMULA_STANDARDS_AUDIT.md).

## Standards citation notes

Cite the standard number, the section that supports the formula, and the URL that was actually opened. If the PDF was not read, say so and leave standards status `PENDING`. Do not replace an official source with a secondary page because the official page returned 403 or a login wall.

How to cite a topic is written in [docs/CITATION.md](docs/CITATION.md).

## How to use the online calculators

1. Open the topic and read the formula, the units, and the worked example.
2. Use the single Online Calculator link in that topic. A site homepage is not a substitute for the tool page.
3. On NetEngineerLab, the Chinese tool page is `/tools/<slug>/zh/` when that page was checked. A `/zh-CN/tools/...` path is not the NetEngineerLab Chinese route.
4. Keep the topic's limits. The page does not become a code-compliance check because the arithmetic was verified.

## How to cite

Name the site, the tool id, the topic path, the calculation status, the standards status, and the verification date from the topic. Details and an example are in [docs/CITATION.md](docs/CITATION.md).

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Add a branch and a pull request. Include the production source and the example you recomputed. Do not invent a tool URL, a standard, or a locale route.

## Version and changelog

- 2026-11-10 — Documentation V2.0. Navigation, citation notes, a checked locale matrix, separate calculation and standards status, and stricter documentation checks. No new formula topics were added. Nothing here deploys the eleven product sites.
- 2026-11-04 through 2026-11-10 — The topic batches and their evidence stay in [reports/FORMULA_VERIFICATION.md](reports/FORMULA_VERIFICATION.md).

## 4. Documentation and verification principles

| Principle | Requirement |
|-----------|-------------|
| Source first | Match real site source / registration before writing |
| Units | Variables and units must be explicit |
| Examples | Worked examples must be independently checkable |
| Standards | Cite only verifiable references; else mark pending |
| Status labels | Only use `VERIFIED` after GATE 4–style checks |
| Uncertainty | Mark `REVIEW_REQUIRED` when disputed or incomplete |
| No marketing filler | Engineering explanation over SEO spam. No fake FAQs and no ranking claims |
| No site source edits | This repo must not modify the eleven website codebases |

`python3 scripts/check-docs.py` checks duplicate titles, relative links, math fences, verification status, topic indexes, and tool URLs. Paths under `promo/` are skipped by those formula gates. [`.github/workflows/doc-checks.yml`](.github/workflows/doc-checks.yml) runs that script on push and pull request and uploads the JSON report. The job does not edit this repository or the eleven product sites.

---

## 5. Online calculator entry

Live calculators remain on the production domains in the table above. Each published topic has one Online Calculator link: the page for that tool. Topic files do not repeat the other ten sites. Folders with `Published topics: 0` do not add tool URLs.

---

## 6. Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Summary: propose changes on a branch / PR; include source location and verification notes; do not invent URLs or standards.

---

## 7. License

Unless noted otherwise in a file header, documentation and scaffolding in this repository are under the [MIT License](LICENSE).

Third-party trademarks and product names belong to their owners. Linked calculator sites have their own terms.

---

## 8. Maintenance

| Item | Practice |
|------|----------|
| Inventory | Refresh `reports/GATE1_*` when tools are added/removed on product sites |
| Formulas | Add/update topic Markdown only with verification evidence |
| Links | Re-check production URLs after site route changes |
| CI | [`.github/workflows/doc-checks.yml`](.github/workflows/doc-checks.yml) runs `python3 scripts/check-docs.py` and reports the result |
| Releases | Prefer PR review into `main`; no unverified bulk dumps. First batch scope is [reports/FIRST_RELEASE.md](reports/FIRST_RELEASE.md) |

Status notes for gates live under [reports/](reports/) (`GATE0_STATUS.md`, `GATE2_STATUS.md`, `GATE3_STATUS.md`, `FORMULA_VERIFICATION.md`, `FIRST_RELEASE.md`).

---

## Repository layout

```text
Calculator/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── .github/workflows/doc-checks.yml
├── NetEngineerLab/ … DIYCalcLab/   # domain docs
├── promo/zh/                       # Chinese outreach drafts, keyed by site
├── scripts/                        # inventory helpers and check-docs.py
└── reports/                        # gate audits, verification, release scope
```
