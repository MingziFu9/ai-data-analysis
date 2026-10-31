---
title: Kappa 计算器
description: 修改两名标注员的混淆表，看一致率、碰巧一致率和 Kappa 怎样变化，理解为什么一致率高不等于标得一致（第 6 章）
---

# Kappa 计算器

<iframe class="sim-frame" src="main.html" height="600" loading="lazy" title="Kappa 计算器"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[6.1.2 一致率与 Kappa 系数](../../chapters/06-annotation-qa/index.md#612-kappa)

## 教学说明

**学习目标**

1. 能根据两名标注员的混淆表算出一致率和 Kappa（应用）；
2. 能解释为什么 Kappa 要扣除“碰巧一致”，以及一致率高而 Kappa 低的原因（理解）。

**画面与操作**

- 表格的行是标注员甲的标签，列是乙的标签，格子里的数字可以直接修改。
- 下方实时显示实际一致率、碰巧一致率、Kappa 和一致程度。上方有四个现成的例子。

**数据来源**：“实验 6-1 的 A 与 B”是随书 `three_annotators.csv` 中标注员 A 和 B 的真实混淆表，其余例子为编者构造。

**课堂用法建议**

1. 先点“两人都几乎全标正面”，让学生看一致率 88% 而 Kappa 为负数，讨论原因。
2. 让学生只改一个格子，使 Kappa 超过 0.8，体会“对角线越集中，Kappa 越高”。
