"""实验 10-2：基于物品的协同过滤与离线评估
用 1～10 月的订单训练，看能不能猜中用户 11～12 月第一次去的新店"""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
shops = pd.read_csv(DATA / "shops.csv").set_index("shop_id")
K = 10                                                   # 每人推荐 10 家

# ---------- 1. 按时间切分：前 10 个月训练，后 2 个月测试 ----------
train = orders[orders["下单时间"] < "2025-11-01"]
test = orders[orders["下单时间"] >= "2025-11-01"]
seen = train.groupby("user_id")["shop_id"].apply(set).to_dict()       # 每人训练期去过的店
truth = {}                                                             # 每人测试期第一次去的新店
for uid, s in test.groupby("user_id")["shop_id"]:
    new = set(s) - seen.get(uid, set())
    if uid in seen and new:
        truth[uid] = new
print(f"训练 {len(train)} 单，测试 {len(test)} 单；参与评估的用户 {len(truth)} 人")

# ---------- 2. 用户—物品矩阵：行是用户，列是餐厅，去过记 1 ----------
ui = (pd.crosstab(train["user_id"], train["shop_id"]) > 0).astype(int)
print("用户—物品矩阵的大小：", ui.shape, f"，填了 1 的格子只占 {ui.values.mean():.1%}")

# ---------- 3. 物品相似度：两家店的“顾客名单”越重合，越相似 ----------
item_sim = cosine_similarity(ui.T)                       # 300 × 300 的相似度矩阵
np.fill_diagonal(item_sim, 0)                            # 自己和自己不算
item_sim = pd.DataFrame(item_sim, index=ui.columns, columns=ui.columns)
top = item_sim["S0283"].sort_values(ascending=False).head(3)
print("和 S0283 阿坊粤菜（天河店）顾客最重合的店：", dict(zip(shops.loc[top.index, "店名"], top.round(3))))


def rec_itemcf(uid):
    """把用户去过的每家店的“相似店”得分加起来，去掉去过的，取前 K 家"""
    score = item_sim.loc[list(seen[uid])].sum().drop(list(seen[uid]))
    return list(score.nlargest(K).index)


hot = train["shop_id"].value_counts().index              # 训练期从热到冷排好的店


def rec_hot(uid):
    """热门推荐：最热门的店中，挑用户没去过的前 K 家"""
    return [s for s in hot if s not in seen[uid]][:K]


# ---------- 4. 离线评估：命中率、召回率、精确率、覆盖率 ----------
def evaluate(rec_func, name):
    hit = recall = precision = 0
    shown = set()                                        # 所有被推荐过的店
    for uid, t in truth.items():
        r = rec_func(uid)
        n = len(set(r) & t)                              # 推荐的 K 家中猜中了几家
        hit += n > 0
        recall += n / len(t)
        precision += n / K
        shown |= set(r)
    u = len(truth)
    return {"方法": name, "命中率": round(hit / u, 3), "召回率": round(recall / u, 3),
            "精确率": round(precision / u, 3), "覆盖率": round(len(shown) / len(shops), 3)}


result = pd.DataFrame([evaluate(rec_hot, "热门推荐"), evaluate(rec_itemcf, "物品协同过滤")])
print(result.to_string(index=False))
