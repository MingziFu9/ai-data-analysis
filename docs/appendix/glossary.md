---
title: 附录 D 术语表
description: 本书主要术语的中英文名称、简明定义和例子，按章节顺序排列
---

# 附录 D 术语表

本表按章节顺序列出本书的主要术语，每个术语给出英文名称、简明定义和例子。正文中带虚线下划线的术语，把鼠标停在上面就能看到定义，点击可以跳到本表。

通用术语（如“过拟合”“精确率”）的译名和定义以本系列教材共用的《系列公共术语表》为准，各书保持一致。

## 第 1 章 数据分析与处理概述

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-数据"></span>数据 | Data | 对客观事物的记录，可以是数字、文字、图片、声音等形式 | 一笔订单的金额、一条评论、一张菜品照片 |
| <span id="g-数据生命周期"></span>数据生命周期 | Data Lifecycle | 数据从产生、采集、存储、加工、使用到归档或销毁的全过程 | 一条评论从用户写下、被采集、清洗、标注、用于训练，到超过保存期限后删除 |
| <span id="g-训练数据"></span>训练数据 | Training Data | 用来训练模型的、通常带有标签的数据 | 标好“好评 / 中评 / 差评”的 3000 条评论 |
| <span id="g-数据处理"></span>数据处理 | Data Processing | 对数据进行采集、清洗、转换、整合等加工，使它能够被分析和使用 | 把三个系统导出的订单合并、去重、统一写法 |
| <span id="g-数据分析"></span>数据分析 | Data Analysis | 用统计、图表等方法从数据中发现规律、得出结论、支持决策的过程 | 发现雨天平均送达时间多 6 分钟，建议给骑手加补贴 |
| <span id="g-数据驱动"></span>数据驱动 | Data-driven | 以数据分析的结果而不是个人经验或直觉作为决策依据的工作方式 | 根据各时段订单量而不是“感觉”安排骑手排班 |
| <span id="g-CRISP-DM"></span>CRISP-DM | Cross-Industry Standard Process for Data Mining | 跨行业数据挖掘标准流程，把项目分为业务理解、数据理解、数据准备、建模、评估、部署六个阶段 | 差评分析项目先明确“把差评率降到 15%”，再去看有哪些数据 |
| <span id="g-结构化数据"></span>结构化数据 | Structured Data | 能整理成行列分明的二维表、每一列含义和类型固定的数据 | 订单表的订单号、下单时间、实付金额 |
| <span id="g-半结构化数据"></span>半结构化数据 | Semi-structured Data | 有一定结构但不是固定二维表的数据，如 JSON、XML、日志 | 开放接口返回的评论 JSON，评论里嵌着商家和用户信息 |
| <span id="g-非结构化数据"></span>非结构化数据 | Unstructured Data | 没有预先定义格式的数据，如自由文本、图片、音频、视频 | 评论正文、菜品照片、客服通话录音 |
| <span id="g-数值型数据"></span>数值型数据 | Numerical Data | 用数字表示、可以做加减乘除和比较大小的数据 | 实付金额 64.9 元、送达时长 24 分钟 |
| <span id="g-类别型数据"></span>类别型数据 | Categorical Data | 取值是有限几个类别的数据，类别之间只能比较相同与否；有顺序的叫有序类别 | 城区、配送方式；年龄段、1～5 星评分是有序类别 |
| <span id="g-时间序列数据"></span>时间序列数据 | Time Series Data | 按时间先后顺序记录的一串数据 | 2025 年每天的订单量 |
| <span id="g-人工智能训练师"></span>人工智能训练师 | AI Trainer | 使用智能训练软件，在人工智能产品使用过程中进行数据库管理、算法参数设置、人机交互设计、性能测试跟踪等工作的人员，2020 年发布的新职业，分五个等级 | 四级训练师负责数据采集和处理、数据标注、智能系统运维 |
| <span id="g-数据标注员"></span>数据标注员 | Data Annotator | 按照标注规范对文本、图像、语音等数据进行分类、框选、转写等加工的人员，是人工智能训练师下的工种 | 每天按规范给 500 条评论标注情感 |
| <span id="g-职业守则"></span>职业守则 | Code of Conduct | 从业人员在职业活动中应当遵守的行为准则 | 工作中接触的用户数据不外传、不拷贝到私人设备 |
| <span id="g-数据字典"></span>数据字典 | Data Dictionary | 说明一份数据中每个字段的名称、含义、类型、取值范围和来源的文档 | 实验 1-2 生成的“数据字典_初稿.csv” |
| <span id="g-虚拟环境"></span>虚拟环境 | Virtual Environment | 为一个项目单独准备的、互不干扰的 Python 运行环境 | 用 uv 为本课程建一个装有 pandas 3.1 的环境 |
| <span id="g-Jupyter"></span>Jupyter | Jupyter | 在网页里一格一格编写和运行代码、并直接显示结果和图表的交互式编程工具 | 按 Shift + Enter 运行一格，柱状图直接显示在下面 |

