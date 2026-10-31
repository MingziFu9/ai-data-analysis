"""实验 1-2 初识“食客说”数据：读入四张表，看规模、字段和类型，生成数据字典初稿。
运行方法：在 labs/ch01 目录下执行  python lab1_2_first_look.py
"""
import pandas as pd

files = {"商家表": "shops.csv", "用户表": "users.csv", "订单表": "orders.csv", "评论表": "reviews.csv"}

dictionary = []                                          # 用来收集每一列的信息
for table, file in files.items():
    df = pd.read_csv("../data/" + file)                  # 读入一张表
    print(f"{table}（{file}）：{df.shape[0]} 行，{df.shape[1]} 列")
    for col in df.columns:                               # 逐列记录：类型、缺失数、不同取值数、一个例子
        dictionary.append({
            "表": table, "字段": col, "类型": str(df[col].dtype),
            "缺失数": int(df[col].isna().sum()), "不同取值数": int(df[col].nunique()),
            "示例值": df[col].iloc[0],
        })

dict_df = pd.DataFrame(dictionary)
dict_df["含义（请补写）"] = ""                            # 字段含义要人来写，程序写不出来
dict_df.to_csv("数据字典_初稿.csv", index=False, encoding="utf-8-sig")
print()
print(dict_df[dict_df["表"] == "订单表"].to_string(index=False))
print("\n数据字典初稿已保存：数据字典_初稿.csv，共", len(dict_df), "个字段")
