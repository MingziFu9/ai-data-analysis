"""实验 4-1 数据质量评估：按六个维度检查“食客说”原始订单表，生成数据质量评估表。
运行方法：在 labs/ch04 目录下执行  python lab4_1_quality_check.py
"""
import pandas as pd

pd.set_option("display.width", 120)
raw = pd.read_csv("../data/orders_raw.csv", dtype=str)       # 全部按文字读，先不让 pandas 自作主张
shops = pd.read_csv("../data/shops.csv")
n = len(raw)
print("原始订单表：", raw.shape)
print(raw.isna().sum()[raw.isna().sum() > 0])                # 每列有多少空值（只显示有空值的列）

num = lambda col: pd.to_numeric(raw[col], errors="coerce")   # 转成数字，转不了的变成空值
time_ok = pd.to_datetime(raw["下单时间"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
checks = [
    # (维度, 检查项, 有问题的行：True 表示有问题)
    ("完整性", "城区为空", raw["城区"].isna()),
    ("完整性", "配送距离为空", raw["配送距离"].isna()),
    ("唯一性", "完全重复的行", raw.duplicated()),
    ("唯一性", "订单号重复", raw["order_id"].duplicated()),
    ("有效性", "下单时间不是标准格式", time_ok.isna()),
    ("有效性", "配送距离不是数字", raw["配送距离"].notna() & num("配送距离").isna()),
    ("有效性", "送达时长为负数", num("送达时长") < 0),
    ("一致性", "城区不在标准城区列表中", raw["城区"].notna() & ~raw["城区"].isin(shops["城区"].unique())),
    ("一致性", "城区与商家表不一致", raw["城区"].notna() & (raw["城区"] != raw["shop_id"].map(shops.set_index("shop_id")["城区"]))),
    ("准确性", "实付 ≠ 订单 − 优惠", (num("实付金额") - (num("订单金额") - num("优惠金额"))).abs() > 0.05),
    ("准确性", "优惠金额大于订单金额", num("优惠金额") > num("订单金额")),
    ("准确性", "送达时长超过 180 分钟", num("送达时长") > 180),
    ("及时性", "下单时间不在 2025 年", time_ok.notna() & (time_ok.dt.year != 2025)),
]
report = pd.DataFrame([(d, item, int(bad.sum()), f"{bad.mean():.2%}") for d, item, bad in checks],
                      columns=["维度", "检查项", "问题行数", "占比"])
print(report.to_string(index=False))
report.to_csv("数据质量评估表.csv", index=False, encoding="utf-8-sig")