## 第 2 章 Python 数据处理入门：从表格到 pandas

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-变量"></span>变量 | Variable | 给一个值起的名字，用 = 把值存进去，之后用名字取用 | price = 64.9，之后写 price * 0.9 就是打九折的价格 |
| <span id="g-列表"></span>列表 | List | Python 中按顺序存放多个值的容器，用方括号表示，从 0 开始编号 | districts = ["天河", "越秀", "海珠"]，districts[0] 是“天河” |
| <span id="g-字典"></span>字典 | Dictionary | Python 中按“键—值”成对存放数据的容器，用花括号表示，通过键取值 | {"订单号": "O000001", "实付金额": 64.9} |
| <span id="g-函数"></span>函数 | Function | 把一段完成特定功能的代码打包起来、起个名字，用“名字(参数)”调用 | len(districts) 返回列表的长度 3 |
| <span id="g-库"></span>库 | Library | 别人写好、打包发布的一组功能代码，安装后用 import 导入使用，也叫包 | import pandas as pd |
| <span id="g-DataFrame"></span>DataFrame | DataFrame | pandas 中的二维表格，有行索引和列名，相当于 Excel 的一个工作表 | pd.read_csv("orders.csv") 读出的订单表 |
| <span id="g-Series"></span>Series | Series | pandas 中带索引的一列数据，DataFrame 的每一列都是一个 Series | orders["实付金额"] |
| <span id="g-索引"></span>索引 | Index | DataFrame 或 Series 中用来标识和定位行的标签，默认是 0、1、2…… | 订单表最左边的 0 到 56654 |
| <span id="g-数据类型"></span>数据类型 | Data Type (dtype) | 一列数据的存储类型，决定了能对它做哪些运算 | int64 整数、float64 小数、str 文字、datetime64 日期时间 |
| <span id="g-条件筛选"></span>条件筛选 | Boolean Filtering | 用一个或多个条件选出满足条件的行，多个条件用 &（并且）、\|（或者）连接，每个条件加括号 | orders[(orders["天气"] == "雨") & (orders["送达时长"] > 45)] |
| <span id="g-loc-与-iloc"></span>loc 与 iloc | loc / iloc | pandas 选取行列的两种方式：loc 按标签（索引和列名）选，iloc 按位置（第几行第几列）选 | orders.loc[0:4, ["订单号", "实付金额"]]、orders.iloc[0:5, 0:3] |
| <span id="g-分组聚合"></span>分组聚合 | Group By | 按某一列的取值把数据分成若干组，对每组分别计算汇总值 | orders.groupby("城区")["实付金额"].sum() |
| <span id="g-拆分-应用-合并"></span>拆分-应用-合并 | Split-Apply-Combine | 分组聚合的三个步骤：按类别拆成小表，对每张小表计算，再把结果合成一张表 | 按城区拆成 8 张表，各自求平均送达时长，再合成 8 行的结果表 |
| <span id="g-透视表"></span>透视表 | Pivot Table | 把一个类别放在行、另一个类别放在列，格子里放汇总值的二维汇总表 | 行是城区、列是配送方式、格子是平均送达时长 |
| <span id="g-交叉表"></span>交叉表 | Crosstab | 统计两个类别变量各种组合出现次数的表格 | 天气 × 是否高峰的订单数 |
| <span id="g-合并"></span>合并 | Merge | 按一个或多个共同的列（键），把两张表横向连接成一张表，相当于 Excel 的 VLOOKUP | 订单表按“商家编号”合并商家表，得到每笔订单的商家品类 |
| <span id="g-连接方式"></span>连接方式 | Join Type | 合并两张表时对“对不上”的行的处理方式，有 inner、left、right、outer 四种 | how="left" 保留左表全部订单，找不到商家的格子填空值 |
| <span id="g-拼接"></span>拼接 | Concatenate | 把结构相同的多张表上下首尾相接（或左右并排）成一张表 | 把 1 月到 12 月的 12 张订单表接成全年订单表 |
| <span id="g-日期时间类型"></span>日期时间类型 | Datetime | pandas 中表示日期和时间的数据类型，可以直接取出年、月、星期、小时，也能相减算间隔 | pd.to_datetime(orders["下单时间"]).dt.hour 取出下单的小时 |
| <span id="g-重采样"></span>重采样 | Resample | 把时间序列按新的时间频率重新分组汇总，例如把每笔订单汇总成每天、每周、每月 | orders.resample("D", on="下单时间").size() 得到每天订单数 |
| <span id="g-NumPy-数组"></span>NumPy 数组 | NumPy Array | NumPy 库提供的同一类型数值组成的多维数组，计算速度很快，pandas 的底层就是它 | np.array([12, 35, 28]) |
| <span id="g-形状"></span>形状 | Shape | 数组或表格在各个维度上的大小 | 订单表的 shape 是 (56655, 12)，即 56655 行 12 列 |
| <span id="g-广播"></span>广播 | Broadcasting | 形状不同的数组做运算时，自动把较小的数组扩展成相同形状再逐个计算的规则 | 一整列金额乘以 0.9，0.9 被自动“复制”到每一行 |
| <span id="g-向量化"></span>向量化 | Vectorization | 对整列或整个数组一次性做运算，代替逐个元素写循环，代码更短、速度快几十到上百倍 | orders["实付金额"] * 0.9 比 for 循环快约 60 倍 |

