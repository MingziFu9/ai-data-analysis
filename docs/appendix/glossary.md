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
| <span id="g-金标准"></span>金标准 | Gold Standard | 由专家按规范仔细标注、反复确认，作为“标准答案”的一批数据，用于计算准确率和考核标注员 | 300 条评论的“金标准”列 |
| <span id="g-标注准确率"></span>标注准确率 | Annotation Accuracy | 标注结果与金标准（或质检复核结果）相同的比例 | 标注员 A 的准确率 92.0% |
| <span id="g-一致率"></span>一致率 | Percent Agreement | 两名标注员对同一批数据给出相同标签的比例 | A 与 B 的一致率 80.7% |
| <span id="g-Kappa-系数"></span>Kappa 系数 | Cohen's Kappa | 扣除碰巧一致后衡量两名标注员一致程度的指标，等于（实际一致率 − 碰巧一致率）÷（1 − 碰巧一致率） | A 与 B 的 Kappa 为 0.686，一致程度较强 |
| <span id="g-Fleiss'-Kappa"></span>Fleiss' Kappa | Fleiss' Kappa | 把 Kappa 推广到三名及以上标注员的一致性指标 | 三人 Fleiss' Kappa 为 0.619 |
| <span id="g-交并比"></span>交并比 | Intersection over Union (IoU) | 两个框重叠部分面积与两框合起来覆盖面积之比，用于衡量目标框的准确程度 | 本书规定与参考框交并比不低于 0.7 为合格 |
| <span id="g-验收"></span>验收 | Acceptance | 质检员或需求方检查一批标注数据，决定是否接收的过程 | 2000 条标注抽检后判定 W03 返工 |
| <span id="g-抽检"></span>抽检 | Sampling Inspection | 按一定方法随机抽出一部分数据检查，用结果推断整批质量 | 从 2000 条中抽 201 条复核 |
| <span id="g-分层抽样"></span>分层抽样 | Stratified Sampling | 先把数据按某个特征分成几层（如按标注员），再在每层中分别随机抽样 | 四名标注员各抽 10% |
| <span id="g-抽检方案"></span>抽检方案 | Sampling Plan | 事先规定抽多少、合格标准是什么、不合格怎么办的验收规则 | 分层抽 10%，准确率 ≥ 95% 合格，不合格加抽 20% |
| <span id="g-错误分析"></span>错误分析 | Error Analysis | 对检查出的错误按类型、原因归类统计，找出改进方向 | 正面误标为中性最多，培训中强调中性的定义 |
| <span id="g-标注审核报告"></span>标注审核报告 | Annotation Audit Report | 记录一批标注的基本情况、抽检方案和结果、错误分析、处理意见的文档 | 实验 6-2 提交的审核报告 |
| <span id="g-多数投票"></span>多数投票 | Majority Voting | 几个人独立标注同一条数据，取得票最多的标签作为最终标签 | 三人投票后准确率 96.7% |
| <span id="g-噪声标签"></span>噪声标签 | Noisy Label | 训练数据中标错了的标签 | 2000 条标注中有 126 条与参考答案不符 |
| <span id="g-预标注"></span>预标注 | Pre-annotation | 先用模型给数据标上初步标签，再由标注员检查和修改 | 用情感模型预标注，标注员只改错的 |
| <span id="g-主动学习"></span>主动学习 | Active Learning | 让模型挑出最拿不准的数据优先交给人标注，以较少的标注量获得较好的模型 | 标 1100 条时准确率 98.8%，随机挑选为 95.2% |
| <span id="g-众包"></span>众包 | Crowdsourcing | 把任务拆成小任务发布到网络平台，由大量兼职人员完成 | 在众包平台上发布评论情感标注任务 |
| <span id="g-数据增强"></span>数据增强 | Data Augmentation | 对已有标注数据做不改变标签的变换，生成更多训练数据 | 把标好“碗”的照片左右翻转 |
| <span id="g-合成数据"></span>合成数据 | Synthetic Data | 用程序或模型生成、而非真实采集的数据 | 本书“食客说”数据；让大模型写 100 条差评 |

