---
title: 在线模拟卷
description: 按期末开卷考试的题型和分值，从各章课后练习中组成的两套在线模拟卷，可以直接作答并查看解析
---

# 在线模拟卷

本课程期末为开卷考试，题目侧重理解和应用。下面两套模拟卷按期末考试的题型和分值，从各章课后练习中抽题组成，覆盖全书 12 章：

| 题型 | 题数 | 每题分值 | 合计 |
|---|---|---|---|
| 单项选择题 | 20 | 2 | 40 |
| 多项选择题 | 5 | 4 | 20 |
| 判断题 | 10 | 1 | 10 |
| 简答题 | 2 | 10 | 20 |
| 实操题 | 1 | 10 | 10 |

建议限时 90 分钟，先独立做完一整套，再展开“答案与解析”核对。简答题和实操题按参考答案的要点自评。实操题要在电脑上运行代码完成。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。

## 模拟卷一

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="C" markdown>

**1.** 给几千条评论逐条标上“好评”“中评”“差评”，这项工作属于（　　）。

- A. 数据采集
- B. 数据清洗
- C. 数据标注
- D. 数据可视化

</div>

??? tip "答案与解析"
    **答案：C**

    按照规范给数据加上标签，供模型学习，就是数据标注。采集是把数据收集来，清洗是把错漏去掉，可视化是画图展示。

    考查：数据的旅程 · 认知层次：理解 · [回看 1.1.1](chapters/01-overview/index.md#111)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**2.** `districts = ["天河", "越秀", "海珠"]`，`districts[1]` 的值是（　　）。

- A. 天河
- B. 越秀
- C. 海珠
- D. 报错

</div>

??? tip "答案与解析"
    **答案：B**

    Python 从 0 开始数，`[0]` 是天河，`[1]` 是越秀。

    考查：列表 · 认知层次：应用 · [回看 2.1.1](chapters/02-pandas/index.md#211)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**3.** 用 `pd.read_csv` 读一个文件时报 `UnicodeDecodeError`，最可能的原因是（　　）。

- A. 文件不存在
- B. 文件中有空值
- C. 文件的编码不是 UTF-8
- D. 文件太大

</div>

??? tip "答案与解析"
    **答案：C**

    `read_csv` 默认按 UTF-8 解码，文件是 GBK 等其他编码时就会报 `UnicodeDecodeError`，加 `encoding="gbk"` 即可。文件不存在报的是 `FileNotFoundError`。

    考查：文件编码 · 认知层次：理解 · [回看 3.2.1](chapters/03-collection/index.md#321-csv)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**4.** 订单表中同一城区有的写“天河”、有的写“天河区”，这属于数据质量的（　　）问题。

- A. 完整性
- B. 一致性
- C. 唯一性
- D. 及时性

</div>

??? tip "答案与解析"
    **答案：B**

    同一个意思有不同写法，是一致性问题。完整性是“缺没缺”，唯一性是“有没有重复”，及时性是“新不新”。

    考查：数据质量维度 · 认知层次：理解 · [回看 4.1.1](chapters/04-cleaning/index.md#411)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**5.** 给评论打上“正面、负面、中性”标签，属于哪类标注任务？（　　）

- A. 实体标注
- B. 文本分类
- C. 目标框标注
- D. 语音转写

</div>

??? tip "答案与解析"
    **答案：B**

    给一段文字分配一个类别，是文本分类；情感只能选一个，是单标签分类。

    考查：文本分类 · 认知层次：理解 · [回看 5.2.1](chapters/05-annotation/index.md#521)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**6.** 由专家按规范仔细标注、反复确认，作为“标准答案”的数据叫（　　）。

- A. 预标注
- B. 噪声标签
- C. 金标准
- D. 合成数据

</div>

??? tip "答案与解析"
    **答案：C**

    金标准用来计算标注准确率、考核标注员。

    考查：金标准 · 认知层次：记忆 · [回看 6.1.1](chapters/06-annotation-qa/index.md#611)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**7.** 订单实付金额平均值 133.2 元，中位数 93.6 元。要说明“一般的订单花多少钱”，更合适的是（　　）。

- A. 平均值
- B. 中位数
- C. 最大值
- D. 标准差

</div>

??? tip "答案与解析"
    **答案：B**

    平均值被少数大单拉高；中位数是排在正中间的订单，更能代表一般情况。

    考查：中位数 · 认知层次：应用 · [回看 7.1.1](chapters/07-statistics/index.md#711)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**8.** 想展示“食客说”2025 年每个月交易额的变化，最合适的图表是（　　）。

- A. 饼图
- B. 散点图
- C. 折线图
- D. 箱线图

</div>

??? tip "答案与解析"
    **答案：C**

    随时间的变化（趋势）用折线图，横轴是按顺序排列的月份。

    考查：图表选择 · 认知层次：应用 · [回看 8.1.1](chapters/08-visualization/index.md#811)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**9.** 根据配送距离、天气等信息预测一单外卖要送多少分钟，属于（　　）。

- A. 分类
- B. 回归
- C. 聚类
- D. 标注

</div>

??? tip "答案与解析"
    **答案：B**

    预测的是一个数值，属于回归。

    考查：回归 · 认知层次：理解 · [回看 9.1.1](chapters/09-modeling/index.md#911)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**10.** 用户—物品矩阵中，填了 1 的格子只占 2.8%，这种情况叫（　　）。

- A. 过拟合
- B. 冷启动
- C. 稀疏
- D. 信息茧房

</div>

??? tip "答案与解析"
    **答案：C**

    每个用户只和很少的物品有过行为，矩阵中绝大多数格子是 0。

    考查：稀疏 · 认知层次：记忆 · [回看 10.1.1](chapters/10-recommendation/index.md#1011)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**11.** 新评论一提交就要马上判断情感并推送给客服，适合的上线方式是（　　）。

- A. 批量预测
- B. 在线服务
- C. 离线评估
- D. 灰度发布

</div>

??? tip "答案与解析"
    **答案：B**

    要求实时响应的场景用在线服务。

    考查：在线服务 · 认知层次：应用 · [回看 11.1.1](chapters/11-operations/index.md#1111)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**12.** 《中华人民共和国个人信息保护法》的施行时间是（　　）。

- A. 2017 年 6 月 1 日
- B. 2021 年 9 月 1 日
- C. 2021 年 11 月 1 日
- D. 2025 年 1 月 1 日

</div>

??? tip "答案与解析"
    **答案：C**

    A 是网络安全法，B 是数据安全法，D 是网络数据安全管理条例。

    考查：个人信息保护法 · 认知层次：记忆 · [回看 12.2.1](chapters/12-ethics-project/index.md#1221)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**13.** “垃圾进，垃圾出”这句话主要说明（　　）。

- A. 数据量越大越好
- B. 数据质量差，模型也学不好
- C. 不需要的数据要及时删除
- D. 模型越复杂效果越好

</div>

??? tip "答案与解析"
    **答案：B**

    输入的数据有错漏，再好的算法也得不到好结果，所以说数据决定模型的上限。A 不全面，数据量大但质量差同样不行。

    考查：数据决定模型上限 · 认知层次：理解 · [回看 1.1.2](chapters/01-overview/index.md#112)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**14.** pandas 中，相当于 Excel 一个工作表的对象是（　　）。

- A. Series
- B. 索引
- C. DataFrame
- D. NumPy 数组

</div>

??? tip "答案与解析"
    **答案：C**

    DataFrame 是二维表；Series 是其中的一列；索引相当于行号。

    考查：DataFrame · 认知层次：记忆 · [回看 2.2.1](chapters/02-pandas/index.md#221-dataframe)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**15.** 保存一个 CSV 文件，要让同事用 Excel 双击打开时中文不乱码，`encoding` 参数最好写（　　）。

- A. `"utf-8"`
- B. `"utf-8-sig"`
- C. `"ascii"`
- D. 不写

</div>

??? tip "答案与解析"
    **答案：B**

    `utf-8-sig` 会在文件开头写一个标记（BOM），Excel 看到它就知道这是 UTF-8 编码。只写 `utf-8` 时，Excel 常常按 GBK 打开，中文变成乱码。

    考查：文件编码 · 认知层次：应用 · [回看 3.2.1](chapters/03-collection/index.md#321-csv)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**16.** 统计每一列有多少个空值，应该写（　　）。

- A. `df.duplicated().sum()`
- B. `df.dropna()`
- C. `df.isna().sum()`
- D. `df.fillna(0)`

</div>

??? tip "答案与解析"
    **答案：C**

    `isna()` 判断每个格子是否为空，`sum()` 按列统计 `True` 的个数。A 是统计重复行，B 是删除含空值的行，D 是把空值填成 0。

    考查：缺失值 · 认知层次：应用 · [回看 4.3.1](chapters/04-cleaning/index.md#431)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**17.** 对“毛肚鸭肠”两个菜品做 BIO 标注，正确的结果是（　　）。

- A. B-菜品 I-菜品 I-菜品 I-菜品
- B. I-菜品 I-菜品 I-菜品 I-菜品
- C. B-菜品 I-菜品 B-菜品 I-菜品
- D. B-菜品 B-菜品 B-菜品 B-菜品

</div>

??? tip "答案与解析"
    **答案：C**

    两个实体各自的第一个字标 B，其余字标 I。A 会被理解成一个四个字的菜品。

    考查：BIO 标注 · 认知层次：应用 · [回看 5.2.2](chapters/05-annotation/index.md#522-bio)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**18.** 两名标注员的实际一致率为 80%，碰巧一致率为 50%，Kappa 为（　　）。

- A. 0.3
- B. 0.6
- C. 0.8
- D. 1.6

</div>

??? tip "答案与解析"
    **答案：B**

    Kappa =（0.8 − 0.5）÷（1 − 0.5）= 0.3 ÷ 0.5 = 0.6。

    考查：Kappa 系数 · 认知层次：应用 · [回看 6.1.2](chapters/06-annotation-qa/index.md#612-kappa)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**19.** “90% 的订单在 41 分钟内送达”中的 41 分钟是送达时长的（　　）。

- A. 平均值
- B. 标准差
- C. 90% 分位数
- D. 众数

</div>

??? tip "答案与解析"
    **答案：C**

    90% 分位数表示有 90% 的数据比它小。

    考查：分位数 · 认知层次：理解 · [回看 7.1.2](chapters/07-statistics/index.md#712)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**20.** 想看“配送距离”和“送达时长”两个数值变量之间有没有关系，应该用（　　）。

- A. 饼图
- B. 散点图
- C. 堆叠柱状图
- D. 直方图

</div>

??? tip "答案与解析"
    **答案：B**

    两个数值变量的关系用散点图，每个点是一笔订单。

    考查：散点图 · 认知层次：应用 · [回看 8.1.1](chapters/08-visualization/index.md#811)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**1.** 人工智能训练师（四级）的职业功能包括（　　）。

- A. 数据采集和处理
- B. 数据标注
- C. 算法原理推导
- D. 智能系统运维

</div>

??? tip "答案与解析"
    **答案：ABD**

    四级的三个职业功能是数据采集和处理、数据标注、智能系统运维。算法原理推导不是训练师的职业功能。

    考查：人工智能训练师四级 · 认知层次：记忆 · [回看 1.4.1](chapters/01-overview/index.md#141)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**2.** 下列关于 Parquet 和 CSV 的说法，正确的有（　　）。

- A. Parquet 文件会记录每列的数据类型
- B. 同样的数据，Parquet 文件通常比 CSV 小
- C. Parquet 文件可以用记事本直接查看
- D. CSV 是纯文本文件，通用性好

</div>

??? tip "答案与解析"
    **答案：ABD**

    Parquet 按列存储、带类型、自动压缩，本书的订单表从 4.4 MB 降到 1.4 MB；但它是二进制文件，不能用记事本或 Excel 直接查看。

    考查：Parquet · 认知层次：理解 · [回看 3.2.4](chapters/03-collection/index.md#324-parquet)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**3.** 一份完整的标注规范通常包括（　　）。

- A. 标签定义和正反例
- B. 边界规则和疑难样例
- C. 标注员的个人信息
- D. 版本记录

</div>

??? tip "答案与解析"
    **答案：ABD**

    此外还有任务说明和质量要求。标注员的个人信息与规范无关。

    考查：标注规范 · 认知层次：记忆 · [回看 5.4.1](chapters/05-annotation/index.md#541)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**4.** 下列可能造成“相关但不是因果”的原因有（　　）。

- A. 存在同时影响两者的第三个因素
- B. 因果方向弄反了
- C. 做了随机对照试验
- D. 纯属巧合

</div>

??? tip "答案与解析"
    **答案：ABD**

    随机对照试验恰恰是确认因果的方法。

    考查：相关不等于因果 · 认知层次：理解 · [回看 7.3.2](chapters/07-statistics/index.md#732)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**5.** 关于 scikit-learn 的流水线（Pipeline），下列说法正确的有（　　）。

- A. 可以把标准化和模型串成一个整体
- B. 一次 `fit` 就能依次完成预处理和训练
- C. 用了流水线就不需要划分测试集
- D. 能避免预处理时用到测试集信息造成的数据泄露

</div>

??? tip "答案与解析"
    **答案：ABD**

    流水线仍然要用测试集来评估。

    考查：流水线 · 认知层次：理解 · [回看 9.2](chapters/09-modeling/index.md#92-scikit-learn)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** 数据标注员是与人工智能训练师并列的另一个独立职业。

</div>

??? tip "答案与解析"
    **答案：×**

    数据标注员是人工智能训练师职业下面的工种之一，另一个工种是人工智能算法测试员。

    考查：人工智能训练师 · 认知层次：记忆 · [回看 1.4.1](chapters/01-overview/index.md#141)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** pandas 中筛选条件的“并且”可以写成 `and`。

</div>

??? tip "答案与解析"
    **答案：×**

    对整列做判断时要用 `&`（并且）和 `|`（或者），用 `and`、`or` 会报 `The truth value of a Series is ambiguous` 错误。

    考查：条件筛选 · 认知层次：记忆 · [回看 2.3.2](chapters/02-pandas/index.md#232)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**3.** 同一个汉字，用 UTF-8 和 GBK 编码保存的字节是一样的。

</div>

??? tip "答案与解析"
    **答案：×**

    “食客说”三个字，UTF-8 是 9 个字节，GBK 是 6 个字节，内容完全不同。用错编码去读就会乱码。

    考查：文件编码 · 认知层次：理解 · [回看 3.2.1](chapters/03-collection/index.md#321-csv)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** 用 3σ 法则找出的异常值都是录入错误，应该删除。

</div>

??? tip "答案与解析"
    **答案：×**

    统计方法找出的只是“可疑值”。本章的例子中，大部分“异常”订单是多人聚餐的真实大单，应该保留。

    考查：异常值 · 认知层次：评价 · [回看 4.4.2](chapters/04-cleaning/index.md#442)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**5.** 有了大模型，人工数据标注就不再需要了。

</div>

??? tip "答案与解析"
    **答案：×**

    大模型训练同样需要人工编写的指令数据和人工排序的偏好数据，而且要求更高；预标注后也需要人工审核。

    考查：数据标注 · 认知层次：理解 · [回看 5.1.2](chapters/05-annotation/index.md#512)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**6.** 两名标注员的一致率高，就说明他们的标注质量高。

</div>

??? tip "答案与解析"
    **答案：×**

    一致率包含碰巧一致的部分；两人也可能一致地标错。要结合 Kappa 和金标准准确率来判断。

    考查：一致率 · 认知层次：理解 · [回看 6.1.2](chapters/06-annotation-qa/index.md#612-kappa)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**7.** p 值小于 0.001，说明两组的差别很大。

</div>

??? tip "答案与解析"
    **答案：×**

    p 值小只说明差别很可能是真的，不说明差别大。数据量很大时，很小的差别也会显著。

    考查：p 值 · 认知层次：评价 · [回看 7.5.4](chapters/07-statistics/index.md#754)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**8.** 条形图和柱状图的数值轴必须从 0 开始。

</div>

??? tip "答案与解析"
    **答案：√**

    读者用长度比较大小，不从 0 开始就会放大差别。

    考查：截断纵轴 · 认知层次：理解 · [回看 8.4.1](chapters/08-visualization/index.md#841)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**9.** 模型越复杂，预测效果一定越好。

</div>

??? tip "答案与解析"
    **答案：×**

    送达时长预测中，随机森林的误差反而比线性回归略大。

    考查：模型选择 · 认知层次：理解 · [回看 9.3.2](chapters/09-modeling/index.md#932)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**10.** 协同过滤不需要知道物品的菜系、标签等内容信息。

</div>

??? tip "答案与解析"
    **答案：√**

    协同过滤只看“谁和谁一起去过”。

    考查：协同过滤 · 认知层次：理解 · [回看 10.3.1](chapters/10-recommendation/index.md#1031)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 为什么说 Kappa 系数比一致率更能反映标注的一致性？

??? tip "答案与解析"
    **参考答案**：一致率没有考虑碰巧一致。即使两人随便标，也会有一部分碰巧相同，尤其是某个标签占比很大时，碰巧一致率会很高。Kappa 先算出碰巧一致率，再看实际一致率超出它多少，用（实际一致率 − 碰巧一致率）÷（1 − 碰巧一致率）计算，扣除了碰巧的部分，只反映“真正的一致”。例如两人几乎都标正面，一致率 88%，Kappa 却接近 0。

    考查：Kappa 系数 · 认知层次：理解 · [回看 6.1.2](chapters/06-annotation-qa/index.md#612-kappa)
    { .quiz-meta }

**2.** 回答情景导入中运营经理的问题：模型是不是坏了？要不要重新训练？请用本章的数据说明。

??? tip "答案与解析"
    **参考答案**：模型本身没坏，问题有两个来源。一是系统问题：第 7 周起 P95 延迟从约 93 毫秒升到 161 毫秒，错误率从 0.3% 升到 2.4%，调用量没有明显增加，应由技术组排查服务器，这和模型无关，重新训练也解决不了。二是数据漂移：第 5 周起约 30% 的评论出现新说法，评论长度 PSI 超过 0.1，含新说法的评论抽检准确率 93.5%，比其他评论低约 3 个百分点。这部分需要更新标注规范、补标数据重新训练，补标 1000 条后准确率可从 95.5% 提高到 97.4%，再经灰度发布上线。

    考查：综合 · 认知层次：评价 · [回看 11.2.3](chapters/11-operations/index.md#1123)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 在实验 4-2 清洗后的订单表 `orders_clean.csv` 上，用箱线图法找出“送达时长”的异常值，有多少行？它们有什么共同特点？

??? tip "答案与解析"
    **参考答案**：

    ```python
    df = pd.read_csv("orders_clean.csv")
    x = df["送达时长"]
    q1, q3 = x.quantile(0.25), x.quantile(0.75)
    iqr = q3 - q1
    out = df[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)]
    print(len(out))
    print(out[["配送距离", "天气", "配送方式"]].describe(include="all"))
    ```

    共 56 行（Q1 = 22，Q3 = 34，上界 52 分钟）。和全部订单相比，它们的平均配送距离是 7.7 公里（全部为 2.4 公里），雨天占 45%（全部为 22%），商家自送占 61%（全部为 32%）。距离远、下雨、商家自送都会让送达变慢，所以它们是真实的慢单，应保留，并可以作为改进配送的分析对象。空值会被 `quantile` 自动忽略。

    考查：箱线图法 · 认知层次：分析 · [回看 4.4.1](chapters/04-cleaning/index.md#441)
    { .quiz-meta }

## 模拟卷二

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="D" markdown>

**1.** 下列数据中，属于非结构化数据的是（　　）。

- A. 订单表中的实付金额
- B. 商家表中的城区
- C. 开放接口返回的 JSON
- D. 用户上传的菜品照片

</div>

??? tip "答案与解析"
    **答案：D**

    照片没有预先定义的格式，是非结构化数据。A、B 是结构化表格中的列；C 有层次和标记，属于半结构化数据。

    考查：结构化、半结构化、非结构化数据 · 认知层次：理解 · [回看 1.3.1](chapters/01-overview/index.md#131)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**2.** 要看一张表有几行几列，应该用（　　）。

- A. `df.head()`
- B. `df.dtypes`
- C. `df.describe()`
- D. `df.shape`

</div>

??? tip "答案与解析"
    **答案：D**

    `shape` 返回（行数，列数）。`head` 看前几行，`dtypes` 看数据类型，`describe` 做描述统计。

    考查：读表看表 · 认知层次：记忆 · [回看 2.2.2](chapters/02-pandas/index.md#222)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**3.** 一个 Excel 文件有 8 个工作表，要一次全部读出来，应该写（　　）。

- A. `pd.read_excel(文件)`
- B. `pd.read_excel(文件, sheet_name=0)`
- C. `pd.read_excel(文件, header=None)`
- D. `pd.read_excel(文件, sheet_name=None)`

</div>

??? tip "答案与解析"
    **答案：D**

    `sheet_name=None` 读全部工作表，结果是一个“表名 → DataFrame”的字典。不写 `sheet_name` 或写 0 只读第一个工作表；`header=None` 是说明没有表头。

    考查：Excel 多工作表 · 认知层次：应用 · [回看 3.2.2](chapters/03-collection/index.md#322-excel)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**4.** 订单表的“优惠金额”为空，经核实表示该订单没有使用优惠。最合适的处理是（　　）。

- A. 填 0
- B. 填平均值
- C. 删除这些行
- D. 填中位数

</div>

??? tip "答案与解析"
    **答案：A**

    空值有明确含义“没有优惠”，真实值就是 0。填平均值、中位数会凭空捏造优惠，删除会丢掉这些订单。

    考查：缺失值处理 · 认知层次：评价 · [回看 4.3.2](chapters/04-cleaning/index.md#432)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**5.** 下列关于目标框标注的要求，错误的是（　　）。

- A. 两个挨在一起的碗可以用一个大框框住
- B. 框的四条边要紧贴物体最外侧的边缘
- C. 只露出一部分的物体也要框出来
- D. 每个框都要选择正确的类别

</div>

??? tip "答案与解析"
    **答案：A**

    目标框要“一物一框”，挨在一起的物体也要分别画框。

    考查：目标框标注 · 认知层次：理解 · [回看 5.2.3](chapters/05-annotation/index.md#523)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**6.** 两名标注员几乎把所有评论都标成“正面”，一致率高达 88%。对此最合理的判断是（　　）。

- A. 两人标注质量很高
- B. 规范写得很清楚
- C. 应该用一致率代替 Kappa
- D. 一致可能主要是碰巧，应计算 Kappa 判断

</div>

??? tip "答案与解析"
    **答案：D**

    两人都几乎只标一个类别时，碰巧一致率本身就很高，Kappa 可能接近 0 甚至为负。

    考查：Kappa 系数 · 认知层次：分析 · [回看 6.1.2](chapters/06-annotation-qa/index.md#612-kappa)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**7.** 一列数据的偏度为 2.0，直方图左高右低、右边拖着长尾，这种分布叫（　　）。

- A. 右偏分布
- B. 左偏分布
- C. 对称分布
- D. 均匀分布

</div>

??? tip "答案与解析"
    **答案：A**

    偏度大于 0、长尾在右边的是右偏分布，此时平均值大于中位数。

    考查：偏度 · 认知层次：理解 · [回看 7.1.3](chapters/07-statistics/index.md#713)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**8.** 下列情况中，最适合用饼图的是（　　）。

- A. 10 个菜系的订单占比
- B. 12 个月的交易额
- C. 8 个城区的好评率
- D. 平台专送和商家自送的订单占比

</div>

??? tip "答案与解析"
    **答案：D**

    饼图只适合 2～5 类、加起来等于 100% 的构成。10 个菜系太多；交易额是趋势；好评率各城区之间是比较，加起来也不等于 100%。

    考查：饼图 · 认知层次：应用 · [回看 8.4.2](chapters/08-visualization/index.md#842)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**9.** 用“评论的评分”作为特征来预测“评论的情感”，但新评论在预测时还没有评分，这属于（　　）。

- A. 数据泄露
- B. 过拟合
- C. 标准化
- D. 聚类

</div>

??? tip "答案与解析"
    **答案：A**

    用了预测时拿不到的信息，测试成绩会虚高，上线后效果差。

    考查：数据泄露 · 认知层次：应用 · [回看 9.1.2](chapters/09-modeling/index.md#912)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**10.** 甲店的向量是（粤菜、深夜营业、网红店、番禺），乙店是（粤菜、适合聚餐、深夜营业、番禺），它们的余弦相似度是（　　）。

- A. 0.6
- B. 0.75
- C. 0.5
- D. 1

</div>

??? tip "答案与解析"
    **答案：B**

    共同的 1 有 3 个，3 ÷ √(4 × 4) = 0.75。

    考查：余弦相似度 · 认知层次：应用 · [回看 10.2.3](chapters/10-recommendation/index.md#1023)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**11.** P95 延迟为 160 毫秒，含义是（　　）。

- A. 95% 的请求处理时间不超过 160 毫秒
- B. 平均每个请求用 160 毫秒
- C. 有 95 个请求超过了 160 毫秒
- D. 最慢的请求用了 160 毫秒

</div>

??? tip "答案与解析"
    **答案：A**

    P95 是 95% 分位数。

    考查：P95 延迟 · 认知层次：理解 · [回看 11.2.2](chapters/11-operations/index.md#1122)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**12.** 做“按城区统计用户数”的分析，只向数据部门申请城区这一列，体现的是（　　）原则。

- A. 公开透明
- B. 知情同意
- C. 保存期限
- D. 最小必要

</div>

??? tip "答案与解析"
    **答案：D**

    只收集、使用实现目的所必需的最少信息。

    考查：最小必要 · 认知层次：应用 · [回看 12.2.3](chapters/12-ethics-project/index.md#1223)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**13.** 把情感标签设计成“正面、负面、中性、满意”，违反了标签体系的哪项要求？（　　）

- A. 完整
- B. 粒度合适
- C. 有“其他”类
- D. 互斥

</div>

??? tip "答案与解析"
    **答案：D**

    “满意”和“正面”含义重叠，一条评论可能同时符合两个标签，违反了互斥。

    考查：标签体系 · 认知层次：分析 · [回看 5.3](chapters/05-annotation/index.md#53)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**14.** 三名或更多标注员标注同一批数据时，衡量一致性常用（　　）。

- A. Fleiss' Kappa
- B. Cohen's Kappa
- C. 交并比
- D. 准确率

</div>

??? tip "答案与解析"
    **答案：A**

    Cohen's Kappa 用于两人，Fleiss' Kappa 用于多人。

    考查：Fleiss' Kappa · 认知层次：记忆 · [回看 6.1.2](chapters/06-annotation-qa/index.md#612-kappa)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**15.** 配送距离与送达时长的相关系数为 0.66，下列说法正确的是（　　）。

- A. 两者没有关系
- B. 两者负相关
- C. 配送距离每增加 1 公里，送达时长增加 0.66 分钟
- D. 两者中等程度正相关，距离越远送达时长往往越长

</div>

??? tip "答案与解析"
    **答案：D**

    相关系数衡量直线关系的强弱和方向，不表示“增加多少”。

    考查：相关系数 · 认知层次：理解 · [回看 7.3.1](chapters/07-statistics/index.md#731)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**16.** 用 Matplotlib 画图时，中文显示成小方框，应该（　　）。

- A. 设置 `plt.rcParams["font.sans-serif"]` 为系统中有的中文字体
- B. 把数据中的中文改成拼音
- C. 增大图片的分辨率 dpi
- D. 把 `figsize` 调大

</div>

??? tip "答案与解析"
    **答案：A**

    Matplotlib 默认字体没有汉字，要指定中文字体。

    考查：Matplotlib · 认知层次：应用 · [回看 8.2.1](chapters/08-visualization/index.md#821)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**17.** scikit-learn 中，用训练集训练模型的方法是（　　）。

- A. `predict`
- B. `transform`
- C. `score`
- D. `fit`

</div>

??? tip "答案与解析"
    **答案：D**

    `fit` 训练，`predict` 预测。

    考查：scikit-learn · 认知层次：记忆 · [回看 9.2](chapters/09-modeling/index.md#92-scikit-learn)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**18.** 上题两家店的杰卡德相似度是（　　）。

- A. 0.6
- B. 0.75
- C. 0.5
- D. 1

</div>

??? tip "答案与解析"
    **答案：A**

    交集 3 个，并集 5 个，3 ÷ 5 = 0.6。

    考查：杰卡德相似度 · 认知层次：应用 · [回看 10.2.3](chapters/10-recommendation/index.md#1023)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**19.** 下列属于业务指标的是（　　）。

- A. 错误率
- B. P95 延迟
- C. 预测为负面的比例
- D. 客服处理差评的平均时长

</div>

??? tip "答案与解析"
    **答案：D**

    A、B 是系统指标，C 是模型指标。

    考查：监控指标 · 认知层次：理解 · [回看 11.2.2](chapters/11-operations/index.md#1122)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**20.** 把手机号 13051490103 处理成 130****0103，使用的脱敏方法是（　　）。

- A. 掩码
- B. 哈希
- C. 泛化
- D. 扰动

</div>

??? tip "答案与解析"
    **答案：A**

    用 * 遮住一部分是掩码。

    考查：掩码 · 认知层次：理解 · [回看 12.4.1](chapters/12-ethics-project/index.md#1241)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="AD" markdown>

**1.** 左表有 S1、S2、S3，右表有 S1、S2、S4，下列连接方式中，结果包含 S3 的有（　　）。

- A. left
- B. inner
- C. right
- D. outer

</div>

??? tip "答案与解析"
    **答案：AD**

    S3 只在左表中。left 保留左表全部，outer 保留两边全部；inner 只留两边都有的，right 保留右表全部。

    考查：连接方式 · 认知层次：应用 · [回看 2.5.2](chapters/02-pandas/index.md#252)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ACD" markdown>

**2.** 关于缺失值的处理，下列说法正确的有（　　）。

- A. 处理前要先弄清楚为什么缺
- B. 填平均值不会改变数据的分布
- C. 能从其他表查回真实值的，优先查回
- D. 填充的值最好加一列标记

</div>

??? tip "答案与解析"
    **答案：ACD**

    填平均值会让很多值堆在同一个位置，分布变“尖”，标准差变小，B 错误。

    考查：缺失值处理 · 认知层次：理解 · [回看 4.3.2](chapters/04-cleaning/index.md#432)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**3.** 标注审核报告通常包括（　　）。

- A. 抽检方案与抽检结果
- B. 错误类型分布和典型错误样例
- C. 返工范围和规范修订建议
- D. 标注员的身份证号

</div>

??? tip "答案与解析"
    **答案：ABC**

    此外还有基本情况和附件。标注员的个人信息不应写进报告。

    考查：标注审核报告 · 认知层次：理解 · [回看 6.3.2](chapters/06-annotation-qa/index.md#632)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**4.** 解决新用户冷启动的办法有（　　）。

- A. 推荐热门
- B. 按注册时填写的信息推荐同类人群的热门
- C. 注册时让用户选择感兴趣的类别
- D. 用基于用户的协同过滤

</div>

??? tip "答案与解析"
    **答案：ABC**

    新用户没有行为数据，协同过滤用不上。

    考查：冷启动 · 认知层次：应用 · [回看 10.5.2](chapters/10-recommendation/index.md#1052)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**5.** 情景导入中，合作方要求提供用户的姓名、手机号和消费金额。下列做法正确的有（　　）。

- A. 先确认用户是否同意向第三方提供个人信息
- B. 评估是否可以只提供汇总统计结果，而不是用户名单
- C. 只要对方是正规公司，直接导出 Excel 发过去
- D. 考虑用隐私计算的方法，在不交出名单的情况下完成合作

</div>

??? tip "答案与解析"
    **答案：ABD**

    向他人提供个人信息，要告知接收方的情况并取得个人的单独同意。

    考查：知情同意 · 认知层次：评价 · [回看 12.2.3](chapters/12-ethics-project/index.md#1223)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="√" markdown>

**1.** 从数据库取数时，应该尽量让数据库先筛选和汇总，只把需要的结果取回来。

</div>

??? tip "答案与解析"
    **答案：√**

    真实业务表可能有上亿行，全部读到本机既放不下也传不动。用 `WHERE`、`GROUP BY` 在数据库里先处理，只取回需要的部分。

    考查：SQL · 认知层次：理解 · [回看 3.3.2](chapters/03-collection/index.md#332-select-where)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**2.** `drop_duplicates()` 不加参数时，删除的是所有列都相同的重复行。

</div>

??? tip "答案与解析"
    **答案：√**

    不加参数时比较全部列；要按主键去重，写 `drop_duplicates("order_id")`。

    考查：重复值 · 认知层次：记忆 · [回看 4.2](chapters/04-cleaning/index.md#42)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**3.** 标签体系中设置“其他”类时，也要写明它的定义，并定期检查其中的数据。

</div>

??? tip "答案与解析"
    **答案：√**

    否则“其他”容易变成拿不准就往里扔的“垃圾桶”。某类数据在“其他”中多起来时，应考虑增加新标签。

    考查：标签体系 · 认知层次：理解 · [回看 5.3](chapters/05-annotation/index.md#53)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**4.** 抽检条数越多，验收的两种误判越少，但成本也越高。

</div>

??? tip "答案与解析"
    **答案：√**

    可以在交互动画“抽检验收模拟”中观察到这一点。

    考查：抽检误判 · 认知层次：理解 · [回看 6.2.2](chapters/06-annotation-qa/index.md#622)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**5.** 相关系数接近 0，只能说明两个变量没有直线关系，可能存在曲线关系。

</div>

??? tip "答案与解析"
    **答案：√**

    所以相关分析要配合散点图。

    考查：相关系数 · 认知层次：理解 · [回看 7.3.1](chapters/07-statistics/index.md#731)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**6.** 三维立体饼图比平面饼图更直观，适合在报告中使用。

</div>

??? tip "答案与解析"
    **答案：×**

    三维透视会让近处的扇形看起来更大，扭曲比例。

    考查：饼图 · 认知层次：评价 · [回看 8.4.2](chapters/08-visualization/index.md#842)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**7.** 模型在训练集上表现很好、在测试集上表现差很多，说明可能发生了过拟合。

</div>

??? tip "答案与解析"
    **答案：√**

    过拟合是把训练集的偶然细节也死记了下来。

    考查：过拟合 · 认知层次：理解 · [回看 9.1.2](chapters/09-modeling/index.md#912)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**8.** 矩阵分解中的“隐含口味”需要由分析人员事先定义好，如“爱吃辣”“预算高”。

</div>

??? tip "答案与解析"
    **答案：×**

    隐含口味是算法从矩阵中自动分解出来的，往往没有现成的名字。

    考查：矩阵分解 · 认知层次：理解 · [回看 10.4](chapters/10-recommendation/index.md#104)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**9.** 告警阈值定得太紧，会频繁误报，反而让人忽视告警。

</div>

??? tip "答案与解析"
    **答案：√**

    阈值要参考正常时期的水平来定。

    考查：告警 · 认知层次：理解 · [回看 11.2.3](chapters/11-operations/index.md#1123)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**10.** 给订单金额加入约 ±5% 的随机误差后，全部订单的平均金额几乎不变。

</div>

??? tip "答案与解析"
    **答案：√**

    实验中平均值只从 133.17 变为 133.14。

    考查：扰动 · 认知层次：理解 · [回看 12.4.2](chapters/12-ethics-project/index.md#1242)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 情景导入中，小林的三维饼图和柱状图各有什么问题？应该怎样改？

??? tip "答案与解析"
    **参考答案**：三维饼图放了 10 个菜系，扇形大小相近，人眼很难比较角度和面积，三维透视又会让近处的扇形显得更大；应改成从大到小排序的平面条形图。柱状图纵轴从 60% 开始，把城区之间几个百分点的差别放大成好几倍，误导老板认为黄埔区的服务很差；应让纵轴从 0 开始，并在柱子上标出数值。

    考查：误导性图表 · 认知层次：评价 · [回看 8.4](chapters/08-visualization/index.md#84)
    { .quiz-meta }

**2.** 什么是“最小必要”原则？结合“食客说”举一个违反和一个遵守这条原则的例子。

??? tip "答案与解析"
    **参考答案**：最小必要是指收集个人信息要限于实现处理目的的最小范围，不得过度收集，处理时采取对个人权益影响最小的方式。违反的例子：做“各城区用户数”统计时，从数据库导出了包含姓名、手机号、详细地址的全量用户表。遵守的例子：只导出“常住城区”一列，或者直接在数据库中汇总后只取统计结果。

    考查：最小必要 · 认知层次：应用 · [回看 12.2.3](chapters/12-ethics-project/index.md#1223)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 用 t 检验比较晴天和雨天的送达时长，写出结论。

??? tip "答案与解析"
    **参考答案**：

    ```python
    sunny = orders[orders["天气"] == "晴"]["送达时长"]
    rainy = orders[orders["天气"] == "雨"]["送达时长"]
    t, p = stats.ttest_ind(rainy, sunny, equal_var=False)
    print(round(sunny.mean(), 1), round(rainy.mean(), 1), p)
    ```

    晴天平均约 27.0 分钟，雨天约 32.9 分钟，p < 0.001。结论：雨天的平均送达时长比晴天长约 6 分钟，差异显著。

    考查：t 检验 · 认知层次：应用 · [回看 7.5.2](chapters/07-statistics/index.md#752-t)
    { .quiz-meta }
