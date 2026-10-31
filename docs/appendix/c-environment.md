---
title: 附录 C 实验环境与数据说明
description: 实验所需的软硬件、Python 与工具库的安装步骤、中文字体设置、Label Studio 的两种启动方式、数据说明、需要联网的实验和课时安排建议
---

# 附录 C 实验环境与数据说明

## C.1 软硬件要求

本书 36 个实验**全部可以在普通笔记本电脑上完成，不需要显卡**。书中的运行结果都是编者实际运行得到的，编者的环境是 Python 3.11。

| 项目 | 最低要求 | 建议 |
|---|---|---|
| 电脑 | 双核 CPU、4 GB 内存 | 4 核以上 CPU、8 GB 以上内存 |
| 操作系统 | Windows 10、macOS 12、主流 Linux | 同左 |
| 硬盘 | 剩余 3 GB | 5 GB（另装 Label Studio 时再加 1 GB） |
| Python | 3.10 | 3.11（与编者一致） |
| 浏览器 | Chrome、Edge、Firefox 的新版本 | 同左，用于 Jupyter、Label Studio 和看板 |

电脑配置较低或者不方便安装软件的同学，可以先用云 Notebook 平台（百度飞桨 AI Studio、魔搭社区 ModelScope 等），打开网页就能写代码。把 `labs` 文件夹打包上传，在平台的终端里安装 `requirements.txt` 即可。第 5 章的 Label Studio 和第 8 章的 Streamlit 要在本机打开网页，云平台上做不了，可以和同学结组用一台电脑完成。

## C.2 安装 Python 和工具库

下面分两种方式，**选一种就行**。完全没装过软件开发工具的同学建议选方式一。

### 方式一：Anaconda（图形界面，适合零基础）

1. 打开 Anaconda 官网或清华大学开源软件镜像站，下载 Windows（或 macOS）版的安装包，双击安装，选项都用默认值。
2. 安装完成后，在“开始”菜单里找到 **Anaconda Prompt** 并打开，这就是后面说的“命令行窗口”。
3. 新建一个本课程专用的虚拟环境，并激活它：

    ```bash
    conda create -n shike python=3.11      # 新建名为 shike 的环境，问 y/n 时输入 y
    conda activate shike                   # 激活；行首出现 (shike) 说明成功
    ```

4. 用 `cd` 命令进入配套资源的文件夹（例如 `cd D:\ai-data-analysis`），安装工具库：

    ```bash
    pip install -r labs/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

以后每次打开 Anaconda Prompt，都要先运行 `conda activate shike` 再做实验。

### 方式二：uv（命令行，速度快）

uv 是一个新的 Python 安装和管理工具，下载和安装都比 pip 快很多。

```bash
# 1 安装 uv（Windows 在 PowerShell 里运行第一行；macOS / Linux 运行第二行）
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
curl -LsSf https://astral.sh/uv/install.sh | sh
# 2 在配套资源文件夹里新建虚拟环境，并装上 Python 3.11
uv venv --python 3.11
# 3 激活：Windows 写 .venv\Scripts\activate，macOS / Linux 写下面这行
source .venv/bin/activate
# 4 安装工具库
uv pip install -r labs/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 检查环境

装好以后，进入 `labs/ch01` 文件夹，运行实验 1-1 的自检程序：

```bash
cd labs/ch01
python lab1_1_check_env.py
```

每个库都显示“通过”，最后画出一张带中文的图，就说明环境没问题了。显示“缺少”的库，按提示单独安装。

**所有实验都要先进入它所在的文件夹再运行**（例如第 7 章的实验先 `cd labs/ch07`），程序才能找到 `../data/` 里的数据。用 Jupyter 的同学，把 Notebook 文件也放在对应章节的文件夹里。

### 编者实测的版本

`labs/requirements.txt` 里列出了编者实测的版本。版本号写的是“至少”，装更新的版本一般也能运行。

| 库 | 编者的版本 | 用途 | 主要用在 |
|---|---|---|---|
| pandas | 3.1.0 | 表格数据处理 | 全书 |
| NumPy | 2.4.6 | 数组计算 | 第 2 章起 |
| Matplotlib | 3.11.2 | 画图 | 第 1、7、8 章起 |
| seaborn | 0.13.2 | 统计图 | 第 8 章 |
| SciPy | 1.17.1 | 假设检验 | 第 7 章 |
| statsmodels | 0.15.0 | A/B 测试 | 第 7 章 |
| scikit-learn | 1.9.1 | 机器学习 | 第 6、9～12 章 |
| cleanlab | 2.9.0 | 找疑似标错的样本 | 第 6 章 |
| pyecharts | 2.1.0 | 交互图表 | 第 8 章 |
| Streamlit | 1.66.1 | 数据看板 | 第 8 章 |
| requests | 2.34.2 | 调用接口 | 第 3、9 章 |
| openpyxl | 3.1.5 | 读写 Excel | 第 2、3 章 |
| pyarrow | 26.0.0 | Parquet 文件 | 第 3 章 |
| jieba | 0.42.1 | 中文分词 | 第 1 章自检 |
| Label Studio | 1.23.2 | 数据标注平台（单独安装，见 C.4） | 第 5、6 章 |

