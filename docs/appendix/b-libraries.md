---
title: 附录 B 常用工具速查
description: 本书用到的 pandas、NumPy、Matplotlib、seaborn、pyecharts、Streamlit、SciPy、statsmodels、scikit-learn、cleanlab、requests、正则表达式和 Label Studio 的常用写法速查
---

# 附录 B 常用工具速查

本附录按工具分节，列出书中实验**真正用到的**写法，并注明第一次出现的章节，方便做实验或写项目时查找。表中 `df` 表示一个 DataFrame，`s` 表示一个 Series（一列）。安装方法见[附录 C](c-environment.md)。

## B.1 pandas：读写数据

```python
import pandas as pd
df = pd.read_csv("../data/orders.csv")                 # 读 CSV
df = pd.read_csv("商家名录_gbk.csv", encoding="gbk")    # 读 GBK 编码的 CSV（Excel 另存的常见）
df = pd.read_excel("商家评分_按城区.xlsx", sheet_name=None)   # 读 Excel；None 表示读全部工作表
df.to_csv("结果.csv", index=False, encoding="utf-8-sig")       # 保存，Excel 打开不乱码
```

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `pd.read_csv(f, encoding=..., dtype={"手机号": str})` | 读 CSV；`dtype` 指定某列按文字读，避免手机号、编号前面的 0 丢失 | 2.2、3.2 |
| `pd.read_excel(f, sheet_name=...)` | 读 Excel 的一个或全部工作表 | 3.2 |
| `pd.read_json(f)`、`pd.json_normalize(数据)` | 读 JSON；把嵌套的 JSON 展平成表 | 3.2 |
| `pd.read_parquet(f)`、`df.to_parquet(f)` | 读写 Parquet 列式文件 | 3.2 |
| `pd.read_sql(sql, conn)` | 用 SQL 从数据库取数，见 B.12 | 3.3 |
| `df.to_csv(f, index=False, encoding="utf-8-sig")` | 保存 CSV | 2.2 |
| `pd.set_option("display.max_columns", None)` | 打印时显示所有列 | 2.2 |

## B.2 pandas：查看和选取

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `df.head(n)`、`df.tail(n)`、`df.sample(n, random_state=1)` | 看前 n 行、后 n 行、随机 n 行 | 2.2 |
| `df.shape`、`len(df)`、`df.columns`、`df.dtypes` | 行列数、行数、列名、每列类型 | 2.2 |
| `df.info()`、`df.describe()` | 每列非空数和类型；数值列的描述统计 | 2.2 |
| `df["列"]`、`df[["列1", "列2"]]` | 选一列（得到 Series）、选多列（得到 DataFrame） | 2.3 |
| `df[df["实付金额"] > 100]` | 条件筛选 | 2.3 |
| `df[(条件1) & (条件2)]`、`df[(条件1) \| (条件2)]` | 同时满足、满足其一；每个条件都要加括号 | 2.3 |
| `df[df["城区"].isin(["天河", "越秀"])]` | 值在列表里 | 2.3 |
| `df["送达时长"].between(30, 45)` | 在区间内（含两端） | 4.4 |
| `df.query("就餐人数 >= 4")` | 用文字写条件筛选 | 2.3 |
| `df.loc[行条件, "列"]`、`df.iloc[0:5, 0:3]` | 按标签选、按位置选 | 2.3 |
| `df.sort_values("列", ascending=False)` | 排序 | 2.3 |
| `df.nlargest(10, "列")` | 取最大的 10 行 | 7.2 |
| `s.unique()`、`s.nunique()`、`s.value_counts()` | 不重复的值、个数、每个值出现几次 | 2.3 |
| `s.value_counts(normalize=True)` | 每个值的占比 | 4.3 |

