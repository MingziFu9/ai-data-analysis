"""实验 8-1 第 1 部分：用 Matplotlib 和 seaborn 画 8 种常用图表，拼成一张大图"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 中文字体：按顺序找，找到哪个用哪个；第二行让负号正常显示
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
shops = pd.read_csv(DATA / "shops.csv")
df = orders.merge(shops, on="shop_id")              # 订单表加上商家的城区、菜系
df["月份"] = df["下单时间"].dt.month
df["星期"] = df["下单时间"].dt.day_of_week + 1      # 1 = 星期一 …… 7 = 星期日
df["小时"] = df["下单时间"].dt.hour

fig, axes = plt.subplots(2, 4, figsize=(20, 9))     # 2 行 4 列，共 8 个子图
ax = axes.flatten()                                 # 变成一维，方便用 ax[0]～ax[7]

# ① 比较：各菜系订单数 → 横向条形图（类别名字长时用横向，排好序）
cnt = df["菜系"].value_counts().sort_values()
ax[0].barh(cnt.index, cnt.values, color="#4C72B0")
ax[0].set_title("① 比较：各菜系订单数（条形图）")

# ② 趋势：每月交易额 → 折线图
gmv = df.groupby("月份")["实付金额"].sum() / 10000
ax[1].plot(gmv.index, gmv.values, marker="o")
ax[1].set_xticks(range(1, 13))
ax[1].set_ylim(0, gmv.max() * 1.15)                 # 纵轴从 0 开始
ax[1].set_title("② 趋势：每月交易额（万元，折线图）")

# ③ 构成：配送方式占比 → 饼图（只有两三类时才用饼图）
share = df["配送方式"].value_counts()
ax[2].pie(share.values, labels=share.index, autopct="%.1f%%", startangle=90)
ax[2].set_title("③ 构成：配送方式占比（饼图）")

# ④ 分布：实付金额 → 直方图
ax[3].hist(df["实付金额"], bins=60, color="#55A868")
ax[3].axvline(df["实付金额"].median(), color="red", linestyle="--", label="中位数")
ax[3].legend()
ax[3].set_title("④ 分布：实付金额（直方图）")

# ⑤ 分布对比：各城区实付金额 → 箱线图（不画超出须线的点，图更清爽）
order = df.groupby("城区")["实付金额"].median().sort_values().index
sns.boxplot(data=df, x="城区", y="实付金额", order=order, showfliers=False, ax=ax[4])
ax[4].set_title("⑤ 分布对比：各城区实付金额（箱线图）")

# ⑥ 关系：配送距离与送达时长 → 散点图（只抽 2000 个点，避免糊成一片）
sample = df.sample(2000, random_state=2026)
ax[5].scatter(sample["配送距离"], sample["送达时长"], s=6, alpha=0.4)
ax[5].set_xlabel("配送距离（公里）")
ax[5].set_ylabel("送达时长（分钟）")
ax[5].set_title("⑥ 关系：距离与送达时长（散点图）")

# ⑦ 两个类别 + 数值：星期 × 小时的订单量 → 热力图
heat = df.pivot_table(index="星期", columns="小时", values="order_id", aggfunc="count")
sns.heatmap(heat, cmap="YlOrRd", ax=ax[6], cbar_kws={"label": "订单数"})
ax[6].set_title("⑦ 星期 × 小时订单量（热力图）")

# ⑧ 构成随类别变化：各城区两种配送方式的订单数 → 堆叠柱状图
stack = pd.crosstab(df["城区"], df["配送方式"]).loc[order]
stack.plot(kind="bar", stacked=True, ax=ax[7], rot=0)
ax[7].set_title("⑧ 各城区配送方式构成（堆叠柱状图）")

plt.tight_layout()
out = Path(__file__).with_name("lab8_1_charts.png")
plt.savefig(out, dpi=110)
print("已保存", out.name)
print("每月交易额（万元）：", gmv.round(1).to_dict())
print("订单最多的时段：", df["小时"].value_counts().head(3).to_dict())
print("周末日均订单 / 工作日日均订单 =",
      round(df[df["星期"] >= 6].shape[0] / 2 / (df[df["星期"] <= 5].shape[0] / 5), 2))
