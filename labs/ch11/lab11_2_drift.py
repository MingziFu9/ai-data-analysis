"""实验 11-2：检测数据漂移——上线后的评论和上线前还一样吗？"""
import re
from collections import Counter
import pandas as pd
from monitor_tools import load_log, load_model, psi, DATA

log = load_log()
clf = load_model()
proba = clf.predict_proba(log["text"])
log["把握"] = proba.max(axis=1)
log["负面概率"] = proba[:, list(clf.classes_).index("负面")]
log["长度"] = log["text"].str.len()
base = log[log["周"] <= 4]                     # 前 4 周作为“正常时期”的基准

# ---------- 1. 每周和基准比较 PSI ----------
rows = []
for w, cur in log.groupby("周"):
    rows.append({"周": w, "评论长度 PSI": psi(base["长度"], cur["长度"]),
                 "模型把握 PSI": psi(base["把握"], cur["把握"]),
                 "负面概率 PSI": psi(base["负面概率"], cur["负面概率"])})
print(pd.DataFrame(rows).set_index("周").round(3))
print("评论平均长度：前 4 周", round(base["长度"].mean(), 1), "，后 4 周", round(log[log["周"] >= 5]["长度"].mean(), 1))


# ---------- 2. 找新说法：后 4 周常见、前 4 周从没出现过的两字组合 ----------
def two_chars(texts):
    """统计每个“相邻两字”出现在多少条评论里"""
    c = Counter()
    for t in texts:
        t = re.sub(r"[^一-龥a-zA-Z]", "", t)            # 只留汉字和字母
        c.update({t[i:i + 2] for i in range(len(t) - 1)})
    return c


before, after = two_chars(base["text"]), two_chars(log[log["周"] >= 5]["text"])
new = {w: n for w, n in after.items() if n >= 30 and before[w] == 0}
print("新出现的说法（出现条数）：", dict(sorted(new.items(), key=lambda x: -x[1])[:14]))

# ---------- 3. 质检员抽检：上线后的评论有参考答案，看模型在新说法上准不准 ----------
online = pd.read_csv(DATA / "reviews_online.csv")
online["预测"] = clf.predict(online["评论内容"])
online["新说法"] = online["评论内容"].str.contains("预制菜|绝绝子|拔草|yyds|冤种")
online["判对"] = online["预测"] == online["情感_参考"]
print(online.groupby("新说法")["判对"].agg(条数="size", 准确率="mean").round(3))
wrong = online[~online["判对"] & online["新说法"]]
print(pd.crosstab(wrong["情感_参考"], wrong["预测"]))
print(wrong[["评论内容", "情感_参考", "预测"]].head(6).to_string(index=False))