## 第 7 章 探索性分析与统计推断

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-描述统计"></span>描述统计 | Descriptive Statistics | 用平均值、中位数、标准差等少数几个数字概括一列数据的特点 | `describe()` 一次给出 8 个统计量 |
| <span id="g-集中趋势"></span>集中趋势 | Central Tendency | 一列数据“一般是多少”，常用平均值、中位数、众数表示 | 实付金额平均 133.2 元、中位数 93.6 元 |
| <span id="g-众数"></span>众数 | Mode | 一列数据中出现次数最多的值，常用于类别数据 | 订单最多的菜系是快餐 |
| <span id="g-离散程度"></span>离散程度 | Dispersion | 一列数据彼此相差有多大，常用标准差、四分位距表示 | 实付金额标准差 120.7 元，相差很大 |
| <span id="g-标准差"></span>标准差 | Standard Deviation | 衡量数据偏离平均值远近的指标，越大说明数据越分散 | 送达时长的标准差 8.3 分钟 |
| <span id="g-分位数"></span>分位数 | Quantile | 把数据从小到大排好后，位于某个百分比位置上的值 | 75% 分位数 175.7 元：四分之三的订单不超过这个金额 |
| <span id="g-分布"></span>分布 | Distribution | 一列数据中各个取值出现的多少，常用直方图展示 | 实付金额的分布左高右低、拖着长尾巴 |
| <span id="g-偏度"></span>偏度 | Skewness | 分布不对称的程度；右边拖长尾巴叫右偏，此时平均值大于中位数 | 实付金额明显右偏 |
| <span id="g-探索性数据分析"></span>探索性数据分析 | Exploratory Data Analysis (EDA) | 在建模或下结论之前，用统计量和图表从多个角度摸清数据的过程 | 实验 7-1 对订单做的四个发现 |
| <span id="g-相关系数"></span>相关系数 | Correlation Coefficient | 衡量两个数值变量直线关系强弱和方向的数，在 −1 到 1 之间 | 配送距离与送达时长的相关系数 0.66 |
| <span id="g-相关矩阵"></span>相关矩阵 | Correlation Matrix | 把多列两两之间的相关系数排成的表格 | `orders.corr(numeric_only=True)` |
| <span id="g-辛普森悖论"></span>辛普森悖论 | Simpson's Paradox | 分组看是一个结论、合起来看却相反的现象，原因是各组人数比例不同 | 新版页面在两个城区都更好，合起来却更差 |
| <span id="g-总体"></span>总体 | Population | 想要研究的全部对象 | “食客说”全部订单 |
| <span id="g-样本"></span>样本 | Sample | 从总体中抽出来、实际拿来观察的一部分对象 | 随机抽出的 200 单 |
| <span id="g-随机抽样"></span>随机抽样 | Random Sampling | 让总体中每个对象都有同样机会被抽中的抽样方法 | `df.sample(200, random_state=2026)` |
| <span id="g-置信区间"></span>置信区间 | Confidence Interval | 根据样本估计出的、有较大把握包含真实值的范围 | 平均送达时长的 95% 置信区间 26.8～29.3 分钟 |
| <span id="g-假设检验"></span>假设检验 | Hypothesis Testing | 先假设“没有差别”，再看样本数据和这个假设是否矛盾，以此判断差别是否真实存在 | 检验雨天和晴天送达时长是否不同 |
| <span id="g-原假设"></span>原假设 | Null Hypothesis | 假设检验中先假定成立的“没有差别、没有关系”的说法 | “用不用优惠券，好评率一样” |
| <span id="g-p-值"></span>p 值 | p-value | 假如原假设成立，碰巧得到眼前这么大（或更大）差别的可能性；越小越说明差别不像巧合 | 优惠券与好评的卡方检验 p = 0.279 |
| <span id="g-显著性水平"></span>显著性水平 | Significance Level | 事先定好的判断标准，p 值小于它就认为差别显著，通常取 0.05 | α = 0.05 |
| <span id="g-t-检验"></span>t 检验 | t-test | 判断两组数值的平均值是否真有差别的检验方法 | 雨天比晴天平均多约 6 分钟，p < 0.001 |
| <span id="g-卡方检验"></span>卡方检验 | Chi-square Test | 判断两个类别变量是否有关系的检验方法 | 用券与否和好评与否没有显著关系 |
| <span id="g-A-B-测试"></span>A/B 测试 | A/B Testing | 把用户随机分成两组，分别使用旧方案和新方案，比较指标判断新方案是否更好 | 新版商家页面转化率提高 1.28 个百分点 |
| <span id="g-指标"></span>指标 | Metric | 用一个数字衡量业务某方面表现，并写清计算口径 | GMV、复购率、好评率 |

