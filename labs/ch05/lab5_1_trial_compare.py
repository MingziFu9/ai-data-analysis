"""实验 5-1 第 3 步：比较两名标注员对同一批 50 条评论的试标结果，找出分歧，用来修订标注规范。
运行方法：在 labs/ch05 目录下执行  python lab5_1_trial_compare.py
你们小组试标完成后，把结果整理成与“试标50条_示例.csv”相同的四列，改下面的文件名即可。
"""
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_colwidth", 40)
df = pd.read_csv("试标50条_示例.csv")                         # 列：review_id、评论内容、标注员甲、标注员乙

same = df["标注员甲"] == df["标注员乙"]
print(f"两人标注一致：{same.sum()} 条，一致率 {same.mean():.0%}")

# 交叉表：行是甲的标签，列是乙的标签，对角线上是两人一致的
print(pd.crosstab(df["标注员甲"], df["标注员乙"], margins=True, margins_name="合计"))

# 列出全部分歧，小组逐条讨论：谁对？规范哪里没写清楚？
diff = df[~same]
print(f"\n分歧 {len(diff)} 条：")
print(diff[["评论内容", "标注员甲", "标注员乙"]].to_string(index=False))
diff.to_csv("试标分歧.csv", index=False, encoding="utf-8-sig")
