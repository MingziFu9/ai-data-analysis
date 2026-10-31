"""第 11 章随书工具函数：读日志、加载情感模型、计算 PSI。实验直接 import 使用，不要求读懂每一行"""
from pathlib import Path
import numpy as np
import pandas as pd
import joblib

DATA = Path(__file__).resolve().parents[1] / "data"
MODEL = Path(__file__).resolve().parents[1] / "ch09" / "sentiment_model.joblib"


def load_log():
    """读取情感分析服务的运行日志（JSON Lines：每行一条 JSON），并加上“第几周”列"""
    log = pd.read_json(DATA / "service_log.jsonl", lines=True)
    log["time"] = pd.to_datetime(log["time"])
    log["周"] = (log["time"] - pd.Timestamp("2026-03-02")).dt.days // 7 + 1
    return log


def load_model():
    """读取第 9 章保存的情感模型；如果还没有，就按实验 9-1 的方法现训练一个"""
    if MODEL.exists():
        return joblib.load(MODEL)
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    train = pd.read_csv(DATA / "annotation" / "batch_2000.csv")
    clf = Pipeline([("tfidf", TfidfVectorizer(analyzer="char", ngram_range=(1, 2))),
                    ("model", LogisticRegression(max_iter=1000, class_weight="balanced"))])
    return clf.fit(train["评论内容"], train["情感标签"])


def psi(expected, actual, bins=10):
    """群体稳定性指标 PSI：比较“上线前（expected）”和“上线后（actual）”两组数的分布差多少。
    经验标准：< 0.1 稳定；0.1～0.25 有变化，需关注；> 0.25 变化显著，需排查"""
    edges = np.unique(np.quantile(expected, np.linspace(0, 1, bins + 1)))  # 按上线前的十分位切箱
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected)                     # 每箱占比
    a = np.histogram(actual, edges)[0] / len(actual)
    e, a = np.clip(e, 1e-4, None), np.clip(a, 1e-4, None)                    # 避免出现 0
    return float(np.sum((a - e) * np.log(a / e)))
