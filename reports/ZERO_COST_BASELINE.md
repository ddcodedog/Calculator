# Zero-Cost Promotion Baseline (GATE 1)

- **Date (Asia/Shanghai):** 2026-11-04, audit window about 22:30–22:41 CST
- **Scope:** GATE 1 only. GATE 2–7 were not implemented. Nothing was posted, submitted, or merged.
- **Cost:** **$0.** No TinyFish, paid browser agents, paid SEO APIs, paid link services, paid ads, or newly purchased SaaS. Evidence is free HTTP fetches, the public GitHub API, and files already in this repository.
- **Repository audited:** `main` at `db858dd` (Merge pull request #2). Open pull request [#4](https://github.com/ddcodedog/Calculator/pull/4) is recorded as **PENDING_MERGE** and was not merged for these counts.

## Executive summary

| Site | Robots | Sitemap | Homepage | Inventory tools | Sample live (HTTP 200 / probed) | GitHub topics on main | Pending PR #4 topics | Off-site published URL | Channel gaps |
|---|---|---|---|---:|---|---:|---:|---|---|
| NetEngineerLab | 200, `Allow: /` | 200, 230 URLs | 200, `index,follow` | 46 | 4 / 4 | 6 | 10 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |
| PCDog | 200, `*` allow; training bots blocked | 200, 144 URLs | 200, no robots meta | 27 | 4 / 4 | 0 | 0 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |
| AIMarkTool | 200, allow except `/workspace` `/api` | 200, 144 URLs | 200, no robots meta | 32 | 4 / 4 | 0 | 0 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |
| PowerEngineerLab | 200, allow except `/projects/` `/api/` | 200, 178 URLs | 200, `index, follow` | 52 | 4 / 4 | 9 | 10 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |
| HVACEngineerLab | 200, `Allow: /` | 200, 36 URLs | 200, `index, follow` | 13 | 4 / 4 | 1 | 10 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |
| PrivacyFileLab | 200, comments only | **404** | 200, no `<title>`, no robots meta | 12 | 4 / 4 | 0 | 0 | NOT_FOUND | No sitemap; analytics NOT_CONNECTED |
| DataFileLab | 200, allow except `/html-render-check` | 200, 46 URLs | 200, no robots meta | 43 | 3 / 4 | 0 | 0 | NOT_FOUND | Inventory drift; GSC NOT_CONNECTED |
| WaterEngineerLab | 200, allow with path blocks | 200, 29 URLs | 200, `index, follow` | 18 | 4 / 4 | 3 | 9 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |
| StructuralEngineerLab | 200, `Allow: /` | 200, 28 URLs | 200, no robots meta | 25 | 3 / 4 | 3 | 4 | NOT_FOUND | Sitemap covers 10/25 inventory URLs |
| DevEngineerLab | 200, comments only | 200, **empty** (0 URLs) | 200, **`noindex, nofollow`** | 67 | 4 / 4 (pages send noindex) | 0 | 0 | NOT_FOUND | Not index-ready |
| DIYCalcLab | 200, allow except account/checkout | 200 index → 85 URLs | 200, no robots meta | 40 | 4 / 4 | 3 | 10 | NOT_FOUND | GSC/Bing/GA4 NOT_CONNECTED |

### Counts

| Check | Result |
|---|---|
| Sites with `robots.txt` HTTP 200 | **11 / 11** |
| Sites whose robots.txt has `User-agent` rules | **9 / 11** (PrivacyFileLab and DevEngineerLab are comment-only) |
| Sites with `sitemap.xml` HTTP 200 | **10 / 11** (PrivacyFileLab **404**) |
| Sites with a populated sitemap (at least one `<loc>`, including DIY child sitemaps) | **9 / 11** (DevEngineerLab is an empty `<urlset>`; PrivacyFileLab has no sitemap) |
| Homepages HTTP 200 | **11 / 11** |
| Homepage explicitly `noindex` | **1 / 11** (DevEngineerLab) |
| GATE1 inventory tools | **375** |
| Spot-checked tool URLs | **44** (4 per site): **42 HTTP 200**, **2 HTTP 404** |
| GitHub formula topics on `main` (site `*.md` excluding each `README.md`) | **25** |
| Topics added by open PR #4, not on `main` | **53** (**PENDING_MERGE**) |
| Topics that would exist on the PR #4 branch | **78** |
| Verified published off-site article URLs | **0** (NOT_FOUND / UNKNOWN; see data-quality note) |

Machine-readable copy of the summary: [ZERO_COST_BASELINE.json](ZERO_COST_BASELINE.json).

## Method

1. Read `reports/GATE1_TOOL_INVENTORY.json` (generated 2026-11-04T08:00:23.882Z, 375 tools) and counted formula `*.md` files on local `main`, which matches `origin/main`.
2. Read open PR #4 via the GitHub API (`state=OPEN`, `mergeable=MERGEABLE`, head `cursor/formula-topics-batch2-ff46`). Added topic files were counted from the PR file list. They are **not** treated as published on `main`.
3. Fetched each production origin with a descriptive User-Agent (`CalculatorGate1Baseline/1.0`). For every site: `/`, `/robots.txt`, `/sitemap.xml`, `/sitemap_index.xml`, `/blog`, `/blog/`, `/articles`, `/posts`, `/news`, and four inventory URLs spread across that site’s list (first, one-third, two-thirds, last).
4. Where `sitemap.xml` was a sitemap index, fetched the child sitemaps. Compared inventory URLs to sitemap `<loc>` values after lowercasing the host and stripping a trailing slash. That comparison is a string match, not a crawl of all 375 tools.
5. Parsed HTML for `<title>`, `meta name=robots`, headings, and same-host links. A “content marker” is a case-insensitive word hit in visible text (`formula`, `how it works`, `worked example`, and similar). It is not a quality score.
6. Off-site checks used only free public URLs. No account was logged in. No post was created.

Search Console clicks, impressions, coverage, Bing Webmaster totals, and GA4 sessions were **not measured**.

## Per-site checks

Shared channel matrix (same for every site; no site-specific public profile was found):

| Channel | Status | Evidence |
|---|---|---|
| GitHub | **AUTHORIZED** | In-repo `reports/GATE0_STATUS.md` records `gh` auth as **ddcodedog**. Public profile https://github.com/ddcodedog (display name NetEngineerLab) owns this Calculator repo and `fiber-loss-calculator`. This audit runner’s token got HTTP 403 on `GET /user`, so this environment cannot act as that user. |
| Blogger | **NOT_CONNECTED** | Task context names blog id `90830016666247746`. `GET https://www.googleapis.com/blogger/v3/blogs/90830016666247746` returned **HTTP 403** (“unregistered callers”). No API key is in this repo. Drafts under `promo/zh/` are not posts. |
| DEV.to | **NOT_FOUND** | `https://dev.to/ddcodedog` and `https://dev.to/netengineerlab` **HTTP 404**. Public article API for both usernames returned `[]`. |
| LinkedIn | **UNKNOWN** | `https://www.linkedin.com/search/results/all/?keywords=netengineerlab` **HTTP 403** (Cloudflare challenge). No profile URL verified. |
| Reddit | **UNKNOWN** | `https://www.reddit.com/search.json?q=netengineerlab` **HTTP 403**. |
| Quora | **UNKNOWN** | `https://quora.com/search?q=netengineerlab` **HTTP 403** (“Just a moment…”). |
| Substack | **NOT_FOUND** | `https://substack.com/search/netengineerlab` **HTTP 200**, `noindex`. The query string is echoed. No publication URL for these sites was present. |
| X | **NOT_FOUND** | `https://x.com/ddcodedog` **HTTP 404**, title “User Profile Not Found”. Other handles were not guessed. |

Google Search Console, Bing Webmaster, and GA4 are **NOT_CONNECTED** for all 11 sites. Nothing in this repo stores a property ID, measurement ID, or export.

### NetEngineerLab — https://netengineerlab.com

1. **Robots and sitemap.** `https://netengineerlab.com/robots.txt` **HTTP 200**. `User-agent: *`, `Allow: /`, `Disallow: /design/` and three legacy optical-power-budget HTML paths. `Sitemap: https://netengineerlab.com/sitemap.xml`. That sitemap **HTTP 200**, urlset, **230** `<loc>` (tools, `/topics/`, `/guides/`, `/zh/`, `/es/`). `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics (not Search Console).** Homepage **HTTP 200**. Title: “NetEngineerLab | Telecom and Network Engineering Tools”. `meta robots`: `index,follow,max-image-preview:large,max-snippet:-1`. Canonical `https://netengineerlab.com/`. Googlebot and Bingbot are not named, so they fall under `User-agent: *` allow. Indexed-page counts: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **46**. All **46** inventory URLs appear in the sitemap (string match). Sample, all **HTTP 200**:
   - https://netengineerlab.com/tools/fiber-loss/
   - https://netengineerlab.com/tools/poe-voltage-drop-calculator/
   - https://netengineerlab.com/tools/data-center-airflow-containment-planner/
   - https://netengineerlab.com/tools/all-reduce-traffic-estimator/
4. **On-site topical content.** Sampled tool pages have sections beyond the widget: “Methodology and engineering notes”, “Standards citations”, “Engineering notes”, FAQ. `https://netengineerlab.com/guides/` **HTTP 200**, title “Network Engineering Guides: Formulas & Worked Examples”, `meta robots` `index,follow`.
5. **Keywords / internal linking.** Homepage H1 “Network & Telecom Engineering Calculators” plus a quick-tool list. Tool pages link `/tools/`, `/guides/`, `/topics/`, language variants, and related calculators (for example fiber-loss → PON splitter, ONU RX, optical power budget). This is an observation, not a completed keyword program.
6. **GitHub topics on `main`:** **6** (`fiber-link-loss.md`, `optical-power-budget.md`, `fiber-propagation-latency.md`, `chromatic-dispersion.md`, `ospf-interface-cost.md`, `stp-path-cost.md`). **PR #4 PENDING_MERGE:** **10** more (16 on that branch).
7. **Off-site articles.** `/blog`, `/articles`, `/posts`, `/news` **HTTP 404**. No verified DEV.to, Blogger, LinkedIn, Reddit, Quora, Substack, or X URL. **NOT_FOUND.**
8. **Channels.** See the shared matrix. **NOT_CONNECTED** for GSC/Bing/GA4.

### PCDog — https://pcdog.com

1. **Robots and sitemap.** `https://pcdog.com/robots.txt` **HTTP 200**. Cloudflare-style content-signal comment, then `User-agent: *` / `Content-Signal: search=yes,ai-train=no,use=reference` / `Allow: /`. Many training and other bots are `Disallow: /` (including `Google-Extended`, `GPTBot`, `Baiduspider`, `GoogleOther`). Classic `Googlebot` and `Bingbot` are not given their own block. `Sitemap: https://pcdog.com/sitemap.xml` **HTTP 200**, **144** URLs. `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “PCDog — PC Diagnostics & Troubleshooting Platform”. No `meta robots` on the homepage (HTML default is indexable). Tool samples send `index, follow`. Canonical homepage `https://pcdog.com`. Search Console / Bing totals: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **27**. Sitemap overlap **26 / 27**. Missing from the sitemap and **HTTP 404** when fetched: https://pcdog.com/tools/network-health. Sample, all **HTTP 200**:
   - https://pcdog.com/tools/backlight-bleed-test
   - https://pcdog.com/tools/screen-information
   - https://pcdog.com/tools/latency-under-load
   - https://pcdog.com/tools/websocket-test
4. **On-site topical content.** Tool pages use “Quick answer”, “How it works”, “Limitations”, and FAQ rather than an engineering formula block. Guide example `https://pcdog.com/guides/backlight-bleed-vs-ips-glow` **HTTP 200**, title “Is Backlight Bleed Normal? How to Tell”, `index, follow`.
5. **Keywords / internal linking.** Homepage links Network Doctor and Display Doctor. Tool pages link `/network`, `/display`, `/tools`, diagnose paths, and related tests or guides.
6. **GitHub topics on `main`:** **0**. **PR #4:** no PCDog files. **PENDING_MERGE count: 0.**
7. **Off-site.** Blog paths **HTTP 404**. No verified external article. **NOT_FOUND.**
8. **Channels.** Shared matrix. Analytics **NOT_CONNECTED**.

### AIMarkTool — https://aimarktool.com

1. **Robots and sitemap.** `https://aimarktool.com/robots.txt` **HTTP 200**. `User-Agent: *`, `Allow: /`, `Disallow: /workspace`, `Disallow: /api`, `Sitemap: https://aimarktool.com/sitemap.xml`. Sitemap **HTTP 200**, **144** URLs (home, `/tools`, `/industries`, `/workflows`, `/templates`, `/guides`, tool URLs). `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “AI MarkTool — AI Marketing Toolbox”. No homepage robots meta. Sampled tools send `index, follow`. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **32**. Sitemap overlap **32 / 32**. Sample, all **HTTP 200**:
   - https://aimarktool.com/tools/roas-calculator
   - https://aimarktool.com/tools/marketing-plan-generator
   - https://aimarktool.com/tools/content-strategy-generator
   - https://aimarktool.com/tools/trend-research-planner
4. **On-site topical content.** ROAS page headings include “How to use it” and “FAQ”, and the visible text contains “formula”. These are short marketing explainers, not lab derivations. `https://aimarktool.com/guides` **HTTP 200**, title “Marketing Guides & Examples”, `index, follow`.
5. **Keywords / internal linking.** Homepage groups work types (marketing plan, product launch, leads). Tool pages link a shared tool/guide chrome (about 16 internal paths on the ROAS sample).
6. **GitHub topics on `main`:** **0**. **PR #4:** 0. Five sites including this one have no formula page because batch 1 did not force formulas onto non-math tools.
7. **Off-site.** Blog paths **HTTP 404**. **NOT_FOUND.**
8. **Channels.** Shared matrix. **NOT_CONNECTED** for GSC/Bing/GA4.

### PowerEngineerLab — https://powerengineerlab.com

1. **Robots and sitemap.** `https://powerengineerlab.com/robots.txt` **HTTP 200**. `Allow: /`, `Disallow: /projects/`, `Disallow: /api/`, sitemap declared. Sitemap **HTTP 200**, **178** URLs (English and `zh-CN`). `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “Electrical Engineering Calculators & Energy Tools | PowerEngineerLab”. `meta robots`: `index, follow`. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **52**. Sitemap overlap **52 / 52**. Sample, all **HTTP 200**:
   - https://powerengineerlab.com/calculators/ac-power/
   - https://powerengineerlab.com/calculators/ev-charging/
   - https://powerengineerlab.com/calculators/power-triangle/
   - https://powerengineerlab.com/calculators/voltage-drop-cable-sizing/
4. **On-site topical content.** Each sample has “Method and boundaries” and FAQ, plus “Related topic and guides”. That is explanation beyond the calculator widget. Sampled tool pages did not set their own robots meta.
5. **Keywords / internal linking.** Nav includes `/categories/`, `/guides/`, `/cases/`, `/calculators/`, and `zh-CN` mirrors. AC power links the three-phase category and a balanced three-phase guide. Voltage-drop links cable ampacity and wiring guides.
6. **GitHub topics on `main`:** **9**. **PR #4 PENDING_MERGE:** **10** (19 on that branch).
7. **Off-site.** Blog paths **HTTP 404**. `promo/zh/PowerEngineerLab/` is a draft. **NOT_FOUND** as a published URL.
8. **Channels.** Shared matrix.

### HVACEngineerLab — https://hvacengineerlab.com

1. **Robots and sitemap.** `https://hvacengineerlab.com/robots.txt` **HTTP 200**. `User-agent: *`, `Allow: /`, `Sitemap: https://hvacengineerlab.com/sitemap.xml`. Sitemap **HTTP 200**, **36** URLs (English and `zh-CN` tools plus a few static pages). `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “HVAC Engineering Calculators & Tools | HVAC Engineer Lab”. `meta robots`: `index, follow`. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **13**. Sitemap overlap **13 / 13**. Sample, all **HTTP 200** and `index, follow`:
   - https://hvacengineerlab.com/tools/building-energy-benchmark/
   - https://hvacengineerlab.com/tools/data-center-cooling-planner/
   - https://hvacengineerlab.com/tools/outdoor-air-ventilation-planner/
   - https://hvacengineerlab.com/tools/thermal-comfort-pmv-planner/
4. **On-site topical content.** Samples include “Method & limitations” and “Formulas, source and scope”. PMV page states it does not certify ASHRAE 55. Homepage H1: “HVAC load calculations, clearly explained.”
5. **Keywords / internal linking.** Tool pages link `/tools`, `/about`, the Chinese mirror, and a short set of sibling planners. Fewer internal links than Net or DIY (about 8 paths on the homepage sample).
6. **GitHub topics on `main`:** **1** (`duct-friction-pressure-drop.md`). **PR #4 PENDING_MERGE:** **10** (11 on that branch).
7. **Off-site.** Blog paths **HTTP 404**. Chinese draft only. **NOT_FOUND.**
8. **Channels.** Shared matrix.

### PrivacyFileLab — https://privacyfilelab.com

1. **Robots and sitemap.** `https://privacyfilelab.com/robots.txt` **HTTP 200**, 1248 bytes, **comments only**. No `User-agent`, no `Allow`/`Disallow`, no `Sitemap`, no `Content-Signal` directive. Default robots behavior is allow. `https://privacyfilelab.com/sitemap.xml` **HTTP 404** (HTML app shell). `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. The fetched HTML has **no `<title>`** and **no `meta robots`**. Visible H1: “Know what your files reveal.” Canonical not found. Whether Google or Bing index it: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **12**. Sitemap overlap **0** because no sitemap exists. Sample, all **HTTP 200**:
   - https://privacyfilelab.com/scan/
   - https://privacyfilelab.com/photo/
   - https://privacyfilelab.com/clean-file-verifier/
   - https://privacyfilelab.com/ocr/
4. **On-site topical content.** Parsed headings are the product names (“Check a file before you share it.”, “See what your photo says before you share it.”). No formula, worked-example, or method section in the sampled HTML. These are local file scanners, which matches the inventory note not to invent formulas.
5. **Keywords / internal linking.** Header links: `/`, `/photo`, `/pdf`, `/ai-upload`, `/zh-CN/`. No related-article cluster was visible in the sample.
6. **GitHub topics on `main`:** **0**. **PR #4:** 0.
7. **Off-site.** Blog paths **HTTP 404**. **NOT_FOUND.**
8. **Channels.** Shared matrix. Missing sitemap is an on-site gap, separate from analytics **NOT_CONNECTED**.

### DataFileLab — https://datafilelab.com

1. **Robots and sitemap.** `https://datafilelab.com/robots.txt` **HTTP 200**. `Allow: /`, `Disallow: /html-render-check`, sitemap declared. Sitemap **HTTP 200**, **46** URLs. `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “DataFileLab — Private browser tools for CSV and Excel”. No robots meta. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **43**. Sitemap overlap **22 / 43**. Sample:
   - https://datafilelab.com/compare **HTTP 200**
   - https://datafilelab.com/csv-sorter **HTTP 200**
   - https://datafilelab.com/csv-column-splitter **HTTP 200**
   - https://datafilelab.com/parquet-to-csv-converter **HTTP 404**
   Extra check: https://datafilelab.com/csv-deduplicator **HTTP 404** (also absent from the sitemap). Live sample **3 / 4**. Inventory rows past the sitemap should not be described as live without another fetch.
4. **On-site topical content.** Sample headings are the tool title and input labels (“See exactly what changed.”, “Sort CSV rows by a column.”). No method / worked-example section. A visible-text scan hit the word “formula” on the column splitter; the headings do not show a formula article.
5. **Keywords / internal linking.** Pages link `/`, `/tools`, `/compare`, `/clean`, `/privacy`. Thin related-link set compared with the engineering labs.
6. **GitHub topics on `main`:** **0**. **PR #4:** 0.
7. **Off-site.** Blog paths **HTTP 404**. **NOT_FOUND.**
8. **Channels.** Shared matrix.

### WaterEngineerLab — https://waterengineerlab.com

1. **Robots and sitemap.** `https://waterengineerlab.com/robots.txt` **HTTP 200**. `Allow: /`. `Disallow: /api/`, `/zh-CN`, `/es`, `/tools/detention-storage-preliminary-sizing`, `/tools/culvert-capacity-preliminary-check`. Sitemap **HTTP 200**, **29** URLs, including `/learn/` articles. `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “WaterEngineerLab — Hydraulic and stormwater calculation tools”. `meta robots`: `index, follow`. The two disallowed tool paths are also **HTTP 404**, so the block matches removed URLs. Chinese and Spanish trees are disallowed even if linked elsewhere. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **18**. Sitemap overlap **16 / 18** (the two disallowed URLs). Sample, all **HTTP 200**, `index, follow`:
   - https://waterengineerlab.com/tools/stormwater-drainage-design-planner/
   - https://waterengineerlab.com/tools/manning-open-channel-flow/
   - https://waterengineerlab.com/tools/pump-duty-point-helper/
   - https://waterengineerlab.com/tools/idf-curve-interpolator/
4. **On-site topical content.** Strongest explanatory pages in the sample. Manning page headings include the formula name, geometries, worked examples, limitations, and source. Learn article `https://waterengineerlab.com/learn/how-to-calculate-rational-method-peak-runoff` **HTTP 200**, title “How to Calculate Rational Peak Runoff | WaterEngineerLab”, `index, follow`, formula language in the body.
5. **Keywords / internal linking.** Homepage hubs: stormwater, open channel, pipe pressure, distribution. Tool pages link `/hubs`, sibling tools, and `/learn/` articles.
6. **GitHub topics on `main`:** **3**. **PR #4 PENDING_MERGE:** **9** (12 on that branch; PR body says one short of a 10-topic target).
7. **Off-site.** Blog paths **HTTP 404**. Chinese draft only. **NOT_FOUND.**
8. **Channels.** Shared matrix.

### StructuralEngineerLab — https://structuralengineerlab.com

1. **Robots and sitemap.** `https://structuralengineerlab.com/robots.txt` **HTTP 200**. `User-Agent: *`, `Allow: /`, sitemap declared. Sitemap **HTTP 200**, **28** URLs. `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “StructuralEngineerLab — Structural Engineering Calculators”. No homepage robots meta. One sampled tool, the review register, sends `noindex, nofollow` and is labeled “Planned”. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **25**. Sitemap overlap **10 / 25**. Sample:
   - https://structuralengineerlab.com/tools/beam-analysis-calculator/ **HTTP 200**
   - https://structuralengineerlab.com/tools/section-modulus-calculator/ **HTTP 200**
   - https://structuralengineerlab.com/tools/beam-reciprocity-checker/ **HTTP 404**
   - https://structuralengineerlab.com/tools/beam-review-register/ **HTTP 200**, `noindex, nofollow`
   Live useful sample: **3 / 4** HTTP 200, of which one is noindex. Other inventory URLs absent from the sitemap were not all fetched.
4. **On-site topical content.** Beam analysis and section modulus pages include formula, explanation, worked example, assumptions, and limitations in visible text, plus headings “Engineering interpretation”, “Example”, “Method & assumptions”. Guide `https://structuralengineerlab.com/guides/how-to-calculate-beam-reactions-shear-moment-deflection/` **HTTP 200**, title “Beam Reactions, Shear, and Moment | StructuralEngineerLab”.
5. **Keywords / internal linking.** Homepage lists beam, section properties, bending stress, Euler buckling. Section-modulus page links section properties, moment of inertia, and bending stress. Beam analysis links `/beam-engineering/` and a guide.
6. **GitHub topics on `main`:** **3**. **PR #4 PENDING_MERGE:** **4** (7 on that branch; PR body says six short of a 10-topic target).
7. **Off-site.** Blog paths **HTTP 404**. Chinese draft only. **NOT_FOUND.**
8. **Channels.** Shared matrix.

### DevEngineerLab — https://devengineerlab.com

1. **Robots and sitemap.** `https://devengineerlab.com/robots.txt` **HTTP 200**, 1248 bytes, **the same comment-only content-signal essay** as PrivacyFileLab. No `User-agent` and no `Sitemap`. `https://devengineerlab.com/sitemap.xml` **HTTP 200** but the body is an empty urlset (`<urlset …> </urlset>`, **0** URLs). `/sitemap_index.xml` **HTTP 404**.
2. **Indexing basics.** Homepage **HTTP 200**. Title: “DevEngineerLab”. `meta robots`: **`noindex, nofollow`**. No canonical. Tool samples repeat `noindex, nofollow` (URL pattern tester: `noindex`). Robots.txt does not block Googlebot, and the HTML asks crawlers not to index. Search Console coverage: **NOT_CONNECTED**, and promotion that assumes indexed pages is not supported by this fetch.
3. **Live calculators.** Inventory **67**. Sitemap overlap **0 / 67**. Sample HTTP status **4 / 4 = 200**, with the noindex caveat:
   - https://devengineerlab.com/tools/json-formatter/ **200**, title “JSON Formatter | DevEngineerLab”
   - https://devengineerlab.com/tools/url-encode-decode/ **200**
   - https://devengineerlab.com/tools/text-case-converter/ **200**
   - https://devengineerlab.com/tools/url-pattern-tester/ **200**, title only “DevEngineerLab”, H1 “Preparing your workspace” (shell, not a finished tool page)
4. **On-site topical content.** Finished samples have “How it works” and “Understand the result before using it.” They are utility notes, not formula articles. The URL-pattern sample does not.
5. **Keywords / internal linking.** Category links (`/categories/json-data`, developer utilities, API tools) and sibling tools (Base64, UUID, timestamp) are present on the finished samples.
6. **GitHub topics on `main`:** **0**. **PR #4:** 0.
7. **Off-site.** Blog paths **HTTP 404**. **NOT_FOUND.**
8. **Channels.** Shared matrix. Indexing gap is on-site (`noindex` + empty sitemap).

### DIYCalcLab — https://diycalclab.com

1. **Robots and sitemap.** `https://diycalclab.com/robots.txt` **HTTP 200**. `User-agent: *` disallows `/api/`, `/account/`, `/projects/`, `/checkout/` and allows `/`. Named search-and-training bots are also allowed on content and blocked on those private paths. `Sitemap: https://diycalclab.com/sitemap.xml` **HTTP 200**, sitemap **index** pointing at:
   - `sitemap-calculators.xml` **HTTP 200**, **40** URLs
   - `sitemap-guides.xml` **HTTP 200**, **12** URLs
   - `sitemap-hubs.xml` **HTTP 200**, **17** URLs
   - `sitemap-pages.xml` **HTTP 200**, **16** URLs
   Combined **85** URLs. `/sitemap_index.xml` **HTTP 404** (the live index is `/sitemap.xml`, not that filename).
2. **Indexing basics.** Homepage **HTTP 200**. Title: “DIYCalcLab – Free DIY & Home Improvement Calculators”. No robots meta. Canonical `https://diycalclab.com/`. Console metrics: **NOT_CONNECTED**.
3. **Live calculators.** Inventory **40**. All **40** match `sitemap-calculators.xml`. Sample, all **HTTP 200**:
   - https://diycalclab.com/concrete/slab-calculator/
   - https://diycalclab.com/landscaping/paver-calculator/
   - https://diycalclab.com/roofing/roof-pitch-calculator/
   - https://diycalclab.com/paint/epoxy-floor-calculator/
4. **On-site topical content.** Each sample has “Method & assumptions”, “How to use this calculator”, “Worked examples”, and a reference table. Guide index `https://diycalclab.com/guides/` **HTTP 200**. Example `https://diycalclab.com/guides/how-much-concrete-do-i-need/` **HTTP 200**, title “How Much Concrete Do I Need? Yards, m³ & Bags Explained”.
5. **Keywords / internal linking.** Homepage: project categories and “Most popular calculators”. Tool pages repeat the category nav (concrete, paint, tile, flooring, roofing, landscaping, and others). About 30+ internal paths on a tool page.
6. **GitHub topics on `main`:** **3**. **PR #4 PENDING_MERGE:** **10** (13 on that branch).
7. **Off-site.** `/blog` and the other blog paths **HTTP 404**. On-site `/guides/` is not an external article. Chinese draft only. **NOT_FOUND.**
8. **Channels.** Shared matrix.

## Cross-cutting repo assets

### Formula topics on `main` versus PR #4

| Folder | Topics on `main` | Added in PR #4 (PENDING_MERGE) | Total on PR branch |
|---|---:|---:|---:|
| NetEngineerLab | 6 | 10 | 16 |
| PCDog | 0 | 0 | 0 |
| AIMarkTool | 0 | 0 | 0 |
| PowerEngineerLab | 9 | 10 | 19 |
| HVACEngineerLab | 1 | 10 | 11 |
| PrivacyFileLab | 0 | 0 | 0 |
| DataFileLab | 0 | 0 | 0 |
| WaterEngineerLab | 3 | 9 | 12 |
| StructuralEngineerLab | 3 | 4 | 7 |
| DevEngineerLab | 0 | 0 | 0 |
| DIYCalcLab | 3 | 10 | 13 |
| **Total** | **25** | **53** | **78** |

[PR #4](https://github.com/ddcodedog/Calculator/pull/4) — “Add 53 formula topics for six engineering sites”. State **OPEN**, mergeable **MERGEABLE**, base `main`, head `cursor/formula-topics-batch2-ff46`, commit `a6a87ff`. Workflow “Markdown and tool URL checks” concluded **SUCCESS** on that branch (runs `41846927790` and `41846860764`). This baseline does not merge it. Root `README.md` on `main` still says “Published formula topics: 25”.

`scripts/check-docs.py` counts the same non-README site markdown files and skips `promo/`. It was not re-executed against the network for this baseline; the 25 count is from the `main` tree.

### `promo/zh/`

Chinese outreach **drafts**, not published posts. `promo/zh/README.md` says they were not posted to Blogger. Files:

- `promo/zh/README.md`
- `promo/zh/overview-formula-library.md`
- `promo/zh/NetEngineerLab/optical-link-budget-latency-dispersion.md`
- `promo/zh/PowerEngineerLab/ohms-law-ac-power-transformer-ratio.md`
- `promo/zh/HVACEngineerLab/pmv-ppd-cooling-heating-load.md`
- `promo/zh/StructuralEngineerLab/beam-deflection-moment-stress.md`
- `promo/zh/WaterEngineerLab/flow-pipe-diameter-headloss.md`
- `promo/zh/DIYCalcLab/paint-and-concrete-quantity.md`

No drafts for PCDog, AIMarkTool, PrivacyFileLab, DataFileLab, or DevEngineerLab.

### Other reports

- `reports/GATE1_TOOL_INVENTORY.md` and `.json` — 375 source-registered tools. `VerificationStatus` is `SOURCE_REGISTERED`, not an independent formula proof.
- `reports/GATE0_STATUS.md` — repo creation and `gh` auth as ddcodedog.
- `reports/FIRST_RELEASE.md` and `reports/FORMULA_VERIFICATION.md` — the 25 topics on `main`.
- `scripts/check-docs.py` — doc checker. Not a promotion tool.

### On-site guides versus off-site articles

Several sites already publish guides on their own domains (Net `/guides/`, PCDog `/guides/`, AI MarkTool `/guides`, Water `/learn/`, Structural `/guides/`, DIY `/guides/` with 12 guide URLs in the sitemap). Those are on-site. They are not counted as off-site publications. Blog-shaped paths (`/blog`, `/articles`, `/posts`, `/news`) returned **HTTP 404** on all 11 origins.

## Gaps and recommended next actions for GATE 2

GATE 2 is not started here. Suggested order, still at $0, using only access the operator already has:

1. **Do not promote DevEngineerLab for search** until someone intentionally changes `noindex, nofollow` and replaces the empty sitemap. Fetch evidence today says crawlers are asked to skip it. The URL-pattern page is still a “Preparing your workspace” shell.
2. **PrivacyFileLab:** add a real `<title>` (and description) and a sitemap that lists the live scanners. Robots.txt is comment-only, which allows crawlers but does not advertise URLs.
3. **Reconcile inventory with production before writing more pages.** Confirmed **HTTP 404**: DataFileLab `parquet-to-csv-converter` and `csv-deduplicator`; Structural `beam-reciprocity-checker`; Water detention-storage and culvert-capacity (also disallowed in robots); PCDog `network-health`. Structural sitemap contains 10 of 25 inventory URLs. DataFileLab sitemap contains 22 of 43.
4. **Keep PR #4 as pending** until it is reviewed and merged. Citing 78 topics as live on `main` would be wrong. After merge, the public GitHub topics become the citable set. Water would still be 12 and Structural 7, short of 10, for the reasons already written in that PR.
5. **Connect measurement before any traffic claim.** Create or confirm Google Search Console, Bing Webmaster, and GA4 on the properties the operator owns, then export. Until then every traffic number stays **NOT_CONNECTED**.
6. **Blogger:** the blog id is known and the API is not callable from here. GATE 2 should confirm the operator can open the blog, list existing posts, and only then decide whether `promo/zh/` drafts are ready. Drafts stay drafts.
7. **Other free channels** (DEV.to, LinkedIn, Reddit, Quora, Substack, X) have no verified profile for these sites. Creating accounts and posting is outside GATE 1. Do not treat a failed search as proof that no post exists under another name.
8. **Use on-site guides that already return HTTP 200** as the first content inventory in GATE 2 (DIY 12 guide URLs, Net guides index, Water learn articles). That does not require a new domain or a paid tool.

## Data-quality note — what was not measured

| Item | Status | Reason |
|---|---|---|
| Google Search Console clicks, impressions, queries, coverage, indexed-page counts | **NOT_CONNECTED** | No property access and no export in this repo |
| Bing Webmaster Tools impressions, clicks, indexed counts | **NOT_CONNECTED** | Same |
| GA4 sessions, users, conversions | **NOT_CONNECTED** | No measurement ID and no export |
| Rankings or “keyword difficulty” | **NOT MEASURED** | Would need a paid SEO API or a logged-in console; not used |
| Full crawl of all 375 inventory URLs | **NOT DONE** | Four URLs per site were fetched, plus a few 404 confirmations. Sitemap overlap is a string match |
| DuckDuckGo HTML results for `site:dev.to` and `"netengineerlab.com" blog` | **UNAVAILABLE** | `https://html.duckduckgo.com/html/` returned **HTTP 202** challenge HTML, not a result list |
| Reddit and LinkedIn search | **UNKNOWN** | HTTP 403 bot walls |
| Quora search | **UNKNOWN** | HTTP 403 interstitial |
| Blogger post list for blog id `90830016666247746` | **UNAVAILABLE** | Blogger API HTTP 403 without an API key or OAuth |
| Whether some other public URL already mentions these domains | **UNKNOWN** | Not proven either way. Only URLs this audit opened are claimed |

No number in this file is a Search Console or analytics metric. HTTP statuses are from the fetches above on 2026-11-04 (Asia/Shanghai).
