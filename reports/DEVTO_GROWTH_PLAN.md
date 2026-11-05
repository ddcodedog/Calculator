# DEV.to SEO Growth V1.0 — GATE 0

- Audit date: 2026-11-05 (Asia/Shanghai and UTC are the same calendar day for every timestamp below)
- Repository: https://github.com/ddcodedog/Calculator
- Scope: planning only. No DEV.to draft, no publish, no series created in the editor, no API key, no change to the eleven product sites.
- Companion file: [DEVTO_CONTENT_MATRIX.csv](DEVTO_CONTENT_MATRIX.csv)
- Not in this gate: `reports/DEVTO_DRAFT_ACCEPTANCE.md` (GATE 4, after drafts exist)

## Result

**GATE 0 plan written.** The public account has three published posts. None of those titles is a Wave-1 fiber article. Wave-1 titles are locked to three live NetEngineerLab calculators. The CSV schedules 30 calendar days from 2026-11-05 and appends the three live posts as `EXISTING_PUBLISHED` so they are not planned again.

## How this was checked

Public HTTP only. No DEV.to API key was used or stored.

| Check | Request | Result |
|---|---|---|
| User | `GET https://dev.to/api/users/by_username?url=netengineerlabcom` | HTTP 200 |
| Article list | `GET https://dev.to/api/articles?username=netengineerlabcom&per_page=30` | HTTP 200, 3 articles |
| Page 2 | same query, `page=2` | HTTP 200, empty list |
| Bodies | `GET https://dev.to/api/articles/{id}` for 4933430, 4909590, 4839123 | HTTP 200, `body_markdown` present |
| Profile | `GET https://dev.to/netengineerlabcom` | HTTP 200 |
| Tool URLs | `curl -L` on each matrix URL, 2026-11-05 | recorded per row; failures called `UNAVAILABLE` |

The user endpoint is the Forem V0 API (response `warning` header says so). It does not include a badges array. Badge text below is from the public profile HTML, not from that JSON.

Tag names used in the matrix were probed with `GET https://dev.to/api/articles?tag={name}&per_page=1`. Each proposed tag returned one article, so the tag exists. `GET /api/tags/{name}` returned HTML 404 and was not used.

## Account inventory

| Field | Value |
|---|---|
| Profile | https://dev.to/netengineerlabcom |
| User id | 4179691 |
| Username | `netengineerlabcom` |
| Display name | NetEngineerLab |
| Summary | Network engineer focused on enterprise networking, switching, routing, capacity planning, and troubleshooting. Building practical engineering tools at NetEngineerLab. |
| Website | https://netengineerlab.com |
| GitHub | `ddcodedog` |
| Twitter / X | `NetEngineerLab` |
| Location | empty in the API |
| Joined | Oct 12, 2026 (`joined_at`) |
| Profile stat | HTML text `3 posts published` next to the Post icon. This matches the article-list count of 3. |
| Badge | Profile badge title `Writing Debut` (badge id 280 in the page). The API user object has no badge field. |
| Series | `collection_id` is null on all three articles. No series is attached. |
| Organization | none in the fetched article objects |

## The three published posts

None of these titles matches a Wave-1 fiber title. All three use the DEV.to URL as `canonical_url` (they do not canonicalize to netengineerlab.com). Public reactions and comments are 0 on every post. Reading times are the API `reading_time_minutes` values.

### 1. id 4839123 — published first

- Title: How Many Uplinks Does a 4-Switch Stack Need? A Practical Network Design Guide
- URL: https://dev.to/netengineerlabcom/how-many-uplinks-does-a-4-switch-stack-need-a-practical-network-design-guide-1apd
- Slug matches the title (`…-1apd`)
- Published: 2026-10-12T15:42:34Z (2026-10-12 23:42 Asia/Shanghai)
- Tags: `networking`, `tutorial`, `architecture`, `beginners` (four tags, also the API `tags` field)
- Reactions / comments: 0 / 0
- Reading time: 4 minutes. Body about 930 words.
- Headings: design question, two redundant uplinks, oversubscription ratio, traffic demand, N-1, stack bandwidth, why more uplinks are not always better, checklist, calculator, recommendation.
- Tool links in the body:
  - https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/ — HTTP 200 on 2026-11-05
  - https://netengineerlab.com — HTTP 200, byline only
