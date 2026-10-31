"""实验 2-2 订单数据的合并与分组统计：订单表关联商家表，按城区、菜系、月份统计。
运行方法：在 labs/ch02 目录下执行  python lab2_2_merge_groupby.py
"""
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)                # 列多时全部显示，不用省略号
orders = pd.read_csv("../data/orders.csv")
shops = pd.read_csv("../data/shops.csv")

# 第 1 步：合并（相当于 Excel 的 VLOOKUP）：给每笔订单查出商家所在的城区和菜系
df = orders.merge(shops[["shop_id", "城区", "菜系"]], on="shop_id", how="left")
print("合并前", orders.shape, "合并后", df.shape)

# 第 2 步：按城区分组统计（相当于 Excel 的“分类汇总”）
by_district = df.groupby("城区").agg(
    订单数=("order_id", "count"),
    销售额=("实付金额", "sum"),
    客单价=("实付金额", "mean"),
).round(1).sort_values("销售额", ascending=False)
print(by_district)

# 第 3 步：透视表（相当于 Excel 的“数据透视表”）：行是菜系，列是配送方式，值是平均送达时长
pivot = pd.pivot_table(df, index="菜系", columns="配送方式", values="送达时长", aggfunc="mean").round(1)
print(pivot)

# 第 4 步：按月份统计。先把“下单时间”从文字转换成日期时间，再取出月份
df["下单时间"] = pd.to_datetime(df["下单时间"])
df["月份"] = df["下单时间"].dt.month
by_month = df.groupby("月份").agg(订单数=("order_id", "count"), 销售额=("实付金额", "sum")).round(0)
print(by_month)

# 可以改这里：把 "城区" 换成 "菜系" 或 "天气"，看看结果怎么变