## 第 3 章 数据采集：文件、数据库与接口

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-数据源"></span>数据源 | Data Source | 数据的来处，如业务系统、日志、开放接口、文件、公开数据、网页、传感器 | 订单库、市场部的商家名录、评论开放接口 |
| <span id="g-数据采集"></span>数据采集 | Data Collection | 按照分析目的，从各种数据源把需要的数据收集过来、保存下来的过程 | 从接口下载 2025 年全部评论存成 CSV |
| <span id="g-文件编码"></span>文件编码 | Character Encoding | 规定文字和计算机中字节如何一一对应的规则，读文件时用错编码就会出现乱码 | 同一个“食客说”，UTF-8 是 9 个字节，GBK 是 6 个字节 |
| <span id="g-UTF-8"></span>UTF-8 | UTF-8 | 国际通用的文字编码，能表示几乎所有文字，一个汉字通常占 3 个字节，是 Python 和网页的默认编码 | pd.read_csv 默认按 UTF-8 读文件 |
| <span id="g-GBK"></span>GBK | GBK | 我国早期的汉字编码，一个汉字占 2 个字节，中文 Windows 的老软件导出的文件常用 | pd.read_csv("商家名录_gbk.csv", encoding="gbk") |
| <span id="g-乱码"></span>乱码 | Mojibake | 用错误的编码解读文字字节而显示出的无意义字符 | “食客说”按错编码读出来变成“椋熷�㈣��” |
| <span id="g-JSON"></span>JSON | JavaScript Object Notation | 用花括号表示“键: 值”、方括号表示列表、可以多层嵌套的文本数据格式，接口返回和日志常用 | {"review_id": "R000001", "shop": {"shop_id": "S0017"}} |
| <span id="g-展平"></span>展平 | Flatten | 把多层嵌套的数据转换成一行一条记录、一列一个字段的二维表 | pd.json_normalize 把 shop 里的 shop_id 展开成 shop.shop_id 列 |
| <span id="g-Parquet"></span>Parquet | Apache Parquet | 一种按列存储、自带数据类型、自动压缩的数据文件格式，适合存储和分析大量数据 | 订单表存成 Parquet 只有 1.4 MB，CSV 是 4.4 MB |
| <span id="g-数据库"></span>数据库 | Database | 按一定结构长期存储、统一管理、可供多人同时安全读写的数据集合及其管理系统 | 存放“食客说”全部订单的 MySQL 数据库 |
| <span id="g-SQL"></span>SQL | Structured Query Language | 结构化查询语言，用来在关系型数据库中查询和管理数据的标准语言 | SELECT 城区, COUNT(*) FROM shops GROUP BY 城区 |
| <span id="g-SQLite"></span>SQLite | SQLite | 一种轻量级的数据库，整个数据库就是一个文件，Python 自带连接它的 sqlite3 模块 | 随书的 shike.db |
| <span id="g-应用程序接口"></span>应用程序接口 | Application Programming Interface (API) | 一个系统按约定格式向别的程序提供数据或功能的“窗口”，调用方按接口文档发请求、拿结果 | “食客说”开放平台的评论接口 /api/reviews |
| <span id="g-HTTP-请求"></span>HTTP 请求 | HTTP Request | 按 HTTP 协议向服务器发出的请求，包括地址、方法、参数和请求头 | requests.get(url, params={"page": 1}, headers={"X-API-Key": "…"}) |
| <span id="g-状态码"></span>状态码 | Status Code | 服务器对每次 HTTP 请求返回的三位数代码，说明请求的结果；2 开头成功，4 开头是请求方的问题，5 开头是服务器的问题 | 200 成功、401 没有权限、429 请求太频繁、500 服务器错误 |
| <span id="g-分页"></span>分页 | Pagination | 数据量大时，接口把数据分成若干页，每次请求只返回一页 | 12000 条评论每页 100 条，分 120 页取 |
| <span id="g-限流"></span>限流 | Rate Limiting | 接口限制每个调用方在一段时间内的请求次数，超过就拒绝，防止服务器被拖垮 | 每秒最多 4 次，超过返回 429 |
| <span id="g-重试"></span>重试 | Retry | 请求因临时故障或限流失败后，等待一段时间再次请求；连续多次失败则停止并报错 | 第 17 页返回 500，等 2 秒重试成功 |
| <span id="g-API-密钥"></span>API 密钥 | API Key | 接口用来识别调用者身份和权限的一串字符，相当于钥匙，应放在环境变量中，不能写进公开的代码 | 请求头 X-API-Key: shike-demo-key |
| <span id="g-采集日志"></span>采集日志 | Collection Log | 采集程序运行时逐条记录的开始时间、采集数量、失败和重试情况的文本，用来事后检查 | “第 17 页第 1 次请求失败，状态码 500，2 秒后重试” |
| <span id="g-增量采集"></span>增量采集 | Incremental Collection | 只采集上次采集之后新增或变化的数据，而不是每次全部重采 | 用 since 参数只取 2025-12-14 23:38 之后的 774 条新评论 |
| <span id="g-网络爬虫"></span>网络爬虫 | Web Crawler | 模拟浏览器自动访问网页、下载并提取网页内容的程序 | 用 requests 下载网页、BeautifulSoup 提取标题 |
| <span id="g-robots-协议"></span>robots 协议 | Robots Exclusion Protocol | 网站在根目录的 robots.txt 中声明允许或不允许爬虫访问哪些页面的约定，2022 年成为互联网标准 RFC 9309 | Disallow: /user/ 表示不允许爬虫访问用户页面 |
| <span id="g-采集方案"></span>采集方案 | Data Collection Plan | 动手采集前写的说明文档，写明目的、数据、来源、范围、频率、合规措施、质量检查和负责人 | 3.6 节的评论采集方案 |