## C.3 中文字体设置

Matplotlib 默认的字体不含中文，图上的中文会显示成一个个方框。本书的画图代码开头都有下面两行，它会按顺序尝试几种常见的中文字体，用第一个能找到的：

```python
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False   # 负号正常显示
```

| 系统 | 自带的中文字体 | 还是方框怎么办 |
|---|---|---|
| Windows | 黑体 SimHei、微软雅黑 | 一般不会出现；出现时检查是否把这两行放在了画图代码前面 |
| macOS | 苹方 PingFang SC | 同上 |
| Linux / 云平台 | 通常没有 | 安装文泉驿字体：`sudo apt install fonts-wqy-zenhei`，然后删除 Matplotlib 的字体缓存（`~/.cache/matplotlib`）再运行 |

运行时出现 `findfont: Font family 'SimHei' not found` 一类的警告**可以忽略**，它只是说明列表里前面几种字体没找到，接着用了后面的。只要图上中文正常，就没问题。

pyecharts 生成的是网页，中文由浏览器显示，不需要设置字体。

## C.4 Label Studio 的两种启动方式

第 5、6 章的标注实验用 Label Studio。它依赖的库较多，**建议不要和上面的工具库装在同一个环境里**。

**方式一：用 pip 或 uv 安装（推荐）。**

```bash
uv venv labelstudio-env --python 3.11      # 单独建一个环境
labelstudio-env\Scripts\activate           # Windows；macOS / Linux 用 source labelstudio-env/bin/activate
uv pip install label-studio -i https://pypi.tuna.tsinghua.edu.cn/simple
label-studio start                         # 浏览器会自动打开 http://localhost:8080
```

用 Anaconda 的同学，把前两行换成 `conda create -n labelstudio python=3.11` 和 `conda activate labelstudio`，第三行换成 `pip install label-studio`。

**方式二：用 Docker 启动。**电脑上已经装好 Docker Desktop 的同学，一条命令就能启动，不用装 Python：

```bash
docker run -it -p 8080:8080 -v ${PWD}/mydata:/label-studio/data heartexlabs/label-studio:latest
```

`-p 8080:8080` 把容器的 8080 端口映射到本机，`-v` 把标注数据保存在当前文件夹的 `mydata` 里，关掉容器后数据也不会丢。Windows 的“命令提示符”里把 `${PWD}` 换成 `%cd%`。

两种方式启动后，第一次使用都要在网页上注册一个账号，这个账号只保存在你自己的电脑上。启动的命令行窗口在标注期间不要关闭。端口 8080 被占用时，方式一加 `--port 8081`，方式二改成 `-p 8081:8080`，然后打开 `http://localhost:8081`。

## C.5 数据说明

全书贯穿案例“食客说”是编者虚构的广州美食点评平台，所有数据都放在 `labs/data/` 里，由 `make_datasets.py` 按固定随机种子生成，**教材编写，内容为虚构**，重新运行会得到完全相同的文件。全部数据约 18 MB。

| 数据 | 内容与规模 | 用于 |
|---|---|---|
| 商家表 `shops.csv` | 300 家店铺：店名、城区、菜系、人均价格、开业日期、标签 | 第 1、2、7、8、10 章 |
| 用户表 `users.csv` | 5000 名用户：昵称、姓名、性别、年龄段、手机号、常住城区、收货地址、注册日期 | 第 2、9、10、12 章 |
| 订单表 `orders.csv` | 2025 年全年 56655 单：下单时间、就餐人数、金额、配送方式、配送距离、天气、送达时长 | 第 1、2、7～10、12 章 |
| 原始订单 `orders_raw.csv` | 8120 行，故意加入了缺失、重复、异常值和格式混乱 | 第 4 章 |
| 评论 `reviews.csv`、`reviews_raw.csv` | 12000 条点评；后者只有评论内容，供标注 | 第 4～9、12 章 |
| 标注数据 `annotation/` | 练习标注的 100 条、三名标注员各标 300 条、一批 2000 条众包结果 | 第 5、6、9 章 |
| 图片 `images/` | 20 张餐桌示意图（编者用程序画的）和菜品框的参考坐标 | 第 5 章 |
| 第 3 章文件 `ch03/` | GBK 编码的商家名录、Excel 评分表、JSON 接口返回、SQLite 数据库、接口全量评论 | 第 3、12 章 |
| A/B 测试 `ab_test.csv`、`ab_simpson.csv` | 20000 和 12000 名用户的分组和是否下单 | 第 7 章 |
| 上线后的数据 `reviews_online.csv`、`service_log.jsonl` | 情感服务上线 8 周收到的 6000 条评论，11820 行调用日志 | 第 11 章 |

