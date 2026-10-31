"""实验 7-2 假设检验：
  ① 商家自送和平台专送的送达时长有没有显著差异（t 检验）；
  ② 订单有没有用优惠，和顾客是否给好评有没有关联（卡方检验）；
  ③ 用 200 笔抽样订单估计全部订单的平均送达时长（置信区间）。
运行方法：在 labs/ch07 目录下执行  python lab7_2_tests.py
"""
import pandas as pd
from scipy import stats

orders = pd.read_csv("../data/orders.csv")
reviews = pd.read_csv("../data/reviews.csv")

# ① t 检验：两组的平均值有没有显著差异
a = orders[orders["配送方式"] == "商家自送"]["送达时长"]
b = orders[orders["配送方式"] == "平台专送"]["送达时长"]
print(f"商家自送 {len(a)} 单，平均 {a.mean():.1f} 分钟；平台专送 {len(b)} 单，平均 {b.mean():.1f} 分钟")
t, p = stats.ttest_ind(a, b, equal_var=False)                # Welch t 检验：不要求两组方差相等
print(f"t = {t:.1f}，p {'< 0.001' if p < 0.001 else f'= {p:.3f}'}", "→ 差异显著" if p < 0.05 else "→ 差异不显著")

# 只用一小部分数据（每组 30 单）再检验一次，看看样本量的影响
a30, b30 = a.sample(30, random_state=3), b.sample(30, random_state=3)
t, p = stats.ttest_ind(a30, b30, equal_var=False)
print(f"每组只抽 30 单：平均 {a30.mean():.1f} 对 {b30.mean():.1f}，p = {p:.3f}", "→ 差异显著" if p < 0.05 else "→ 差异不显著")

# ② 卡方检验：两个类别变量有没有关联
df = reviews.merge(orders[["order_id", "优惠金额"]], on="order_id")
df["用了优惠"] = df["优惠金额"] > 0
df["好评"] = df["评分"] >= 4
table = pd.crosstab(df["用了优惠"], df["好评"])
print(table)
print("好评率：", df.groupby("用了优惠")["好评"].mean().round(3).to_dict())
chi2, p, dof, expected = stats.chi2_contingency(table)
print(f"卡方 = {chi2:.2f}，p = {p:.3f}", "→ 有关联" if p < 0.05 else "→ 没有发现关联")

# ③ 置信区间：只抽 200 单，估计全部订单的平均送达时长
s = orders["送达时长"].sample(200, random_state=7)
low, high = stats.t.interval(0.95, len(s) - 1, loc=s.mean(), scale=stats.sem(s))
print(f"样本平均 {s.mean():.1f}，95% 置信区间 [{low:.1f}, {high:.1f}]；全部订单的真实平均 {orders['送达时长'].mean():.1f}")