- Promo CTA: section “Use a Calculator to Validate the Design” links that uplink calculator and says the result does not replace traffic measurements. This is the clearest of the three CTAs.
- Keywords: the title is a practical question. Tags match the topic. No hashtag line at the end. No keyword stuffing.
- GitHub formula on `main`: **UNAVAILABLE**. Switch-uplink oversubscription has no file under `NetEngineerLab/`.

### 2. id 4909590 — slug does not match the title

- Title: Why Is One LACP Link at 100% While the Other Is Almost Idle?
- URL path and slug: `how-many-uplinks-does-a-4-switch-stack-need-a-practical-network-design-guide-2d8l`
- Full URL: https://dev.to/netengineerlabcom/how-many-uplinks-does-a-4-switch-stack-need-a-practical-network-design-guide-2d8l
- `canonical_url` is that same DEV.to URL, so the canonical slug is the uplink guide, not the LACP title.
- The stem is the same as article 4839123. Only the suffix differs (`2d8l` vs `1apd`).
- Published: 2026-10-24T08:57:40Z (2026-10-24 16:57 Asia/Shanghai)
- Tags: `networking`, `tutorial`, `architecture`, `troubleshooting`
- Reactions / comments: 0 / 0
- Reading time: 5 minutes. Body about 1,270 words.
- The markdown title and the opening are about LACP member imbalance, hashing, and N-1. The URL reads as a second “how many uplinks” article.
- Tool and guide links, all HTTP 200 on 2026-11-05:
  - https://netengineerlab.com/guides/switch-oversubscription-n-1/
  - https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/
  - https://netengineerlab.com/ (closing visit line)
- Promo CTA: the calculator paragraph says a capacity calculator cannot predict the LACP hash or guarantee zero drops. That limitation is accurate and should be kept if this post is ever edited. Editing the live slug is out of scope for GATE 0.
- GitHub formula on `main`: **UNAVAILABLE** for this uplink tool.

### 3. id 4933430 — newest

- Title: VLAN Trunk Troubleshooting: 7 Checks Before You Blame the Switch
- URL: https://dev.to/netengineerlabcom/vlan-trunk-troubleshooting-7-checks-before-you-blame-the-switch-3f3j
- Slug matches the title
- Published: 2026-10-28T09:14:38Z (2026-10-28 17:14 Asia/Shanghai)
- Tags: `networking`, `devops`, `cisco`, `networkengineering`
- Reactions / comments: 0 / 0
- Reading time: 5 minutes. Body about 1,190 words.
- Checklist covers physical errors, allowed VLAN list, native VLAN, spanning tree, MTU, MAC learning, and capture. Cisco IOS command names appear as examples. The physical-layer section mentions optical power in prose and does not link a fiber calculator.
- Links: only https://netengineerlab.com/ in the closing “visit NetEngineerLab” line. HTTP 200.
- Specific tool URL: **UNAVAILABLE** in this body.
- Promo CTA: generic homepage. Weaker than the other two posts.
- The body ends with `#networking #devops #cisco #networkengineering`, which repeats the four tags. Do not copy that pattern. It is redundant, not a second keyword strategy.
- GitHub formula on `main`: **UNAVAILABLE** (no VLAN-trunk topic file).

### What the three posts imply

- Distribution is still the account baseline: 0 reactions and 0 comments after 8 to 24 days.
- Two posts already teach uplink capacity and point at the same calculator. A third uplink post would be a duplicate topic even with a new title. The matrix does not schedule one.
- There is no series to extend. Wave-1 should open a fiber series instead of joining a collection that does not exist.
- Canonical is DEV.to. This audit did not find article pages on netengineerlab.com for these three titles or for the Wave-1 titles. The production URLs below are calculator pages. Do not invent a canonical on the product site.

