"""实验 8-2：用 pyecharts 做交互图表，拼成一个网页版经营看板"""
from pathlib import Path
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Line, Bar, Pie, Page

DATA = Path(__file__).resolve().parents[1] / "data"
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["下单时间"])
shops = pd.read_csv(DATA / "shops.csv")
reviews = pd.read_csv(DATA / "reviews.csv")
df = orders.merge(shops, on="shop_id")
df["月份"] = df["下单时间"].dt.month

# ① 地图：各城区交易额。地图上的区名带“区”字，所以要在城区后面加上“区”
area = (df.groupby("城区")["实付金额"].sum() / 10000).round(1)
pairs = [(name + "区", value) for name, value in area.items()]
m = (
    Map()
    .add("交易额（万元）", pairs, maptype="广州", is_map_symbol_show=False,
         label_opts=opts.LabelOpts(is_show=False))     # 不显示区名，鼠标悬停时再显示
    .set_global_opts(title_opts=opts.TitleOpts(title="各城区交易额（万元）"),
                     visualmap_opts=opts.VisualMapOpts(min_=0, max_=float(area.max())))
)

# ② 折线图：每月订单数和交易额，下方加一个可以拖动的时间范围条
mon = df.groupby("月份").agg(订单数=("order_id", "count"), 交易额=("实付金额", "sum"))
months = [f"{i}月" for i in mon.index]
line = (
    Line()
    .add_xaxis(months)
    .add_yaxis("交易额（万元）", (mon["交易额"] / 10000).round(1).tolist())
    .set_global_opts(title_opts=opts.TitleOpts(title="每月交易额"),
                     tooltip_opts=opts.TooltipOpts(trigger="axis"),
                     datazoom_opts=opts.DataZoomOpts(range_start=0, range_end=100))
)

# ③ 条形图：各菜系好评率（评分 4 星及以上的比例）
rv = reviews.merge(shops, on="shop_id")
good = (rv.groupby("菜系")["评分"].apply(lambda s: (s >= 4).mean()) * 100).round(1).sort_values()
bar = (
    Bar()
    .add_xaxis(good.index.tolist())
    .add_yaxis("好评率（%）", good.tolist())
    .reversal_axis()                                   # 横过来，变成条形图
    .set_global_opts(title_opts=opts.TitleOpts(title="各菜系好评率"))
)

# ④ 环形图：配送方式占比
share = df["配送方式"].value_counts()
pie = (
    Pie()
    .add("", list(zip(share.index, share.tolist())), radius=["40%", "70%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="配送方式占比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}：{d}%"))
)

# 把四张图放进同一个网页，用浏览器打开就能用鼠标悬停、缩放、点图例
page = Page(page_title="食客说经营看板", layout=Page.SimplePageLayout)
page.add(m, line, bar, pie)
out = page.render(str(Path(__file__).with_name("lab8_2_dashboard.html")))
print("已生成", Path(out).name)
print("各城区交易额（万元）：", area.sort_values(ascending=False).to_dict())
print("好评率最高和最低的菜系：", good.idxmax(), good.max(), "/", good.idxmin(), good.min())
