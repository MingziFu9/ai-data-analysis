# 实验代码

按章存放，`chNN/` 对应第 NN 章，每章有一个 `README.md` 说明各个文件。文件名 `labN_M_英文短名.py` 是第 N 章实验 N-M，`demo_*.py` 是正文里的演示。公共数据放在 `data/`，见 `data/README.md`。

## 安装（只需一次）

推荐 Python 3.11（3.10–3.12 都可以）。在 `labs` 文件夹里打开终端：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

装好后运行第 1 章的环境检查：`cd ch01`，再 `python lab1_1_check_env.py`。不会安装的同学先看附录 C。

## 运行

**先进入这一章的文件夹再运行**，例如：

```bash
cd labs/ch07
python lab7_1_eda.py
```

程序会读取 `../data/` 里的数据，输出的数字应当和教材正文里的“运行结果”一致。图片和结果文件保存在当前文件夹。

## 说明

- 标 ★ 的实验给出完整代码：先读懂、运行，再按“运行并修改”改参数观察变化。标 ☆ 的是选做。
- 需要联网或额外安装的实验（第 3 章的模拟接口要先启动 `mock_api.py`；第 5 章 Label Studio；第 9 章预训练模型、大模型预标注），文件开头的注释写明了运行条件。
- 第 11 章会读取第 9 章保存的情感模型 `ch09/sentiment_model.joblib`，没有也能运行（自动重新训练）。
