# Intentional English / Chinese formula differences

Date: 2026-11-10.

The twelve NetEngineerLab `*.zh-CN.md` files were compared with the English topic beside them. Display-math blocks match after whitespace is removed. No intentional formula difference was found, so `reports/ZH_FORMULA_REVIEW.json` lists none.

Checked together with the math blocks:

- Unit tokens that appear as units in the English formula section still appear in the Chinese file.
- Worked-example numbers in a Chinese `算例` section still include the English example numbers.
- Limitation numbers are still present where both files have a limitations section.
- Related-formula links in the Chinese files point at Chinese companions when those companions exist. The link back to the English original is the one allowed English link.

The English kilowatt-to-horsepower note contains both 745.6999 and 735.49875. There is no Chinese companion for that topic in this repository. The 735.49875 factor is a calculator constant, not an English-versus-Chinese documentation drift.