## 第 8 章 数据可视化与分析报告

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-数据可视化"></span>数据可视化 | Data Visualization | 把数据画成图表，让人通过眼睛快速看出数量的大小、变化和关系 | 把每月交易额画成折线图 |
| <span id="g-条形图"></span>条形图 | Bar Chart | 用矩形的长度表示数值大小的图表，竖着放的也叫柱状图，最适合比较各类别的大小 | 各菜系订单数，从大到小排序 |
| <span id="g-折线图"></span>折线图 | Line Chart | 把各时间点的数值用线连起来，表示随时间变化的趋势 | 2025 年每月交易额 |
| <span id="g-饼图"></span>饼图 | Pie Chart | 用扇形的大小表示各部分占整体的比例，只适合 2～5 类 | 平台专送 67.8%、商家自送 32.2% |
| <span id="g-直方图"></span>直方图 | Histogram | 把数值分成若干区间，用柱子高度表示每个区间里有多少个数据，用来看分布 | 实付金额的直方图左高右低、拖着长尾 |
| <span id="g-箱线图"></span>箱线图 | Box Plot | 用箱子和须线画出一组数据的中位数、四分位数和异常值，适合比较几组数据的分布 | 各城区实付金额的箱线图 |
| <span id="g-散点图"></span>散点图 | Scatter Plot | 以两个数值变量为横、纵坐标，每个数据画一个点，用来看两者的关系 | 配送距离与送达时长的散点图 |
| <span id="g-热力图"></span>热力图 | Heatmap | 用颜色深浅表示表格中每个格子数值大小的图 | 星期 × 小时的订单量热力图 |
| <span id="g-堆叠柱状图"></span>堆叠柱状图 | Stacked Bar Chart | 把一根柱子按组成部分分段堆起来，同时看总量和构成 | 各城区两种配送方式的订单数 |
| <span id="g-Matplotlib"></span>Matplotlib | Matplotlib | Python 中最基础、最常用的画图库 | `plt.subplots`、`ax.bar` |
| <span id="g-seaborn"></span>seaborn | seaborn | 基于 Matplotlib 的统计图表库，几行代码就能画出箱线图、热力图等 | `sns.heatmap(透视表)` |
| <span id="g-子图"></span>子图 | Subplot | 在一块画布上排列的多张小图 | `plt.subplots(2, 4)` 得到 8 张子图 |
| <span id="g-数据透视图"></span>数据透视图 | PivotChart | WPS / Excel 中由数据透视表直接生成、能随字段拖放变化的图表 | 把“城区”拖到轴、“实付金额”拖到值 |
| <span id="g-商业智能"></span>商业智能 | Business Intelligence (BI) | 连接数据、拖拽做图、组合看板并分享给他人的一类软件和方法 | 帆软 FineBI、阿里云 Quick BI |
| <span id="g-误导性图表"></span>误导性图表 | Misleading Chart | 由于画法不当，使读者对数据得出错误印象的图表 | 纵轴从 60% 开始的好评率柱状图 |
| <span id="g-截断纵轴"></span>截断纵轴 | Truncated Axis | 柱状图的数值轴不从 0 开始，从而放大差别 | 越秀的柱子看起来是黄埔的 10 倍 |
| <span id="g-双纵轴"></span>双纵轴 | Dual Axis | 一张图左右各有一个纵轴，分别表示两个量；刻度可随意设定，容易制造假象 | 订单数和平均送达时长“一起涨落” |
| <span id="g-交互图表"></span>交互图表 | Interactive Chart | 可以用鼠标悬停看数值、缩放、点击图例的网页图表 | pyecharts 生成的网页 |
| <span id="g-pyecharts"></span>pyecharts | pyecharts | 把百度开源的 ECharts 包装成 Python 写法的交互图表库，自带中国地图 | 广州各城区交易额地图 |
| <span id="g-数据看板"></span>数据看板 | Dashboard | 把核心指标和关键图表放在一个页面上、可以筛选查看的展示页面 | “食客说”经营看板 |
| <span id="g-指标卡"></span>指标卡 | KPI Card | 看板上用大号字显示单个核心指标及其涨跌的区块 | 订单量 56,655 |
| <span id="g-Streamlit"></span>Streamlit | Streamlit | 用很少的 Python 代码把数据分析程序变成网页应用的库 | `streamlit run app.py` |
| <span id="g-数据分析报告"></span>数据分析报告 | Data Analysis Report | 把分析的目的、数据、方法、发现和建议写给决策者看的文档 | “食客说”2025 年经营分析报告 |
| <span id="g-数据叙事"></span>数据叙事 | Data Storytelling | 把数据、图表和文字组织成有逻辑的线索，引导读者得出结论 | 结论先行，一条发现配一张图 |

