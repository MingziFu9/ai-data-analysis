"""实验 9-3 第 3 部分（待实测，需要能访问模型下载站）：用现成的预训练中文情感模型做预标注
安装：pip install transformers torch
国内下载慢时，先设置镜像：set HF_ENDPOINT=https://hf-mirror.com（macOS / Linux 用 export）
这个模型用大众点评的评论训练，只分“正面 / 负面”两类，所以和参考答案比较时，把“中性”和“负面”合并为“非正面”
"""
from pathlib import Path
import pandas as pd
from transformers import pipeline

DATA = Path(__file__).resolve().parents[1] / "data"
todo = pd.read_csv(DATA / "annotation" / "to_label_100.csv")
ref = pd.read_csv(DATA / "reviews_参考答案.csv")[["review_id", "情感_参考"]]
todo = todo.merge(ref, on="review_id")

# 第一次运行会自动下载模型（约 400MB），以后直接从本机读取
clf = pipeline("text-classification", model="uer/roberta-base-finetuned-dianping-chinese")
out = clf(todo["text"].tolist(), batch_size=16)
todo["模型结果"] = ["正面" if o["label"].startswith("positive") else "非正面" for o in out]
todo["把握"] = [round(o["score"], 2) for o in out]
todo["参考_两类"] = todo["情感_参考"].where(todo["情感_参考"] == "正面", "非正面")
print(f"两类准确率：{(todo['模型结果'] == todo['参考_两类']).mean():.1%}")
print(todo[todo["模型结果"] != todo["参考_两类"]][["text", "模型结果", "情感_参考"]].head(10))
