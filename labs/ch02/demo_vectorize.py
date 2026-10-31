"""2.7 节演示：同样计算 5 万多笔订单的实付金额，用循环和用向量化各要多久。"""
import time
import numpy as np
import pandas as pd

orders = pd.read_csv("../data/orders.csv")
amount = orders["订单金额"].to_numpy()          # 转成 NumPy 数组
discount = orders["优惠金额"].to_numpy()

t0 = time.perf_counter()
result_loop = []
for i in range(len(amount)):                   # 方法一：一笔一笔地算
    result_loop.append(amount[i] - discount[i])
t1 = time.perf_counter()
result_vec = amount - discount                 # 方法二：整列一起减（向量化）
t2 = time.perf_counter()

print("订单数：", len(amount))
print(f"循环用时：{(t1 - t0) * 1000:.1f} 毫秒")
print(f"向量化用时：{(t2 - t1) * 1000:.2f} 毫秒")
print("两种方法结果一致：", np.allclose(result_loop, result_vec))
a = np.array([30, 45, 60])
print(a * 0.9, a + np.array([1, 2, 3]), a.shape, a.dtype)
