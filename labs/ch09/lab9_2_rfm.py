"""实验 9-2：RFM 用户分群——先按规则分，再用 K 均值聚类"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
today = pd.Timestamp("2026-01-01")               # 以 2026 年 1 月 1 日作为“今天”

# ---------- 1. 计算每个用户的 R、F、M ----------
rfm = orders.groupby("user_id").agg(
    最近下单=("下单时间", "max"),
    F=("order_id", "count"),                     # 频率：下了几单
    M=("实付金额", "sum"),                       # 金额：一共花了多少钱
)
rfm["R"] = (today - rfm["最近下单"]).dt.days    # 最近一次下单距今几天，越小越好
rfm = rfm[["R", "F", "M"]]
print(rfm.describe().round(1))

# ---------- 2. 规则分群：每个指标和中位数比，分“高 / 低” ----------
r_good = rfm["R"] <= rfm["R"].median()          # R 小 = 最近来过 = 好
f_high = rfm["F"] > rfm["F"].median()
m_high = rfm["M"] > rfm["M"].median()
names = {(True, True, True): "重要价值客户", (False, True, True): "重要唤回客户",
         (True, False, True): "重要发展客户", (False, False, True): "重要挽留客户",
         (True, True, False): "一般价值客户", (False, True, False): "一般唤回客户",
         (True, False, False): "一般发展客户", (False, False, False): "一般挽留客户"}
rfm["规则分群"] = [names[k] for k in zip(r_good, f_high, m_high)]
print(rfm["规则分群"].value_counts())

# ---------- 3. K 均值聚类：先取对数、再标准化，然后分成 4 群 ----------
X = StandardScaler().fit_transform(np.log1p(rfm[["R", "F", "M"]]))
for k in range(2, 7):                            # 看看分几群合适：惯性越小越紧凑
    print(k, "群，惯性", round(KMeans(k, n_init=10, random_state=2026).fit(X).inertia_))
km = KMeans(n_clusters=4, n_init=10, random_state=2026).fit(X)
rfm["聚类"] = km.labels_

# ---------- 4. 分群画像：每群的人数和 R、F、M 的中位数 ----------
profile = rfm.groupby("聚类").agg(人数=("R", "size"), R中位数=("R", "median"),
                                F中位数=("F", "median"), M中位数=("M", "median")).round(0)
profile["交易额占比"] = (rfm.groupby("聚类")["M"].sum() / rfm["M"].sum()).round(3)
print(profile.sort_values("M中位数", ascending=False))

# ---------- 5. 画图：F 和 M 的散点图，颜色表示聚类 ----------
fig, ax = plt.subplots(figsize=(7, 5))
for c, g in rfm.groupby("聚类"):
    ax.scatter(g["F"], g["M"], s=6, alpha=0.5, label=f"第 {c} 群（{len(g)} 人）")
ax.set_xlabel("F：全年下单次数"); ax.set_ylabel("M：全年消费金额（元）")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(); ax.set_title("用户分群（K 均值，4 群）")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("lab9_2_rfm.png"), dpi=110)
rfm.to_csv(Path(__file__).with_name("用户分群结果.csv"), encoding="utf-8-sig")
