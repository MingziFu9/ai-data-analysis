"""实验 3-1 多格式文件读取与乱码排查：GBK 编码的 CSV、多工作表 Excel、嵌套 JSON，统一成一张商家表。
运行方法：在 labs/ch03 目录下执行  python lab3_1_read_files.py
"""
import json
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)
D = "../data/ch03/"

# 第 1 步：读 GBK 编码的 CSV。先故意不写编码，看看会发生什么
try:
    shops = pd.read_csv(D + "商家名录_gbk.csv")                 # 默认按 UTF-8 读
except UnicodeDecodeError as e:
    print("出错了：", type(e).__name__, "——文件不是 UTF-8 编码")
shops = pd.read_csv(D + "商家名录_gbk.csv", encoding="gbk")     # 告诉 pandas 文件是 GBK 编码
print("商家名录：", shops.shape)
print(shops.head(3))

# 第 2 步：读 Excel 的全部工作表。sheet_name=None 表示“所有工作表”，结果是一个字典：{表名: 表格}
sheets = pd.read_excel(D + "商家评分_按城区.xlsx", sheet_name=None)
print("工作表：", list(sheets.keys()))
scores = pd.concat(sheets.values(), ignore_index=True)        # 8 张表上下拼成一张
print("评分表：", scores.shape)

# 第 3 步：读嵌套 JSON，用 json_normalize 展平
with open(D + "reviews_page1.json", encoding="utf-8") as f:
    payload = json.load(f)                                     # 读成 Python 字典
items = payload["data"]["items"]                               # 一层层取到评论列表
reviews = pd.json_normalize(items)                             # 嵌套的 shop.shop_id 变成一列
print("评论（第 1 页）：", reviews.shape, list(reviews.columns))

# 第 4 步：统一成一张表：商家名录 + 平均评分 + 第 1 页评论条数
cnt = reviews.groupby("shop.shop_id").size().rename("第1页评论数")
result = shops.merge(scores[["shop_id", "平均评分"]], on="shop_id", how="left")
result = result.merge(cnt, left_on="shop_id", right_index=True, how="left")
result["第1页评论数"] = result["第1页评论数"].fillna(0).astype(int)
print(result.head())
result.to_csv("商家汇总.csv", index=False, encoding="utf-8-sig")  # utf-8-sig：Excel 打开不乱码
print("已保存 商家汇总.csv，共", len(result), "行")
