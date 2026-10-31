"""实验 10-1：热门推荐与基于内容的推荐"""
from pathlib import Path
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv")
shops = pd.read_csv(DATA / "shops.csv").set_index("shop_id")

# ---------- 1. 热门推荐：订单最多的 10 家餐厅，人人都一样 ----------
hot = orders["shop_id"].value_counts().head(10)
print("热门 10 家：")
print(shops.loc[hot.index, ["店名", "菜系", "标签"]].assign(订单数=hot.values).to_string())

# ---------- 2. 给每家餐厅做一个“内容向量”：菜系、标签、城区，有就记 1，没有记 0 ----------
feat = pd.concat([
    pd.get_dummies(shops["菜系"]),                 # 10 个菜系，每家只有一个是 1
    shops["标签"].str.get_dummies("|"),           # 标签用 | 分隔，每家可以有好几个 1
    pd.get_dummies(shops["城区"]),                 # 8 个城区
], axis=1).astype(int)
print("内容向量的列数：", feat.shape[1])
print(feat.loc["S0001"][feat.loc["S0001"] == 1])  # 看第一家店有哪些 1

# ---------- 3. 余弦相似度：两家店的向量方向越接近，越相似（0～1） ----------
sim = pd.DataFrame(cosine_similarity(feat), index=feat.index, columns=feat.index)
top = sim["S0001"].drop("S0001").sort_values(ascending=False).head(5)
print(f"和 {shops.loc['S0001', '店名']} 最相似的 5 家：")
print(shops.loc[top.index, ["店名", "标签"]].assign(相似度=top.round(2).values).to_string())

# ---------- 4. 给一个用户推荐：把他去过的店的向量加起来，当作他的“口味画像” ----------
uid = "U00002"
history = orders[orders["user_id"] == uid]["shop_id"].value_counts()   # 去过哪些店、各几次
print(f"用户 {uid} 去过 {len(history)} 家店，共 {history.sum()} 单：")
print(shops.loc[history.index, ["店名", "标签"]].assign(次数=history.values).to_string())
profile = feat.loc[history.index].mul(history.values, axis=0).sum()   # 去得多的店权重大
score = pd.Series(cosine_similarity([profile], feat)[0], index=feat.index)
rec = score.drop(history.index).sort_values(ascending=False).head(10)  # 去掉已经去过的
print("基于内容推荐的 10 家：")
print(shops.loc[rec.index, ["店名", "标签"]].assign(得分=rec.round(2).values).to_string())
