# Calculator — Engineering Formula Library

Open engineering calculator formulas, worked examples, and links to online tools for eleven related product sites under the **ddcodedog** organization.

This repository is a **documentation and verification** library. Formula Markdown is written only after local source and production URL audit. Unverified content is never labeled `VERIFIED`.

**Repository:** https://github.com/ddcodedog/Calculator

---

## 1. Introduction

Engineering teams and learners often need:

- Clear formulas with units and assumptions
- Worked numerical examples
- Pointers to the matching online calculator

This library collects that material per domain site. Content is English-first, engineering-oriented, and tied to real tools registered in GATE 1 inventory reports.

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
- 同一专题的简体中文稿，不另计篇数：[先把报头算进字节，再取安全上行，最后算时间](NetEngineerLab/on-wire-bytes-at-safe-uplink.zh-CN.md)

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
