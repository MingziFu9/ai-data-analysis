# 第 9 章 建模应用：实验代码

| 文件 | 用途 | 运行方式 |
|---|---|---|
| lab9_1_regression.py | 实验 9-1 送达时长预测（线性回归、随机森林、残差图） | `python labs/ch09/lab9_1_regression.py` |
| lab9_1_sentiment.py | 实验 9-1 评论情感分类（TF-IDF + 逻辑回归），保存模型 `sentiment_model.joblib` 和 `错误案例.csv` | `python labs/ch09/lab9_1_sentiment.py` |
| lab9_2_rfm.py | 实验 9-2 RFM 计算、规则分群、K 均值聚类 | `python labs/ch09/lab9_2_rfm.py` |
| lab9_3_prelabel.py | 实验 9-3 用自己训练的模型预标注（需先运行 lab9_1_sentiment.py） | `python labs/ch09/lab9_3_prelabel.py` |
| lab9_3_llm_prelabel.py | 实验 9-3 调用大模型 API 预标注（待实测，需要 API 密钥） | 见文件开头说明；不加 `--run` 只打印提示词 |
| lab9_3_pretrained.py | 实验 9-3 用预训练中文情感模型预标注（待实测，需要 transformers、torch） | `python labs/ch09/lab9_3_pretrained.py` |
| lab9_1_residual.png、lab9_2_rfm.png | 参考图 | — |

第 11 章会用到本章保存的 `sentiment_model.joblib`。