每个文件的详细说明见 `labs/data/README.md`。数据中故意放进了姓名、手机号、地址等“个人信息”，是为了第 4、12 章练习脱敏。它们虽然是虚构的，也请按真实个人信息的要求对待，不要上传到公开网站。

## C.6 需要联网或特殊条件的实验

除了下表，其余实验都只读取 `labs/data/` 里的数据，不需要联网。

| 实验 | 需要什么 | 说明 |
|---|---|---|
| 实验 1-1 | 联网 | 安装 Python 和工具库 |
| 实验 1-3（可选） | 能使用一个大模型对话工具 | 不用大模型也能做；想比较的同学用文心一言、通义千问、DeepSeek、Kimi 等任一网页版即可 |
| 实验 3-3 | 在本机启动模拟接口 | 先在一个窗口运行 `python mock_api.py`，再在另一个窗口运行采集程序，不需要公网 |
| 实验 5-2、5-3 | Label Studio | 见 C.4 |
| 实验 8-3 | 本机打开网页 | `streamlit run lab8_3_streamlit_app.py` 会在浏览器打开看板 |
| 实验 9-3 第 2 部分 | 大模型 API 密钥（待实测） | 在大模型平台申请密钥，按 `lab9_3_llm_prelabel.py` 开头的说明设置 `LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL`；100 条评论的费用一般不到 1 元 |
| 实验 9-3 第 3 部分 | 下载预训练模型（待实测） | 另装 `transformers` 和 `torch`，第一次运行下载约 400 MB 的模型；国内设置镜像 `HF_ENDPOINT=https://hf-mirror.com`，或改用魔搭社区 |

标“待实测”的部分，编者的编写环境无法访问模型下载站和大模型 API，所以书上没有给出运行结果，而是留了记录表，请你运行后填写。这两部分是选做的拓展内容，不做也不影响后面的学习。

## C.7 课时安排建议

全课程 4 学分、72 学时：线上理论 40 学时、线上实验 18 学时、线下理论 14 学时。线上学时用于阅读教材、操作动画、在线练习和完成实验；线下学时用于重点难点讲解、实验答疑和讨论。第 5、6 章的标注规范和质量审核需要讨论和互评，各安排 2 个线下学时。

| 章 | 理论 | 实验 | 合计 | 线上 | 线下 |
|---|---|---|---|---|---|
| 第 1 章 数据分析与处理概述 | 4 | 1 | 5 | 4 | 1 |
| 第 2 章 Python 数据处理入门：从表格到 pandas | 5 | 2 | 7 | 6 | 1 |
| 第 3 章 数据采集：文件、数据库与接口 | 4 | 2 | 6 | 5 | 1 |
| 第 4 章 数据清洗与整合 | 5 | 2 | 7 | 6 | 1 |
| 第 5 章 数据标注：任务、规范与工具 | 5 | 2 | 7 | 5 | 2 |
| 第 6 章 数据标注：质量审核与管理 | 4 | 2 | 6 | 4 | 2 |
| 第 7 章 探索性分析与统计推断 | 5 | 1 | 6 | 5 | 1 |
| 第 8 章 数据可视化与分析报告 | 5 | 2 | 7 | 6 | 1 |
| 第 9 章 建模应用：从 scikit-learn 到预训练模型 | 5 | 1 | 6 | 5 | 1 |
| 第 10 章 推荐系统 | 4 | 1 | 5 | 4 | 1 |
| 第 11 章 智能系统运维与优化 | 4 | 1 | 5 | 4 | 1 |
| 第 12 章 数据伦理、隐私合规与综合项目 | 4 | 1 | 5 | 4 | 1 |
| **合计** | **54** | **18** | **72** | **58** | **14** |

每章 3 个实验。标 ★ 的是基础实验，给出了完整代码，建议都做：先读懂代码、运行，再按“运行并修改”改参数观察变化；标 ☆ 的是拓展实验，可以留作课后选做。实验学时不够的章，教师可从 ★ 实验中选做。第 12 章的综合项目建议分组完成，课后用一到两周时间，最后一次线下课汇报。
