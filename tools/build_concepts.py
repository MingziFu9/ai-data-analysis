"""生成《人工智能数据分析与处理》学习图谱概念表（大纲阶段）。

每行：概念 | 章 | 类别 | 先修（用概念名，| 分隔） | 深入学习去处（；分隔）
输出 learning-graph.csv（技能标准四列 + 章、深入学习）和 概念清单.md。
用法：python tools/build_concepts.py docs/learning-graph
"""
import csv, sys, collections

CATS = {
    "FOUND": "基础与职业", "PD": "数据处理基本功", "COLL": "数据采集",
    "CLEAN": "数据清洗与整合", "LABEL": "数据标注", "STAT": "统计分析",
    "VIS": "可视化与报告", "MODEL": "建模应用", "REC": "推荐系统",
    "OPS": "智能系统运维", "ETH": "伦理、隐私与合规",
}
CHAPTERS = ["", "数据分析与处理概述", "NumPy 与 pandas 进阶", "数据采集：文件、数据库与接口",
            "数据清洗与整合", "数据标注：任务、规范与工具", "数据标注：质量审核与管理",
            "探索性分析与统计推断", "数据可视化与分析报告", "建模应用：从 scikit-learn 到预训练模型",
            "推荐系统", "智能系统运维与优化", "数据伦理、隐私合规与综合项目"]

