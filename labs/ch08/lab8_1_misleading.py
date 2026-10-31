"""实验 8-1 第 2 部分：4 张误导性图表和改正后的图（上排是误导的，下排是改正的）"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
shops = pd.read_csv(DATA / "shops.csv")
reviews = pd.read_csv(DATA / "reviews.csv")
df = orders.merge(shops, on="shop_id")
df["月份"] = df["下单时间"].dt.month
rv = reviews.merge(shops, on="shop_id")
rv["好评"] = rv["评分"] >= 4

fig, ax = plt.subplots(2, 4, figsize=(20, 9))

# 问题 1：截断纵轴。三个城区好评率只差几个百分点，纵轴从 0.6 开始就显得差很多
rate = rv.groupby("城区")["好评"].mean().loc[["黄埔", "天河", "越秀"]]
ax[0, 0].bar(rate.index, rate.values, color="#C44E52")
ax[0, 0].set_ylim(0.6, 0.72)
ax[0, 0].set_title("✗ 纵轴从 0.6 开始：越秀像是黄埔的 10 倍")
ax[1, 0].bar(rate.index, rate.values, color="#4C72B0")
ax[1, 0].set_ylim(0, 1)
for i, v in enumerate(rate.values):                 # 柱子上标出数值
    ax[1, 0].text(i, v + 0.02, f"{v:.1%}", ha="center")
ax[1, 0].set_title("✓ 纵轴从 0 开始，并标出数值")

# 问题 2：饼图切成 10 块，相近的扇形根本比不出大小
cnt = df["菜系"].value_counts()
ax[0, 1].pie(cnt.values, labels=cnt.index)
ax[0, 1].set_title("✗ 10 个菜系的饼图：湘菜和火锅谁多？")
cnt.sort_values().plot(kind="barh", ax=ax[1, 1], color="#4C72B0")
ax[1, 1].set_title("✓ 排好序的条形图，一眼看出排名")

# 问题 3：双纵轴。左右两个刻度随意设定，两条线就能“想交叉就交叉”
m = df.groupby("月份").agg(订单数=("order_id", "count"), 平均送达=("送达时长", "mean"))
ax[0, 2].plot(m.index, m["订单数"], color="#4C72B0", label="订单数")
right = ax[0, 2].twinx()                             # 共用横轴，再建一个右纵轴
right.plot(m.index, m["平均送达"], color="#C44E52", label="平均送达时长")
right.set_ylim(27.3, 29.3)                           # 故意把右轴范围设得很窄
ax[0, 2].set_title("✗ 双纵轴：看起来订单越多送得越慢")
ax[1, 2].plot(m.index, m["订单数"] / m["订单数"].iloc[0] * 100, marker="o", label="订单数")
ax[1, 2].plot(m.index, m["平均送达"] / m["平均送达"].iloc[0] * 100, marker="s", label="平均送达时长")
ax[1, 2].set_ylabel("以 1 月为 100 的指数")
ax[1, 2].legend()
ax[1, 2].set_title("✓ 换算成同一刻度（1 月 = 100）再比较")

# 问题 4：只截取对自己有利的一段时间
gmv = df.groupby("月份")["实付金额"].sum() / 10000
ax[0, 3].plot(gmv.loc[8:9].index, gmv.loc[8:9].values, marker="o", color="#C44E52")
ax[0, 3].set_xticks([8, 9])
ax[0, 3].set_title("✗ 只看 8～9 月：交易额“暴跌”")
ax[1, 3].plot(gmv.index, gmv.values, marker="o")
ax[1, 3].set_xticks(range(1, 13))
ax[1, 3].set_ylim(0, gmv.max() * 1.15)
ax[1, 3].set_title("✓ 看全年：9 月回落，全年是上升趋势")

plt.tight_layout()
plt.savefig(Path(__file__).with_name("lab8_1_misleading.png"), dpi=110)
print("三个城区好评率：", rate.round(3).to_dict())
print("订单数与平均送达时长的相关系数：", round(m["订单数"].corr(m["平均送达"]), 2))
print("8 月 → 9 月交易额：", gmv.loc[8].round(1), "→", gmv.loc[9].round(1), "万元，",
      f"下降 {1 - gmv.loc[9] / gmv.loc[8]:.1%}")
