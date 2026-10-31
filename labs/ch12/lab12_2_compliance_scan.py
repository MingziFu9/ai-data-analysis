"""实验 12-2：对本书用过的数据文件做一次个人信息扫描，生成合规检查表的“自动检查”部分"""
from pathlib import Path
import sqlite3
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
PATTERNS = {"手机号": r"(?<!\d)1[3-9]\d{9}(?!\d)",
            "详细地址": r"(?:路|街|道)\d+号",
            "身份证号": r"(?<!\d)\d{17}[\dXx](?!\d)"}
NAME_COLS = ["姓名", "name", "收货人"]                 # 列名就说明是姓名的


def scan(df, file):
    rows = []
    for col in df.columns:
        s = df[col].astype(str)
        for kind, pat in PATTERNS.items():
            n = s.str.contains(pat, regex=True).sum()
            if n:
                rows.append({"文件": file, "列": col, "发现": kind, "条数": n, "示例": s[s.str.contains(pat)].iloc[0][:30]})
        if col in NAME_COLS:
            rows.append({"文件": file, "列": col, "发现": "姓名", "条数": s.ne("").sum(), "示例": s.iloc[0]})
    return rows


def read_any(f):
    """先按 UTF-8 读，读不了再按 GBK 读（第 3 章的编码问题）"""
    try:
        return pd.read_csv(f, dtype=str)
    except UnicodeDecodeError:
        return pd.read_csv(f, dtype=str, encoding="gbk")


found = []
for f in sorted(DATA.glob("*.csv")) + sorted(DATA.glob("*/*.csv")):
    found += scan(read_any(f), str(f.relative_to(DATA)))
found += scan(pd.read_json(DATA / "service_log.jsonl", lines=True, dtype=str), "service_log.jsonl")
with sqlite3.connect(DATA / "ch03" / "shike.db") as con:              # 第 3 章的数据库，逐张表检查
    for t in pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", con)["name"]:
        found += scan(pd.read_sql(f"SELECT * FROM {t}", con).astype(str), f"ch03/shike.db 的 {t} 表")
result = pd.DataFrame(found)
print(result.to_string(index=False))

# 检查表：自动扫描能回答的项目先填上，其余留给人工检查
checklist = pd.DataFrame([
    ("收集", "是否只收集了业务必需的个人信息（最小必要）", "人工"),
    ("收集", "收集前是否告知用途并取得同意", "人工"),
    ("存储", "含个人信息的文件", "、".join(sorted(result["文件"].unique()))),
    ("存储", "个人信息是否已脱敏或加密存储", "否：上表文件中仍有明文" if len(result) else "是"),
    ("使用", "标注、分析时是否只使用脱敏后的数据", "人工"),
    ("使用", "运行日志中是否记录了评论原文等可能含个人信息的内容", "是：service_log.jsonl 的 text 列" if "service_log.jsonl" in set(result["文件"]) else "人工"),
    ("提供", "是否把个人信息发送给外部接口或大模型（如实验 9-3）", "人工"),
    ("删除", "是否规定了数据和日志的保存期限，到期删除", "人工"),
    ("算法", "推荐、定价是否对不同用户实行不合理的差别待遇", "人工"),
    ("算法", "是否提供关闭个性化推荐的选项", "人工"),
], columns=["环节", "检查项", "检查结果"])
checklist["整改措施"] = ""
checklist.to_csv(Path(__file__).with_name("合规检查表.csv"), index=False, encoding="utf-8-sig")
print(checklist.to_string(index=False))
