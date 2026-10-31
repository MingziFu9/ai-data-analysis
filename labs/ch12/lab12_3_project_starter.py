"""实验 12-3 综合项目起步程序（选题一：“食客说”评论分析）
把全书学过的步骤串成一条流水线：采集 → 清洗 → 脱敏 → 情感分析 → 汇总 → 出图 → 输出
跑通以后，在每一步上做你自己的改进，并写进项目报告"""
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

LABS = Path(__file__).resolve().parents[1]
sys.path += [str(LABS / "ch04"), str(LABS / "ch11")]     # 借用第 4 章和第 11 章写好的函数
from cleaning import clean_review                         # 第 4 章：评论清洗（含手机号替换）
from monitor_tools import load_model                      # 第 9、11 章：情感模型

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False
OUT = Path(__file__).with_name("项目输出")
OUT.mkdir(exist_ok=True)

# ① 采集：读入原始评论（第 3 章也可以改成从接口或数据库读取）
raw = pd.read_csv(LABS / "data" / "reviews_raw.csv")
meta = pd.read_csv(LABS / "data" / "reviews.csv")[["review_id", "shop_id", "评分", "评论时间"]]
shops = pd.read_csv(LABS / "data" / "shops.csv")
print("① 原始评论", len(raw), "条")

# ② 清洗 + ③ 脱敏：clean_review 会去广告、去网页残留，并把手机号替换成 [手机号]
df = raw.assign(评论内容=raw["评论内容"].map(clean_review))
df = df[df["评论内容"].str.len() >= 4]                     # 太短的视为无效评论（第 4 章的规则）
print("②③ 清洗脱敏后", len(df), "条；还含手机号的：", df["评论内容"].str.contains(r"1[3-9]\d{9}").sum(), "条")

# ④ 情感分析：用第 9 章的模型给每条评论打标签
clf = load_model()
df["情感"] = clf.predict(df["评论内容"])
df = df.merge(meta, on="review_id").merge(shops[["shop_id", "城区", "菜系"]], on="shop_id")
print("④ 情感分布：", df["情感"].value_counts(normalize=True).round(3).to_dict())

# ⑤ 汇总：各菜系的负面评论占比，以及负面最多的 5 家店
by_cuisine = df.groupby("菜系")["情感"].apply(lambda s: (s == "负面").mean()).sort_values()
worst = (df.groupby("shop_id")["情感"].agg(评论数="size", 负面占比=lambda s: (s == "负面").mean())
           .query("评论数 >= 30").sort_values("负面占比", ascending=False).head(5))
print("⑤ 负面占比最高的 5 家店（评论 30 条以上）：")
print(worst.round(3).join(shops.set_index("shop_id")["店名"]).to_string())

# ⑥ 出图：各菜系负面评论占比（条形图，从 0 开始，第 8 章）
fig, ax = plt.subplots(figsize=(7, 4))
ax.barh(by_cuisine.index, by_cuisine.values)
ax.set_xlim(0, by_cuisine.max() * 1.2)
ax.set_title(f"{by_cuisine.index[-1]}、{by_cuisine.index[-2]}的负面评论占比最高（共 {len(df)} 条评论）")  # 标题写结论
ax.set_xlabel("负面评论占比")
plt.tight_layout()
plt.savefig(OUT / "菜系负面占比.png", dpi=120)

# ⑦ 输出：只输出脱敏、汇总后的结果，不输出用户编号等个人信息（第 12 章）
df[["review_id", "shop_id", "城区", "菜系", "评分", "评论内容", "情感"]].to_csv(
    OUT / "评论情感结果.csv", index=False, encoding="utf-8-sig")
print("⑥⑦ 图表和结果已保存到", OUT.name)
