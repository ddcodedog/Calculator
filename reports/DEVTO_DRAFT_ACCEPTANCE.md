# DEV.to Wave-1 draft acceptance

Status is **PUBLISHED**. The user approved publishing after the unpublished drafts existed. This file only records that result. It does not call the DEV.to API.

Local markdown under `promo/devto/wave1/` is unchanged and still has `published: false` in front matter. The live posts are the DEV.to articles below.

## Status

| Item | Value |
|---|---|
| Status | **PUBLISHED** |
| Prior statuses | `LOCAL_READY`, then `DRAFTS_CREATED_UNPUBLISHED` |
| Create request | `published: false`. Create response was `published: null` (draft). |
| Live `published` | **true** on ids 4979932, 4979933, and 4979934 |
| Series used | **NetEngineerLab Fiber Engineering** (`collection_id` 46199 on the public article records) |
| API key in this repository | **None.** |
| Account | `netengineerlabcom` (user id 4179691) |
| Authenticated inventory | **6 published** articles via `GET /api/articles/me` (3 earlier posts + these 3) |
| Upload | 2026-11-05, parent API upload, then user-approved publish. Names are not recorded in this file. |

| Title | id | Live URL | `published` | `published_at` |
|---|---|---|---|---|
| How to Calculate Fiber Optic Power Budget | 4979932 | https://dev.to/netengineerlabcom/how-to-calculate-fiber-optic-power-budget-bd5 | true | 2026-11-05T06:52:48Z |
| Understanding Optical Loss: dB, dBm and Link Margin | 4979933 | https://dev.to/netengineerlabcom/understanding-optical-loss-db-dbm-and-link-margin-2en2 | true | 2026-11-05T06:52:49Z |
| Fiber Latency Calculation Explained | 4979934 | https://dev.to/netengineerlabcom/fiber-latency-calculation-explained-35em | true | 2026-11-05T06:53:22Z |

Draft URLs before publish (temp slugs, normal for unpublished DEV.to drafts):

| id | Draft URL at GATE 2 |
|---|---|
| 4979932 | https://dev.to/netengineerlabcom/how-to-calculate-fiber-optic-power-budget-2aon-temp-slug-2176682 |
| 4979933 | https://dev.to/netengineerlabcom/understanding-optical-loss-db-dbm-and-link-margin-1fmi-temp-slug-4501061 |
| 4979934 | https://dev.to/netengineerlabcom/fiber-latency-calculation-explained-3hkg-temp-slug-6537799 |

Public read while recording this update, 2026-11-05:

- Each live URL returned HTTP 200.
- `GET /api/articles/4979932` and `GET /api/articles/4979933` returned HTTP 200. `published_at`, slug, and `canonical_url` match the live URLs. `canonical_url` is the DEV.to article, not the calculator. Tags match the local front matter. `collection_id` is 46199.
- `GET /api/articles/4979934` returned HTTP 404. `GET /api/articles/netengineerlabcom/fiber-latency-calculation-explained-35em` returned HTTP 200 with the same `published_at`, live URL, canonical URL, tags, and `collection_id` 46199.
- `GET /api/articles?username=netengineerlabcom&per_page=30` was inconsistent in the same minute: one response listed 6 ids (4979934, 4979933, 4979932, 4933430, 4909590, 4839123), and later responses listed only the original 3. The account total of 6 is the authenticated `/api/articles/me` count supplied with the publish record.

## GATE 2 results

| Check | Result |
|---|---|
| Drafts created | 3 (ids 4979932, 4979933, 4979934) |
| Request flag | `published: false` |
| Response flag | `published: null` on each draft |
| Pre-upload inventory | 0 unpublished, 3 published (VLAN / LACP / stack uplinks) |
| Pre-upload title collision | none |
| Post-upload inventory | 3 unpublished drafts, still 3 published |
| Series sent | NetEngineerLab Fiber Engineering |
| Article bodies edited in this gate | no |
| Later publish | User approved. Live `published: true`. Authenticated account total 6. |

The three earlier posts stay as they were: id 4839123 (stack uplinks), id 4909590 (LACP), id 4933430 (VLAN trunk troubleshooting). They were not edited or moved into this series. With the three Wave-1 posts, `/api/articles/me` reports 6 published articles.