## Tool URL verification (Wave-1 and the six `main` Net topics)

Fetched 2026-11-05. Prefer these production URLs over the GitHub files. The GitHub pages cite the same URLs.

| Tool | Production URL | HTTP | Page title | Formula file on `main` |
|---|---|---|---|---|
| Optical power budget | https://netengineerlab.com/tools/optical-power-budget/ | 200 | Optical Power Budget Calculator \| NetEngineerLab | [NetEngineerLab/optical-power-budget.md](../NetEngineerLab/optical-power-budget.md) |
| Fiber link loss | https://netengineerlab.com/tools/fiber-loss/ | 200 | Fiber Loss Calculator & Optical Link Budget \| NetEngineerLab | [NetEngineerLab/fiber-link-loss.md](../NetEngineerLab/fiber-link-loss.md) |
| Fiber latency | https://netengineerlab.com/tools/fiber-latency-calculator/ | 200 | Fiber Latency Calculator – µs per km, One-Way & RTT | [NetEngineerLab/fiber-propagation-latency.md](../NetEngineerLab/fiber-propagation-latency.md) |
| Chromatic dispersion | https://netengineerlab.com/tools/chromatic-dispersion-calculator/ | 200 | not required for the lock | [NetEngineerLab/chromatic-dispersion.md](../NetEngineerLab/chromatic-dispersion.md) |
| OSPF interface cost | https://netengineerlab.com/tools/ospf-cost-calculator/ | 200 | not required for the lock | [NetEngineerLab/ospf-interface-cost.md](../NetEngineerLab/ospf-interface-cost.md) |
| STP path cost | https://netengineerlab.com/tools/stp-path-cost-calculator/ | 200 | not required for the lock | [NetEngineerLab/stp-path-cost.md](../NetEngineerLab/stp-path-cost.md) |

Wave-1 article 2 uses the fiber-loss tool, not the power-budget tool. The loss page title contains the words “Optical Link Budget”. GATE 1 must keep the two drafts on different calculations: transmit power and receiver sensitivity versus span attenuation in dB, dBm, and margin.

Other matrix URLs were checked the same day. HVAC, Water, Privacy, DevEngineerLab, and some DataFileLab paths answer 308 from the trailing-slash inventory form to the no-slash URL, which then returns 200. The CSV stores the final 200 URL.

**UNAVAILABLE inventory path:** `https://datafilelab.com/csv-to-json-converter` returned HTTP 404. The matrix uses `https://datafilelab.com/csv-to-json`, which returned HTTP 200. `https://datafilelab.com/csv-deduplicator` and `https://datafilelab.com/csv-to-markdown-table` also returned 404 and are not scheduled. `https://datafilelab.com/compare` returned 200 and is day 22.

Sites with no formula file on `main` (PCDog, AIMarkTool, PrivacyFileLab, DataFileLab, DevEngineerLab) use a live tool URL and `related_github_formula_path` = `UNAVAILABLE`. That is inventory-backed, not a missing fetch.

## Open PR #4 (not live on `main`)

https://github.com/ddcodedog/Calculator/pull/4 is **OPEN** (`cursor/formula-topics-batch2-ff46` → `main`). Title: “Add 53 formula topics for six engineering sites”.

It would add these NetEngineerLab files, among others: `pon-splitter-loss.md`, `pon-maximum-distance.md`, `poe-voltage-drop.md`, `ethernet-serialization-delay.md`, `pmd-budget.md`, `poe-power-budget.md`, `wireless-link-budget.md`, `data-center-pue.md`, `ring-all-reduce.md`, `ipv4-subnet.md`. It would also add `HVACEngineerLab/pipe-darcy-pressure-drop.md`.

