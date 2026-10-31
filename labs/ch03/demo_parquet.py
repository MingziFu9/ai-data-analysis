"""3.2 节演示：同一张订单表存成 CSV 和 Parquet，比较文件大小和读取速度。"""
import os
import time
import pandas as pd

orders = pd.read_csv("../data/orders.csv", parse_dates=["下单时间"])
orders.to_parquet("orders.parquet", index=False)              # 需要 pyarrow 库
for name in ["../data/orders.csv", "orders.parquet"]:
    t = time.perf_counter()
    df = pd.read_parquet(name) if name.endswith("parquet") else pd.read_csv(name)
    ms = (time.perf_counter() - t) * 1000
    print(f"{name:22s} {os.path.getsize(name) / 1024 / 1024:5.1f} MB  读取 {ms:5.0f} 毫秒  下单时间类型 {df['下单时间'].dtype}")
os.remove("orders.parquet")
