"""实验 6-3 预标注、主动学习与噪声标签：
  第 1 部分 比较“随机挑选”和“最拿不准的先标”两种方式，标注量相同时哪种模型更准；
  第 2 部分 用 cleanlab 在 2000 条人工标注中找出可疑标签。
运行方法：在 labs/ch06 目录下执行  python lab6_3_active_cleanlab.py （约 1 分钟）
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cleanlab.filter import find_label_issues
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False
rv = pd.read_csv("../data/reviews.csv").merge(pd.read_csv("../data/reviews_参考答案.csv"), on="review_id")
vec = TfidfVectorizer(analyzer="char", ngram_range=(1, 2), min_df=2)   # 按单字和两字词把评论变成数字
X = vec.fit_transform(rv["评论内容"])
y = rv["情感_参考"].to_numpy()
rng = np.random.default_rng(6)
idx = rng.permutation(len(rv))
pool, test = idx[:8000], idx[8000:10000]                       # 8000 条“待标注池”，2000 条测试

def run(strategy, rounds=10, step=100):
    """从 100 条开始，每轮再“标注”100 条，记录测试准确率"""
    labeled = list(pool[:100])
    acc = []
    for r in range(rounds + 1):
        model = LogisticRegression(max_iter=1000).fit(X[labeled], y[labeled])
        acc.append((len(labeled), (model.predict(X[test]) == y[test]).mean()))
        rest = np.setdiff1d(pool, labeled)
        if strategy == "随机":
            pick = rng.choice(rest, step, replace=False)
        else:                                                   # 最拿不准：最大概率最小的
            prob = model.predict_proba(X[rest]).max(axis=1)
            pick = rest[np.argsort(prob)[:step]]
        labeled += list(pick)
    return pd.DataFrame(acc, columns=["已标注条数", strategy]).set_index("已标注条数")

curve = pd.concat([run("随机"), run("最拿不准先标")], axis=1)
print(curve.round(3))
curve.plot(marker="o", title="标注同样多的数据，哪种挑法模型更准？")
plt.ylabel("测试准确率")
plt.savefig("lab6_3_active.png", dpi=150, bbox_inches="tight")

# 第 2 部分：用 cleanlab 找出 2000 条人工标注中的可疑标签
batch = pd.read_csv("../data/annotation/batch_2000.csv")
classes = ["中性", "正面", "负面"]
labels = batch["情感标签"].map({c: i for i, c in enumerate(classes)}).to_numpy()
Xb = vec.transform(batch["评论内容"])
prob = cross_val_predict(LogisticRegression(max_iter=1000), Xb, labels, cv=5, method="predict_proba")
issues = find_label_issues(labels, prob, return_indices_ranked_by="self_confidence")
truly_wrong = (batch["情感标签"] != batch["情感_参考"]).to_numpy()
print(f"cleanlab 找出可疑标签 {len(issues)} 条，其中真的标错的 {truly_wrong[issues].sum()} 条"
      f"（查准 {truly_wrong[issues].mean():.0%}）；全部标错的 {truly_wrong.sum()} 条，找到了 {truly_wrong[issues].sum() / truly_wrong.sum():.0%}")
show = batch.iloc[issues[:6]][["评论内容", "标注员", "情感标签", "情感_参考"]]
print(show.to_string(index=False))