## B.3 pandas：新增、修改和清洗

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `df["客单价"] = df["实付金额"] / df["就餐人数"]` | 新增计算列（整列一起算） | 2.3 |
| `df.loc[df["送达时长"] < 0, "送达时长"] = None` | 把满足条件的值改掉 | 4.4 |
| `df["城区"].map(对照字典)`、`s.replace({"旧": "新"})` | 按对照表换值 | 4.5 |
| `s.apply(函数)` | 对每个值调用一个函数 | 4.6 |
| `s.astype(int)`、`pd.to_numeric(s, errors="coerce")` | 转换类型；转不了的变成缺失值 | 4.5 |
| `df.rename(columns={"旧名": "新名"})` | 改列名 | 4.5 |
| `df.isna().sum()`、`df.dropna(subset=["列"])`、`s.fillna(值)` | 每列缺失数；删除缺失行；填充缺失值 | 4.3 |
| `df.groupby("城区")["列"].transform("median")` | 按组算中位数，并对齐到每一行（按组填充） | 4.3 |
| `df.duplicated(subset=[...])`、`df.drop_duplicates()` | 判断重复、删除重复 | 4.2 |
| `s.clip(下限, 上限)`、`s.where(条件, 其他值)` | 把超出范围的值截到边界；不满足条件的换掉 | 4.4 |
| `pd.get_dummies(df["菜系"])`、`s.str.get_dummies("\|")` | 把类别变成 0/1 列；把“深夜营业\|网红店”这样的标签拆成多列 | 9.3、10.2 |

## B.4 pandas：文本和日期

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `s.str.len()`、`s.str.strip()` | 文字长度；去掉两头空格 | 4.6 |
| `s.str.contains("送得慢")`、`s.str.contains(正则)` | 是否包含某段文字或某种模式 | 4.6 |
| `s.str.replace(正则, "[手机号]", regex=True)` | 替换，如把手机号换成占位符 | 4.6 |
| `s.str.extract(r"广州市(.+?)区")` | 用正则表达式提取一部分 | 12.4 |
| `s.str.removesuffix("区")` | 去掉结尾的某几个字 | 8.5 |
| `pd.to_datetime(s, errors="coerce")` | 把文字转换成日期时间 | 2.6 |
| `s.dt.year`、`s.dt.month`、`s.dt.hour`、`s.dt.day_of_week` | 取年、月、小时、星期几（0 是周一） | 2.6 |
| `df.set_index("下单时间").resample("MS")["实付金额"].sum()` | 按月汇总（`"D"` 按天、`"W"` 按周） | 2.6 |
| `(日期1 - 日期2).dt.days` | 两个日期相差几天 | 9.5 |

## B.5 pandas：分组、透视和合并

```python
# 分组统计：每个城区的订单数、平均实付金额、总实付金额
df.groupby("城区").agg(订单数=("order_id", "count"),
                       平均实付=("实付金额", "mean"),
                       总实付=("实付金额", "sum")).round(1)
```

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `df.groupby("列")["另一列"].mean()` | 分组求平均（`sum`、`count`、`max`、`median` 同理） | 2.4 |
| `df.groupby([...]).agg(新列名=("列", "函数"))` | 一次算多个统计量，并起好列名 | 2.4 |
| `pd.pivot_table(df, index=, columns=, values=, aggfunc=)` | 透视表 | 2.4 |
| `pd.crosstab(df["行"], df["列"], normalize="index")` | 交叉表（计数或行百分比） | 2.4 |
| `pd.merge(左表, 右表, on="shop_id", how="left")` | 合并（VLOOKUP）；`how` 可选 `inner`、`left`、`right`、`outer` | 2.5 |
| `pd.concat([表1, 表2])` | 上下拼接 | 2.5 |
| `s.idxmax()`、`df.corr(numeric_only=True)` | 最大值所在的行；相关系数矩阵 | 7.3 |

## B.6 NumPy

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `import numpy as np`、`np.array([1, 2, 3])` | 导入；创建数组 | 2.7 |
| `a.shape`、`a.mean()`、`a.sum()`、`np.quantile(a, 0.95)` | 形状；平均；求和；分位数（如 P95 延迟） | 2.7、11.2 |
| `np.random.default_rng(42)` | 带随机种子的随机数生成器，结果可重复 | 6.5、12.4 |
| `np.log1p(x)` | 取对数（先加 1），让右偏的数据不那么“偏” | 9.5 |
| `np.histogram(a, bins=10)` | 分箱计数（计算 PSI 时用） | 11.3 |

