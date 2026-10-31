"""实验 2-3（拓展）找出订单高峰：按小时、按星期统计订单量。
运行方法：在 labs/ch02 目录下执行  python lab2_3_peak_hours.py
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

orders = pd.read_csv("../data/orders.csv", parse_dates=["下单时间"])   # 读入时直接把这一列转成日期时间

orders["小时"] = orders["下单时间"].dt.hour
orders["星期"] = orders["下单时间"].dt.day_of_week + 1                 # day_of_week 中星期一是 0，加 1 变成 1～7
by_hour = orders.groupby("小时")["order_id"].count()
by_week = orders.groupby("星期")["order_id"].count()
print("订单最多的 3 个小时：")
print(by_hour.sort_values(ascending=False).head(3))
print("每个星期几的订单数：")
print(by_week)

# 交叉表：行是星期几，列是小时，格子里是订单数
table = pd.crosstab(orders["星期"], orders["小时"])
print("周六 12 点的订单数：", table.loc[6, 12], "；周三 12 点：", table.loc[3, 12])

# 按天汇总，再按月取平均：每个月“平均每天多少单”
daily = orders.set_index("下单时间").resample("D")["order_id"].count()
print("全年平均每天", round(daily.mean(), 1), "单；最多的一天", daily.idxmax().date(), daily.max(), "单")
monthly_avg = daily.resample("MS").mean().round(1)
monthly_avg.index = monthly_avg.index.month
print(monthly_avg)

fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
by_hour.plot(kind="bar", ax=axes[0], title="各小时订单数", color="#5c6bc0")
by_week.plot(kind="bar", ax=axes[1], title="周一至周日订单数", color="#26a69a")
axes[0].set_ylabel("订单数")
plt.tight_layout()
plt.savefig("lab2_3_peak.png", dpi=120)
print("图已保存为 lab2_3_peak.png")
