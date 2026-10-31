"""实验 11-1：分析情感分析服务 8 周的运行日志，做一个监控看板"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from monitor_tools import load_log, load_model

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

# ---------- 1. 读日志，看看一条记录长什么样 ----------
log = load_log()
print("共", len(log), "条调用记录，时间从", log["time"].min(), "到", log["time"].max())
print(log.iloc[0].to_dict())

# ---------- 2. 系统指标：每周调用量、平均延迟、P95 延迟、错误率 ----------
week = log.groupby("周").agg(
    调用量=("request_id", "count"),
    平均延迟=("latency_ms", "mean"),
    P95延迟=("latency_ms", lambda s: s.quantile(0.95)),     # 95% 的请求比它快
    错误率=("status", lambda s: (s != 200).mean()),          # 状态码不是 200 的比例
)

# ---------- 3. 模型指标：每周预测为“负面”的比例、模型把握小于 0.6 的比例 ----------
clf = load_model()
proba = clf.predict_proba(log["text"])
log["预测"] = clf.classes_[proba.argmax(axis=1)]
log["把握"] = proba.max(axis=1)
week["负面占比"] = log.groupby("周")["预测"].apply(lambda s: (s == "负面").mean())
week["低把握占比"] = log.groupby("周")["把握"].apply(lambda s: (s < 0.6).mean())
print(week.round(3))

# ---------- 4. 告警规则：超过阈值就报警 ----------
RULES = {"P95延迟": 150, "错误率": 0.01, "负面占比": 0.25}
for col, limit in RULES.items():
    bad = week[week[col] > limit]
    for w, v in bad[col].items():
        print(f"【告警】第 {w} 周 {col} = {v:.3f}，超过阈值 {limit}")

# ---------- 5. 监控看板：四个指标的周趋势，红色虚线是告警阈值 ----------
fig, ax = plt.subplots(2, 2, figsize=(11, 6))
for a, col, title in [(ax[0, 0], "调用量", "调用量（次 / 周）"), (ax[0, 1], "P95延迟", "P95 延迟（毫秒）"),
                      (ax[1, 0], "错误率", "错误率"), (ax[1, 1], "负面占比", "预测为负面的比例")]:
    a.plot(week.index, week[col], marker="o")
    a.set_ylim(0, week[col].max() * 1.3)
    if col in RULES:
        a.axhline(RULES[col], color="red", linestyle="--", label="告警阈值")
        a.legend()
    a.set_title(title)
    a.set_xticks(week.index)
    a.set_xlabel("第几周（2026-03-02 起）")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("lab11_1_monitor.png"), dpi=110)

# ---------- 6. 找出出错的请求：哪种错误、集中在哪几周 ----------
err = log[log["status"] != 200]
print("出错请求按状态码：", err["status"].value_counts().to_dict())
print(pd.crosstab(err["周"], err["status"]))