## 第 9 章 建模应用：从 scikit-learn 到预训练模型

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-机器学习"></span>机器学习 | Machine Learning | 让计算机从数据中自动找出规律，再用规律对新数据做预测或判断的方法 | 从历史订单学出送达时长的规律 |
| <span id="g-特征"></span>特征 | Feature | 用来做预测的输入信息，通常是表格中的一列 | 配送距离、是否雨天、是否高峰 |
| <span id="g-模型"></span>模型 | Model | 算法从训练数据中学到的规律，可以对新数据做预测 | 训练好的送达时长预测模型 |
| <span id="g-回归"></span>回归 | Regression | 预测一个数值的机器学习任务 | 预测送达时长 |
| <span id="g-分类"></span>分类 | Classification | 预测属于哪一个类别的机器学习任务 | 判断评论是正面、中性还是负面 |
| <span id="g-聚类"></span>聚类 | Clustering | 没有标签，把相似的对象自动分成几群的任务 | 把 4670 名用户分成 4 群 |
| <span id="g-训练集"></span>训练集 | Training Set | 交给算法学习规律的那部分数据 | 80% 的订单，45324 单 |
| <span id="g-测试集"></span>测试集 | Test Set | 训练时不让模型看到、用来检验模型真实水平的数据 | 20% 的订单，11331 单 |
| <span id="g-数据泄露"></span>数据泄露 | Data Leakage | 测试集或预测时拿不到的信息在训练时被模型用到，使测试成绩虚高 | 用评论的评分预测评论的情感 |
| <span id="g-过拟合"></span>过拟合 | Overfitting | 模型把训练集中的偶然细节也学了下来，在训练集上好、在新数据上差 | 训练集准确率 100%，测试集只有 80% |
| <span id="g-scikit-learn"></span>scikit-learn | scikit-learn | Python 中最常用的机器学习库，各种算法都用 fit、predict 两步调用 | `LinearRegression().fit(X, y)` |
| <span id="g-流水线"></span>流水线 | Pipeline | 把预处理步骤和模型串成一个整体，一次训练、一次预测 | 标准化 → 线性回归 |
| <span id="g-标准化"></span>标准化 | Standardization | 把一列数据减去平均值再除以标准差，使各列数值范围相近 | `StandardScaler()` |
| <span id="g-平均绝对误差"></span>平均绝对误差 | Mean Absolute Error (MAE) | 每个预测值与实际值之差的绝对值的平均数，单位和标签相同 | 送达时长预测平均差 3.45 分钟 |
| <span id="g-决定系数"></span>决定系数 | Coefficient of Determination (R²) | 衡量回归模型解释了标签多大比例变化的指标，越接近 1 越好 | R² = 0.721 |
| <span id="g-残差"></span>残差 | Residual | 实际值减去预测值 | 实际 40 分钟、预测 24.9 分钟，残差 15.1 |
| <span id="g-TF-IDF"></span>TF-IDF | Term Frequency–Inverse Document Frequency | 把文本变成数字的方法：字词在本文中出现越多、在所有文本中越少见，权重越高 | “踩雷”的权重高，“的”的权重低 |
| <span id="g-逻辑回归"></span>逻辑回归 | Logistic Regression | 输出属于各类别概率的常用分类算法 | 评论情感分类 |
| <span id="g-混淆矩阵"></span>混淆矩阵 | Confusion Matrix | 把真实类别和预测类别交叉统计的表格，对角线是判对的 | 36 条中性评论被判为负面 |
| <span id="g-精确率"></span>精确率 | Precision | 模型判为某一类的样本中，真正属于这一类的比例 | 判为负面的评论中 88.0% 真是负面 |
| <span id="g-召回率"></span>召回率 | Recall | 真正属于某一类的样本中，被模型找出来的比例 | 负面评论中 98.0% 被找出 |
| <span id="g-RFM-模型"></span>RFM 模型 | RFM Model | 用最近一次消费（R）、消费频率（F）、消费金额（M）衡量用户价值并分群的方法 | 重要价值客户：三项都好 |
| <span id="g-K-均值"></span>K 均值 | K-means | 先指定群数 K，反复调整使群内对象尽量相似的聚类算法 | `KMeans(n_clusters=4)` |
| <span id="g-预训练模型"></span>预训练模型 | Pre-trained Model | 已在海量数据上训练好、可以直接使用或稍加训练后使用的模型 | 大众点评评论训练的中文情感模型 |
| <span id="g-提示词"></span>提示词 | Prompt | 发给大模型的指令文字，说明要做什么、按什么规则、输出什么格式 | 把标注规范写进提示词 |