## Drafts

Series on all three files: **NetEngineerLab Fiber Engineering**.

`canonical_url` is an empty string on every file. These are original drafts, not republications. Calculator pages are not article canonicals.

| Title | Local path | Tags (4) | `published` |
|---|---|---|---|
| How to Calculate Fiber Optic Power Budget | [promo/devto/wave1/how-to-calculate-fiber-optic-power-budget.md](../promo/devto/wave1/how-to-calculate-fiber-optic-power-budget.md) | networking, fiberoptics, tutorial, networkengineering | false |
| Understanding Optical Loss: dB, dBm and Link Margin | [promo/devto/wave1/understanding-optical-loss-db-dbm-link-margin.md](../promo/devto/wave1/understanding-optical-loss-db-dbm-link-margin.md) | networking, fiberoptics, tutorial, beginners | false |
| Fiber Latency Calculation Explained | [promo/devto/wave1/fiber-latency-calculation-explained.md](../promo/devto/wave1/fiber-latency-calculation-explained.md) | networking, fiberoptics, tutorial, performance | false |

The `published` column above is the local front matter, which was left at `false`. On DEV.to the same three ids are published.

Descriptions in front matter:

- Power budget: "Calculate a fiber power budget from minimum launch power and receiver sensitivity, then check overload and remaining reach."
- Optical loss: "Separate optical loss in dB from power in dBm, then see how span loss and engineering margin set two different link margins."
- Latency: "Calculate one-way fiber delay and round-trip time from route length, group index, equipment delay, and serialization."

Worked examples use the verified formula-doc inputs and were recomputed on 2026-11-05:

| Article | Check result |
|---|---|
| Power budget, 20 km, 0.35 dB/km, 2/5 dBm, sensitivity −28 dBm, overload +2 dBm | Design loss 11.40 dB, remaining 17.60 dB, sensitivity margin 21.60 dB, overload margin 5.40 dB, `d_max` 70.2857 km, status healthy. Overload moved to −8 dBm fails at −4.60 dB. |
| Fiber loss, 10 km PON feeder | Physical 25.30 dB, design 28.30 dB, remaining 3.70 dB, receive −22.30 dBm, receive margin 4.70 dB, status healthy. Available budget 28 dB fails at −0.30 dB. |
| Latency, 100 km, route factor 1, group index 1.468 | One-way 489.67209175… µs, display 489.67 µs. RTT display 979.34 µs. Per km 4.8967209… µs. Serialization check (separate inputs: 1500 bytes, 1 Gbit/s, 2 hops) is 24 µs. |

Each body links one production tool URL and the matching formula file on GitHub. No closing hashtag line. No second tool URL.

## Tool URL HTTP checks

Checked 2026-11-05 with an HTTP GET (Python `urllib`, follow redirects). No failures.

| Article | URL | HTTP | Final URL | Page title |
|---|---|---|---|---|
| Power budget | https://netengineerlab.com/tools/optical-power-budget/ | 200 | same | Optical Power Budget Calculator \| NetEngineerLab |
| Optical loss | https://netengineerlab.com/tools/fiber-loss/ | 200 | same | Fiber Loss Calculator & Optical Link Budget \| NetEngineerLab |
| Latency | https://netengineerlab.com/tools/fiber-latency-calculator/ | 200 | same | Fiber Latency Calculator – µs per km, One-Way & RTT |

The fiber-loss page title contains the words "Optical Link Budget". The day-2 draft still calculates span loss, dB versus dBm, and the two margins from [fiber-link-loss.md](../NetEngineerLab/fiber-link-loss.md). It does not repeat the day-1 power-budget walkthrough. Day 1 stays on [optical-power-budget.md](../NetEngineerLab/optical-power-budget.md). Day 3 stays on [fiber-propagation-latency.md](../NetEngineerLab/fiber-propagation-latency.md).

URL verification failures: **none**.

## Duplicate check against live DEV.to posts

Public read on 2026-11-05:

- `GET https://dev.to/api/articles?username=netengineerlabcom&per_page=30` → HTTP 200, 3 articles
- same query with `page=2` → HTTP 200, empty list