## B.7 Matplotlib 和 seaborn

```python
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC",
                                   "WenQuanYi Zen Hei", "Noto Sans CJK SC"]   # 中文字体
plt.rcParams["axes.unicode_minus"] = False
fig, axes = plt.subplots(1, 2, figsize=(10, 4))    # 一行两个子图
s.plot(kind="bar", ax=axes[0], title="各区订单数")  # pandas 直接画图
axes[1].hist(df["送达时长"], bins=30)
plt.tight_layout(); plt.savefig("图.png", dpi=150)
```

| 图表 | 写法 | 适合 | 首次出现 |
|---|---|---|---|
| 条形图 | `s.plot(kind="bar")`、横向 `kind="barh"` | 比较各类的多少 | 8.2 |
| 折线图 | `s.plot()` | 随时间的变化趋势 | 8.2 |
| 饼图 | `s.plot(kind="pie", autopct="%.0f%%")` | 占比（类别不超过 5 个） | 8.2 |
| 直方图 | `plt.hist(s, bins=30)` | 一个数值的分布 | 7.1 |
| 箱线图 | `df.boxplot(column=, by=)`、`sns.boxplot(data=df, x=, y=)` | 比较几组的分布、看异常值 | 7.2 |
| 散点图 | `df.plot(kind="scatter", x=, y=)` | 两个数值的关系 | 7.3 |
| 热力图 | `sns.heatmap(表, annot=True, cmap="Blues")` | 交叉表、相关矩阵 | 7.3 |

中文显示成方框的处理办法见[附录 C](c-environment.md) 的 C.3 节。

## B.8 pyecharts 和 Streamlit

```python
from pyecharts.charts import Bar
from pyecharts import options as opts
bar = (Bar().add_xaxis(["天河", "越秀"]).add_yaxis("GMV（万元）", [150.7, 112.3])
       .set_global_opts(title_opts=opts.TitleOpts(title="各区 GMV")))
bar.render("各区GMV.html")             # 生成网页，用浏览器打开
```

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `Bar`、`Line`、`Pie`、`Map("广州")` | 条形图、折线图、饼图、地图 | 8.5 |
| `opts.DataZoomOpts()` | 加一个可拖动的缩放条 | 8.5 |
| `Page().add(图1, 图2)` | 把几张图放在一个网页里，做成看板 | 8.5 |
| `streamlit run 文件.py` | 在命令行运行 Streamlit 程序，浏览器自动打开 | 8.5 |
| `st.title()`、`st.columns(4)`、`列.metric()`、`st.dataframe()`、`st.line_chart()` | 标题、分栏、指标卡、表格、简单图表 | 8.5 |
| `st.sidebar.multiselect()`、`st.sidebar.slider()` | 侧边栏的多选框、滑块 | 8.5 |
| `@st.cache_data` | 写在读数据函数的上一行，数据只读一次，加快速度 | 8.5 |

## B.9 SciPy 和 statsmodels：统计检验

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `stats.ttest_ind(a, b, equal_var=False)` | 两组平均值是否有差异（t 检验） | 7.5 |
| `stats.chi2_contingency(交叉表)` | 两个类别变量是否有关联（卡方检验） | 7.5 |
| `stats.t.interval(0.95, df=n-1, loc=均值, scale=stats.sem(a))` | 平均值的 95% 置信区间 | 7.4 |
| `proportions_ztest(成功数, 样本数)` | 两组比例（如转化率）是否有差异，A/B 测试用 | 7.6 |
| `confint_proportions_2indep(...)` | 两组比例之差的置信区间 | 7.6 |
| `fleiss_kappa(aggregate_raters(表)[0])` | 多名标注员的一致性 | 6.1 |