## 第 10 章 推荐系统

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-推荐系统"></span>推荐系统 | Recommender System | 根据用户的历史行为和物品信息，从大量物品中挑出用户可能感兴趣的一小部分主动展示的系统 | “食客说”首页的“猜你喜欢” |
| <span id="g-用户—物品矩阵"></span>用户—物品矩阵 | User-Item Matrix | 行是用户、列是物品、格子记录用户对物品行为的表格 | 4600 个用户 × 300 家餐厅 |
| <span id="g-稀疏"></span>稀疏 | Sparsity | 矩阵中绝大多数格子为 0 或空的情况 | 填了 1 的格子只占 2.8% |
| <span id="g-显式反馈"></span>显式反馈 | Explicit Feedback | 用户明确表达喜好的行为 | 打 1～5 星、点“不喜欢” |
| <span id="g-隐式反馈"></span>隐式反馈 | Implicit Feedback | 从用户行为中推测出的喜好 | 下单、浏览、收藏 |
| <span id="g-热门推荐"></span>热门推荐 | Popularity-based Recommendation | 把最受欢迎的物品推荐给所有人 | 订单最多的 10 家餐厅 |
| <span id="g-基于内容的推荐"></span>基于内容的推荐 | Content-based Recommendation | 根据物品自身的信息，推荐和用户喜欢过的物品相似的物品 | 喜欢深夜营业的湘菜，就推荐类似的店 |
| <span id="g-余弦相似度"></span>余弦相似度 | Cosine Similarity | 用两个向量夹角的余弦衡量相似程度；对 0/1 向量等于共同的 1 的个数 ÷ √(两者 1 的个数之积) | 两家店相似度 0.75 |
| <span id="g-杰卡德相似度"></span>杰卡德相似度 | Jaccard Similarity | 两个集合的交集大小 ÷ 并集大小 | 3 ÷ 5 = 0.6 |
| <span id="g-协同过滤"></span>协同过滤 | Collaborative Filtering | 不看物品内容，只根据用户的行为找出相似的用户或物品来推荐 | “去过这家店的人也常去……” |
| <span id="g-基于用户的协同过滤"></span>基于用户的协同过滤 | User-based CF | 先找和目标用户行为相似的用户，再推荐他们喜欢的物品 | 和你口味相近的人最近常去的店 |
| <span id="g-基于物品的协同过滤"></span>基于物品的协同过滤 | Item-based CF | 根据“顾客名单”的重合程度算物品相似度，推荐和用户喜欢过的物品相似的物品 | 实验 10-2，命中率 57.3% |
| <span id="g-矩阵分解"></span>矩阵分解 | Matrix Factorization | 把用户—物品矩阵分解成用户和物品在少数几个隐含因素上的取值，用来估计未知的格子 | `TruncatedSVD` 分解出 10 个隐含口味 |
| <span id="g-召回"></span>召回 | Candidate Generation | 推荐的第一阶段，用简单快速的方法从海量物品中挑出几百个候选 | 本区召回、协同过滤召回 |
| <span id="g-排序"></span>排序 | Ranking | 推荐的第二阶段，用更准的模型给候选打分并排出最终展示顺序 | 预测用户会不会点的概率 |
| <span id="g-冷启动"></span>冷启动 | Cold Start | 新用户或新物品没有行为数据，难以推荐的问题 | 新用户只能先推本区热门 |
| <span id="g-离线评估"></span>离线评估 | Offline Evaluation | 用历史数据检验推荐方法能否猜中之后发生的行为 | 1～10 月训练、11～12 月测试 |
| <span id="g-命中率"></span>命中率 | Hit Rate | 推荐列表中至少猜中一个的用户所占的比例 | 协同过滤 57.3%，热门 18.0% |
| <span id="g-覆盖率"></span>覆盖率 | Coverage | 所有推荐列表合起来用到的物品占全部物品的比例 | 热门推荐只有 6.7% |
| <span id="g-信息茧房"></span>信息茧房 | Information Cocoon | 推荐总是迎合已有偏好，使用户接触的信息越来越窄的现象 | 只给爱吃火锅的人推火锅店 |