RAW = """
数据|1|FOUND||
数据分析|1|FOUND|数据|
数据处理|1|FOUND|数据|
人工智能训练师|1|FOUND|数据处理|导论
数据标注员|1|FOUND|人工智能训练师|
职业守则|1|FOUND|人工智能训练师|
数据生命周期|1|FOUND|数据处理|
结构化数据|1|FOUND|数据|
半结构化数据|1|FOUND|结构化数据|
非结构化数据|1|FOUND|结构化数据|
数值型数据|1|FOUND|结构化数据|
类别型数据|1|FOUND|结构化数据|
时间序列数据|1|FOUND|数值型数据|
训练数据|1|FOUND|数据|机器学习
数据驱动|1|FOUND|数据分析|
CRISP-DM|1|FOUND|数据分析|数据生命周期|机器学习
Jupyter|1|FOUND||Python
虚拟环境|1|FOUND||Python
NumPy 数组|2|PD||Python
形状|2|PD|NumPy 数组|
数据类型|2|PD|NumPy 数组|
向量化|2|PD|NumPy 数组|
广播|2|PD|向量化|形状|
布尔索引|2|PD|NumPy 数组|
Series|2|PD|NumPy 数组|
DataFrame|2|PD|Series|
索引|2|PD|DataFrame|
loc 与 iloc|2|PD|索引|
条件筛选|2|PD|布尔索引|DataFrame|
链式操作|2|PD|DataFrame|
合并|2|PD|DataFrame|
连接方式|2|PD|合并|
拼接|2|PD|DataFrame|
分组聚合|2|PD|DataFrame|
拆分-应用-合并|2|PD|分组聚合|
透视表|2|PD|分组聚合|
交叉表|2|PD|透视表|
宽表与长表|2|PD|透视表|
窗口函数|2|PD|分组聚合|
时间索引|2|PD|索引|时间序列数据|
重采样|2|PD|时间索引|
滚动窗口|2|PD|时间索引|窗口函数|
字符串方法|2|PD|Series|
分类数据类型|2|PD|数据类型|类别型数据|
内存优化|2|PD|分类数据类型|
数据源|3|COLL|数据|
数据采集|3|COLL|数据源|
文件编码|3|COLL|数据采集|
CSV|3|COLL|文件编码|
Excel 文件|3|COLL|数据采集|
JSON|3|COLL|半结构化数据|
JSON 展平|3|COLL|JSON|DataFrame|
Parquet|3|COLL|数据采集|内存优化|
关系数据库|3|COLL|数据源|数据库
SQL 查询|3|COLL|关系数据库|数据库
数据库连接|3|COLL|SQL 查询|
SQLite|3|COLL|关系数据库|
API|3|COLL|数据源|
HTTP 请求|3|COLL|API|
请求参数|3|COLL|HTTP 请求|
状态码|3|COLL|HTTP 请求|
分页|3|COLL|请求参数|
限流|3|COLL|HTTP 请求|
API 密钥|3|COLL|API|
网页采集|3|COLL|HTTP 请求|网络爬虫
robots 协议|3|COLL|网页采集|网络爬虫
增量采集|3|COLL|数据采集|时间索引|
采集日志|3|COLL|数据采集|
数据质量|4|CLEAN|数据|
完整性|4|CLEAN|数据质量|
准确性|4|CLEAN|数据质量|
一致性|4|CLEAN|数据质量|
唯一性|4|CLEAN|数据质量|
及时性|4|CLEAN|数据质量|
有效性|4|CLEAN|数据质量|
数据质量评估报告|4|CLEAN|完整性|准确性|一致性|唯一性|及时性|有效性|
数据清洗|4|CLEAN|数据质量|机器学习
缺失值|4|CLEAN|完整性|机器学习
缺失机制|4|CLEAN|缺失值|
删除法|4|CLEAN|缺失值|
填充法|4|CLEAN|缺失值|分组聚合|
重复值|4|CLEAN|唯一性|
主键|4|CLEAN|唯一性|关系数据库|
异常值|4|CLEAN|准确性|机器学习
3σ 法则|4|CLEAN|异常值|
箱线图法|4|CLEAN|异常值|
业务规则校验|4|CLEAN|有效性|
格式统一|4|CLEAN|一致性|字符串方法|
单位换算|4|CLEAN|一致性|
日期解析|4|CLEAN|格式统一|时间索引|
正则表达式|4|CLEAN|字符串方法|
文本清洗|4|CLEAN|正则表达式|
数据整合|4|CLEAN|合并|主键|
实体对齐|4|CLEAN|数据整合|
清洗规范|4|CLEAN|数据清洗|
清洗流水线|4|CLEAN|清洗规范|链式操作|
数据字典|4|CLEAN|清洗规范|
数据标注|5|LABEL|训练数据|
标签体系|5|LABEL|数据标注|类别型数据|
标注任务|5|LABEL|数据标注|
文本分类标注|5|LABEL|标注任务|
序列标注|5|LABEL|标注任务|
实体标注|5|LABEL|序列标注|自然语言处理
BIO 标注|5|LABEL|实体标注|自然语言处理
目标框标注|5|LABEL|标注任务|计算机视觉
图像分割标注|5|LABEL|目标框标注|计算机视觉
关键点标注|5|LABEL|标注任务|
语音转写|5|LABEL|标注任务|语音技术
时间戳标注|5|LABEL|语音转写|
偏好标注|5|LABEL|标注任务|自然语言处理
指令数据|5|LABEL|偏好标注|自然语言处理
标注规范|5|LABEL|标签体系|
边界规则|5|LABEL|标注规范|
疑难样例|5|LABEL|标注规范|
标注工具|5|LABEL|数据标注|
Label Studio|5|LABEL|标注工具|
标注模板|5|LABEL|Label Studio|
标注项目|5|LABEL|Label Studio|
标注导出格式|5|LABEL|标注项目|JSON|
COCO 格式|5|LABEL|标注导出格式|目标框标注|
YOLO 格式|5|LABEL|标注导出格式|目标框标注|计算机视觉
标注质量|6|LABEL|标注规范|
标注准确率|6|LABEL|标注质量|
一致率|6|LABEL|标注质量|
Kappa 系数|6|LABEL|一致率|
交并比|6|LABEL|目标框标注|计算机视觉
金标准数据|6|LABEL|标注准确率|
抽样检验|6|LABEL|标注质量|
验收标准|6|LABEL|抽样检验|
标注审核|6|LABEL|验收标准|
返工|6|LABEL|标注审核|
标注审核报告|6|LABEL|标注审核|
多人标注|6|LABEL|一致率|
多数投票|6|LABEL|多人标注|
标签噪声|6|LABEL|标注质量|
预标注|6|LABEL|标注项目|
主动学习|6|LABEL|预标注|机器学习
标注效率|6|LABEL|预标注|
众包|6|LABEL|多人标注|
数据增强|6|LABEL|训练数据|开发框架
合成数据|6|LABEL|数据增强|
描述统计|7|STAT|数值型数据|
集中趋势|7|STAT|描述统计|
离散程度|7|STAT|描述统计|
分位数|7|STAT|离散程度|
分布|7|STAT|描述统计|
偏度|7|STAT|分布|
正态分布|7|STAT|分布|
长尾分布|7|STAT|分布|
频数分析|7|STAT|类别型数据|描述统计|
探索性数据分析|7|STAT|描述统计|数据质量|机器学习
相关系数|7|STAT|描述统计|机器学习
相关与因果|7|STAT|相关系数|
辛普森悖论|7|STAT|分组聚合|相关与因果|
总体与样本|7|STAT|描述统计|
抽样方法|7|STAT|总体与样本|
分层抽样|7|STAT|抽样方法|
置信区间|7|STAT|总体与样本|正态分布|
假设检验|7|STAT|置信区间|
原假设|7|STAT|假设检验|
p 值|7|STAT|原假设|
显著性水平|7|STAT|p 值|
t 检验|7|STAT|假设检验|
卡方检验|7|STAT|假设检验|交叉表|
A/B 测试|7|STAT|t 检验|分层抽样|
指标体系|7|STAT|数据驱动|
数据可视化|8|VIS|描述统计|
图表选择|8|VIS|数据可视化|
柱状图|8|VIS|图表选择|
折线图|8|VIS|图表选择|时间序列数据|
散点图|8|VIS|图表选择|相关系数|
直方图|8|VIS|图表选择|分布|
箱线图|8|VIS|图表选择|分位数|
热力图|8|VIS|图表选择|相关系数|
饼图|8|VIS|图表选择|
地理图|8|VIS|图表选择|
Matplotlib|8|VIS|数据可视化|
中文字体配置|8|VIS|Matplotlib|
seaborn|8|VIS|Matplotlib|
pyecharts|8|VIS|数据可视化|
交互式图表|8|VIS|pyecharts|
数据看板|8|VIS|交互式图表|指标体系|
Streamlit|8|VIS|数据看板|
误导性图表|8|VIS|图表选择|
数据分析报告|8|VIS|数据看板|假设检验|
数据叙事|8|VIS|数据分析报告|
建模流程|9|MODEL|CRISP-DM|机器学习
特征|9|MODEL|训练数据|机器学习
训练集与测试集|9|MODEL|训练数据|机器学习
数据泄露|9|MODEL|训练集与测试集|机器学习
scikit-learn 流水线|9|MODEL|清洗流水线|特征|机器学习
列转换器|9|MODEL|scikit-learn 流水线|
回归模型|9|MODEL|建模流程|机器学习
分类模型|9|MODEL|建模流程|机器学习
聚类|9|MODEL|建模流程|机器学习
混淆矩阵|9|MODEL|分类模型|机器学习
精确率与召回率|9|MODEL|混淆矩阵|机器学习
用户分群|9|MODEL|聚类|
RFM 模型|9|MODEL|用户分群|分组聚合|
特征重要性|9|MODEL|分类模型|机器学习
错误案例分析|9|MODEL|混淆矩阵|
预训练模型|9|MODEL|建模流程|开发框架
模型推理|9|MODEL|预训练模型|
大模型辅助分析|9|MODEL|模型推理|自然语言处理
模型文件|9|MODEL|分类模型|开发框架
推荐系统|10|REC|用户分群|
用户-物品矩阵|10|REC|推荐系统|宽表与长表|
显式反馈|10|REC|用户-物品矩阵|
隐式反馈|10|REC|用户-物品矩阵|
热门推荐|10|REC|推荐系统|
基于内容的推荐|10|REC|推荐系统|特征|
相似度|10|REC|用户-物品矩阵|
余弦相似度|10|REC|相似度|
协同过滤|10|REC|相似度|
基于用户的协同过滤|10|REC|协同过滤|
基于物品的协同过滤|10|REC|协同过滤|
矩阵分解|10|REC|协同过滤|
召回与排序|10|REC|协同过滤|
冷启动|10|REC|协同过滤|
推荐评估|10|REC|推荐系统|精确率与召回率|
命中率|10|REC|推荐评估|
覆盖率|10|REC|推荐评估|
信息茧房|10|REC|推荐系统|导论
智能系统|11|OPS|模型推理|
部署方式|11|OPS|智能系统|开发框架
批量预测|11|OPS|部署方式|
在线服务|11|OPS|部署方式|API|开发框架
系统运维|11|OPS|智能系统|
运行日志|11|OPS|系统运维|采集日志|
监控指标|11|OPS|系统运维|指标体系|
告警|11|OPS|监控指标|
数据漂移|11|OPS|分布|监控指标|
概念漂移|11|OPS|数据漂移|
PSI|11|OPS|数据漂移|
坏案例|11|OPS|错误案例分析|运行日志|
人工反馈|11|OPS|坏案例|
数据闭环|11|OPS|人工反馈|预标注|
模型更新|11|OPS|数据闭环|
运维报告|11|OPS|监控指标|坏案例|
优化需求|11|OPS|运维报告|
数据伦理|12|ETH|数据|导论
个人信息|12|ETH|数据伦理|
敏感个人信息|12|ETH|个人信息|
知情同意|12|ETH|个人信息|
个人信息保护法|12|ETH|个人信息|导论
数据安全法|12|ETH|数据伦理|
数据分类分级|12|ETH|数据安全法|
数据脱敏|12|ETH|敏感个人信息|
假名化|12|ETH|数据脱敏|
匿名化|12|ETH|假名化|
最小必要原则|12|ETH|个人信息保护法|
算法偏见|12|ETH|训练数据|数据伦理|导论
样本偏差|12|ETH|算法偏见|抽样方法|
数据合规检查|12|ETH|数据分类分级|数据脱敏|最小必要原则|
综合项目|12|ETH|数据分析报告|运维报告|数据合规检查|
"""

