"""实验 6-1 一致性分析：三名标注员对同一批 300 条评论的情感标注，计算准确率、一致率、Kappa，找出分歧样本。
运行方法：在 labs/ch06 目录下执行  python lab6_1_agreement.py
"""
import pandas as pd
from sklearn.metrics import cohen_kappa_score
from statsmodels.stats.inter_rater import aggregate_raters, fleiss_kappa

pd.set_option("display.width", 120)
pd.set_option("display.max_colwidth", 36)
df = pd.read_csv("../data/annotation/three_annotators.csv")
people = ["标注员A", "标注员B", "标注员C"]
print("样本数：", len(df))

# 第 1 步：对照金标准，算每个人的准确率
for p in people:
    print(f"{p} 准确率：{(df[p] == df['金标准']).mean():.1%}")

# 第 2 步：两两之间的一致率和 Cohen's Kappa
for i in range(3):
    for j in range(i + 1, 3):
        a, b = df[people[i]], df[people[j]]
        print(f"{people[i]} 与 {people[j]}：一致率 {(a == b).mean():.1%}，Kappa {cohen_kappa_score(a, b):.3f}")

# 第 3 步：三个人一起的 Fleiss' Kappa
table, _ = aggregate_raters(df[people].to_numpy())           # 统计每条评论各标签得了几票
print(f"三人 Fleiss' Kappa：{fleiss_kappa(table):.3f}")

# 第 4 步：标注员 C 的混淆表：行是金标准，列是 C 标的
print(pd.crosstab(df["金标准"], df["标注员C"], margins=True, margins_name="合计"))

# 第 5 步：多数投票，三人中至少两人相同就取它
df["多数投票"] = df[people].mode(axis=1)[0]
all_diff = df[people].nunique(axis=1) == 3                   # 三人三个答案，投票无效
print(f"多数投票准确率：{(df['多数投票'] == df['金标准']).mean():.1%}；三人各不相同：{all_diff.sum()} 条")

# 第 6 步：分歧样本，交给规范制定者复核
diff = df[df[people].nunique(axis=1) > 1]
print(f"有分歧的样本：{len(diff)} 条，例如：")
print(diff[["评论内容"] + people + ["金标准"]].head(8).to_string(index=False))
diff.to_csv("分歧样本.csv", index=False, encoding="utf-8-sig")