## 第 4 章 数据清洗与整合

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-数据质量"></span>数据质量 | Data Quality | 数据满足使用要求的程度，通常从完整性、唯一性、有效性、一致性、准确性、及时性等维度衡量 | 订单表有 8.6% 的日期格式不对，数据质量不能直接满足分析要求 |
| <span id="g-数据质量维度"></span>数据质量维度 | Data Quality Dimension | 把“数据质量”拆成的若干个可以逐项检查、用数字衡量的方面 | 完整性、唯一性、有效性、一致性、准确性、及时性 |
| <span id="g-完整性"></span>完整性 | Completeness | 该有的数据是否齐全，没有缺失 | 315 笔订单缺配送距离 |
| <span id="g-唯一性"></span>唯一性 | Uniqueness | 同一个对象是否只被记录一次，没有重复 | 同一订单号出现两行 |
| <span id="g-有效性"></span>有效性 | Validity | 数据的格式、类型、取值范围是否符合规定 | 送达时长为负数、日期写成“2025年03月05日” |
| <span id="g-一致性"></span>一致性 | Consistency | 同一件事在不同地方、不同时间的记录是否一致 | “天河”和“天河区”；订单表和商家表的城区不同 |
| <span id="g-准确性"></span>准确性 | Accuracy | 数据是否如实反映真实情况 | 实付金额按“分”录入，比真实值大 100 倍 |
| <span id="g-及时性"></span>及时性 | Timeliness | 数据是否足够新、是否按时到达 | 2025 年报表中混入了 2023 年的旧订单 |
| <span id="g-数据质量评估报告"></span>数据质量评估报告 | Data Quality Assessment Report | 说明一份数据的概况、各维度检查结果、问题示例、影响和处理建议的文档 | 实验 4-1 的数据质量评估表加上文字说明 |
| <span id="g-主键"></span>主键 | Primary Key | 能唯一标识表中每一行的列或列的组合，不能为空、不能重复 | 订单表的 order_id、商家表的 shop_id |
| <span id="g-缺失值"></span>缺失值 | Missing Value | 该有值却没有值的格子，pandas 中显示为 NaN（日期为 NaT） | 配送距离为空 |
| <span id="g-中位数"></span>中位数 | Median | 把数据从小到大排列后处在正中间的值，不受极端值影响 | 实付金额中位数 93.6 元，平均值 133.2 元 |
| <span id="g-按组填充"></span>按组填充 | Group-wise Imputation | 用缺失值所在分组（如同一城区）的统计值填充，比用全体统计值更接近真实值 | 天河的配送距离缺失值用天河订单的距离中位数填 |
| <span id="g-异常值"></span>异常值 | Outlier | 明显偏离大多数数据的值，也叫离群值；可能是错误，也可能是真实的极端情况 | 送达时长 600 分钟（错误）；4 人火锅 900 元（真实） |
| <span id="g-3σ-法则"></span>3σ 法则 | Three-sigma Rule | 把离平均值超过 3 个标准差的值判为异常值的方法，适用于大致呈钟形分布的数据 | 实付金额平均 135.0、标准差 124.0，超过 507.0 元判为异常 |
| <span id="g-箱线图法"></span>箱线图法 | IQR Method | 把小于 Q1 − 1.5×IQR 或大于 Q3 + 1.5×IQR 的值判为异常值的方法，IQR 是上下四分位数之差 | 实付金额 Q1 50.8、Q3 177.8，超过 368.3 元判为异常 |
| <span id="g-业务规则校验"></span>业务规则校验 | Business Rule Validation | 用业务上必须成立的规则检查数据，如金额关系、取值范围、先后顺序 | 实付金额 = 订单金额 − 优惠金额 |
| <span id="g-正则表达式"></span>正则表达式 | Regular Expression | 描述一类文字模式的规则，用来查找、提取、替换符合模式的文字 | 1[3-9]\d{9} 匹配手机号 |
| <span id="g-脱敏"></span>脱敏 | Data Masking | 对敏感信息进行替换、遮挡或删除，使其不能识别到具体个人，同时尽量保留数据的可用性 | 18545161843 → 185****1843 或 [手机号] |
| <span id="g-无效评论"></span>无效评论 | Invalid Review | 清洗后几乎没有内容、没有分析价值的评论 | 只有“。。。”的评论 |
| <span id="g-清洗规范"></span>清洗规范 | Data Cleaning Specification | 规定每类数据问题如何识别、如何处理、为什么这样处理的文档，保证不同人清洗结果一致 | 4.7.1 节的订单数据清洗规范 |
| <span id="g-数据处理流水线"></span>数据处理流水线 | Data Pipeline | 把多个数据处理步骤按顺序串起来、可以对新数据反复执行的处理过程 | cleaning.py 中的 clean_orders 函数 |

