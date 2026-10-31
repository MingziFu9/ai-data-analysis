"""实验 4-3 清洗函数与评论文本清洗：用 cleaning.py 里的函数清洗两批订单和 1.2 万条评论。
运行方法：在 labs/ch04 目录下执行  python lab4_3_pipeline.py
"""
import pandas as pd
from cleaning import clean_orders, clean_review              # 从同目录的 cleaning.py 导入自己写的函数

shops = pd.read_csv("../data/shops.csv")
raw = pd.read_csv("../data/orders_raw.csv", dtype=str)

# 第 1 部分：把原始订单当作“上半年”“下半年”两批先后到达的数据，分别调用同一个函数清洗
first = raw[raw["order_id"] < "O028000"]
second = raw[raw["order_id"] >= "O028000"]
parts = [clean_orders(first, shops), clean_orders(second, shops)]
for name, p in zip(["第一批", "第二批"], parts):
    print(name, "清洗后", p.shape, "实付合计", round(p["实付金额"].sum(), 1))
both = pd.concat(parts)
once = clean_orders(raw, shops)
print("分两批清洗 与 一次清洗 的实付合计是否相同：", round(both["实付金额"].sum(), 1) == round(once["实付金额"].sum(), 1))

# 第 2 部分：清洗评论文本
rv = pd.read_csv("../data/reviews_raw.csv")
rv["清洗后"] = rv["评论内容"].apply(clean_review)          # 对每一条评论调用 clean_review
changed = rv[rv["清洗后"] != rv["评论内容"]]
print("被修改的评论：", len(changed), "条")
for a, b in changed[["评论内容", "清洗后"]].head(5).itertuples(index=False):
    print("  原文：", a, "\n  清洗：", b)
useless = rv["清洗后"].str.len() < 4                         # 清洗后不到 4 个字的视为无效评论
print("无效评论：", useless.sum(), "条，例如：", rv.loc[useless, "评论内容"].head(3).tolist())
rv[~useless][["review_id", "清洗后"]].rename(columns={"清洗后": "评论内容"}).to_csv(
    "reviews_clean.csv", index=False, encoding="utf-8-sig")
print("已保存 reviews_clean.csv，共", (~useless).sum(), "条")