BOOKS = {"大数据": "《大数据技术处理技术》", "机器学习": "《机器学习》",
         "开发框架": "《人工智能开发框架技术》", "自然语言处理": "《自然语言处理导论》",
         "导论": "《人工智能导论》", "计算机视觉": "《计算机视觉及应用实战》",
         "语音技术": "《TTS、SST 与语音克隆》", "网络爬虫": "网络爬虫技术（课程）",
         "Python": "Python 程序设计（课程）", "数据库": "数据库基础与应用（课程）"}

def parse():
    rows = []
    for line in RAW.strip().splitlines():
        parts = line.split("|")
        name, ch, cat = parts[0], int(parts[1]), parts[2]
        more = parts[-1]
        deps = [p for p in parts[3:-1] if p]
        rows.append(dict(name=name, ch=ch, cat=cat, deps=deps, more=more))
    return rows

def main(outdir):
    rows = parse()
    ids = {r["name"]: i + 1 for i, r in enumerate(rows)}
    assert len(ids) == len(rows), "重复概念"
    for r in rows:
        for d in r["deps"]:
            assert d in ids, f"{r['name']} 的先修 {d} 不存在"
            assert ids[d] < ids[r["name"]], f"{r['name']} 的先修 {d} 排在它后面"
        for m in (r["more"].split("；") if r["more"] else []):
            assert m in BOOKS, m
    with open(f"{outdir}/learning-graph.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ConceptID", "ConceptLabel", "Dependencies", "TaxonomyID", "Chapter", "FurtherReading"])
        for r in rows:
            w.writerow([ids[r["name"]], r["name"], "|".join(str(ids[d]) for d in r["deps"]),
                        r["cat"], r["ch"], r["more"]])
    edges = sum(len(r["deps"]) for r in rows)
    dependents = collections.Counter(d for r in rows for d in r["deps"])
    cc = collections.Counter(r["cat"] for r in rows)
    out = ["# 《人工智能数据分析与处理》学习图谱概念清单（大纲阶段草案）", "",
           f"共 **{len(rows)} 个概念、{edges} 条先修关系**，分 {len(CATS)} 类，检查过无环（先修都排在后续之前）。"
           "“深入学习”一列标出这个概念在系列里由哪本书或哪门课讲透，本书只做速记并链接过去；空白表示由本书讲透。", "",
           "| 类别 | 概念数 |", "|---|---|"]
    for k, v in CATS.items():
        out.append(f"| {v} | {cc[k]} |")
    out.append("")
    for ch in range(1, len(CHAPTERS)):
        sub = [r for r in rows if r["ch"] == ch]
        out += [f"## 第 {ch} 章 {CHAPTERS[ch]}（{len(sub)} 个）", "",
                "| 概念 | 类别 | 直接先修 | 深入学习 |", "|---|---|---|---|"]
        for r in sub:
            more = "、".join(BOOKS[m] for m in r["more"].split("；")) if r["more"] else ""
            out.append(f"| {r['name']} | {CATS[r['cat']]} | {'、'.join(r['deps']) or '—'} | {more} |")
        out.append("")
    open(f"{outdir}/概念清单.md", "w", encoding="utf-8").write("\n".join(out))
    roots = [r["name"] for r in rows if not r["deps"]]
    leaves = [r["name"] for r in rows if dependents[r["name"]] == 0]
    print(len(rows), "concepts", edges, "edges; roots", roots, "; leaves", len(leaves))
    print({CATS[k]: cc[k] for k in CATS})
    print("per chapter", sorted(collections.Counter(r["ch"] for r in rows).items()))

main(sys.argv[1])
