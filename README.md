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
| NetEngineerLab | [NetEngineerLab/](NetEngineerLab/) | 6 | https://netengineerlab.com |
| PCDog | [PCDog/](PCDog/) | 0 | https://pcdog.com |
| AIMarkTool | [AIMarkTool/](AIMarkTool/) | 0 | https://aimarktool.com |
| PowerEngineerLab | [PowerEngineerLab/](PowerEngineerLab/) | 9 | https://powerengineerlab.com |
| HVACEngineerLab | [HVACEngineerLab/](HVACEngineerLab/) | 1 | https://hvacengineerlab.com |
| PrivacyFileLab | [PrivacyFileLab/](PrivacyFileLab/) | 0 | https://privacyfilelab.com |
| DataFileLab | [DataFileLab/](DataFileLab/) | 0 | https://datafilelab.com |
| WaterEngineerLab | [WaterEngineerLab/](WaterEngineerLab/) | 3 | https://waterengineerlab.com |
| StructuralEngineerLab | [StructuralEngineerLab/](StructuralEngineerLab/) | 3 | https://structuralengineerlab.com |
| DevEngineerLab | [DevEngineerLab/](DevEngineerLab/) | 0 | https://devengineerlab.com |
| DIYCalcLab | [DIYCalcLab/](DIYCalcLab/) | 3 | https://diycalclab.com |

Each folder README is the topic index for that site. A zero means batch 1 published no formula file there. Deferred inventory rows are listed in [reports/FIRST_RELEASE.md](reports/FIRST_RELEASE.md), not as extra pages.

---

## 3. Formula knowledge-base navigation

Published formula topics: 25

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

### StructuralEngineerLab

- [Euler elastic column buckling load](StructuralEngineerLab/euler-column-buckling.md)
- [Elastic beam bending stress](StructuralEngineerLab/beam-bending-stress.md)
- [Centroidal area and section modulus](StructuralEngineerLab/section-properties.md)

### WaterEngineerLab

- [Manning open-channel discharge](WaterEngineerLab/manning-open-channel-flow.md)
- [Rational-method peak runoff](WaterEngineerLab/rational-method-peak-runoff.md)
- [Darcy-Weisbach major pipe headloss](WaterEngineerLab/darcy-weisbach-pipe-headloss.md)

### HVACEngineerLab

- [Duct friction and local pressure drop](HVACEngineerLab/duct-friction-pressure-drop.md)

### DIYCalcLab

- [Concrete slab volume and bag count](DIYCalcLab/concrete-slab-volume.md)
- [Roof pitch and slope factor](DIYCalcLab/roof-pitch.md)
- [Board-foot lumber volume](DIYCalcLab/board-foot.md)

### No published topic in batch 1

[AIMarkTool](AIMarkTool/), [DataFileLab](DataFileLab/), [DevEngineerLab](DevEngineerLab/), [PCDog](PCDog/), and [PrivacyFileLab](PrivacyFileLab/) link to the inventory and the deferred list. They do not contain formula pages.

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
