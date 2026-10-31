"""实验 12-1：识别个人信息，按场景选择脱敏方法，比较脱敏前后的分析结果"""
import hashlib
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
users = pd.read_csv(DATA / "users.csv", dtype={"手机号": str})
orders = pd.read_csv(DATA / "orders.csv")

# ---------- 1. 识别：哪些列可能是个人信息？用正则表达式逐列检查 ----------
RULES = {"手机号": r"^1[3-9]\d{9}$", "地址": r"(?:省|市|区|县).*(?:路|街|号|栋|房)",
         "姓名": r"^[一-龥]{2,3}$"}
for col in users.columns:
    s = users[col].astype(str)
    for kind, pat in RULES.items():
        rate = s.str.contains(pat).mean()
        if rate > 0.8:
            print(f"列“{col}”有 {rate:.0%} 的值像{kind}")

# ---------- 2. 四种脱敏方法 ----------
SALT = "shike-2026"                                   # 加“盐”：别人不知道它，就没法反查


def mask_phone(p):          # 掩码：保留前 3 后 4 位，中间换成 *
    return p[:3] + "****" + p[-4:]


def hash_id(x):             # 哈希：同一个输入永远得到同一串乱码，但从乱码推不回原值
    return hashlib.sha256((SALT + x).encode("utf-8")).hexdigest()[:12]


def generalize_addr(a):     # 泛化：详细地址只保留到区
    return a[:a.index("区") + 1] if "区" in a else a


safe = pd.DataFrame({
    "用户编号": users["user_id"].map(hash_id),                # 假名化：换成哈希编号
    "手机号": users["手机号"].map(mask_phone),
    "地址": users["收货地址"].map(generalize_addr),
    "性别": users["性别"], "年龄段": users["年龄段"], "常住城区": users["常住城区"],
})                                                             # 姓名、昵称直接删除
print(users[["user_id", "姓名", "手机号", "收货地址"]].head(2).to_string(index=False))
print(safe.head(2).to_string(index=False))

# ---------- 3. 扰动：给金额加一点随机误差，个人的具体数字不准了，总体统计几乎不变 ----------
rng = np.random.default_rng(2026)
noisy = orders["实付金额"] * (1 + rng.normal(0, 0.05, len(orders)))   # ±5% 左右的误差
print(f"实付金额平均值：原始 {orders['实付金额'].mean():.2f}，扰动后 {noisy.mean():.2f}")
print(f"单笔订单平均改变了 {(noisy - orders['实付金额']).abs().mean():.2f} 元")

# ---------- 4. 脱敏前后的分析结果一样吗？各城区用户数 ----------
before = users["收货地址"].str.extract(r"广州市(.+?)区")[0].value_counts()
after = safe["地址"].str.extract(r"广州市(.+?)区")[0].value_counts()
print("按城区统计用户数，脱敏前后完全一致：", before.equals(after))

# ---------- 5. 重识别风险：几列组合起来，能不能“认出”某一个人？ ----------
safe["注册日期"] = users["注册日期"]
for cols in [["性别", "年龄段", "常住城区"], ["性别", "年龄段", "常住城区", "注册日期"]]:
    size = safe.groupby(cols)["用户编号"].transform("size")   # 每个人所在组合有几个人
    print(f"{'+'.join(cols)}：同组少于 5 人的用户 {(size < 5).mean():.1%}，独一无二的用户 {(size == 1).mean():.1%}")
