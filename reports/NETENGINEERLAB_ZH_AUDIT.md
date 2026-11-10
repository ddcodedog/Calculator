# NetEngineerLab Chinese edition audit

Date: 2026-11-10. Phase 1 only. No new Chinese topic files were added.

## Pairing

Each of the twelve `*.zh-CN.md` files sits next to an English topic of the same basename. English files were not overwritten. Display-math blocks match after whitespace is removed. `reports/ZH_FORMULA_REVIEW.json` has no intentional difference.

The Chinese files identify themselves as Simplified Chinese and link back to the English original. Related-formula links point at `*.zh-CN.md` companions. Locale lines are `Locale: zh-CN` and `Locale: en`.

## Live tool pages

Checked with HTTP GET on 2026-11-10. The Chinese URL in each companion is `/tools/<slug>/zh/`. All ten distinct tool pages returned HTTP 200, `html lang="zh-CN"`, a Chinese title, a canonical URL equal to that Chinese page, and hreflang for `en`, `zh-CN`, `es`, and `x-default`.

| Topic file | Chinese URL | HTTP | Language |
|---|---|---:|---|
| bandwidth-transfer-time.zh-CN.md | https://netengineerlab.com/tools/bandwidth-calculator/zh/ | 200 | zh-CN |
| chromatic-dispersion.zh-CN.md | https://netengineerlab.com/tools/chromatic-dispersion-calculator/zh/ | 200 | zh-CN |
| cutover-wait-versus-fiber-delay.zh-CN.md | https://netengineerlab.com/tools/dns-ttl-propagation-calculator/zh/ | 200 | zh-CN |
| dns-ttl-cache-window.zh-CN.md | https://netengineerlab.com/tools/dns-ttl-propagation-calculator/zh/ | 200 | zh-CN |
| fiber-link-loss.zh-CN.md | https://netengineerlab.com/tools/fiber-loss/zh/ | 200 | zh-CN |
| fiber-propagation-latency.zh-CN.md | https://netengineerlab.com/tools/fiber-latency-calculator/zh/ | 200 | zh-CN |
| mtu-mss-overhead.zh-CN.md | https://netengineerlab.com/tools/mtu-calculator/zh/ | 200 | zh-CN |
| on-wire-bytes-at-safe-uplink.zh-CN.md | https://netengineerlab.com/tools/bandwidth-calculator/zh/ | 200 | zh-CN |
| optical-power-budget.zh-CN.md | https://netengineerlab.com/tools/optical-power-budget/zh/ | 200 | zh-CN |
| ospf-interface-cost.zh-CN.md | https://netengineerlab.com/tools/ospf-cost-calculator/zh/ | 200 | zh-CN |
| stp-path-cost.zh-CN.md | https://netengineerlab.com/tools/stp-path-cost-calculator/zh/ | 200 | zh-CN |
| switch-uplink-safe-capacity.zh-CN.md | https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/zh/ | 200 | zh-CN |

Two topics share the bandwidth calculator and two share the DNS TTL calculator. That is 12 documents and 10 tool pages.

## STP page

`https://netengineerlab.com/tools/stp-path-cost-calculator/zh/` returned 200. Title: `STP 路径开销计算器｜802.1D/802.1Q 长短开销与根路径对比`. Canonical is that same URL. Final URL did not fall back to the homepage.

These two shapes returned 404 and an English "Page not found" title:

- `https://netengineerlab.com/zh-CN/tools/stp-path-cost-calculator/`
- `https://netengineerlab.com/tools/stp-path-cost-calculator/zh-CN/`

They are not used in the topic files.

## What was not changed

Chinese prose that already matched the English formula, units, and example numbers was left in place. Titles were already in Chinese and were not renamed. No production route was created.
