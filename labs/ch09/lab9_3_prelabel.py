"""实验 9-3 第 1 部分：用实验 9-1 训练好的模型给 100 条新评论做预标注
把握大的直接采用，把握小的交给人工，比较准确率和省下的时间"""
from pathlib import Path
import pandas as pd
import joblib

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
clf = joblib.load(HERE / "sentiment_model.joblib")       # 先运行 lab9_1_sentiment.py 得到

todo = pd.read_csv(DATA / "annotation" / "to_label_100.csv")          # 第 5 章待标注的 100 条
ref = pd.read_csv(DATA / "reviews_参考答案.csv")[["review_id", "情感_参考"]]
todo = todo.merge(ref, on="review_id")

# predict_proba 给出属于每一类的概率，最大的那个就是模型的“把握”
proba = clf.predict_proba(todo["text"])
todo["预标注"] = clf.classes_[proba.argmax(axis=1)]
todo["把握"] = proba.max(axis=1).round(2)

THRESHOLD = 0.6                                           # 把握 ≥ 0.6 的直接采用
sure = todo[todo["把握"] >= THRESHOLD]
unsure = todo[todo["把握"] < THRESHOLD]
print(f"预标注整体准确率：{(todo['预标注'] == todo['情感_参考']).mean():.0%}")
print(f"把握 ≥ {THRESHOLD}：{len(sure)} 条，准确率 {(sure['预标注'] == sure['情感_参考']).mean():.1%}")
print(f"把握 < {THRESHOLD}：{len(unsure)} 条，准确率 {(unsure['预标注'] == unsure['情感_参考']).mean():.1%}，交给人工")
print(unsure.sort_values("把握")[["text", "预标注", "把握", "情感_参考"]].head(6).to_string(index=False))

# 估算工作量：人工从头标一条约 15 秒，检查一条预标注约 5 秒
manual = len(todo) * 15
assisted = len(sure) * 5 + len(unsure) * 15
print(f"全部人工：{manual / 60:.0f} 分钟；预标注 + 人工：{assisted / 60:.0f} 分钟，节省 {1 - assisted / manual:.0%}")
todo.to_csv(HERE / "预标注结果.csv", index=False, encoding="utf-8-sig")
