"""实验 11-3：收集坏案例并归因，补标后重新训练，比较效果"""
from pathlib import Path
import pandas as pd
from sklearn.base import clone
from monitor_tools import load_model, DATA

HERE = Path(__file__).resolve().parent
clf = load_model()
online = pd.read_csv(DATA / "reviews_online.csv")           # 上线后的 6000 条评论，已抽检得到参考答案
online["预测"] = clf.predict(online["评论内容"])
online["新说法"] = online["评论内容"].str.contains("预制菜|绝绝子|拔草|yyds|冤种")

# ---------- 1. 坏案例：模型判错的评论，随机抽 100 条，先按规则“预归因”，再由人逐条确认 ----------
bad = online[online["预测"] != online["情感_参考"]]
print(f"上线后 6000 条中判错 {len(bad)} 条，错误率 {len(bad) / len(online):.1%}")
sample = bad.sample(100, random_state=2026).copy()
sample["预归因"] = "模型问题：好坏都有，没看结尾表态"                  # 默认
sample.loc[sample["评论内容"].str.len() <= 8, "预归因"] = "模型问题：评论太短"
sample.loc[sample["新说法"], "预归因"] = "业务变化：出现新说法"
sample["人工确认归因"] = ""                                          # 留给你逐条填写
sample["备注"] = ""
sample[["review_id", "评论内容", "情感_参考", "预测", "预归因", "人工确认归因", "备注"]].to_csv(
    HERE / "坏案例归因表.csv", index=False, encoding="utf-8-sig")
print(sample["预归因"].value_counts())

# ---------- 2. 数据闭环：从上线后的评论中抽 1000 条补标，加入训练集重新训练 ----------
add = online.sample(1000, random_state=2026)                  # 补标的 1000 条（参考答案作为补标结果）
hold = online.drop(add.index)                                 # 其余 5000 条留作验证，不参与训练
old_train = pd.read_csv(DATA / "annotation" / "batch_2000.csv")
new_clf = clone(clf).fit(pd.concat([old_train["评论内容"], add["评论内容"]]),
                         pd.concat([old_train["情感标签"], add["情感_参考"]]))

# ---------- 3. 新旧模型在同一批验证数据上比较 ----------
rows = []
for name, m in [("旧模型", clf), ("补标重训后", new_clf)]:
    ok = m.predict(hold["评论内容"]) == hold["情感_参考"]
    rows.append({"模型": name, "整体准确率": ok.mean(),
                 "含新说法": ok[hold["新说法"]].mean(), "不含新说法": ok[~hold["新说法"]].mean()})
print(pd.DataFrame(rows).set_index("模型").round(3))
