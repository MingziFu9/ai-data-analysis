"""4.4 节演示：用 3σ 法则和箱线图法（IQR）找实付金额的异常值，看看它们是不是“错误”。"""
import pandas as pd

df = pd.read_csv("orders_clean.csv")
x = df["实付金额"]
mean, std = x.mean(), x.std()
out1 = df[(x - mean).abs() > 3 * std]                       # 3σ 法则：离平均值超过 3 个标准差
q1, q3 = x.quantile(0.25), x.quantile(0.75)
iqr = q3 - q1
out2 = df[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)]       # 箱线图法：超出“上下须”
print(f"平均 {mean:.1f}，标准差 {std:.1f}，3σ 上界 {mean + 3 * std:.1f}，异常 {len(out1)} 行")
print(f"Q1 {q1:.1f}，Q3 {q3:.1f}，IQR {iqr:.1f}，上须 {q3 + 1.5 * iqr:.1f}，异常 {len(out2)} 行")
print("3σ 异常订单的就餐人数分布：")
print(out1["就餐人数"].value_counts().sort_index())
print("全部订单的就餐人数分布：")
print(df["就餐人数"].value_counts(normalize=True).sort_index().round(3))
