"""实验 1-3 让大模型写分析代码，再找出它的错。
任务：统计 2025 年每个城区的“订单数、下单用户数、平均实付金额”。
下面的 ai_version 是编者模仿大模型常犯的错误写成的“AI 答案”，correct_version 是改正后的写法。
运行方法：在 labs/ch01 目录下执行  python lab1_3_check_ai_code.py
"""
import pandas as pd

orders = pd.read_csv("../data/orders.csv")
shops = pd.read_csv("../data/shops.csv")


def ai_version():
    df = orders.merge(shops, on="shop_id")
    result = df.groupby("城区").agg(
        订单数=("order_id", "count"),
        下单用户数=("user_id", "count"),        # 错误 1：count 数的是行数，同一个用户下多单会被重复计算
        平均实付金额=("订单金额", "mean"),        # 错误 2：用了“订单金额”，没有减去优惠
    )
    return result.round(1)


def correct_version():
    df = orders.merge(shops[["shop_id", "城区"]], on="shop_id")   # 只取需要的列，避免列名冲突
    result = df.groupby("城区").agg(
        订单数=("order_id", "count"),
        下单用户数=("user_id", "nunique"),       # nunique：去重后再数
        平均实付金额=("实付金额", "mean"),
    )
    return result.round(1).sort_values("订单数", ascending=False)


a, c = ai_version(), correct_version()
print("AI 版本：")
print(a.to_string())
print("\n改正后：")
print(c.to_string())
# 核对：订单数之和应等于订单表的行数
print("\n核对：订单表共", len(orders), "行；改正后各区订单数之和", c["订单数"].sum())
print("核对：全部订单的平均实付金额", round(orders["实付金额"].mean(), 1))