## 第 11 章 智能系统运维与优化

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-智能系统运维"></span>智能系统运维 | AI System Operations | 维护智能系统日常运行，收集分析运行数据，发现和解决问题，提出优化需求的工作 | 监控情感服务的延迟和准确率 |
| <span id="g-批量预测"></span>批量预测 | Batch Prediction | 定时把一批数据全部预测一遍、结果存起来的上线方式 | 每周一重新计算用户分群 |
| <span id="g-在线服务"></span>在线服务 | Online Serving | 模型一直运行、来一个请求马上返回结果的上线方式 | 新评论一提交就判断情感 |
| <span id="g-灰度发布"></span>灰度发布 | Canary Release | 新版本先让一小部分请求使用，观察正常后再逐步扩大的上线方式 | 10% → 50% → 100% |
| <span id="g-运行日志"></span>运行日志 | Service Log | 系统处理每个请求时自动记下的记录 | service_log.jsonl 的 11820 条记录 |
| <span id="g-监控指标"></span>监控指标 | Monitoring Metric | 从日志等数据汇总出的、用来衡量系统运行状况的数字，分系统、模型、业务三类 | P95 延迟、负面占比、抽检准确率 |
| <span id="g-延迟"></span>延迟 | Latency | 从收到请求到返回结果所用的时间 | 平均 48 毫秒 |
| <span id="g-P95-延迟"></span>P95 延迟 | 95th Percentile Latency | 所有请求的延迟从小到大排列后第 95% 位置的值，即 95% 的请求都比它快 | 第 7 周 P95 延迟 161 毫秒 |
| <span id="g-错误率"></span>错误率 | Error Rate | 处理失败（状态码不是 200）的请求所占的比例 | 第 7 周错误率 2.4% |
| <span id="g-告警"></span>告警 | Alert | 指标超过事先设定的阈值时自动通知负责人 | P95 延迟超过 150 毫秒就告警 |
| <span id="g-数据漂移"></span>数据漂移 | Data Drift | 上线后输入数据的分布和训练时不同 | 评论中出现“绝绝子”“yyds”等新说法 |
| <span id="g-概念漂移"></span>概念漂移 | Concept Drift | 输入和标签之间的关系发生变化，同样的输入应该得到不同的标签 | “是预制菜吧”从中性描述变成表达不满 |
| <span id="g-群体稳定性指标"></span>群体稳定性指标 | Population Stability Index (PSI) | 按基准期分箱，比较两个时期各箱占比差异的指标；小于 0.1 稳定，大于 0.25 变化显著 | 第 5 周评论长度 PSI 为 0.113 |
| <span id="g-坏案例"></span>坏案例 | Bad Case | 系统处理错了或用户不满意的具体案例 | 正面评论被判为中性 |
| <span id="g-归因"></span>归因 | Attribution | 找出坏案例出错的原因，一般分为数据问题、模型问题、业务变化 | 39 条归因为“出现新说法” |
| <span id="g-数据闭环"></span>数据闭环 | Data Flywheel / Closed Loop | 监控 → 收集坏案例 → 补标 → 重训 → 评估 → 灰度上线，不断循环改进系统的过程 | 补标 1000 条后准确率从 95.5% 升到 97.4% |
| <span id="g-运维报告"></span>运维报告 | Operations Report | 定期汇报系统运行指标、异常处理、坏案例分析和下一步计划的文档 | 第 1～8 周情感服务运维报告 |
| <span id="g-优化需求"></span>优化需求 | Improvement Request | 把运维中发现的问题写给算法或开发人员的需求文档，包括现象、影响、原因、需求和验收标准 | 补标重训，含新说法准确率不低于 96% |

