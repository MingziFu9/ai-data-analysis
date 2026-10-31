"""实验 9-1 第 1 部分：预测送达时长（回归），看误差、看残差"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

DATA = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])

# ---------- 1. 准备特征 X 和标签 y ----------
df["小时"] = df["下单时间"].dt.hour
df["高峰"] = df["小时"].isin([11, 12, 17, 18, 19]).astype(int)   # 午、晚高峰记 1
df["雨天"] = (df["天气"] == "雨").astype(int)                    # 文字变成 0 / 1
df["商家自送"] = (df["配送方式"] == "商家自送").astype(int)
features = ["配送距离", "雨天", "商家自送", "高峰", "就餐人数"]
X, y = df[features], df["送达时长"]

# ---------- 2. 划分训练集和测试集（8:2） ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2026)
print("训练集", len(X_train), "单；测试集", len(X_test), "单")

# ---------- 3. 基准：不管什么订单，都猜训练集的平均值 ----------
base = [y_train.mean()] * len(y_test)
print(f"基准（都猜平均值 {y_train.mean():.1f} 分钟）：平均绝对误差 {mean_absolute_error(y_test, base):.2f} 分钟")

# ---------- 4. 流水线：标准化 → 线性回归 ----------
lin = Pipeline([("scale", StandardScaler()), ("model", LinearRegression())])
lin.fit(X_train, y_train)                       # 用训练集训练
pred = lin.predict(X_test)                      # 对测试集预测
print(f"线性回归：平均绝对误差 {mean_absolute_error(y_test, pred):.2f} 分钟，R² = {r2_score(y_test, pred):.3f}")
coef = pd.Series(lin.named_steps["model"].coef_, index=features)
scale = lin.named_steps["scale"].scale_
print("每个特征增加 1 个单位，送达时长约增加（分钟）：", (coef / scale).round(2).to_dict())

# ---------- 5. 换一个模型试试：随机森林 ----------
rf = RandomForestRegressor(n_estimators=100, min_samples_leaf=20, random_state=2026, n_jobs=-1)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
print(f"随机森林：平均绝对误差 {mean_absolute_error(y_test, pred_rf):.2f} 分钟，R² = {r2_score(y_test, pred_rf):.3f}")

# ---------- 6. 看残差：误差最大的订单有什么特点 ----------
res = X_test.copy()
res["实际"], res["预测"] = y_test, pred.round(1)
res["残差"] = (res["实际"] - res["预测"]).round(1)       # 正数 = 实际比预测慢
print("误差超过 10 分钟的订单占", f"{(res['残差'].abs() > 10).mean():.1%}")
print(res.sort_values("残差", ascending=False).head(3).to_string())

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].scatter(res["预测"], res["实际"], s=4, alpha=0.3)
ax[0].plot([5, 70], [5, 70], color="red")               # 对角线：预测 = 实际
ax[0].set_xlabel("预测送达时长（分钟）"); ax[0].set_ylabel("实际送达时长（分钟）")
ax[0].set_title("预测值与实际值")
ax[1].hist(res["残差"], bins=50)
ax[1].set_xlabel("残差 = 实际 − 预测（分钟）"); ax[1].set_title("残差的分布")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("lab9_1_residual.png"), dpi=110)
