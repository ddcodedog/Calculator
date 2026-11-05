# DEV.to Wave-1 draft acceptance

Scaffolding for GATE 4. Local drafts exist. DEV.to draft IDs are not assigned yet. This file does not publish anything.

## Status

| Item | Value |
|---|---|
| Status | **LOCAL_READY** |
| DEV.to draft IDs | **TBD** — parent fills the table below after the API upload |
| `published` | **false** on every Wave-1 file. Required. |
| Auto-publish | **No.** Do not send `published: true`. Do not call a publish endpoint. |
| API key in this repository | **None.** This run did not call the DEV.to write API. |
| Account checked | `netengineerlabcom` (user id 4179691), public `GET` only, 2026-11-05 |

Parent fill-in after upload:

| Draft | DEV.to id | API `published` flag observed | Notes |
|---|---|---|---|
| How to Calculate Fiber Optic Power Budget | TBD | must be false | |
| Understanding Optical Loss: dB, dBm and Link Margin | TBD | must be false | |
| Fiber Latency Calculation Explained | TBD | must be false | |

Upload date: TBD. Uploaded by: TBD.

## Drafts

Series on all three files: **NetEngineerLab Fiber Engineering**.

`canonical_url` is an empty string on every file. These are original drafts, not republications. Calculator pages are not article canonicals.

| Title | Local path | Tags (4) | `published` |
|---|---|---|---|
| How to Calculate Fiber Optic Power Budget | [promo/devto/wave1/how-to-calculate-fiber-optic-power-budget.md](../promo/devto/wave1/how-to-calculate-fiber-optic-power-budget.md) | networking, fiberoptics, tutorial, networkengineering | false |
| Understanding Optical Loss: dB, dBm and Link Margin | [promo/devto/wave1/understanding-optical-loss-db-dbm-link-margin.md](../promo/devto/wave1/understanding-optical-loss-db-dbm-link-margin.md) | networking, fiberoptics, tutorial, beginners | false |
| Fiber Latency Calculation Explained | [promo/devto/wave1/fiber-latency-calculation-explained.md](../promo/devto/wave1/fiber-latency-calculation-explained.md) | networking, fiberoptics, tutorial, performance | false |

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

Tag probe the same day, `GET https://dev.to/api/articles?tag={name}&per_page=1` → HTTP 200 and one article each for `networking`, `fiberoptics`, `tutorial`, `networkengineering`, `beginners`, and `performance`.

## Series and tag note for the uploader

GATE 0 ([DEVTO_GROWTH_PLAN.md](DEVTO_GROWTH_PLAN.md), [DEVTO_CONTENT_MATRIX.csv](DEVTO_CONTENT_MATRIX.csv)) names the series **Fiber Optic Link Calculations** and uses the subject tag `fiber` with these fourth tags: `networkengineering`, `beginners`, `performance`.

This run's brief locks the front matter to series **NetEngineerLab Fiber Engineering** and to the subject tag `fiberoptics`, with the same fourth tags as the matrix. The markdown files follow that brief. Both `fiber` and `fiberoptics` returned at least one public article on 2026-11-05.

Before the API call, pick one series name and send that name. Do not create the series by publishing. GATE 0 files on this branch are unchanged.

## Checklist for GATE 2 API upload

1. Keep the DEV.to API key in the parent environment only. Do not commit it, do not echo it into a log that lands in git, and do not put it in this file.
2. Upload the three markdown files as drafts. `published` must be false on the request and on the response. If a response comes back published, stop and do not "fix" it by editing the live post in this gate.
3. Send `title`, `description`, `body_markdown`, the four tags, and the chosen series. Max four tags. Do not append a hashtag line to the body.
4. Leave `canonical_url` empty. Do not point canonical at the calculator. After a DEV.to URL exists, that DEV.to URL is the canonical until a real article page exists on the product site (GATE 0 rule 7).
5. Record the returned draft ids in the fill-in table above. Status stays short of published until a person approves a later publish gate.
6. Re-GET the three tool URLs. A 404 or 410 stops the upload for that article.
7. Re-GET `https://dev.to/api/articles?username=netengineerlabcom&per_page=30` and compare titles case-insensitively with the three drafts plus the VLAN, LACP, and stack-uplink posts. Any collision stops the upload.
8. Confirm each body still contains one production tool URL: power budget → `https://netengineerlab.com/tools/optical-power-budget/`, loss → `https://netengineerlab.com/tools/fiber-loss/`, latency → `https://netengineerlab.com/tools/fiber-latency-calculator/`.
9. Do not publish two of these on the same calendar day to catch up (GATE 0 rule 10). The matrix dates are 2026-11-05, 2026-11-06, and 2026-11-07 (Asia/Shanghai).
10. Do not attach the existing VLAN, LACP, or uplink posts to this series as part of the upload.

## GATE 0 files on this branch

Included by branching from `cursor/devto-growth-gate0-c93d` (those files were not on `main` when this branch was cut):

- [reports/DEVTO_GROWTH_PLAN.md](DEVTO_GROWTH_PLAN.md)
- [reports/DEVTO_CONTENT_MATRIX.csv](DEVTO_CONTENT_MATRIX.csv)
