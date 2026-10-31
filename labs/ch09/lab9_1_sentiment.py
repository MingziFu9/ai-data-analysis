"""实验 9-1 第 2 部分：用标注好的评论训练情感分类模型（TF-IDF + 逻辑回归）"""
from pathlib import Path
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

DATA = Path(__file__).resolve().parents[1] / "data"
LABELS = ["正面", "中性", "负面"]

# ---------- 1. 训练集：第 6 章审核过的 2000 条标注（标注员给的标签，里面有少量标错的） ----------
train = pd.read_csv(DATA / "annotation" / "batch_2000.csv")
print("训练集", len(train), "条：", train["情感标签"].value_counts().to_dict())

# ---------- 2. 测试集：从没参加标注的评论中随机抽 2000 条，用参考答案评估 ----------
reviews = pd.read_csv(DATA / "reviews.csv").merge(pd.read_csv(DATA / "reviews_参考答案.csv"), on="review_id")
rest = reviews[~reviews["review_id"].isin(train["review_id"])]
test = rest.sample(2000, random_state=2026)

# ---------- 3. 流水线：把文字变成数字（TF-IDF）→ 逻辑回归分类 ----------
clf = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char", ngram_range=(1, 2))),   # 按单字和相邻两字切分
    ("model", LogisticRegression(max_iter=1000, class_weight="balanced")),
])
clf.fit(train["评论内容"], train["情感标签"])
pred = clf.predict(test["评论内容"])

# ---------- 4. 测试报告：准确率、各类别的精确率和召回率、混淆矩阵 ----------
print(f"测试集准确率：{accuracy_score(test['情感_参考'], pred):.3f}")
print(classification_report(test["情感_参考"], pred, labels=LABELS, digits=3))
cm = pd.DataFrame(confusion_matrix(test["情感_参考"], pred, labels=LABELS),
                  index=["真实" + l for l in LABELS], columns=["预测" + l for l in LABELS])
print(cm)

# ---------- 5. 错误案例：模型判错的评论 ----------
test = test.assign(预测=pred)
wrong = test[test["预测"] != test["情感_参考"]]
print("判错", len(wrong), "条，举例：")
print(wrong[["评论内容", "情感_参考", "预测"]].head(8).to_string(index=False))
wrong[["review_id", "评论内容", "情感_参考", "预测"]].to_csv(
    Path(__file__).with_name("错误案例.csv"), index=False, encoding="utf-8-sig")

# ---------- 6. 保存模型，第 9-3 和第 11 章还要用 ----------
joblib.dump(clf, Path(__file__).with_name("sentiment_model.joblib"))
print("模型已保存为 sentiment_model.joblib")