| id | Title | Slug note |
|---|---|---|
| 4839123 | How Many Uplinks Does a 4-Switch Stack Need? A Practical Network Design Guide | Slug matches the title (`…-1apd`) |
| 4909590 | Why Is One LACP Link at 100% While the Other Is Almost Idle? | Slug is the uplink stem with suffix `2d8l` |
| 4933430 | VLAN Trunk Troubleshooting: 7 Checks Before You Blame the Switch | Slug matches the title |

Case-insensitive comparison of those three titles with the three Wave-1 titles: **no collision**. VLAN trunk troubleshooting, LACP member imbalance, and stack-uplink count are different topics. They stay out of this series. This gate does not edit those posts, their slugs, or their canonicals.

GATE 2 counts for the same account:

- Pre-upload: **0 unpublished**, **3 published**. No title collision with the Wave-1 titles.
- After upload: **3 unpublished drafts**, **3 published** still. The new rows are ids 4979932, 4979933, and 4979934.

Tag probe the same day, `GET https://dev.to/api/articles?tag={name}&per_page=1` → HTTP 200 and one article each for `networking`, `fiberoptics`, `tutorial`, `networkengineering`, `beginners`, and `performance`.

## Series and tag note for the uploader

GATE 0 ([DEVTO_GROWTH_PLAN.md](DEVTO_GROWTH_PLAN.md), [DEVTO_CONTENT_MATRIX.csv](DEVTO_CONTENT_MATRIX.csv)) names the series **Fiber Optic Link Calculations** and uses the subject tag `fiber` with these fourth tags: `networkengineering`, `beginners`, `performance`.

This run's brief locks the front matter to series **NetEngineerLab Fiber Engineering** and to the subject tag `fiberoptics`, with the same fourth tags as the matrix. The markdown files follow that brief. Both `fiber` and `fiberoptics` returned at least one public article on 2026-11-05.

GATE 2 sent series **NetEngineerLab Fiber Engineering** and created the drafts unpublished. The user then approved publish. Public article records show `collection_id` 46199. GATE 0 files on this branch are unchanged. Local article front matter was not edited for the publish.

## GATE 2 upload checklist

Completed 2026-11-05 by the parent upload. Article bodies were not changed in the follow-up that recorded these results.

1. API key stayed out of this repository. It is not in this file.
2. Three drafts were created with request `published: false`. Each response has `published: null`. None came back as a published post.
3. Series sent: **NetEngineerLab Fiber Engineering**. Titles are the three Wave-1 titles. Local front matter still has four tags and an empty `canonical_url`.
4. `canonical_url` was left empty. Calculator pages were not used as canonicals. The temp-slug URLs above are draft URLs, not a reason to set a canonical.
5. Returned ids were recorded as 4979932, 4979933, and 4979934. Status at the end of GATE 2 was **DRAFTS_CREATED_UNPUBLISHED**. Current status is **PUBLISHED** (see the status table).
6. Tool URL HTTP checks from GATE 1 (2026-11-05) were 200 for all three calculators. No 404 or 410 was recorded.
7. Pre-upload duplicate check: 0 unpublished, 3 published, no title collision. After upload: 3 unpublished drafts and the same 3 published posts.
8. Local bodies still contain one production tool URL each (power budget, fiber loss, fiber latency). Bodies were not edited for GATE 2.
9. GATE 2 did not publish. A later user-approved publish set all three live on 2026-11-05 (`published_at` 06:52:48Z, 06:52:49Z, and 06:53:22Z). Matrix dates remain 2026-11-05, 2026-11-06, and 2026-11-07 (Asia/Shanghai). Publishing the three approved drafts on the same clock day is the approval, not a catch-up of later matrix rows.
10. The existing VLAN, LACP, and uplink posts were not attached to this series.

## GATE 0 files on this branch

Included by branching from `cursor/devto-growth-gate0-c93d` (those files were not on `main` when this branch was cut):

- [reports/DEVTO_GROWTH_PLAN.md](DEVTO_GROWTH_PLAN.md)
- [reports/DEVTO_CONTENT_MATRIX.csv](DEVTO_CONTENT_MATRIX.csv)
