# 第 11 章 智能系统运维与优化：实验代码

| 文件 | 用途 | 运行方式 |
|---|---|---|
| monitor_tools.py | 随书工具函数：读日志 `load_log()`、加载情感模型 `load_model()`、计算 PSI `psi()` | 被实验程序 import，不单独运行 |
| lab11_1_log_monitor.py | 实验 11-1 按周统计调用量、延迟、错误率、预测分布，告警，画监控看板 | `python labs/ch11/lab11_1_log_monitor.py` |
| lab11_2_drift.py | 实验 11-2 PSI、找新说法、抽检准确率对比 | `python labs/ch11/lab11_2_drift.py` |
| lab11_3_badcase_retrain.py | 实验 11-3 坏案例预归因表、补标重训、新旧模型比较 | `python labs/ch11/lab11_3_badcase_retrain.py` |
| lab11_1_monitor.png | 监控看板参考图 | — |

数据：`labs/data/service_log.jsonl`（情感服务 8 周的调用日志）、`reviews_online.csv`（上线后 6000 条评论及抽检参考答案）。
情感模型优先读取第 9 章保存的 `labs/ch09/sentiment_model.joblib`；没有的话 `load_model()` 会按实验 9-1 的方法自动训练一个，结果相同。
