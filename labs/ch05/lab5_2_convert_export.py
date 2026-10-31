"""实验 5-2 第 5 步：把 Label Studio 导出的 JSON 转成训练用的表格，并把菜品实体转成 BIO 序列。
运行方法：在 labs/ch05 目录下执行  python lab5_2_convert_export.py
换成你自己导出的文件：把 EXPORT 改成你的文件名。
"""
import json
import pandas as pd

pd.set_option("display.width", 120)
EXPORT = "示例导出/评论标注_导出.json"
ASPECTS = ["口味", "服务", "环境", "价格", "配送"]
tasks = json.load(open(EXPORT, encoding="utf-8"))           # 一个列表，每个元素是一条任务
print("任务数：", len(tasks))

rows, bio_lines = [], []
for t in tasks:
    text = t["data"]["text"]
    result = t["annotations"][0]["result"]                   # 取第一份标注结果
    row = {"review_id": t["data"]["review_id"], "text": text, "情感": None, "菜品": []}
    tags = ["O"] * len(text)                                 # 每个字先标 O（不是实体）
    for r in result:
        if r["from_name"] == "sentiment":
            row["情感"] = r["value"]["choices"][0]
        elif r["from_name"] == "aspect":
            for a in r["value"]["choices"]:
                row[a] = 1
        elif r["from_name"] == "entity":
            s, e = r["value"]["start"], r["value"]["end"]
            row["菜品"].append(r["value"]["text"])
            tags[s] = "B-菜品"                               # 实体的第一个字
            for i in range(s + 1, e):
                tags[i] = "I-菜品"                           # 实体的其余字
    rows.append(row)
    bio_lines += [f"{ch} {tag}" for ch, tag in zip(text, tags)] + [""]   # 每字一行，句子之间空一行

table = pd.DataFrame(rows)
table[ASPECTS] = table.reindex(columns=ASPECTS).fillna(0).astype(int)    # 没选的方面记 0
table["菜品"] = table["菜品"].str.join("|")
table = table[["review_id", "text", "情感"] + ASPECTS + ["菜品"]]   # 调整列的顺序
print(table.head())
print("情感分布：", table["情感"].value_counts().to_dict())
print("各方面被提到的次数：", table[ASPECTS].sum().to_dict())
table.to_csv("训练表_情感与方面.csv", index=False, encoding="utf-8-sig")
open("训练数据_菜品BIO.txt", "w", encoding="utf-8").write("\n".join(bio_lines))
print("BIO 示例（第 1 条）：")
print("\n".join(bio_lines[:bio_lines.index("")]))
