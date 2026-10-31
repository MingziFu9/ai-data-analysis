"""实验 4-2 按规范实施清洗：处理重复、格式、缺失、单位、异常和业务规则问题，清洗前后逐项核对。
运行方法：在 labs/ch04 目录下执行  python lab4_2_clean_orders.py
"""
import pandas as pd

pd.set_option("display.width", 120)
df = pd.read_csv("../data/orders_raw.csv", dtype=str)
shops = pd.read_csv("../data/shops.csv")
steps = [("原始数据", len(df))]                               # 记录每一步之后的行数

# 规则 1 重复：完全相同的行只保留一行
df = df.drop_duplicates()
steps.append(("1 删除完全重复的行", len(df)))

# 规则 2 日期：把“2025/03/05 12:30”“2025年03月05日 12:30”统一成标准日期时间
t = df["下单时间"].str.replace("/", "-").str.replace("年", "-").str.replace("月", "-").str.replace("日", "")
df["下单时间"] = pd.to_datetime(t, format="mixed")
print("日期转换后为空的行数：", df["下单时间"].isna().sum())

# 规则 3 城区：去掉多余的“区”字；为空的按商家表补上
df["城区"] = df["城区"].str.removesuffix("区")
df["城区"] = df["城区"].fillna(df["shop_id"].map(shops.set_index("shop_id")["城区"]))
print("城区取值：", sorted(df["城区"].unique()))

# 规则 4 数值列：去掉“km”，转换成数字
df["配送距离"] = pd.to_numeric(df["配送距离"].str.replace("km", ""))
for col in ["就餐人数", "订单金额", "优惠金额", "实付金额", "送达时长"]:
    df[col] = pd.to_numeric(df[col])

# 规则 5 单位：实付金额按“分”录入的（除以 100 后才等于 订单 − 优惠），换算成元
fen = ((df["实付金额"] / 100 - (df["订单金额"] - df["优惠金额"])).abs() < 0.05) & (df["实付金额"] > 0)
df.loc[fen, "实付金额"] = (df.loc[fen, "实付金额"] / 100).round(1)
print("按分录入、已换算的行数：", fen.sum())

# 规则 6 业务规则：优惠金额大于订单金额的，按 优惠 = 订单 − 实付 重新计算
bad = df["优惠金额"] > df["订单金额"]
df.loc[bad, "优惠金额"] = (df.loc[bad, "订单金额"] - df.loc[bad, "实付金额"]).round(1)
print("按业务规则修正优惠金额的行数：", bad.sum())

# 规则 7 异常：送达时长为负的取绝对值（录入时多了负号）；超过 180 分钟的置为空值，不参与时长统计
neg = df["送达时长"] < 0
df.loc[neg, "送达时长"] = -df.loc[neg, "送达时长"]
df.loc[df["送达时长"] > 180, "送达时长"] = None
print("负数改正：", neg.sum(), " 超长置空：", df["送达时长"].isna().sum())

# 规则 8 缺失：配送距离为空的，用同一城区的中位数填充，并加一列标记
df["距离为填充值"] = df["配送距离"].isna()
df["配送距离"] = df["配送距离"].fillna(df.groupby("城区")["配送距离"].transform("median"))
steps.append(("2–8 格式、单位、异常、缺失处理后", len(df)))

print(pd.DataFrame(steps, columns=["步骤", "行数"]).to_string(index=False))
print(df.isna().sum()[df.isna().sum() > 0])
df.to_csv("orders_clean.csv", index=False, encoding="utf-8-sig")

# 核对：和随书的“干净”订单表逐列比较（真实工作中没有标准答案，要抽样人工核对）
truth = pd.read_csv("../data/orders.csv", parse_dates=["下单时间"]).set_index("order_id").loc[df["order_id"]]
mine = df.set_index("order_id")
for col in ["下单时间", "实付金额", "优惠金额", "送达时长", "配送距离"]:
    same = (mine[col] == truth[col]) | (mine[col] - truth[col]).abs().lt(0.05) if col != "下单时间" else \
           (mine[col] == truth[col]) | (mine[col] - truth[col]).abs().lt(pd.Timedelta("1min"))
    print(f"{col}：与标准答案一致 {same.mean():.2%}")
