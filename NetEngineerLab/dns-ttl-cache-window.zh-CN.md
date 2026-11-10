# 记录变更前的 DNS TTL 窗口

本文是同目录英文稿的简体中文版，英文原文保持不变：[DNS TTL window before a record change](dns-ttl-cache-window.md)。

## 概述

缓存了记录的解析器会保留旧答案，直到缓存中的 TTL 到期。这个计算器把旧 TTL、已经过去的时间、新 TTL 和一小段权威侧延迟，换成三个时钟估计和每日查询率之比。它不查询现网解析器，也不证明互联网上每台递归服务器都已丢掉旧答案。

下面的数字来自该工具生产 `engine.js` 中的 `dns-ttl-engine/2.0.0`，读于 2026-11-08。算例省略 `peakOldTtl`，所以引擎只返回基线情景。

## 公式

剩余缓存时间是旧 TTL 还剩下的部分：

$$
t_{\mathrm{left}} = \max(T_{\mathrm{old}} - t_{\mathrm{elapsed}}, 0)
$$

典型等待和最坏等待以秒为单位，再加上权威侧延迟：

$$
t_{\mathrm{typical}} = 0.5\,t_{\mathrm{left}} + t_{\mathrm{auth}}, \qquad t_{\mathrm{worst}} = \max(t_{\mathrm{left}}, T_{\mathrm{neg}}) + t_{\mathrm{auth}}
$$

显示的分钟保留一位小数：\(\mathrm{round}((v+\epsilon)\times 10)/10\)，其中 \(\epsilon\) 是 JavaScript 的 `Number.EPSILON`。一天的查询次数为

$$
Q_{\mathrm{old}} = \begin{cases} 86400/T_{\mathrm{old}} & T_{\mathrm{old}}>0 \\ 86400 & T_{\mathrm{old}}=0 \end{cases}, \qquad Q_{\mathrm{new}} = 86400/T_{\mathrm{new}}, \qquad R = Q_{\mathrm{new}}/Q_{\mathrm{old}}
$$

\(T_{\mathrm{old}}\ge 0\)，\(T_{\mathrm{new}}>0\)，已过时间、延迟、负缓存 TTL 和“提前降低”的小时数必须有限且 ≥ 0。只有提前降低的窗口短于旧 TTL（`lowerBeforeHours × 3600 < T_old`）时，状态才是 `warning`。新 TTL 低于 60 秒会把 `highAuthoritativeQps` 加进告警列表，但除非同时有那个过晚窗口告警，状态仍为 `pass`。

## 变量

| 名称 | 含义 | 单位 |
|---|---|---|
| 旧 TTL | 当前被缓存的 TTL | s |
| 新 TTL | 变更之后的 TTL | s |
| 已过时间 | 自旧 TTL 发布以来的时间 | s |
| 权威侧延迟 | 缓存计时之外另加的等待 | s |
| 负缓存 TTL | 否定答案可以保留多久 | s |
| 提前降低 | TTL 提前了多久被减小 | h |

## 工程含义

剩余 TTL 的一半是规划中点，不是解析器时钟的实测中位数。最坏情况取剩余正缓存和负缓存 TTL 中较长的一个，再加上同一个权威侧延迟。查询比假定在稳定的 86,400 秒里，每个 TTL 做一次未命中查询。它不是真实 QPS 的预测，因为重试、解析器池和 serve-stale 策略都在这条基线之外。

## 算例

旧 TTL 3600 s，新 TTL 300 s，已经过去 600 s，权威侧延迟 30 s，负缓存 TTL 300 s，提前 24 h 降低。

1. 剩余秒数 = \(\max(3600-600, 0) = 3000\)。显示的剩余时间 = 50.0 min。
2. 典型秒数 = \(0.5\times 3000 + 30 = 1530\)，显示 25.5 min。
3. 最坏秒数 = \(\max(3000, 300)+30 = 3030\)，显示 50.5 min。
4. 旧的每日查询 = \(86400/3600 = 24\)。新的查询 = \(86400/300 = 288\)。增加倍数 = 12.0。
5. \(24\times 3600 = 86400\)，不小于 3600，所以状态为 `pass`。

边界：同一旧 TTL，若“提前降低”设为 0.5 h，则 \(1800 < 3600\)，状态变为 `warning`，并带 `lowerTtlTooLate`。新 TTL 为 30 s 会增加 `highAuthoritativeQps`，但单凭这一点不会把 `pass` 改成 `warning`。非有限 TTL 返回 `{ok:false}`。

## 限制

- 只有基线路径。提供 `peakOldTtl` 会打开后面的风险报告；本篇不走那条分支。
- 没有现网 DNS 查询。解析器提供过期数据的时间可能长于 \(t_{\mathrm{worst}}\)。
- 一位小数的分钟显示值，不要在还需要原始秒数时再拿去相乘。

## 参考标准

引擎没有为 0.5 这个系数引用 RFC 章节。RFC 1035 和 RFC 2308 描述 TTL 与负缓存；本篇没有重读那些文件。状态：待定。


## 在线计算器

在生产页上运行 3600 s 改为 300 s、已过 600 s 的案例：

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/dns-ttl-propagation-calculator/zh/

## 相关公式

- [由链路速率得到的文件传输时间](bandwidth-transfer-time.zh-CN.md)
- [MTU、MSS 与封装开销](mtu-mss-overhead.zh-CN.md)

## 核对

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `dns-ttl-propagation-calculator` |
| 证据 | 生产 `js/engine.js`，模型 `dns-ttl-engine/2.0.0`；缺少 `peakOldTtl` 时返回基线 |
| 方法 | 在 Node 中用引擎的 `round` 辅助函数重算 |
| 算例结果 | 50.0 / 25.5 / 50.5 min，查询增加 12.0，状态 pass |
| 日期 | 2026-11-08 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