Until that PR merges, those paths are **not** on `main`. The 30-day matrix does not treat them as published formula docs. Day 20 links the live HVAC pipe-flow page and records the GitHub path as `UNAVAILABLE`. A later gate may point day 20 at `HVACEngineerLab/pipe-darcy-pressure-drop.md` after merge. Do not schedule the PR #4 Net topics in this lock.

PR #5 (`reports/ZERO_COST_BASELINE.*`) is a separate promotion baseline. This file does not edit it.

## Rules

1. Drafts only until a person approves publishing. GATE 0 does not create drafts and does not publish.
2. No duplicate titles. Compare case-insensitively with the three `EXISTING_PUBLISHED` titles and with every other matrix title before a draft is written.
3. Cost stays $0. No paid boost, no DEV.to credit purchase, and no API key in this repository. Public GETs are enough for the weekly counts below.
4. No keyword stuffing. One natural title. At most four tags, each of which matches the article. Do not repeat the tags as a hashtag line in the body. Do not add `webdev`, `python`, or `javascript` to a fiber or hydraulics post.
5. One contextual tool link, plus the site homepage at most once. Name the limitation of the calculator when the article is about operations the tool does not measure (the LACP post already does this).
6. Do not change the three live posts, their slugs, or their canonicals in this program’s early gates. The LACP slug mismatch is documented so it is not copied.
7. New drafts keep the DEV.to URL as canonical until a real article URL exists on the product site. Calculator pages are not article canonicals.
8. Do not write `DEVTO_DRAFT_ACCEPTANCE.md` until GATE 4, and only after drafts exist.
9. If a planned URL starts returning 404, mark that row `UNAVAILABLE` and skip it. Do not swap in an unverified path to keep the calendar full.
10. A missed day moves forward. Do not publish two posts on one day to catch up.

## Wave-1 titles locked for GATE 1

These three titles are the only Wave-1 set. Dates are the first three Asia/Shanghai calendar days. Series name, when a draft is eventually saved in DEV.to: **Fiber Optic Link Calculations**. Do not create that series in GATE 0.

| Day | Date | Locked title | Tool | Formula on `main` | Tags |
|---|---|---|---|---|---|
| 1 | 2026-11-05 | How to Calculate Fiber Optic Power Budget | https://netengineerlab.com/tools/optical-power-budget/ | `NetEngineerLab/optical-power-budget.md` | networking, tutorial, fiber, networkengineering |
| 2 | 2026-11-06 | Understanding Optical Loss: dB, dBm and Link Margin | https://netengineerlab.com/tools/fiber-loss/ | `NetEngineerLab/fiber-link-loss.md` | networking, tutorial, fiber, beginners |
| 3 | 2026-11-07 | Fiber Latency Calculation Explained | https://netengineerlab.com/tools/fiber-latency-calculator/ | `NetEngineerLab/fiber-propagation-latency.md` | networking, tutorial, fiber, performance |

Search intent: all three are how-to / explanatory queries a network engineer types before opening a calculator. Day 2 is the unit-and-margin explanation. It must not repeat the day 1 power-budget walkthrough.

Day 4 (planned, not part of the lock) stays in the same series: chromatic dispersion, same site, formula already on `main`.

## Series recommendation

Create series only when the first approved draft is saved. GATE 0 does not call the DEV.to editor.

| Series | Rows | Why separate |
|---|---|---|
| Fiber Optic Link Calculations | days 1–4 | Power budget, loss, latency, then dispersion. This is the Net wave. |
| Routing and Switching Metrics | days 15 and 26 | OSPF cost and STP path cost. Different job from fiber. |
| Electrical Calculations | days 5, 16, 27 | Ohm’s law, power triangle, transformer full-load current. |
| Water and Open-Channel Hydraulics | days 6, 17, 28 | Manning, rational method, Darcy-Weisbach. |
| Structural Section Checks | days 7, 18, 29 | Euler buckling, bending stress, moment of inertia. |
| Jobsite Quantity Calculations | days 8, 19, 30 | Slab volume, roof pitch, board feet. |
| HVAC Pressure Drop | days 9 and 20 | Duct friction, then hydronic pipe pressure drop. |
| Developer Text Utilities | days 10 and 21 | JSON formatter, regex tester. |
| CSV Workflows | days 11 and 22 | CSV to JSON, CSV compare. |
| Browser Network Checks | days 12 and 23 | Latency test, packet-loss test. |
| Campaign Math | days 13 and 24 | ROAS, CAC/LTV. |
| Local File Privacy | days 14 and 25 | SHA-256, photo EXIF. The photo URL is shared by inventory tools T04 and T05. |

