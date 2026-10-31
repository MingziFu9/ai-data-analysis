"""实验 3-2 从数据库取数：用 SQL 从 SQLite 订单库抽取指定时间段的数据，与文件数据合并。
运行方法：在 labs/ch03 目录下执行  python lab3_2_sql.py
"""
import sqlite3
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)
conn = sqlite3.connect("../data/ch03/shike.db")               # 连接数据库（SQLite 就是一个文件）

# 第 1 步：数据库里有哪些表？
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("表：", tables["name"].tolist())

# 第 2 步：取 2025 年 12 月、雨天的订单，只要 5 列
sql = """
SELECT order_id, shop_id, 下单时间, 实付金额, 送达时长
FROM orders
WHERE 下单时间 >= '2025-12-01' AND 下单时间 < '2026-01-01'
  AND 天气 = '雨'
"""
dec_rain = pd.read_sql(sql, conn)                            # 查询结果直接变成 DataFrame
print("12 月雨天订单：", dec_rain.shape)
print(dec_rain.head(3))

# 第 3 步：让数据库先分组汇总，只把结果取回来
sql2 = """
SELECT s.城区, COUNT(*) AS 订单数, ROUND(AVG(o.送达时长), 1) AS 平均送达时长
FROM orders o JOIN shops s ON o.shop_id = s.shop_id
WHERE o.下单时间 >= '2025-12-01' AND o.下单时间 < '2026-01-01' AND o.天气 = '雨'
GROUP BY s.城区
ORDER BY 平均送达时长 DESC
"""
print(pd.read_sql(sql2, conn))

# 第 4 步：和第 3-1 实验得到的文件数据合并：给 12 月雨天订单加上商家平均评分
summary = pd.read_csv("商家汇总.csv")                         # 实验 3-1 保存的文件
df = dec_rain.merge(summary[["shop_id", "店名", "平均评分"]], on="shop_id", how="left")
print(df.head(3))
print("评分 4.0 以上的商家 平均送达时长：", df[df["平均评分"] >= 4.0]["送达时长"].mean().round(1))
print("评分 4.0 以下的商家 平均送达时长：", df[df["平均评分"] < 4.0]["送达时长"].mean().round(1))
conn.close()                                                 # 用完关闭连接
