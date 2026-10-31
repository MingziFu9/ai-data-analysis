"""实验 6-2 抽检验收：对一批 2000 条情感标注按标注员分层抽检 10%，判断是否合格，找出需要返工的部分。
运行方法：在 labs/ch06 目录下执行  python lab6_2_sampling_check.py
说明：“情感_参考”列模拟质检员复核后给出的正确标签。真实工作中，只有被抽中的样本才有这一列，由质检员逐条复核填写。
"""
import pandas as pd

batch = pd.read_csv("../data/annotation/batch_2000.csv")
STANDARD = 0.95                                               # 验收标准：准确率不低于 95%
print("本批标注：", len(batch), "条；各标注员条数：", batch["标注员"].value_counts().to_dict())

# 第 1 步：分层抽样，每个标注员各抽 10%（random_state 固定，保证每次抽到同样的样本）
sample = batch.groupby("标注员").sample(frac=0.10, random_state=2026)
print("抽检：", len(sample), "条")

# 第 2 步：质检员逐条复核，记录对错
sample["是否正确"] = sample["情感标签"] == sample["情感_参考"]
total = sample["是否正确"].mean()
print(f"整批抽检准确率：{total:.1%}，{'合格' if total >= STANDARD else '不合格'}")

# 第 3 步：按标注员看
by_worker = sample.groupby("标注员")["是否正确"].agg(抽检条数="count", 正确条数="sum", 准确率="mean")
by_worker["结论"] = by_worker["准确率"].map(lambda x: "合格" if x >= STANDARD else "加抽")
print(by_worker.round(3))

# 第 4 步：错误类型：质检员复核的标签 vs 标注员标的标签
wrong = sample[~sample["是否正确"]]
print("错误类型（行：正确标签，列：标注员标的）：")
print(pd.crosstab(wrong["情感_参考"], wrong["情感标签"]))

# 第 5 步：第一次抽检不合格的，再加抽：从没抽到的部分再抽 20%，与第一次合并后重新判断
fail = by_worker[by_worker["结论"] == "加抽"].index
more = batch.drop(sample.index)
more = more[more["标注员"].isin(fail)].groupby("标注员").sample(frac=0.20, random_state=2030)
more["是否正确"] = more["情感标签"] == more["情感_参考"]
both = pd.concat([sample[sample["标注员"].isin(fail)], more])
again = both.groupby("标注员")["是否正确"].agg(抽检条数="count", 准确率="mean")
again["结论"] = again["准确率"].map(lambda x: "合格" if x >= STANDARD else "返工")
print("加抽后：")
print(again.round(3))

# 第 6 步：保存返工清单
rework_workers = again[again["结论"] == "返工"].index
rework = batch[batch["标注员"].isin(rework_workers)]
rework.drop(columns="情感_参考").to_csv("返工清单.csv", index=False, encoding="utf-8-sig")
print("需返工：", list(rework_workers), len(rework), "条，已保存 返工清单.csv")

# 第 7 步（教学用）：本书数据有全部参考答案，可以看看抽检的判断对不对
full = (batch["情感标签"] == batch["情感_参考"]).groupby(batch["标注员"]).mean()
print("全量真实准确率：", full.round(3).to_dict(), " 整批：", round((batch["情感标签"] == batch["情感_参考"]).mean(), 3))