Do not attach the VLAN, LACP, or uplink posts to the fiber series. They can stay series-less. Putting them in “Routing and Switching Metrics” would mix troubleshooting narratives with calculator posts. Leave that decision until someone edits those posts on purpose.

DEV.to allows four tags. The matrix uses tags that already returned articles on 2026-11-05. Net posts keep `networking` plus `tutorial`. A subject tag (`fiber`, `electrical`, `water`, `hvac`, `security`, `hardware`, `json`, `csv`, `privacy`, `seo`, `marketing`, `math`) is included only where it matches the tool. `cisco` stays off the fiber posts. `devops` stays off unless the article is about a developer utility (days 10, 11, 21, 22).

## Thirty-day matrix

[DEVTO_CONTENT_MATRIX.csv](DEVTO_CONTENT_MATRIX.csv) has a header plus 33 data rows:

- Rows with `day` 1–30 are the calendar, 2026-11-05 through 2026-12-04 (Asia/Shanghai).
- `day` 1–3 are `WAVE1` and use the locked titles.
- `day` 4–30 are `PLANNED`.
- Rows `E1`, `E2`, `E3` are the three live posts, status `EXISTING_PUBLISHED`, with their real publish dates. They are not extra publishing days.

Site counts inside the 30 days: NetEngineerLab 6, PowerEngineerLab 3, WaterEngineerLab 3, StructuralEngineerLab 3, DIYCalcLab 3, and 2 each for HVACEngineerLab, DevEngineerLab, DataFileLab, PCDog, AIMarkTool, and PrivacyFileLab. Every site in the [GATE 1 inventory](GATE1_TOOL_INVENTORY.md) appears at least twice. Days 4–30 rotate sites instead of stacking another 27 Net posts.

Formula files cited for days 1–9, 15–19, and 26–30 are the files on `main` today (25-topic batch). Days that point at PCDog, AIMarkTool, PrivacyFileLab, DataFileLab, or DevEngineerLab have no formula file. That gap is labeled `UNAVAILABLE`, not filled from PR #4.

## Weekly review cadence (GATE 3)

Clock: Asia/Shanghai. Review the posts whose `proposed_publish_date` fell in the previous seven days. Do not review a row that is still only `PLANNED` and was not published.

| Review date | Days in scope |
|---|---|
| 2026-11-12 | 1–7 |
| 2026-11-19 | 8–14 |
| 2026-11-26 | 15–21 |
| 2026-12-03 | 22–28 |
| 2026-12-10 | 29–30, plus any row whose date was moved |

Each review records, in a later gate report (not this file):

- Published or still draft. Anything published without approval is a stop.
- `positive_reactions_count` and `comments_count` from `GET https://dev.to/api/articles?username=netengineerlabcom`.
- Page views: **UNAVAILABLE** in the public list payload used here. Do not add an API key to this repo to fetch the dashboard.
- Tool URL still HTTP 200.
- Title still unique against `EXISTING_PUBLISHED` and the rest of the matrix.
- Series name still matches the table above.
- Whether the LACP slug mismatch is still untouched.

Baseline on 2026-11-05: three posts, 0 reactions, 0 comments. A new post that is still at zero after seven days matches that baseline. It is not, by itself, a reason to rewrite. Rewrite or pull the row if the tool URL 404s, the title collides, or the draft explains the wrong calculator.

GATE 3 does not publish the next week’s rows. It only decides keep, revise the next draft, or pause the calendar.
