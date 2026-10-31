"""实验 2-1 用 pandas 做一遍 Excel 里做过的事：读表、看表、筛选、排序、新增列。
运行方法：在 labs/ch02 目录下执行  python lab2_1_excel_to_pandas.py
"""
import pandas as pd

pd.set_option("display.width", 120)                  # 让打印的表格宽一些，不折行

# 第 1 步：读表、看表（相当于用 Excel 打开文件，看看有几行几列）
orders = pd.read_csv("../data/orders.csv")
print("行数和列数：", orders.shape)
print(orders.head(3))                                 # 前 3 行
print(orders.dtypes)                                  # 每一列的数据类型

# 第 2 步：描述统计（相当于对数值列算平均值、最大值、最小值……）
print(orders[["实付金额", "配送距离", "送达时长"]].describe().round(1))

# 第 3 步：筛选（相当于 Excel 的“筛选”）：雨天、送达时长超过 45 分钟的订单
slow_rain = orders[(orders["天气"] == "雨") & (orders["送达时长"] > 45)]
print("雨天且超过 45 分钟的订单：", len(slow_rain), "单")

# 第 4 步：排序（相当于 Excel 的“排序”）：实付金额最高的 5 单
top5 = orders.sort_values("实付金额", ascending=False).head(5)
print(top5[["order_id", "下单时间", "就餐人数", "实付金额"]])

# 第 5 步：新增列（相当于在 Excel 里新建一列写公式）：人均实付、优惠比例
orders["人均实付"] = (orders["实付金额"] / orders["就餐人数"]).round(1)
orders["优惠比例"] = (orders["优惠金额"] / orders["订单金额"]).round(3)
print(orders[["order_id", "实付金额", "就餐人数", "人均实付", "优惠比例"]].head(3))

# 第 6 步：保存结果（相当于“另存为”），Excel 能直接打开
slow_rain.to_csv("雨天慢单.csv", index=False, encoding="utf-8-sig")
print("已保存 雨天慢单.csv")
