"""实验 7-1 门店经营探索性分析：单变量 → 双变量 → 分组对比 → 相关分析，最后列出发现。
运行方法：在 labs/ch07 目录下执行  python lab7_1_eda.py
"""
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option("display.width", 120)
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False
orders = pd.read_csv("../data/orders.csv")
shops = pd.read_csv("../data/shops.csv")
df = orders.merge(shops[["shop_id", "城区", "菜系", "人均价格"]], on="shop_id", how="left")

# 第 1 步 单变量：数值看描述统计和偏度，类别看频数
x = df["实付金额"]
print(x.describe().round(1))
print(f"偏度 {x.skew():.2f}；平均值 {x.mean():.1f} 比中位数 {x.median():.1f} 大，说明右边有长尾")
print(df["菜系"].value_counts(normalize=True).round(3).head(5))

# 第 2 步 画分布：实付金额的直方图
fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))
x.plot.hist(bins=60, ax=ax[0], title="实付金额的分布（右偏、长尾）")
ax[0].axvline(x.mean(), color="red", linestyle="--", label=f"平均值 {x.mean():.1f}")
ax[0].axvline(x.median(), color="green", linestyle="--", label=f"中位数 {x.median():.1f}")
ax[0].set_ylabel("订单数")
ax[0].legend()
df.sample(2000, random_state=1).plot.scatter(x="配送距离", y="送达时长", s=4, alpha=0.4, ax=ax[1], title="配送距离与送达时长")
plt.tight_layout()
plt.savefig("lab7_1_eda.png", dpi=150)

# 第 3 步 分组对比：各菜系客单价（平均值和中位数都看）
print(df.groupby("菜系")["实付金额"].agg(订单数="count", 平均值="mean", 中位数="median").round(1).sort_values("中位数"))

# 第 4 步 相关分析：几个数值列两两之间的相关系数
cols = ["配送距离", "送达时长", "就餐人数", "实付金额", "优惠金额"]
print(df[cols].corr().round(2))

# 第 5 步 再分组看一个关键问题：天气和配送方式对送达时长的影响
print(df.pivot_table(index="天气", columns="配送方式", values="送达时长", aggfunc="mean").round(1))