## 第 5 章 数据标注：任务、规范与工具

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-监督学习"></span>监督学习 | Supervised Learning | 让模型从大量“输入 + 正确答案（标签）”的样本中学习规律，再对新输入给出答案的学习方式 | 用 3000 条标好情感的评论训练情感分析模型 |
| <span id="g-标签"></span>标签 | Label | 监督学习中每条数据对应的“正确答案”，由标注得到 | 评论的“正面”、图中碗的位置和类别 |
| <span id="g-数据标注"></span>数据标注 | Data Annotation | 按照标注规范，对文本、图像、语音等数据进行分类、框选、转写等加工，给数据加上标签的工作 | 按规范给 100 条评论标注情感、方面和菜品 |
| <span id="g-指令数据"></span>指令数据 | Instruction Data | 由人编写的“指令或问题 + 高质量回答”，用来教大模型听懂指令、按要求回答 | “请用三句话总结这条差评的主要问题”及示范回答 |
| <span id="g-偏好数据"></span>偏好数据 | Preference Data | 标注员对同一问题的几个模型回答按好坏排序或打分得到的数据，用来教大模型分辨什么样的回答更好 | 回答 A 比回答 B 更有用、更准确 |
| <span id="g-文本分类"></span>文本分类 | Text Classification | 给一段文字分配一个（单标签）或多个（多标签）类别的任务 | 情感单选正面 / 负面 / 中性；方面多选 |
| <span id="g-实体标注"></span>实体标注 | Named Entity Annotation | 在文字中找出特定类型的词语，标出起止位置和类型 | 在评论中划出“三文鱼刺身”，类型为菜品 |
| <span id="g-BIO-标注"></span>BIO 标注 | BIO Tagging | 把实体标注转换为逐字标签的方法：实体第一个字标 B，其余字标 I，非实体标 O | 三 B-菜品 文 I-菜品 鱼 I-菜品 |
| <span id="g-目标框标注"></span>目标框标注 | Bounding Box Annotation | 用矩形框标出图像中每个目标物体的位置并标明类别 | 框出餐桌照片中的每一个碗、盘子、杯子 |
| <span id="g-图像分割"></span>图像分割 | Image Segmentation | 沿物体轮廓勾画，或为每个像素标注类别的图像标注任务 | 沿盘子边缘描出它的形状 |
| <span id="g-关键点标注"></span>关键点标注 | Keypoint Annotation | 标出物体上若干个约定特征点位置的图像标注任务 | 标出人手的 21 个关节点 |
| <span id="g-语音转写"></span>语音转写 | Speech Transcription | 把录音逐字写成文字，通常还要标出时间戳和说话人 | 把语音点餐录音写成“我要一份猪脚饭” |
| <span id="g-偏好标注"></span>偏好标注 | Preference Annotation | 比较模型对同一问题的几个回答，按规范判断哪个更好或给出评分的标注任务 | 判断哪个回答更准确地概括了评论 |
| <span id="g-标签体系"></span>标签体系 | Label Taxonomy | 一个标注任务中全部标签的集合及其组织方式，应互斥、完整、粒度合适 | 情感三类 + 方面五类 + 菜品实体 |
| <span id="g-标注规范"></span>标注规范 | Annotation Guideline | 说明每个标签的含义和各种情况如何标注的文档，包括定义、正反例、边界规则、疑难样例、质量要求、版本记录 | labs/ch05/标注规范_v1.0.md |
| <span id="g-边界规则"></span>边界规则 | Boundary Rule | 标注规范中针对介于两个标签之间、容易产生分歧的情况所规定的统一判法 | 好坏都有时，按结尾的总结性表态判断 |
| <span id="g-试标"></span>试标 | Pilot Annotation | 规范定稿前，请几个人独立标注少量数据，用来发现分歧、修订规范 | 两人各自标注 50 条评论，一致率 72% |
| <span id="g-Label-Studio"></span>Label Studio | Label Studio | 开源的网页版数据标注工具，支持文本、图像、音频、视频等多种标注任务和多种导出格式 | 本书实验 5-2、5-3 使用的工具 |
| <span id="g-标注模板"></span>标注模板 | Labeling Configuration | Label Studio 中用标签语言描述标注界面的配置，规定显示什么数据、有哪些标注项 | <Choices name="sentiment" …> 定义情感单选题 |
| <span id="g-COCO-格式"></span>COCO 格式 | COCO Format | 目标检测常用的标注格式，所有图片的标注存在一个 JSON 文件中，框写成左上角坐标和宽高（像素） | "bbox": [426, 8, 98, 98] |
| <span id="g-YOLO-格式"></span>YOLO 格式 | YOLO Format | 每张图片一个文本文件，每行一个框，写成类别编号和中心点、宽高（相对图片宽高的比例） | 2 0.742 0.119 0.153 0.204 |

## 第 6 章 数据标注：质量审核与管理

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 7 章 探索性分析与统计推断

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 8 章 数据可视化与分析报告

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 9 章 建模应用：从 scikit-learn 到预训练模型

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 10 章 推荐系统

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 11 章 智能系统运维与优化

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 12 章 数据伦理、隐私合规与综合项目

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
