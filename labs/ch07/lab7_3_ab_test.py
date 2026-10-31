"""实验 7-3 A/B 测试与辛普森悖论：
  ① 规范的 A/B 测试：新版商家页面（B）是否提高了下单转化率；
  ② 不规范的“试验”：B 版主要投放在新城区，整体结论和分城区结论相反。
运行方法：在 labs/ch07 目录下执行  python lab7_3_ab_test.py
"""
import pandas as pd
from statsmodels.stats.proportion import confint_proportions_2indep, proportions_ztest

def ab_report(df, title):
    g = df.groupby("版本")["是否下单"].agg(访客数="count", 下单数="sum", 转化率="mean")
    print(f"—— {title} ——")
    print(g.round(4))
    z, p = proportions_ztest(g["下单数"][["B", "A"]], g["访客数"][["B", "A"]])   # 两个比例的 z 检验
    low, high = confint_proportions_2indep(g.loc["B", "下单数"], g.loc["B", "访客数"],
                                           g.loc["A", "下单数"], g.loc["A", "访客数"])
    diff = g.loc["B", "转化率"] - g.loc["A", "转化率"]
    ptxt = "< 0.001" if p < 0.001 else f"= {p:.3f}"
    print(f"B − A = {diff:+.2%}，95% 置信区间 [{low:+.2%}, {high:+.2%}]，p {ptxt}")
    return g

# ① 规范的 A/B 测试：访客随机分到 A、B 两组
ab = pd.read_csv("../data/ab_test.csv")
print("两组中老城区访客的比例：", ab.groupby("版本")["城区类型"].apply(lambda s: (s == "老城区").mean()).round(3).to_dict())
ab_report(ab, "规范的 A/B 测试")

# ② 不规范的试验：B 版主要投放在新城区
sp = pd.read_csv("../data/ab_simpson.csv")
print("两组中老城区访客的比例：", sp.groupby("版本")["城区类型"].apply(lambda s: (s == "老城区").mean()).round(3).to_dict())
ab_report(sp, "不规范的试验：整体看")
for area, part in sp.groupby("城区类型"):
    ab_report(part, f"不规范的试验：只看{area}")
