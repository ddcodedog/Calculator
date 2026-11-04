# Contributing to Calculator

Thank you for helping improve this engineering formula library.

## Scope

- Add or fix **formula / algorithm documentation** under the eleven domain folders
- Improve inventory and verification reports under `reports/`
- Improve validation scripts under `scripts/` (GATE 6+)

**Out of scope:** modifying the source code of the eleven production websites from this repository.

## Workflow

1. Fork or branch from the latest `main` (or open a PR against `main`).
2. Prefer a focused branch name, e.g. `docs/netengineerlab-fiber-loss`.
3. Follow the topic template (Overview → Formula → Variables → Principles → Worked Example → Limitations → Standards → Online Calculator → Related → Verification).
4. Filenames: English lowercase kebab-case, e.g. `optical-power-budget.md`.
5. Link only **real** production calculator URLs from the GATE1 inventory (or freshly verified routes).
6. Do **not** mark a document `VERIFIED` without independent checks against source and at least one worked example.
7. Run any available doc checks in `scripts/` / CI before requesting review.
8. Open a Pull Request with: what changed, which tool IDs, verification evidence, and remaining risks.

## Content standards

- English preferred
- No copy-paste of entire marketing pages
- No keyword stuffing or fake FAQs
- No invented standards, papers, or tool links
- Non-math tools → algorithm / protocol / unit-conversion docs instead of forced formulas
- Uncertain items → `REVIEW_REQUIRED`

## Reporting issues

Open a GitHub Issue with the domain name, tool ID, production URL, and what is wrong (formula, units, link, example).

## License

By contributing, you agree your contributions are licensed under the MIT License in this repository.
