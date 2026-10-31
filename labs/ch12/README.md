# 第 12 章 数据伦理、隐私合规与综合项目：实验代码

| 文件 | 用途 | 运行方式 |
|---|---|---|
| lab12_1_masking.py | 实验 12-1 找出个人信息字段，用掩码、哈希、泛化、扰动脱敏，检查脱敏后的可用性和准标识符风险 | `python lab12_1_masking.py` |
| lab12_2_compliance_scan.py | 实验 12-2 扫描 `data/` 下所有文件（含 GBK 编码和 SQLite 数据库），找出含个人信息的文件和字段，生成合规检查表 | `python lab12_2_compliance_scan.py` |
| lab12_bias_demo.py | 12.5 节演示：只用平台专送订单训练送达时间模型，对商家自送订单系统性少估 | `python lab12_bias_demo.py` |
| lab12_3_project_starter.py | 实验 12-3 综合项目的起步代码：采集 → 脱敏 → 清洗 → 情感分析 → 分组统计 → 出图，结果写到 `项目输出/` | `python lab12_3_project_starter.py` |

都在 `labs/ch12` 文件夹下运行。实验 12-3 会用到第 9 章保存的情感模型，没有的话自动重新训练。
`项目输出/` 和 `合规检查表.csv` 是运行生成的，不提交到仓库；里面的数据虽然已经脱敏，也只在本机使用。