## 第 12 章 数据伦理、隐私合规与综合项目

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-个人信息"></span>个人信息 | Personal Information | 以电子或者其他方式记录的、与已识别或者可识别的自然人有关的各种信息，匿名化处理后的信息除外 | 姓名、手机号、住址、点评记录 |
| <span id="g-敏感个人信息"></span>敏感个人信息 | Sensitive Personal Information | 一旦泄露或被非法使用，容易导致人格尊严受到侵害或者人身、财产安全受到危害的个人信息 | 身份证号、银行账户、行踪轨迹、医疗健康信息 |
| <span id="g-知情同意"></span>知情同意 | Informed Consent | 处理个人信息前，向个人清楚告知处理目的、方式和范围，并取得其同意 | 注册时弹出的隐私政策和勾选框 |
| <span id="g-最小必要"></span>最小必要 | Data Minimization | 只收集、使用实现目的所必需的最少个人信息，不多拿、不多用、不多存 | 情感分析只取评论文本，不取手机号 |
| <span id="g-数据分类分级"></span>数据分类分级 | Data Classification and Grading | 按数据的内容和一旦泄露造成的危害程度，把数据分成不同类别和级别，分别采取保护措施 | 手机号列为敏感，菜系列为公开 |
| <span id="g-掩码"></span>掩码 | Masking | 用 * 等符号遮住数据的一部分，只保留部分字符的脱敏方法 | 185****1843 |
| <span id="g-哈希"></span>哈希 | Hashing | 用哈希函数把原值变成一串固定长度、无法反推的字符，相同的原值得到相同的结果 | 用户编号 → 9f3a2c71b0de |
| <span id="g-泛化"></span>泛化 | Generalization | 把精确的值换成更粗的范围或类别，降低识别个人的可能 | 具体地址 → 天河区；28 岁 → 25-34 岁 |
| <span id="g-扰动"></span>扰动 | Perturbation | 给数值加上小的随机噪声，单条记录不再精确，整体统计结果基本不变 | 每单金额随机加减几元 |
| <span id="g-准标识符"></span>准标识符 | Quasi-identifier | 单独不能识别个人、但几项组合起来可能识别出个人的字段 | 性别 + 年龄段 + 城区 + 注册日期 |
| <span id="g-去标识化"></span>去标识化 | De-identification | 处理个人信息后，使其在不借助额外信息的情况下无法识别特定个人 | 用户编号哈希、手机号掩码，密钥另行保管 |
| <span id="g-匿名化"></span>匿名化 | Anonymization | 处理个人信息后，使其无法识别特定个人且不能复原；匿名化后的信息不再属于个人信息 | 只保留按城区汇总的订单数 |
| <span id="g-样本偏差"></span>样本偏差 | Sampling Bias | 训练或分析用的数据不能代表真实总体，导致结论或模型对某些群体不准 | 只用平台专送订单训练送达时间模型 |
| <span id="g-算法偏见"></span>算法偏见 | Algorithmic Bias | 模型对不同群体的结果系统性地不公平，常来自有偏的数据或有偏的标注 | 对商家自送订单系统性少估送达时间 |
| <span id="g-隐私计算"></span>隐私计算 | Privacy-preserving Computation | 在不暴露原始数据的前提下，让多方数据一起参与计算的技术 | 联邦学习、多方安全计算 |
