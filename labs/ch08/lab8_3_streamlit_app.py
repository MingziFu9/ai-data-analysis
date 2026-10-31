"""实验 8-3：用 Streamlit 搭一个能筛选的“食客说”经营看板
运行方法（在命令行里输入，不是在 Python 里运行）：
    streamlit run labs/ch08/lab8_3_streamlit_app.py
浏览器会自动打开 http://localhost:8501
"""
from pathlib import Path
import pandas as pd
import streamlit as st

DATA = Path(__file__).resolve().parents[1] / "data"


@st.cache_data                     # 数据只读一次，以后每次点选都直接用缓存
def load():
    orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
    shops = pd.read_csv(DATA / "shops.csv")
    df = orders.merge(shops, on="shop_id")
    df["月份"] = df["下单时间"].dt.month
    return df


df = load()
st.set_page_config(page_title="食客说经营看板", layout="wide")
st.title("“食客说”经营看板（2025 年）")

# ---------- 左侧边栏：筛选条件 ----------
areas = st.sidebar.multiselect("城区", sorted(df["城区"].unique()), default=sorted(df["城区"].unique()))
start, end = st.sidebar.slider("月份", 1, 12, (1, 12))
mode = st.sidebar.radio("配送方式", ["全部", "平台专送", "商家自送"])

sel = df[df["城区"].isin(areas) & df["月份"].between(start, end)]
if mode != "全部":
    sel = sel[sel["配送方式"] == mode]

# ---------- 第一行：指标卡 ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("订单量", f"{len(sel):,}")
c2.metric("交易额（万元）", f"{sel['实付金额'].sum() / 10000:,.1f}")
c3.metric("客单价中位数（元）", f"{sel['实付金额'].median():.1f}")
c4.metric("平均送达时长（分钟）", f"{sel['送达时长'].mean():.1f}")

# ---------- 第二行：两张图 ----------
left, right = st.columns(2)
left.subheader("每月交易额（万元）")
left.line_chart(sel.groupby("月份")["实付金额"].sum() / 10000)
right.subheader("各菜系订单数")
right.bar_chart(sel["菜系"].value_counts())

# ---------- 第三行：明细表，可以点表头排序 ----------
st.subheader("各城区汇总")
table = sel.groupby("城区").agg(订单量=("order_id", "count"),
                              交易额=("实付金额", "sum"),
                              平均送达时长=("送达时长", "mean")).round(1)
st.dataframe(table.sort_values("交易额", ascending=False))
