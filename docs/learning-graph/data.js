// 学习图谱数据：由编者整理，概念与定义取自附录 D 术语表
// 改完后运行 python tools/graph_text.py，检查数据并更新 index.md 里的文字版
var CATS = ["示例类别一", "示例类别二"];
var CHAPTERS = ["", "概述", "pandas 入门", "数据采集", "数据清洗", "标注规范与工具", "标注质量审核", "统计分析", "可视化与报告", "建模应用", "推荐系统", "系统运维", "合规与综合项目"];
var CHDIRS = ["", "01-overview", "02-pandas", "03-collection", "04-cleaning", "05-annotation", "06-annotation-qa", "07-statistics", "08-visualization", "09-modeling", "10-recommendation", "11-operations", "12-ethics-project"];
var NODES = [
  {"id": "示例术语", "ch": 1, "cat": 0, "a": "g-示例术语", "d": "这里是术语表中的定义，鼠标悬停时显示"},
  {"id": "另一个术语", "ch": 1, "cat": 1, "a": "g-另一个术语", "d": "以示例术语为基础的概念"}
];
var EDGES = [["示例术语", "另一个术语"]];