## B.10 scikit-learn：建模

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Pipeline([("tfidf", TfidfVectorizer(analyzer="char", ngram_range=(1, 2))),
                  ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))])
model.fit(X_train, y_train)            # 训练
pred = model.predict(X_test)           # 预测
```

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `train_test_split(X, y, test_size=0.2, random_state=42)` | 划分训练集和测试集 | 9.2 |
| `Pipeline([...])`、`StandardScaler()` | 流水线；标准化 | 9.2 |
| `LinearRegression()`、`RandomForestRegressor()` | 线性回归、随机森林（预测数值） | 9.3 |
| `LogisticRegression()`、`TfidfVectorizer()` | 逻辑回归（分类）；把文字变成 TF-IDF 特征 | 9.4 |
| `KMeans(n_clusters=4, random_state=42)` | K 均值聚类 | 9.5 |
| `model.fit()`、`model.predict()`、`model.predict_proba()` | 训练；预测；预测每类的概率 | 9.2 |
| `mean_absolute_error`、`r2_score` | 回归的评估指标 | 9.3 |
| `accuracy_score`、`confusion_matrix`、`classification_report` | 分类的评估指标 | 9.4 |
| `cohen_kappa_score(a, b)` | 两名标注员的一致性 | 6.1 |
| `cross_val_predict(...)` | 交叉验证预测（找噪声标签时用） | 6.4 |
| `cosine_similarity(矩阵)`、`TruncatedSVD(n_components=10)` | 余弦相似度；矩阵分解 | 10.2、10.4 |
| `joblib.dump(model, "m.joblib")`、`joblib.load(...)` | 保存和加载模型 | 9.4 |

## B.11 cleanlab 和 Label Studio：标注

| 写法 / 操作 | 作用 | 首次出现 |
|---|---|---|
| `find_label_issues(labels, pred_probs, return_indices_ranked_by="self_confidence")` | 找出可能标错的样本，按可疑程度排序 | 6.4 |
| `label-studio start` | 启动 Label Studio，打开 `http://localhost:8080` | 5.5 |
| 新建项目 → Labeling Setup → Code | 粘贴标注模板（XML），见 `labs/ch05/评论标注模板.xml` | 5.5 |
| Import / Export | 导入 CSV、JSON、图片；导出 JSON、CSV、COCO、YOLO | 5.5 |

## B.12 requests、json、sqlite3 和正则表达式

```python
import requests, json, sqlite3, re
r = requests.get(url, params={"page": 1}, headers={"X-API-Key": key}, timeout=10)
r.status_code, r.json()                         # 状态码；把返回的 JSON 变成字典
conn = sqlite3.connect("../data/ch03/shike.db")
df = pd.read_sql("SELECT * FROM orders WHERE 城区 = '天河'", conn)
re.sub(r"1[3-9]\d{9}", "[手机号]", "电话18545161843")   # → '电话[手机号]'
```

| 正则写法 | 含义 | 例子 |
|---|---|---|
| `\d`、`\d{11}` | 一个数字；连续 11 个数字 | 手机号 |
| `[3-9]` | 3 到 9 中的一个 | 手机号第二位 |
| `.`、`.+?` | 任意一个字符；任意多个字符（尽量少） | `广州市(.+?)区` |
| `( )`、`(?: )` | 分组并提取；只分组不提取 | `str.extract` |
| `^`、`$` | 开头、结尾 | `^S\d{4}$` 匹配店铺编号 |
| `\|` | 或 | `送得慢\|太慢了` |

| SQL 写法 | 作用 |
|---|---|
| `SELECT 列1, 列2 FROM 表 WHERE 条件` | 选列、筛选 |
| `ORDER BY 列 DESC LIMIT 10` | 排序取前 10 |
| `GROUP BY 列`、`COUNT(*)`、`AVG(列)` | 分组统计 |
| `JOIN 表2 ON 表1.键 = 表2.键` | 连接两张表 |

SQL 的详细用法见 3.3 节，正则表达式见 4.6 节，接口调用见 3.4 节。
