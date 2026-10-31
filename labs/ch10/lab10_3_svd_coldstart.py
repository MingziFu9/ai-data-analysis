"""实验 10-3：矩阵分解、基于内容推荐的离线评估、新用户冷启动"""
from pathlib import Path
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
shops = pd.read_csv(DATA / "shops.csv").set_index("shop_id")
users = pd.read_csv(DATA / "users.csv").set_index("user_id")
K = 10
train = orders[orders["下单时间"] < "2025-11-01"]
test = orders[orders["下单时间"] >= "2025-11-01"]
seen = train.groupby("user_id")["shop_id"].apply(set).to_dict()
truth = {u: set(s) - seen[u] for u, s in test.groupby("user_id")["shop_id"]
         if u in seen and set(s) - seen[u]}
ui = (pd.crosstab(train["user_id"], train["shop_id"]) > 0).astype(int)


def evaluate(rec_func, name, users_truth):
    hit = recall = 0
    shown = set()
    for uid, t in users_truth.items():
        r = rec_func(uid)
        hit += len(set(r) & t) > 0
        recall += len(set(r) & t) / len(t)
        shown |= set(r)
    n = len(users_truth)
    return {"方法": name, "命中率": round(hit / n, 3), "召回率": round(recall / n, 3),
            "覆盖率": round(len(shown) / len(shops), 3)}


# ---------- 1. 矩阵分解：把 4600 × 300 的大矩阵压缩成 10 个“隐含口味” ----------
svd = TruncatedSVD(n_components=10, random_state=2026)
user_f = svd.fit_transform(ui)                          # 每个用户 10 个数
pred = pd.DataFrame(user_f @ svd.components_, index=ui.index, columns=ui.columns)  # 还原出打分
rec_svd = lambda u: list(pred.loc[u].drop(list(seen[u])).nlargest(K).index)

# ---------- 2. 基于内容：分别用“菜系 + 标签”和“菜系 + 标签 + 城区”做内容向量 ----------
def content_recommender(feat):
    def rec(u):
        profile = feat.loc[list(seen[u])].sum()
        score = pd.Series(cosine_similarity([profile], feat)[0], index=feat.index)
        return list(score.drop(list(seen[u])).nlargest(K).index)
    return rec


base = pd.concat([pd.get_dummies(shops["菜系"]), shops["标签"].str.get_dummies("|")], axis=1).astype(int)
with_area = pd.concat([base, pd.get_dummies(shops["城区"]).astype(int)], axis=1)
rows = [evaluate(content_recommender(base), "内容（菜系+标签）", truth),
        evaluate(content_recommender(with_area), "内容（菜系+标签+城区）", truth),
        evaluate(rec_svd, "矩阵分解（10 个隐含口味）", truth)]
print(pd.DataFrame(rows).to_string(index=False))

# ---------- 3. 冷启动：假装 11～12 月才注册的新用户，没有任何历史，用三种办法推荐 ----------
new_truth = {u: set(s) for u, s in test.groupby("user_id")["shop_id"]}   # 测试期去过的所有店
hot = train["shop_id"].value_counts().index
shop_area = shops["城区"]
hot_area = {a: [s for s in hot if shop_area[s] == a] for a in shop_area.unique()}
train_age = train.merge(users[["年龄段"]], left_on="user_id", right_index=True)
hot_age = {a: list(g["shop_id"].value_counts().index) for a, g in train_age.groupby("年龄段")}

rows = [evaluate(lambda u: list(hot[:K]), "全站热门", new_truth),
        evaluate(lambda u: hot_area[users.loc[u, "常住城区"]][:K], "本区热门（注册时填的城区）", new_truth),
        evaluate(lambda u: hot_age[users.loc[u, "年龄段"]][:K], "同年龄段热门", new_truth)]
print("—— 新用户冷启动 ——")
print(pd.DataFrame(rows).to_string(index=False))
