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

| Domain | Folder | Production site |
|--------|--------|-----------------|
| NetEngineerLab | [NetEngineerLab/](NetEngineerLab/) | https://netengineerlab.com |
| PCDog | [PCDog/](PCDog/) | https://pcdog.com |
| AIMarkTool | [AIMarkTool/](AIMarkTool/) | https://aimarktool.com |
| PowerEngineerLab | [PowerEngineerLab/](PowerEngineerLab/) | https://powerengineerlab.com |
| HVACEngineerLab | [HVACEngineerLab/](HVACEngineerLab/) | https://hvacengineerlab.com |
| PrivacyFileLab | [PrivacyFileLab/](PrivacyFileLab/) | https://privacyfilelab.com |
| DataFileLab | [DataFileLab/](DataFileLab/) | https://datafilelab.com |
| WaterEngineerLab | [WaterEngineerLab/](WaterEngineerLab/) | https://waterengineerlab.com |
| StructuralEngineerLab | [StructuralEngineerLab/](StructuralEngineerLab/) | https://structuralengineerlab.com |
| DevEngineerLab | [DevEngineerLab/](DevEngineerLab/) | https://devengineerlab.com |
| DIYCalcLab | [DIYCalcLab/](DIYCalcLab/) | https://diycalclab.com |

Each domain folder contains a README topic index. Individual formula files (kebab-case `.md`) are added after verification.

---

## 3. Formula knowledge-base navigation

1. Start from this README → open a domain folder.
2. Read that domain’s README topic index.
3. Open a topic file (when present) for Overview, Formula, Variables, Principles, Worked Example, Limitations, Standards, Online Calculator, Related Formulas, and Verification.
4. Cross-check status in [reports/](reports/) (inventory and later verification reports).

**Current stage:** GATE 3/4 first batch — 25 formula topics are published and marked `VERIFIED` against production calculator code. The other registered tools are not documented yet. See [reports/FORMULA_VERIFICATION.md](reports/FORMULA_VERIFICATION.md) and [reports/GATE3_STATUS.md](reports/GATE3_STATUS.md).

Audit inventory (375 registered tools):

- [reports/GATE1_TOOL_INVENTORY.md](reports/GATE1_TOOL_INVENTORY.md)
- [reports/GATE1_TOOL_INVENTORY.json](reports/GATE1_TOOL_INVENTORY.json)

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
| No marketing filler | Engineering explanation over SEO spam |
| No site source edits | This repo must not modify the eleven website codebases |

Automation (GATE 6) will lint Markdown, links, and verification flags — it will **not** rewrite the eleven product apps.

---

## 5. Online calculator entry

Live calculators remain on the production domains listed above. Topic pages will link **only** to the matching tool URL (from inventory), never a blanket list of all eleven sites in every article.

Until topic pages exist, use each domain’s production homepage or the URLs in the GATE1 inventory.

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
| CI | Upcoming GitHub Actions doc checks (GATE 6) |
| Releases | Prefer PR review into `main`; no unverified bulk dumps |

Status notes for gates live under [reports/](reports/) (`GATE0_STATUS.md`, `GATE2_STATUS.md`, `GATE3_STATUS.md`, `FORMULA_VERIFICATION.md`).

---

## Repository layout

```text
Calculator/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── NetEngineerLab/ … DIYCalcLab/   # domain docs
├── scripts/                        # inventory & (later) validators
└── reports/                        # gate audits & verification
```
