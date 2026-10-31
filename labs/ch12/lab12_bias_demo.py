"""12.5 节示例：样本偏差——只用平台专送的订单训练送达时长模型，对商家自送的订单会怎样？"""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

DATA = Path(__file__).resolve().parents[1] / "data"
df = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
df["高峰"] = df["下单时间"].dt.hour.isin([11, 12, 17, 18, 19]).astype(int)
df["雨天"] = (df["天气"] == "雨").astype(int)
X_cols = ["配送距离", "雨天", "高峰", "就餐人数"]          # 注意：特征里没有“配送方式”

train = df[df["配送方式"] == "平台专送"].sample(frac=0.8, random_state=2026)   # 只采集到了平台专送
model = LinearRegression().fit(train[X_cols], train["送达时长"])

for name, part in df.drop(train.index).groupby("配送方式"):
    pred = model.predict(part[X_cols])
    print(f"{name}：{len(part)} 单，平均绝对误差 {mean_absolute_error(part['送达时长'], pred):.2f} 分钟，"
          f"平均少估了 {(part['送达时长'] - pred).mean():.2f} 分钟，"
          f"实际比预测晚 10 分钟以上的占 {((part['送达时长'] - pred) > 10).mean():.1%}")
