"""实验 1-1 环境自检：检查 Python 版本、常用库能否导入，读一张表、画一张带中文的图。
运行方法：在 labs/ch01 目录下执行  python lab1_1_check_env.py
"""
import sys
import importlib

print("Python 版本：", sys.version.split()[0])          # 本书要求 3.10 及以上，推荐 3.11

# 逐个尝试导入本书用到的库，导入成功就打印版本号
libs = ["numpy", "pandas", "matplotlib", "openpyxl", "scipy", "sklearn", "requests", "jieba"]
for name in libs:
    try:
        module = importlib.import_module(name)
        print(f"  [通过] {name:<11}{module.__version__}")
    except ImportError:
        print(f"  [缺少] {name:<11}请运行 pip install {name if name != 'sklearn' else 'scikit-learn'}")

import pandas as pd
import matplotlib
matplotlib.use("Agg")                                   # 不弹窗口，直接把图存成文件
import matplotlib.pyplot as plt

# 读一张表：“食客说”的商家表
shops = pd.read_csv("../data/shops.csv")
print("商家表读取成功：", shops.shape[0], "行", shops.shape[1], "列")

# 画一张带中文的图，检查中文能不能正常显示
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False              # 负号正常显示
counts = shops["菜系"].value_counts()                   # 每种菜系有几家店
counts.plot(kind="bar", figsize=(7, 3.5), title="各菜系商家数")
plt.ylabel("商家数")
plt.tight_layout()
plt.savefig("lab1_1_check.png", dpi=120)
print("图已保存为 lab1_1_check.png，打开看看中文是否显示正常")
