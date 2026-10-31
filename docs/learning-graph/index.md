---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **255 个概念、344 条先修关系**，概念按章排列，颜色表示 11 个类别（基础概念、Python 与 pandas、数据采集、数据清洗、数据标注、统计分析、可视化与报告、建模应用、推荐系统、系统运维、伦理与合规）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 概述（19 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [数据](../appendix/glossary.md#g-数据) | 基础概念 | — |
    | [数据生命周期](../appendix/glossary.md#g-数据生命周期) | 基础概念 | [数据处理](../appendix/glossary.md#g-数据处理) |
    | [训练数据](../appendix/glossary.md#g-训练数据) | 基础概念 | [数据](../appendix/glossary.md#g-数据) |
    | [数据处理](../appendix/glossary.md#g-数据处理) | 基础概念 | [数据](../appendix/glossary.md#g-数据) |
    | [数据分析](../appendix/glossary.md#g-数据分析) | 基础概念 | [数据](../appendix/glossary.md#g-数据) |
    | [数据驱动](../appendix/glossary.md#g-数据驱动) | 基础概念 | [数据分析](../appendix/glossary.md#g-数据分析) |
    | [CRISP-DM](../appendix/glossary.md#g-CRISP-DM) | 基础概念 | [数据分析](../appendix/glossary.md#g-数据分析)、[数据生命周期](../appendix/glossary.md#g-数据生命周期) |
    | [结构化数据](../appendix/glossary.md#g-结构化数据) | 基础概念 | [数据](../appendix/glossary.md#g-数据) |
    | [半结构化数据](../appendix/glossary.md#g-半结构化数据) | 基础概念 | [结构化数据](../appendix/glossary.md#g-结构化数据) |
    | [非结构化数据](../appendix/glossary.md#g-非结构化数据) | 基础概念 | [结构化数据](../appendix/glossary.md#g-结构化数据) |
    | [数值型数据](../appendix/glossary.md#g-数值型数据) | 基础概念 | [结构化数据](../appendix/glossary.md#g-结构化数据) |
    | [类别型数据](../appendix/glossary.md#g-类别型数据) | 基础概念 | [结构化数据](../appendix/glossary.md#g-结构化数据) |
    | [时间序列数据](../appendix/glossary.md#g-时间序列数据) | 基础概念 | [数值型数据](../appendix/glossary.md#g-数值型数据) |
    | [人工智能训练师](../appendix/glossary.md#g-人工智能训练师) | 基础概念 | [数据处理](../appendix/glossary.md#g-数据处理) |
    | [数据标注员](../appendix/glossary.md#g-数据标注员) | 基础概念 | [人工智能训练师](../appendix/glossary.md#g-人工智能训练师) |
    | [职业守则](../appendix/glossary.md#g-职业守则) | 基础概念 | [人工智能训练师](../appendix/glossary.md#g-人工智能训练师) |
    | [数据字典](../appendix/glossary.md#g-数据字典) | 数据清洗 | [结构化数据](../appendix/glossary.md#g-结构化数据) |
    | [虚拟环境](../appendix/glossary.md#g-虚拟环境) | 基础概念 | — |
    | [Jupyter](../appendix/glossary.md#g-Jupyter) | 基础概念 | [虚拟环境](../appendix/glossary.md#g-虚拟环境) |

??? note "第 2 章 pandas 入门（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [变量](../appendix/glossary.md#g-变量) | Python 与 pandas | [Jupyter](../appendix/glossary.md#g-Jupyter) |
    | [列表](../appendix/glossary.md#g-列表) | Python 与 pandas | [变量](../appendix/glossary.md#g-变量) |
    | [字典](../appendix/glossary.md#g-字典) | Python 与 pandas | [变量](../appendix/glossary.md#g-变量) |
    | [函数](../appendix/glossary.md#g-函数) | Python 与 pandas | [变量](../appendix/glossary.md#g-变量) |
    | [库](../appendix/glossary.md#g-库) | Python 与 pandas | [函数](../appendix/glossary.md#g-函数) |
    | [DataFrame](../appendix/glossary.md#g-DataFrame) | Python 与 pandas | [Series](../appendix/glossary.md#g-Series)、[库](../appendix/glossary.md#g-库)、[结构化数据](../appendix/glossary.md#g-结构化数据) |
    | [Series](../appendix/glossary.md#g-Series) | Python 与 pandas | [NumPy 数组](../appendix/glossary.md#g-NumPy-数组) |
    | [索引](../appendix/glossary.md#g-索引) | Python 与 pandas | [DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [数据类型](../appendix/glossary.md#g-数据类型) | Python 与 pandas | [NumPy 数组](../appendix/glossary.md#g-NumPy-数组) |
    | [条件筛选](../appendix/glossary.md#g-条件筛选) | Python 与 pandas | [NumPy 数组](../appendix/glossary.md#g-NumPy-数组)、[DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [loc 与 iloc](../appendix/glossary.md#g-loc-与-iloc) | Python 与 pandas | [索引](../appendix/glossary.md#g-索引) |
    | [分组聚合](../appendix/glossary.md#g-分组聚合) | Python 与 pandas | [DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [拆分-应用-合并](../appendix/glossary.md#g-拆分-应用-合并) | Python 与 pandas | [分组聚合](../appendix/glossary.md#g-分组聚合) |
    | [透视表](../appendix/glossary.md#g-透视表) | Python 与 pandas | [分组聚合](../appendix/glossary.md#g-分组聚合) |
    | [交叉表](../appendix/glossary.md#g-交叉表) | Python 与 pandas | [透视表](../appendix/glossary.md#g-透视表) |
    | [合并](../appendix/glossary.md#g-合并) | Python 与 pandas | [DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [连接方式](../appendix/glossary.md#g-连接方式) | Python 与 pandas | [合并](../appendix/glossary.md#g-合并) |
    | [拼接](../appendix/glossary.md#g-拼接) | Python 与 pandas | [DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [日期时间类型](../appendix/glossary.md#g-日期时间类型) | Python 与 pandas | [数据类型](../appendix/glossary.md#g-数据类型) |
    | [重采样](../appendix/glossary.md#g-重采样) | Python 与 pandas | [索引](../appendix/glossary.md#g-索引)、[时间序列数据](../appendix/glossary.md#g-时间序列数据) |
    | [NumPy 数组](../appendix/glossary.md#g-NumPy-数组) | Python 与 pandas | — |
    | [形状](../appendix/glossary.md#g-形状) | Python 与 pandas | [NumPy 数组](../appendix/glossary.md#g-NumPy-数组) |
    | [广播](../appendix/glossary.md#g-广播) | Python 与 pandas | [向量化](../appendix/glossary.md#g-向量化)、[形状](../appendix/glossary.md#g-形状) |
    | [向量化](../appendix/glossary.md#g-向量化) | Python 与 pandas | [NumPy 数组](../appendix/glossary.md#g-NumPy-数组) |

??? note "第 3 章 数据采集（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [数据源](../appendix/glossary.md#g-数据源) | 数据采集 | [数据](../appendix/glossary.md#g-数据) |
    | [数据采集](../appendix/glossary.md#g-数据采集) | 数据采集 | [数据源](../appendix/glossary.md#g-数据源) |
    | [文件编码](../appendix/glossary.md#g-文件编码) | 数据采集 | [数据采集](../appendix/glossary.md#g-数据采集) |
    | [UTF-8](../appendix/glossary.md#g-UTF-8) | 数据采集 | [文件编码](../appendix/glossary.md#g-文件编码) |
    | [GBK](../appendix/glossary.md#g-GBK) | 数据采集 | [文件编码](../appendix/glossary.md#g-文件编码) |
    | [乱码](../appendix/glossary.md#g-乱码) | 数据采集 | [UTF-8](../appendix/glossary.md#g-UTF-8)、[GBK](../appendix/glossary.md#g-GBK) |
    | [JSON](../appendix/glossary.md#g-JSON) | 数据采集 | [半结构化数据](../appendix/glossary.md#g-半结构化数据) |
    | [展平](../appendix/glossary.md#g-展平) | 数据采集 | [JSON](../appendix/glossary.md#g-JSON)、[DataFrame](../appendix/glossary.md#g-DataFrame) |
    | [Parquet](../appendix/glossary.md#g-Parquet) | 数据采集 | [数据采集](../appendix/glossary.md#g-数据采集)、[数据类型](../appendix/glossary.md#g-数据类型)、[类别型数据](../appendix/glossary.md#g-类别型数据) |
    | [数据库](../appendix/glossary.md#g-数据库) | 数据采集 | [数据源](../appendix/glossary.md#g-数据源) |
    | [SQL](../appendix/glossary.md#g-SQL) | 数据采集 | [数据库](../appendix/glossary.md#g-数据库) |
    | [SQLite](../appendix/glossary.md#g-SQLite) | 数据采集 | [数据库](../appendix/glossary.md#g-数据库) |
    | [应用程序接口](../appendix/glossary.md#g-应用程序接口) | 数据采集 | [数据源](../appendix/glossary.md#g-数据源) |
    | [HTTP 请求](../appendix/glossary.md#g-HTTP-请求) | 数据采集 | [应用程序接口](../appendix/glossary.md#g-应用程序接口) |
    | [状态码](../appendix/glossary.md#g-状态码) | 数据采集 | [HTTP 请求](../appendix/glossary.md#g-HTTP-请求) |
    | [分页](../appendix/glossary.md#g-分页) | 数据采集 | [HTTP 请求](../appendix/glossary.md#g-HTTP-请求) |
    | [限流](../appendix/glossary.md#g-限流) | 数据采集 | [HTTP 请求](../appendix/glossary.md#g-HTTP-请求) |
    | [重试](../appendix/glossary.md#g-重试) | 数据采集 | [HTTP 请求](../appendix/glossary.md#g-HTTP-请求)、[状态码](../appendix/glossary.md#g-状态码) |
    | [API 密钥](../appendix/glossary.md#g-API-密钥) | 数据采集 | [应用程序接口](../appendix/glossary.md#g-应用程序接口) |
    | [采集日志](../appendix/glossary.md#g-采集日志) | 数据采集 | [数据采集](../appendix/glossary.md#g-数据采集) |
    | [增量采集](../appendix/glossary.md#g-增量采集) | 数据采集 | [数据采集](../appendix/glossary.md#g-数据采集)、[索引](../appendix/glossary.md#g-索引)、[时间序列数据](../appendix/glossary.md#g-时间序列数据) |
    | [网络爬虫](../appendix/glossary.md#g-网络爬虫) | 数据采集 | [HTTP 请求](../appendix/glossary.md#g-HTTP-请求) |
    | [robots 协议](../appendix/glossary.md#g-robots-协议) | 数据采集 | [网络爬虫](../appendix/glossary.md#g-网络爬虫) |
    | [采集方案](../appendix/glossary.md#g-采集方案) | 数据采集 | [数据采集](../appendix/glossary.md#g-数据采集)、[数据源](../appendix/glossary.md#g-数据源) |

??? note "第 4 章 数据清洗（22 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [数据质量](../appendix/glossary.md#g-数据质量) | 数据清洗 | [数据](../appendix/glossary.md#g-数据) |
    | [数据质量维度](../appendix/glossary.md#g-数据质量维度) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [完整性](../appendix/glossary.md#g-完整性) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [唯一性](../appendix/glossary.md#g-唯一性) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [有效性](../appendix/glossary.md#g-有效性) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [一致性](../appendix/glossary.md#g-一致性) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [准确性](../appendix/glossary.md#g-准确性) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [及时性](../appendix/glossary.md#g-及时性) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [数据质量评估报告](../appendix/glossary.md#g-数据质量评估报告) | 数据清洗 | [完整性](../appendix/glossary.md#g-完整性)、[准确性](../appendix/glossary.md#g-准确性)、[一致性](../appendix/glossary.md#g-一致性)、[唯一性](../appendix/glossary.md#g-唯一性)、[及时性](../appendix/glossary.md#g-及时性)、[有效性](../appendix/glossary.md#g-有效性) |
    | [主键](../appendix/glossary.md#g-主键) | 数据清洗 | [唯一性](../appendix/glossary.md#g-唯一性)、[数据库](../appendix/glossary.md#g-数据库) |
    | [缺失值](../appendix/glossary.md#g-缺失值) | 数据清洗 | [完整性](../appendix/glossary.md#g-完整性) |
    | [中位数](../appendix/glossary.md#g-中位数) | 数据清洗 | [缺失值](../appendix/glossary.md#g-缺失值) |
    | [按组填充](../appendix/glossary.md#g-按组填充) | 数据清洗 | [缺失值](../appendix/glossary.md#g-缺失值)、[分组聚合](../appendix/glossary.md#g-分组聚合) |
    | [异常值](../appendix/glossary.md#g-异常值) | 数据清洗 | [准确性](../appendix/glossary.md#g-准确性) |
    | [3σ 法则](../appendix/glossary.md#g-3σ-法则) | 数据清洗 | [异常值](../appendix/glossary.md#g-异常值) |
    | [箱线图法](../appendix/glossary.md#g-箱线图法) | 数据清洗 | [异常值](../appendix/glossary.md#g-异常值) |
    | [业务规则校验](../appendix/glossary.md#g-业务规则校验) | 数据清洗 | [有效性](../appendix/glossary.md#g-有效性) |
    | [正则表达式](../appendix/glossary.md#g-正则表达式) | 数据清洗 | [Series](../appendix/glossary.md#g-Series) |
    | [脱敏](../appendix/glossary.md#g-脱敏) | 数据清洗 | [正则表达式](../appendix/glossary.md#g-正则表达式) |
    | [无效评论](../appendix/glossary.md#g-无效评论) | 数据清洗 | [业务规则校验](../appendix/glossary.md#g-业务规则校验) |
    | [清洗规范](../appendix/glossary.md#g-清洗规范) | 数据清洗 | [数据质量](../appendix/glossary.md#g-数据质量) |
    | [数据处理流水线](../appendix/glossary.md#g-数据处理流水线) | 数据清洗 | [清洗规范](../appendix/glossary.md#g-清洗规范)、[DataFrame](../appendix/glossary.md#g-DataFrame)、[函数](../appendix/glossary.md#g-函数) |

??? note "第 5 章 标注规范与工具（21 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [监督学习](../appendix/glossary.md#g-监督学习) | 数据标注 | [训练数据](../appendix/glossary.md#g-训练数据) |
    | [标签](../appendix/glossary.md#g-标签) | 数据标注 | [监督学习](../appendix/glossary.md#g-监督学习) |
    | [数据标注](../appendix/glossary.md#g-数据标注) | 数据标注 | [训练数据](../appendix/glossary.md#g-训练数据)、[标签](../appendix/glossary.md#g-标签) |
    | [指令数据](../appendix/glossary.md#g-指令数据) | 数据标注 | [偏好标注](../appendix/glossary.md#g-偏好标注) |
    | [偏好数据](../appendix/glossary.md#g-偏好数据) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [文本分类](../appendix/glossary.md#g-文本分类) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [实体标注](../appendix/glossary.md#g-实体标注) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [BIO 标注](../appendix/glossary.md#g-BIO-标注) | 数据标注 | [实体标注](../appendix/glossary.md#g-实体标注) |
    | [目标框标注](../appendix/glossary.md#g-目标框标注) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [图像分割](../appendix/glossary.md#g-图像分割) | 数据标注 | [目标框标注](../appendix/glossary.md#g-目标框标注) |
    | [关键点标注](../appendix/glossary.md#g-关键点标注) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [语音转写](../appendix/glossary.md#g-语音转写) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [偏好标注](../appendix/glossary.md#g-偏好标注) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [标签体系](../appendix/glossary.md#g-标签体系) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注)、[类别型数据](../appendix/glossary.md#g-类别型数据) |
    | [标注规范](../appendix/glossary.md#g-标注规范) | 数据标注 | [标签体系](../appendix/glossary.md#g-标签体系) |
    | [边界规则](../appendix/glossary.md#g-边界规则) | 数据标注 | [标注规范](../appendix/glossary.md#g-标注规范) |
    | [试标](../appendix/glossary.md#g-试标) | 数据标注 | [标注规范](../appendix/glossary.md#g-标注规范) |
    | [Label Studio](../appendix/glossary.md#g-Label-Studio) | 数据标注 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [标注模板](../appendix/glossary.md#g-标注模板) | 数据标注 | [Label Studio](../appendix/glossary.md#g-Label-Studio) |
    | [COCO 格式](../appendix/glossary.md#g-COCO-格式) | 数据标注 | [Label Studio](../appendix/glossary.md#g-Label-Studio)、[JSON](../appendix/glossary.md#g-JSON)、[目标框标注](../appendix/glossary.md#g-目标框标注) |
    | [YOLO 格式](../appendix/glossary.md#g-YOLO-格式) | 数据标注 | [Label Studio](../appendix/glossary.md#g-Label-Studio)、[JSON](../appendix/glossary.md#g-JSON)、[目标框标注](../appendix/glossary.md#g-目标框标注) |

??? note "第 6 章 标注质量审核（19 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [金标准](../appendix/glossary.md#g-金标准) | 数据标注 | [标注准确率](../appendix/glossary.md#g-标注准确率)、[标注规范](../appendix/glossary.md#g-标注规范) |
    | [标注准确率](../appendix/glossary.md#g-标注准确率) | 数据标注 | [标注规范](../appendix/glossary.md#g-标注规范) |
    | [一致率](../appendix/glossary.md#g-一致率) | 数据标注 | [标注规范](../appendix/glossary.md#g-标注规范) |
    | [Kappa 系数](../appendix/glossary.md#g-Kappa-系数) | 数据标注 | [一致率](../appendix/glossary.md#g-一致率) |
    | [Fleiss' Kappa](../appendix/glossary.md#g-Fleiss'-Kappa) | 数据标注 | [Kappa 系数](../appendix/glossary.md#g-Kappa-系数) |
    | [交并比](../appendix/glossary.md#g-交并比) | 数据标注 | [目标框标注](../appendix/glossary.md#g-目标框标注) |
    | [验收](../appendix/glossary.md#g-验收) | 数据标注 | [抽检](../appendix/glossary.md#g-抽检)、[标注准确率](../appendix/glossary.md#g-标注准确率) |
    | [抽检](../appendix/glossary.md#g-抽检) | 数据标注 | [标注规范](../appendix/glossary.md#g-标注规范)、[分层抽样](../appendix/glossary.md#g-分层抽样) |
    | [分层抽样](../appendix/glossary.md#g-分层抽样) | 统计分析 | — |
    | [抽检方案](../appendix/glossary.md#g-抽检方案) | 数据标注 | [抽检](../appendix/glossary.md#g-抽检)、[分层抽样](../appendix/glossary.md#g-分层抽样) |
    | [错误分析](../appendix/glossary.md#g-错误分析) | 数据标注 | [抽检](../appendix/glossary.md#g-抽检) |
    | [标注审核报告](../appendix/glossary.md#g-标注审核报告) | 数据标注 | [验收](../appendix/glossary.md#g-验收) |
    | [多数投票](../appendix/glossary.md#g-多数投票) | 数据标注 | [一致率](../appendix/glossary.md#g-一致率) |
    | [噪声标签](../appendix/glossary.md#g-噪声标签) | 数据标注 | [标注规范](../appendix/glossary.md#g-标注规范)、[标注准确率](../appendix/glossary.md#g-标注准确率) |
    | [预标注](../appendix/glossary.md#g-预标注) | 数据标注 | [Label Studio](../appendix/glossary.md#g-Label-Studio) |
    | [主动学习](../appendix/glossary.md#g-主动学习) | 数据标注 | [预标注](../appendix/glossary.md#g-预标注) |
    | [众包](../appendix/glossary.md#g-众包) | 数据标注 | [一致率](../appendix/glossary.md#g-一致率) |
    | [数据增强](../appendix/glossary.md#g-数据增强) | 数据标注 | [训练数据](../appendix/glossary.md#g-训练数据) |
    | [合成数据](../appendix/glossary.md#g-合成数据) | 数据标注 | [数据增强](../appendix/glossary.md#g-数据增强) |

??? note "第 7 章 统计分析（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [描述统计](../appendix/glossary.md#g-描述统计) | 统计分析 | [数值型数据](../appendix/glossary.md#g-数值型数据) |
    | [集中趋势](../appendix/glossary.md#g-集中趋势) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计) |
    | [众数](../appendix/glossary.md#g-众数) | 统计分析 | [集中趋势](../appendix/glossary.md#g-集中趋势) |
    | [离散程度](../appendix/glossary.md#g-离散程度) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计) |
    | [标准差](../appendix/glossary.md#g-标准差) | 统计分析 | [离散程度](../appendix/glossary.md#g-离散程度) |
    | [分位数](../appendix/glossary.md#g-分位数) | 统计分析 | [离散程度](../appendix/glossary.md#g-离散程度) |
    | [分布](../appendix/glossary.md#g-分布) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计) |
    | [偏度](../appendix/glossary.md#g-偏度) | 统计分析 | [分布](../appendix/glossary.md#g-分布) |
    | [探索性数据分析](../appendix/glossary.md#g-探索性数据分析) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计)、[数据质量](../appendix/glossary.md#g-数据质量) |
    | [相关系数](../appendix/glossary.md#g-相关系数) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计) |
    | [相关矩阵](../appendix/glossary.md#g-相关矩阵) | 统计分析 | [相关系数](../appendix/glossary.md#g-相关系数) |
    | [辛普森悖论](../appendix/glossary.md#g-辛普森悖论) | 统计分析 | [分组聚合](../appendix/glossary.md#g-分组聚合)、[相关系数](../appendix/glossary.md#g-相关系数) |
    | [总体](../appendix/glossary.md#g-总体) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计) |
    | [样本](../appendix/glossary.md#g-样本) | 统计分析 | [描述统计](../appendix/glossary.md#g-描述统计)、[总体](../appendix/glossary.md#g-总体) |
    | [随机抽样](../appendix/glossary.md#g-随机抽样) | 统计分析 | [总体](../appendix/glossary.md#g-总体)、[样本](../appendix/glossary.md#g-样本) |
    | [置信区间](../appendix/glossary.md#g-置信区间) | 统计分析 | [总体](../appendix/glossary.md#g-总体)、[样本](../appendix/glossary.md#g-样本)、[分布](../appendix/glossary.md#g-分布) |
    | [假设检验](../appendix/glossary.md#g-假设检验) | 统计分析 | [置信区间](../appendix/glossary.md#g-置信区间) |
    | [原假设](../appendix/glossary.md#g-原假设) | 统计分析 | [假设检验](../appendix/glossary.md#g-假设检验) |
    | [p 值](../appendix/glossary.md#g-p-值) | 统计分析 | [原假设](../appendix/glossary.md#g-原假设) |
    | [显著性水平](../appendix/glossary.md#g-显著性水平) | 统计分析 | [p 值](../appendix/glossary.md#g-p-值) |
    | [t 检验](../appendix/glossary.md#g-t-检验) | 统计分析 | [假设检验](../appendix/glossary.md#g-假设检验) |
    | [卡方检验](../appendix/glossary.md#g-卡方检验) | 统计分析 | [假设检验](../appendix/glossary.md#g-假设检验)、[交叉表](../appendix/glossary.md#g-交叉表) |
    | [A/B 测试](../appendix/glossary.md#g-A-B-测试) | 统计分析 | [t 检验](../appendix/glossary.md#g-t-检验)、[分层抽样](../appendix/glossary.md#g-分层抽样) |
    | [指标](../appendix/glossary.md#g-指标) | 统计分析 | [数据驱动](../appendix/glossary.md#g-数据驱动)、[描述统计](../appendix/glossary.md#g-描述统计) |

??? note "第 8 章 可视化与报告（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [数据可视化](../appendix/glossary.md#g-数据可视化) | 可视化与报告 | [描述统计](../appendix/glossary.md#g-描述统计) |
    | [条形图](../appendix/glossary.md#g-条形图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [折线图](../appendix/glossary.md#g-折线图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化)、[时间序列数据](../appendix/glossary.md#g-时间序列数据) |
    | [饼图](../appendix/glossary.md#g-饼图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [直方图](../appendix/glossary.md#g-直方图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化)、[分布](../appendix/glossary.md#g-分布) |
    | [箱线图](../appendix/glossary.md#g-箱线图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化)、[分位数](../appendix/glossary.md#g-分位数) |
    | [散点图](../appendix/glossary.md#g-散点图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化)、[相关系数](../appendix/glossary.md#g-相关系数) |
    | [热力图](../appendix/glossary.md#g-热力图) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化)、[相关系数](../appendix/glossary.md#g-相关系数) |
    | [堆叠柱状图](../appendix/glossary.md#g-堆叠柱状图) | 可视化与报告 | [条形图](../appendix/glossary.md#g-条形图) |
    | [Matplotlib](../appendix/glossary.md#g-Matplotlib) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [seaborn](../appendix/glossary.md#g-seaborn) | 可视化与报告 | [Matplotlib](../appendix/glossary.md#g-Matplotlib) |
    | [子图](../appendix/glossary.md#g-子图) | 可视化与报告 | [Matplotlib](../appendix/glossary.md#g-Matplotlib) |
    | [数据透视图](../appendix/glossary.md#g-数据透视图) | 可视化与报告 | [透视表](../appendix/glossary.md#g-透视表)、[数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [商业智能](../appendix/glossary.md#g-商业智能) | 可视化与报告 | [数据看板](../appendix/glossary.md#g-数据看板) |
    | [误导性图表](../appendix/glossary.md#g-误导性图表) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [截断纵轴](../appendix/glossary.md#g-截断纵轴) | 可视化与报告 | [误导性图表](../appendix/glossary.md#g-误导性图表) |
    | [双纵轴](../appendix/glossary.md#g-双纵轴) | 可视化与报告 | [误导性图表](../appendix/glossary.md#g-误导性图表) |
    | [交互图表](../appendix/glossary.md#g-交互图表) | 可视化与报告 | [pyecharts](../appendix/glossary.md#g-pyecharts)、[数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [pyecharts](../appendix/glossary.md#g-pyecharts) | 可视化与报告 | [数据可视化](../appendix/glossary.md#g-数据可视化) |
    | [数据看板](../appendix/glossary.md#g-数据看板) | 可视化与报告 | [交互图表](../appendix/glossary.md#g-交互图表)、[指标](../appendix/glossary.md#g-指标) |
    | [指标卡](../appendix/glossary.md#g-指标卡) | 可视化与报告 | [数据看板](../appendix/glossary.md#g-数据看板)、[指标](../appendix/glossary.md#g-指标) |
    | [Streamlit](../appendix/glossary.md#g-Streamlit) | 可视化与报告 | [数据看板](../appendix/glossary.md#g-数据看板) |
    | [数据分析报告](../appendix/glossary.md#g-数据分析报告) | 可视化与报告 | [数据看板](../appendix/glossary.md#g-数据看板)、[假设检验](../appendix/glossary.md#g-假设检验) |
    | [数据叙事](../appendix/glossary.md#g-数据叙事) | 可视化与报告 | [数据分析报告](../appendix/glossary.md#g-数据分析报告) |

??? note "第 9 章 建模应用（25 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [机器学习](../appendix/glossary.md#g-机器学习) | 建模应用 | [训练数据](../appendix/glossary.md#g-训练数据)、[监督学习](../appendix/glossary.md#g-监督学习) |
    | [特征](../appendix/glossary.md#g-特征) | 建模应用 | [训练数据](../appendix/glossary.md#g-训练数据) |
    | [模型](../appendix/glossary.md#g-模型) | 建模应用 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [回归](../appendix/glossary.md#g-回归) | 建模应用 | [CRISP-DM](../appendix/glossary.md#g-CRISP-DM)、[监督学习](../appendix/glossary.md#g-监督学习)、[模型](../appendix/glossary.md#g-模型) |
    | [分类](../appendix/glossary.md#g-分类) | 建模应用 | [CRISP-DM](../appendix/glossary.md#g-CRISP-DM)、[监督学习](../appendix/glossary.md#g-监督学习)、[模型](../appendix/glossary.md#g-模型) |
    | [聚类](../appendix/glossary.md#g-聚类) | 建模应用 | [CRISP-DM](../appendix/glossary.md#g-CRISP-DM) |
    | [训练集](../appendix/glossary.md#g-训练集) | 建模应用 | [训练数据](../appendix/glossary.md#g-训练数据)、[模型](../appendix/glossary.md#g-模型) |
    | [测试集](../appendix/glossary.md#g-测试集) | 建模应用 | [训练数据](../appendix/glossary.md#g-训练数据)、[训练集](../appendix/glossary.md#g-训练集) |
    | [数据泄露](../appendix/glossary.md#g-数据泄露) | 建模应用 | [训练集](../appendix/glossary.md#g-训练集)、[测试集](../appendix/glossary.md#g-测试集) |
    | [过拟合](../appendix/glossary.md#g-过拟合) | 建模应用 | [训练集](../appendix/glossary.md#g-训练集)、[测试集](../appendix/glossary.md#g-测试集) |
    | [scikit-learn](../appendix/glossary.md#g-scikit-learn) | 建模应用 | [库](../appendix/glossary.md#g-库)、[机器学习](../appendix/glossary.md#g-机器学习) |
    | [流水线](../appendix/glossary.md#g-流水线) | 建模应用 | [数据处理流水线](../appendix/glossary.md#g-数据处理流水线)、[特征](../appendix/glossary.md#g-特征)、[scikit-learn](../appendix/glossary.md#g-scikit-learn) |
    | [标准化](../appendix/glossary.md#g-标准化) | 建模应用 | [特征](../appendix/glossary.md#g-特征)、[标准差](../appendix/glossary.md#g-标准差) |
    | [平均绝对误差](../appendix/glossary.md#g-平均绝对误差) | 建模应用 | [回归](../appendix/glossary.md#g-回归) |
    | [决定系数](../appendix/glossary.md#g-决定系数) | 建模应用 | [回归](../appendix/glossary.md#g-回归) |
    | [残差](../appendix/glossary.md#g-残差) | 建模应用 | [回归](../appendix/glossary.md#g-回归) |
    | [TF-IDF](../appendix/glossary.md#g-TF-IDF) | 建模应用 | [特征](../appendix/glossary.md#g-特征)、[文本分类](../appendix/glossary.md#g-文本分类) |
    | [逻辑回归](../appendix/glossary.md#g-逻辑回归) | 建模应用 | [CRISP-DM](../appendix/glossary.md#g-CRISP-DM)、[分类](../appendix/glossary.md#g-分类) |
    | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) | 建模应用 | [分类](../appendix/glossary.md#g-分类)、[逻辑回归](../appendix/glossary.md#g-逻辑回归) |
    | [精确率](../appendix/glossary.md#g-精确率) | 建模应用 | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [召回率](../appendix/glossary.md#g-召回率) | 建模应用 | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [RFM 模型](../appendix/glossary.md#g-RFM-模型) | 建模应用 | [聚类](../appendix/glossary.md#g-聚类)、[分组聚合](../appendix/glossary.md#g-分组聚合) |
    | [K 均值](../appendix/glossary.md#g-K-均值) | 建模应用 | [聚类](../appendix/glossary.md#g-聚类) |
    | [预训练模型](../appendix/glossary.md#g-预训练模型) | 建模应用 | [CRISP-DM](../appendix/glossary.md#g-CRISP-DM) |
    | [提示词](../appendix/glossary.md#g-提示词) | 建模应用 | [预训练模型](../appendix/glossary.md#g-预训练模型) |

??? note "第 10 章 推荐系统（20 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [推荐系统](../appendix/glossary.md#g-推荐系统) | 推荐系统 | [聚类](../appendix/glossary.md#g-聚类) |
    | [用户—物品矩阵](../appendix/glossary.md#g-用户—物品矩阵) | 推荐系统 | [推荐系统](../appendix/glossary.md#g-推荐系统)、[透视表](../appendix/glossary.md#g-透视表) |
    | [稀疏](../appendix/glossary.md#g-稀疏) | 推荐系统 | [用户—物品矩阵](../appendix/glossary.md#g-用户—物品矩阵) |
    | [显式反馈](../appendix/glossary.md#g-显式反馈) | 推荐系统 | [用户—物品矩阵](../appendix/glossary.md#g-用户—物品矩阵) |
    | [隐式反馈](../appendix/glossary.md#g-隐式反馈) | 推荐系统 | [用户—物品矩阵](../appendix/glossary.md#g-用户—物品矩阵) |
    | [热门推荐](../appendix/glossary.md#g-热门推荐) | 推荐系统 | [推荐系统](../appendix/glossary.md#g-推荐系统) |
    | [基于内容的推荐](../appendix/glossary.md#g-基于内容的推荐) | 推荐系统 | [推荐系统](../appendix/glossary.md#g-推荐系统)、[特征](../appendix/glossary.md#g-特征) |
    | [余弦相似度](../appendix/glossary.md#g-余弦相似度) | 推荐系统 | [用户—物品矩阵](../appendix/glossary.md#g-用户—物品矩阵) |
    | [杰卡德相似度](../appendix/glossary.md#g-杰卡德相似度) | 推荐系统 | [基于内容的推荐](../appendix/glossary.md#g-基于内容的推荐) |
    | [协同过滤](../appendix/glossary.md#g-协同过滤) | 推荐系统 | [用户—物品矩阵](../appendix/glossary.md#g-用户—物品矩阵) |
    | [基于用户的协同过滤](../appendix/glossary.md#g-基于用户的协同过滤) | 推荐系统 | [协同过滤](../appendix/glossary.md#g-协同过滤) |
    | [基于物品的协同过滤](../appendix/glossary.md#g-基于物品的协同过滤) | 推荐系统 | [协同过滤](../appendix/glossary.md#g-协同过滤) |
    | [矩阵分解](../appendix/glossary.md#g-矩阵分解) | 推荐系统 | [协同过滤](../appendix/glossary.md#g-协同过滤) |
    | [召回](../appendix/glossary.md#g-召回) | 推荐系统 | [协同过滤](../appendix/glossary.md#g-协同过滤)、[推荐系统](../appendix/glossary.md#g-推荐系统) |
    | [排序](../appendix/glossary.md#g-排序) | 推荐系统 | [协同过滤](../appendix/glossary.md#g-协同过滤)、[召回](../appendix/glossary.md#g-召回) |
    | [冷启动](../appendix/glossary.md#g-冷启动) | 推荐系统 | [协同过滤](../appendix/glossary.md#g-协同过滤) |
    | [离线评估](../appendix/glossary.md#g-离线评估) | 推荐系统 | [推荐系统](../appendix/glossary.md#g-推荐系统)、[精确率](../appendix/glossary.md#g-精确率)、[召回率](../appendix/glossary.md#g-召回率)、[测试集](../appendix/glossary.md#g-测试集) |
    | [命中率](../appendix/glossary.md#g-命中率) | 推荐系统 | [离线评估](../appendix/glossary.md#g-离线评估) |
    | [覆盖率](../appendix/glossary.md#g-覆盖率) | 推荐系统 | [离线评估](../appendix/glossary.md#g-离线评估) |
    | [信息茧房](../appendix/glossary.md#g-信息茧房) | 推荐系统 | [推荐系统](../appendix/glossary.md#g-推荐系统) |

??? note "第 11 章 系统运维（18 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [智能系统运维](../appendix/glossary.md#g-智能系统运维) | 系统运维 | [预训练模型](../appendix/glossary.md#g-预训练模型)、[在线服务](../appendix/glossary.md#g-在线服务) |
    | [批量预测](../appendix/glossary.md#g-批量预测) | 系统运维 | [预训练模型](../appendix/glossary.md#g-预训练模型) |
    | [在线服务](../appendix/glossary.md#g-在线服务) | 系统运维 | [预训练模型](../appendix/glossary.md#g-预训练模型)、[应用程序接口](../appendix/glossary.md#g-应用程序接口) |
    | [灰度发布](../appendix/glossary.md#g-灰度发布) | 系统运维 | [在线服务](../appendix/glossary.md#g-在线服务) |
    | [运行日志](../appendix/glossary.md#g-运行日志) | 系统运维 | [智能系统运维](../appendix/glossary.md#g-智能系统运维)、[采集日志](../appendix/glossary.md#g-采集日志) |
    | [监控指标](../appendix/glossary.md#g-监控指标) | 系统运维 | [智能系统运维](../appendix/glossary.md#g-智能系统运维)、[指标](../appendix/glossary.md#g-指标) |
    | [延迟](../appendix/glossary.md#g-延迟) | 系统运维 | [监控指标](../appendix/glossary.md#g-监控指标) |
    | [P95 延迟](../appendix/glossary.md#g-P95-延迟) | 系统运维 | [延迟](../appendix/glossary.md#g-延迟)、[分位数](../appendix/glossary.md#g-分位数) |
    | [错误率](../appendix/glossary.md#g-错误率) | 系统运维 | [监控指标](../appendix/glossary.md#g-监控指标) |
    | [告警](../appendix/glossary.md#g-告警) | 系统运维 | [监控指标](../appendix/glossary.md#g-监控指标) |
    | [数据漂移](../appendix/glossary.md#g-数据漂移) | 系统运维 | [分布](../appendix/glossary.md#g-分布)、[监控指标](../appendix/glossary.md#g-监控指标) |
    | [概念漂移](../appendix/glossary.md#g-概念漂移) | 系统运维 | [数据漂移](../appendix/glossary.md#g-数据漂移) |
    | [群体稳定性指标](../appendix/glossary.md#g-群体稳定性指标) | 系统运维 | [数据漂移](../appendix/glossary.md#g-数据漂移)、[分布](../appendix/glossary.md#g-分布) |
    | [坏案例](../appendix/glossary.md#g-坏案例) | 系统运维 | [错误分析](../appendix/glossary.md#g-错误分析)、[运行日志](../appendix/glossary.md#g-运行日志) |
    | [归因](../appendix/glossary.md#g-归因) | 系统运维 | [坏案例](../appendix/glossary.md#g-坏案例) |
    | [数据闭环](../appendix/glossary.md#g-数据闭环) | 系统运维 | [坏案例](../appendix/glossary.md#g-坏案例)、[预标注](../appendix/glossary.md#g-预标注) |
    | [运维报告](../appendix/glossary.md#g-运维报告) | 系统运维 | [监控指标](../appendix/glossary.md#g-监控指标)、[坏案例](../appendix/glossary.md#g-坏案例) |
    | [优化需求](../appendix/glossary.md#g-优化需求) | 系统运维 | [运维报告](../appendix/glossary.md#g-运维报告) |

??? note "第 12 章 合规与综合项目（15 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [个人信息](../appendix/glossary.md#g-个人信息) | 伦理与合规 | [数据](../appendix/glossary.md#g-数据) |
    | [敏感个人信息](../appendix/glossary.md#g-敏感个人信息) | 伦理与合规 | [个人信息](../appendix/glossary.md#g-个人信息) |
    | [知情同意](../appendix/glossary.md#g-知情同意) | 伦理与合规 | [个人信息](../appendix/glossary.md#g-个人信息) |
    | [最小必要](../appendix/glossary.md#g-最小必要) | 伦理与合规 | [个人信息](../appendix/glossary.md#g-个人信息) |
    | [数据分类分级](../appendix/glossary.md#g-数据分类分级) | 伦理与合规 | [数据](../appendix/glossary.md#g-数据) |
    | [掩码](../appendix/glossary.md#g-掩码) | 伦理与合规 | [脱敏](../appendix/glossary.md#g-脱敏) |
    | [哈希](../appendix/glossary.md#g-哈希) | 伦理与合规 | [脱敏](../appendix/glossary.md#g-脱敏) |
    | [泛化](../appendix/glossary.md#g-泛化) | 伦理与合规 | [脱敏](../appendix/glossary.md#g-脱敏) |
    | [扰动](../appendix/glossary.md#g-扰动) | 伦理与合规 | [脱敏](../appendix/glossary.md#g-脱敏) |
    | [准标识符](../appendix/glossary.md#g-准标识符) | 伦理与合规 | [个人信息](../appendix/glossary.md#g-个人信息) |
    | [去标识化](../appendix/glossary.md#g-去标识化) | 伦理与合规 | [掩码](../appendix/glossary.md#g-掩码)、[哈希](../appendix/glossary.md#g-哈希)、[准标识符](../appendix/glossary.md#g-准标识符) |
    | [匿名化](../appendix/glossary.md#g-匿名化) | 伦理与合规 | [脱敏](../appendix/glossary.md#g-脱敏)、[掩码](../appendix/glossary.md#g-掩码)、[泛化](../appendix/glossary.md#g-泛化) |
    | [样本偏差](../appendix/glossary.md#g-样本偏差) | 伦理与合规 | [随机抽样](../appendix/glossary.md#g-随机抽样) |
    | [算法偏见](../appendix/glossary.md#g-算法偏见) | 伦理与合规 | [训练数据](../appendix/glossary.md#g-训练数据)、[数据](../appendix/glossary.md#g-数据)、[样本偏差](../appendix/glossary.md#g-样本偏差) |
    | [隐私计算](../appendix/glossary.md#g-隐私计算) | 伦理与合规 | [去标识化](../appendix/glossary.md#g-去标识化) |

<!-- graph:end -->
