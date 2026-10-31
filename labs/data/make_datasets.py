"""生成本书贯穿案例“食客说”城市美食点评平台的全部实验数据。

所有数据都是编者按真实业务的大致分布虚构生成的，不对应任何真实的人、商家和订单。
姓名、手机号、地址随机拼出，仅供第 12 章练习识别和脱敏。
运行：python labs/data/make_datasets.py      （约 20 秒，结果固定，可重复生成）
"""
from pathlib import Path
import json
import sqlite3

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(2026)

DISTRICTS = ["天河", "越秀", "海珠", "荔湾", "白云", "番禺", "黄埔", "花都"]
D_WEIGHT = np.array([0.20, 0.14, 0.15, 0.10, 0.14, 0.13, 0.08, 0.06])
CUISINES = {  # 菜系: (人均价格均值, 代表菜品)
    "粤菜": (85, ["白切鸡", "烧鹅", "虾饺", "肠粉", "叉烧", "煲仔饭"]),
    "湘菜": (65, ["剁椒鱼头", "小炒黄牛肉", "辣椒炒肉", "口味虾"]),
    "川菜": (70, ["水煮鱼", "麻婆豆腐", "回锅肉", "毛血旺"]),
    "火锅": (110, ["毛肚", "肥牛", "鸭肠", "虾滑"]),
    "烧烤": (75, ["烤羊肉串", "烤鸡翅", "烤茄子", "烤生蚝"]),
    "快餐": (28, ["猪脚饭", "黄焖鸡", "牛肉面", "鸡腿饭"]),
    "甜品饮品": (32, ["双皮奶", "杨枝甘露", "奶茶", "芒果班戟"]),
    "日料": (150, ["三文鱼刺身", "寿司拼盘", "鳗鱼饭", "天妇罗"]),
    "西餐": (130, ["牛排", "意面", "披萨", "沙拉"]),
    "面馆": (30, ["云吞面", "牛腩面", "炸酱面", "酸辣粉"]),
}
C_NAMES = list(CUISINES)
C_WEIGHT = np.array([0.18, 0.10, 0.10, 0.09, 0.08, 0.15, 0.10, 0.06, 0.06, 0.08])
TAGS = ["环境好", "适合聚餐", "有包间", "老字号", "网红店", "性价比高", "出餐快", "可停车", "深夜营业", "适合约会"]
SURNAMES = list("陈李黄张梁林刘吴罗何郑杨谢周叶王蔡许邓冯")
GIVEN = list("伟芳娜敏静丽强磊军洋勇艳杰涛明超秀霞平刚桂英华建国志文玲婷")
ROADS = ["中山大道", "天河路", "体育东路", "江南大道", "工业大道", "黄埔大道", "广园路", "北京路", "东风路", "市桥大北路"]


def make_shops(n=300):
    cuisine = rng.choice(C_NAMES, n, p=C_WEIGHT)
    district = rng.choice(DISTRICTS, n, p=D_WEIGHT)
    prefix = ["老", "阿", "小", "大", "金", "福", "鲜", "好", "旺", "鸿"]
    mid = ["记", "家", "姐", "哥", "城", "味", "坊", "轩", "居", "阁"]
    names, prices, tags = [], [], []
    for i, c in enumerate(cuisine):
        base = CUISINES[c][0]
        names.append(f"{rng.choice(prefix)}{rng.choice(mid)}{c if c != '甜品饮品' else '甜品'}（{district[i]}店）")
        prices.append(int(max(15, rng.normal(base, base * 0.2))))
        k = rng.integers(1, 4)
        tags.append("|".join(rng.choice(TAGS, k, replace=False)))
    open_days = rng.integers(0, 365 * 8, n)
    shops = pd.DataFrame({
        "shop_id": [f"S{i:04d}" for i in range(1, n + 1)],
        "店名": names, "城区": district, "菜系": cuisine, "人均价格": prices,
        "开业日期": (pd.Timestamp("2025-01-01") - pd.to_timedelta(open_days, unit="D")).date,
        "标签": tags,
        "品质分": np.round(np.clip(rng.normal(0, 1, n), -2.5, 2.5), 2),  # 隐藏的“真实好吃程度”，只用于生成数据
    })
    return shops


def make_users(n=5000):
    gender = rng.choice(["男", "女"], n, p=[0.46, 0.54])
    age = rng.choice(["18-24", "25-30", "31-40", "41-50", "50以上"], n, p=[0.22, 0.30, 0.28, 0.13, 0.07])
    names = [rng.choice(SURNAMES) + "".join(rng.choice(GIVEN, rng.integers(1, 3))) for _ in range(n)]
    phones = ["1" + str(rng.choice([3, 5, 7, 8, 9])) + "".join(map(str, rng.integers(0, 10, 9))) for _ in range(n)]
    district = rng.choice(DISTRICTS, n, p=D_WEIGHT)
    addr = [f"广州市{d}区{rng.choice(ROADS)}{rng.integers(1, 999)}号{rng.integers(1, 30)}栋{rng.integers(101, 2999)}房"
            for d in district]
    reg = pd.Timestamp("2022-01-01") + pd.to_timedelta(rng.integers(0, 365 * 3 + 300, n), unit="D")
    users = pd.DataFrame({
        "user_id": [f"U{i:05d}" for i in range(1, n + 1)],
        "昵称": [f"食客{rng.integers(1000, 99999)}" for _ in range(n)],
        "姓名": names, "性别": gender, "年龄段": age, "手机号": phones,
        "常住城区": district, "收货地址": addr, "注册日期": reg.date,
        "活跃度": np.round(rng.gamma(1.2, 1.0, n), 3),  # 隐藏参数
    })
    return users


def make_orders(shops, users, n=60000):
    act = users["活跃度"].to_numpy()
    uid = rng.choice(users.index, n, p=act / act.sum())
    # 用户更常去本区和偏好的菜系；商家受欢迎程度跟品质分有关
    pop = np.exp(0.6 * shops["品质分"].to_numpy())
    sid = np.empty(n, dtype=int)
    home = users["常住城区"].to_numpy()
    shop_d = shops["城区"].to_numpy()
    same = {d: np.where(shop_d == d)[0] for d in DISTRICTS}
    for i in range(n):
        if rng.random() < 0.7:
            cand = same[home[uid[i]]]
        else:
            cand = np.arange(len(shops))
        p = pop[cand] / pop[cand].sum()
        sid[i] = rng.choice(cand, p=p)
    # 下单时间：一年，午餐和晚餐两个高峰，周末多一些，12 月多一些
    day = rng.integers(0, 365, n)
    date = pd.Timestamp("2025-01-01") + pd.to_timedelta(day, unit="D")
    weekend = date.day_of_week >= 5
    keep = rng.random(n) < np.where(weekend, 1.0, 0.82)
    hour = rng.choice(np.arange(24), n, p=_hour_p())
    minute = rng.integers(0, 60, n)
    ts = date + pd.to_timedelta(hour, unit="h") + pd.to_timedelta(minute, unit="m") + pd.to_timedelta(rng.integers(0, 60, n), unit="s")
    price = shops["人均价格"].to_numpy()[sid]
    people = rng.choice([1, 1, 1, 2, 2, 3, 4], n)
    amount = np.round(price * people * rng.lognormal(0, 0.25, n), 1)
    discount = np.where(rng.random(n) < 0.35, np.round(np.minimum(amount * 0.3, rng.choice([5, 8, 10, 15, 20], n)), 1), 0.0)
    method = rng.choice(["平台专送", "商家自送"], n, p=[0.68, 0.32])
    dist = np.round(np.clip(rng.gamma(2.2, 1.1, n), 0.2, 12), 1)
    rain = rng.random(n) < np.where(date.month.isin([5, 6, 7, 8, 9]), 0.35, 0.12)
    peak = np.isin(hour, [11, 12, 18, 19])
    dur = 14 + 3.4 * dist + 7 * peak + 6 * rain + np.where(method == "商家自送", 4.5, 0) + rng.normal(0, 4, n)
    dur = np.round(np.clip(dur, 8, None)).astype(int)
    orders = pd.DataFrame({
        "order_id": [f"O{i:06d}" for i in range(1, n + 1)],
        "user_id": users["user_id"].to_numpy()[uid],
        "shop_id": shops["shop_id"].to_numpy()[sid],
        "下单时间": ts, "就餐人数": people, "订单金额": amount, "优惠金额": discount,
        "实付金额": np.round(amount - discount, 1), "配送方式": method, "配送距离": dist,
        "天气": np.where(rain, "雨", "晴"), "送达时长": dur,
    })[keep].sort_values("下单时间").reset_index(drop=True)
    orders["order_id"] = [f"O{i:06d}" for i in range(1, len(orders) + 1)]
    return orders


def _hour_p():
    w = np.array([1, 0.5, 0.3, 0.2, 0.2, 0.3, 1, 2.5, 3, 2.5, 4, 12, 13, 5, 3, 3, 3.5, 7, 12, 10, 6, 4, 3, 2])
    return w / w.sum()


# ---------------- 评论文本 ----------------
ASPECT = {
    "口味": {"pos": ["{dish}味道很正宗", "{dish}做得特别好吃", "{dish}鲜嫩入味", "口味很赞，{dish}必点", "{dish}一绝，回味无穷", "菜品味道在线"],
             "neg": ["{dish}太咸了", "{dish}一点味道都没有", "{dish}不新鲜，有股怪味", "味道很一般，{dish}踩雷了", "{dish}又冷又硬", "口味不行"]},
    "服务": {"pos": ["服务员很热情", "老板人很好", "服务周到，主动加茶", "上菜很快"],
             "neg": ["服务员态度很差", "叫了三次都没人理", "上菜太慢了，等了四十分钟", "收银员爱答不理"]},
    "环境": {"pos": ["环境干净整洁", "装修很有格调", "座位宽敞", "适合朋友聚会"],
             "neg": ["环境太吵", "桌子油腻腻的", "店面很小很挤", "卫生堪忧，地上有垃圾"]},
    "价格": {"pos": ["性价比很高", "价格实惠", "分量足，价格公道", "用了优惠券很划算"],
             "neg": ["价格偏贵", "分量太少不值这个价", "性价比很低", "比别家贵一倍"]},
    "配送": {"pos": ["外卖送得很快", "骑手很准时", "包装很严实", "送到还是热的"],
             "neg": ["外卖送了一个多小时", "汤洒了一袋子", "骑手送错地址", "送到都凉了"]},
}
NEUTRAL = ["还行吧", "中规中矩", "一般般，没什么特别的", "第一次来，感觉普通", "和以前差不多"]
OPEN_POS = ["", "下次还会再来", "推荐！", "五星好评", "强烈推荐给大家"]
OPEN_NEG = ["", "不会再来了", "差评", "大家避雷", "失望"]
EMOJI_POS = ["😋", "👍", "❤️", "[赞]", "[憨笑]"]
EMOJI_NEG = ["😡", "👎", "[怒]", "[失望]"]
ADS = ["加微信 {wx} 领五元红包", "关注公众号“美食小达人”抽免单", "代写好评，私聊 {wx}"]


def make_review(dish, sentiment):
    """按给定的整体情感（正面/负面/中性）拼出一条评论，返回 (文本, 涉及方面列表)。"""
    asp_names = list(ASPECT)
    k = rng.choice([1, 2, 2, 3])
    aspects = list(rng.choice(asp_names, k, replace=False, p=[0.4, 0.17, 0.13, 0.15, 0.15]))
    parts = []
    force_tail = False
    if sentiment in ("正面", "负面"):
        main, other = ("pos", "neg") if sentiment == "正面" else ("neg", "pos")
        pols = [main] * k
        if k >= 2 and rng.random() < 0.25:  # 有褒有贬，但明显偏向一边
            pols[-1] = other
            force_tail = (k == 2)            # 两个方面一褒一贬时，用结尾的总结话表明倾向
    else:
        if k == 1:
            parts.append(rng.choice(NEUTRAL))
            aspects, pols = [], []
        else:                                 # 褒贬各一，没有明显倾向
            aspects = aspects[:2]
            pols = list(rng.permutation(["pos", "neg"]))
    for a, p in zip(aspects, pols):
        parts.append(rng.choice(ASPECT[a][p]).format(dish=dish))
    if sentiment == "中性" and rng.random() < 0.6:
        parts.append(rng.choice(NEUTRAL))
    pool = OPEN_POS if sentiment == "正面" else OPEN_NEG if sentiment == "负面" else [""]
    tail = rng.choice(pool[1:] if force_tail else pool)
    if tail:
        parts.append(tail)
    sep = rng.choice(["，", "，", "。", "！", " "])
    text = sep.join(parts)
    # 但是/不过 让“正面为主”更像真话
    if sentiment in ("正面", "负面") and len(parts) >= 2 and rng.random() < 0.3:
        text = text.replace(sep, "，不过", 1) if pols[0] != pols[-1] else text
    if rng.random() < 0.18:
        text += rng.choice(EMOJI_POS if sentiment == "正面" else EMOJI_NEG if sentiment == "负面" else ["🤔", "[思考]"])
    return text, aspects


def make_reviews(orders, shops, n=12000, start_id=1, period=None, drift=False):
    o = orders.sample(n=n, random_state=int(rng.integers(1e9))).sort_values("下单时间").reset_index(drop=True)
    sh = shops.set_index("shop_id")
    q = sh.loc[o["shop_id"], "品质分"].to_numpy()
    late = (o["送达时长"].to_numpy() > 45)
    score = 0.9 * q - 0.8 * late + rng.normal(0, 1, n)
    sentiment = np.where(score > 0.25, "正面", np.where(score < -0.75, "负面", "中性"))
    texts, aspects, stars = [], [], []
    for i in range(n):
        c = sh.loc[o.loc[i, "shop_id"], "菜系"]
        dish = rng.choice(CUISINES[c][1])
        t, a = make_review(dish, sentiment[i])
        if drift and rng.random() < 0.3:  # 第 11 章：上线后出现的新说法
            t = rng.choice(["{d}是预制菜吧，", "绝绝子，{d}", "{d}拔草了，", "{d}yyds，", "纯纯冤种，"]).format(d=dish) + t
        texts.append(t)
        aspects.append("|".join(a))
        base = {"正面": [4, 5, 5], "负面": [1, 1, 2], "中性": [3, 3, 4, 2]}[sentiment[i]]
        stars.append(int(rng.choice(base)))
    rv = pd.DataFrame({
        "review_id": [f"R{i:06d}" for i in range(start_id, start_id + n)],
        "order_id": o["order_id"], "user_id": o["user_id"], "shop_id": o["shop_id"],
        "评分": stars, "评论内容": texts,
        "评论时间": o["下单时间"] + pd.to_timedelta(rng.integers(1, 72, n), unit="h"),
        "情感_参考": sentiment, "方面_参考": aspects,
    })
    return rv


def add_review_noise(rv):
    """第 4 章文本清洗用：给评论加广告、HTML 残留、手机号、重复标点等噪声。"""
    rv = rv.copy()
    t = rv["评论内容"].to_numpy().astype(object)
    idx = rng.random(len(t))
    for i in range(len(t)):
        if idx[i] < 0.03:
            t[i] = t[i] + " " + rng.choice(ADS).format(wx="wx" + str(rng.integers(10000, 99999)))
        elif idx[i] < 0.05:
            t[i] = t[i].replace("，", "&nbsp;", 1) + "<br>"
        elif idx[i] < 0.065:
            t[i] = t[i] + f"，有事打我电话1{rng.choice([3, 5, 8])}{rng.integers(100000000, 999999999)}"
        elif idx[i] < 0.10:
            t[i] = t[i] + "！！！！！"
        elif idx[i] < 0.115:
            t[i] = "   " + t[i] + "   "
        elif idx[i] < 0.125:
            t[i] = "。。。"  # 无意义评论
    rv["评论内容"] = t
    return rv


def make_dirty_orders(orders, shops):
    """第 4 章：在干净订单上人为制造六类质量问题，并记录每类问题的数量。"""
    d = orders.merge(shops[["shop_id", "城区"]], on="shop_id").sort_values("order_id").reset_index(drop=True)
    d = d.sample(n=8000, random_state=4).sort_values("order_id").reset_index(drop=True)
    d["下单时间"] = d["下单时间"].dt.strftime("%Y-%m-%d %H:%M:%S")
    d = d.astype({"下单时间": object, "城区": object, "实付金额": object, "配送距离": object})
    n = len(d)
    log = {}
    # 1 缺失
    m = rng.random(n) < 0.04
    d.loc[m, "配送距离"] = np.nan
    log["配送距离缺失"] = int(m.sum())
    m = rng.random(n) < 0.02
    d.loc[m, "城区"] = np.nan
    log["城区缺失"] = int(m.sum())
    # 2 格式不一致：日期写法
    m = rng.random(n) < 0.06
    d.loc[m, "下单时间"] = pd.to_datetime(d.loc[m, "下单时间"]).dt.strftime("%Y/%m/%d %H:%M")
    log["日期写成斜杠格式"] = int(m.sum())
    m = (rng.random(n) < 0.03) & ~m
    d.loc[m, "下单时间"] = pd.to_datetime(d.loc[m, "下单时间"]).dt.strftime("%Y年%m月%d日 %H:%M")
    log["日期写成中文格式"] = int(m.sum())
    # 城区写法不一
    m = rng.random(n) < 0.08
    d.loc[m & d["城区"].notna(), "城区"] = d.loc[m & d["城区"].notna(), "城区"] + "区"
    log["城区多了“区”字"] = int((m & d["城区"].str.endswith("区", na=False)).sum())
    # 3 单位不一致：实付金额按“分”录入
    m = rng.random(n) < 0.01
    d.loc[m, "实付金额"] = (d.loc[m, "实付金额"].astype(float) * 100).round(0)
    log["实付金额按分录入"] = int(m.sum())
    # 配送距离带单位
    m = (rng.random(n) < 0.05) & d["配送距离"].notna()
    d.loc[m, "配送距离"] = d.loc[m, "配送距离"].astype(str) + "km"
    log["配送距离带km"] = int(m.sum())
    # 4 异常：负的送达时长、超长送达
    m = rng.random(n) < 0.004
    d.loc[m, "送达时长"] = -d.loc[m, "送达时长"]
    log["送达时长为负"] = int(m.sum())
    m = rng.random(n) < 0.003
    d.loc[m, "送达时长"] = rng.integers(300, 900, m.sum())
    log["送达时长超过300分钟"] = int(m.sum())
    # 5 业务规则：优惠大于订单金额
    m = rng.random(n) < 0.003
    d.loc[m, "优惠金额"] = d.loc[m, "订单金额"] + 5
    log["优惠金额大于订单金额"] = int(m.sum())
    # 6 重复
    dup = d.sample(n=120, random_state=5)
    d = pd.concat([d, dup]).sort_values("order_id").reset_index(drop=True)
    log["完全重复的行"] = 120
    cols = ["order_id", "user_id", "shop_id", "城区", "下单时间", "就餐人数", "订单金额", "优惠金额",
            "实付金额", "配送方式", "配送距离", "天气", "送达时长"]
    return d[cols], log


def make_annotators(rv, n=300):
    """第 6 章：三名标注员对同一批 300 条评论的情感标注（标注员 C 容易把“中性”标成“正面”）。"""
    s = rv.sample(n=n, random_state=6).reset_index(drop=True)
    truth = s["情感_参考"].to_numpy()
    labels = ["正面", "负面", "中性"]
    out = {"review_id": s["review_id"], "评论内容": s["评论内容"]}
    for name, acc, bias in [("标注员A", 0.92, None), ("标注员B", 0.88, None), ("标注员C", 0.80, "正面")]:
        lab = truth.copy()
        for i in range(n):
            if rng.random() > acc:
                if bias and truth[i] == "中性" and rng.random() < 0.8:
                    lab[i] = bias
                else:
                    lab[i] = rng.choice([x for x in labels if x != truth[i]])
        out[name] = lab
    df = pd.DataFrame(out)
    df["金标准"] = truth
    return df


def make_batch(rv, n=2000):
    """第 6 章：一批 2000 条待验收的标注，错误率约 6.5%，错误集中在标注员 W03。"""
    s = rv.sample(n=n, random_state=7).reset_index(drop=True)
    workers = rng.choice(["W01", "W02", "W03", "W04"], n, p=[0.3, 0.3, 0.2, 0.2])
    err = np.where(workers == "W03", 0.18, 0.035)
    lab = s["情感_参考"].to_numpy().copy()
    wrong = rng.random(n) < err
    for i in np.where(wrong)[0]:
        lab[i] = rng.choice([x for x in ["正面", "负面", "中性"] if x != lab[i]])
    return pd.DataFrame({"task_id": [f"T{i:05d}" for i in range(1, n + 1)], "review_id": s["review_id"],
                         "评论内容": s["评论内容"], "标注员": workers, "情感标签": lab,
                         "情感_参考": s["情感_参考"]})


def make_ab():
    """第 7 章：A/B 测试。ab_test.csv 为随机分组的规范试验；ab_simpson.csv 为按城区投放的不规范试验。"""
    n = 20000
    grp = rng.choice(["A", "B"], n)
    old = rng.random(n) < 0.5
    p = np.where(old, 0.10, 0.05) + np.where(grp == "B", 0.008, 0)
    ab = pd.DataFrame({"user_id": [f"V{i:05d}" for i in range(n)], "版本": grp,
                       "城区类型": np.where(old, "老城区", "新城区"), "是否下单": (rng.random(n) < p).astype(int)})
    # 辛普森：B 版主要投放在转化率低的新城区
    n2 = 12000
    old2 = rng.random(n2) < 0.5
    grp2 = np.where(old2, np.where(rng.random(n2) < 0.2, "B", "A"), np.where(rng.random(n2) < 0.8, "B", "A"))
    p2 = np.where(old2, 0.12, 0.04) + np.where(grp2 == "B", 0.01, 0)
    simpson = pd.DataFrame({"user_id": [f"W{i:05d}" for i in range(n2)], "版本": grp2,
                            "城区类型": np.where(old2, "老城区", "新城区"), "是否下单": (rng.random(n2) < p2).astype(int)})
    return ab, simpson


def make_logs(model_rv_old, model_rv_new):
    """第 11 章：情感分析服务 8 周的调用日志（JSON Lines）。第 5 周起出现新说法、延迟上升。"""
    rows = []
    t0 = pd.Timestamp("2026-03-02")
    frames = [(w, model_rv_old if w < 4 else model_rv_new) for w in range(8)]
    k = 0
    for w, src in frames:
        m = 1500 + int(rng.integers(-100, 100))
        s = src.sample(n=m, random_state=100 + w)
        for _, r in s.iterrows():
            ts = t0 + pd.Timedelta(days=7 * w) + pd.Timedelta(seconds=int(rng.integers(0, 7 * 86400)))
            lat = float(np.round(rng.gamma(4, 12 if w < 6 else 20), 1))
            status = 200 if rng.random() > (0.004 if w < 6 else 0.02) else int(rng.choice([500, 504]))
            rows.append({"time": ts.isoformat(), "request_id": f"req{k:06d}", "review_id": r["review_id"],
                         "text": r["评论内容"], "latency_ms": lat, "status": status})
            k += 1
    return pd.DataFrame(rows).sort_values("time").reset_index(drop=True)


def draw_tables(n=20):
    """第 5、6 章：画 20 张简笔“餐桌俯视图”，有碗、盘子、杯子三类物体，同时输出参考框。"""
    img_dir = OUT / "images"
    img_dir.mkdir(exist_ok=True)
    gt = []
    for i in range(1, n + 1):
        W, H = 640, 480
        im = Image.new("RGB", (W, H), tuple(int(x) for x in rng.integers(150, 210, 3)))
        dr = ImageDraw.Draw(im)
        for _ in range(30):  # 桌面纹理
            y = int(rng.integers(0, H))
            dr.line([(0, y), (W, y + int(rng.integers(-20, 20)))], fill=tuple(int(x) for x in rng.integers(130, 190, 3)), width=2)
        boxes = []
        for _ in range(int(rng.integers(2, 6))):
            cls = rng.choice(["碗", "盘子", "杯子"])
            r = {"碗": 45, "盘子": 70, "杯子": 28}[cls] + int(rng.integers(-8, 9))
            for _try in range(50):
                cx, cy = int(rng.integers(r + 5, W - r - 5)), int(rng.integers(r + 5, H - r - 5))
                if all(abs(cx - b[1]) > r + b[3] or abs(cy - b[2]) > r + b[3] for b in boxes):
                    break
            boxes.append((cls, cx, cy, r))
            if cls == "盘子":
                dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(245, 245, 240), outline=(120, 120, 120), width=3)
                dr.ellipse([cx - r * 0.6, cy - r * 0.6, cx + r * 0.6, cy + r * 0.6], fill=tuple(int(x) for x in rng.integers(120, 220, 3)))
            elif cls == "碗":
                dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(230, 230, 250), outline=(60, 60, 140), width=5)
                dr.ellipse([cx - r * 0.7, cy - r * 0.7, cx + r * 0.7, cy + r * 0.7], fill=(200, 150, 90))
            else:
                dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255), outline=(30, 30, 30), width=3)
                dr.ellipse([cx - r * 0.75, cy - r * 0.75, cx + r * 0.75, cy + r * 0.75], fill=(110, 70, 40))
                dr.rectangle([cx + r - 2, cy - 6, cx + r + 14, cy + 6], fill=(255, 255, 255), outline=(30, 30, 30))
        name = f"table_{i:02d}.jpg"
        im.save(img_dir / name, quality=90)
        for cls, cx, cy, r in boxes:
            x2 = cx + r + (14 if cls == "杯子" else 0)
            gt.append({"图片": name, "类别": cls, "x_min": cx - r, "y_min": cy - r, "x_max": x2, "y_max": cy + r})
    pd.DataFrame(gt).to_csv(OUT / "images_boxes_参考.csv", index=False, encoding="utf-8-sig")


def main():
    shops = make_shops()
    users = make_users()
    orders = make_orders(shops, users)
    reviews = make_reviews(orders, shops)
    reviews_noisy = add_review_noise(reviews)

    # ---- 基础四张表（第 1、2、7、8、9、10 章）----
    shops.drop(columns="品质分").to_csv(OUT / "shops.csv", index=False, encoding="utf-8-sig")
    users.drop(columns="活跃度").to_csv(OUT / "users.csv", index=False, encoding="utf-8-sig")
    orders.to_csv(OUT / "orders.csv", index=False, encoding="utf-8-sig")
    reviews.drop(columns=["情感_参考", "方面_参考"]).to_csv(OUT / "reviews.csv", index=False, encoding="utf-8-sig")
    reviews[["review_id", "情感_参考", "方面_参考"]].to_csv(OUT / "reviews_参考答案.csv", index=False, encoding="utf-8-sig")

    # ---- 第 3 章：多种格式与数据库 ----
    src = OUT / "ch03"
    src.mkdir(exist_ok=True)
    shops.drop(columns="品质分").to_csv(src / "商家名录_gbk.csv", index=False, encoding="gbk")
    with pd.ExcelWriter(src / "商家评分_按城区.xlsx") as xw:
        sc = shops.drop(columns="品质分").copy()
        sc["平均评分"] = np.round(np.clip(4.0 + 0.35 * shops["品质分"] + rng.normal(0, 0.15, len(shops)), 2.5, 5.0), 1)
        for d in DISTRICTS:
            sc[sc["城区"] == d][["shop_id", "店名", "平均评分"]].to_excel(xw, sheet_name=d, index=False)
    conn = sqlite3.connect(src / "shike.db")
    orders.assign(下单时间=orders["下单时间"].dt.strftime("%Y-%m-%d %H:%M:%S")).to_sql("orders", conn, if_exists="replace", index=False)
    shops.drop(columns="品质分").to_sql("shops", conn, if_exists="replace", index=False)
    conn.close()
    # 接口原始返回（嵌套 JSON），供 3.2 节和模拟接口使用
    sub = reviews.head(30)
    payload = {"code": 0, "msg": "ok", "data": {"page": 1, "page_size": 30, "total": len(reviews), "items": [
        {"review_id": r.review_id, "shop": {"shop_id": r.shop_id}, "user": {"user_id": r.user_id},
         "rating": int(r.评分), "content": r.评论内容, "created_at": r.评论时间.isoformat()} for r in sub.itertuples()]}}
    (src / "reviews_page1.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    reviews_noisy.drop(columns=["情感_参考", "方面_参考"]).to_csv(src / "api_reviews_all.csv", index=False, encoding="utf-8-sig")

    # ---- 第 4 章：脏数据 ----
    dirty, log = make_dirty_orders(orders, shops)
    dirty.to_csv(OUT / "orders_raw.csv", index=False, encoding="utf-8-sig")
    (OUT / "orders_raw_问题清单.json").write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    reviews_noisy[["review_id", "评论内容"]].to_csv(OUT / "reviews_raw.csv", index=False, encoding="utf-8-sig")

    # ---- 第 5、6 章：标注 ----
    ann = OUT / "annotation"
    ann.mkdir(exist_ok=True)
    reviews.sample(n=100, random_state=5)[["review_id", "评论内容"]].to_csv(ann / "to_label_100.csv", index=False, encoding="utf-8-sig")
    make_annotators(reviews).to_csv(ann / "three_annotators.csv", index=False, encoding="utf-8-sig")
    make_batch(reviews).to_csv(ann / "batch_2000.csv", index=False, encoding="utf-8-sig")
    draw_tables()

    # ---- 第 7 章：A/B 测试 ----
    ab, simpson = make_ab()
    ab.to_csv(OUT / "ab_test.csv", index=False, encoding="utf-8-sig")
    simpson.to_csv(OUT / "ab_simpson.csv", index=False, encoding="utf-8-sig")

    # ---- 第 11 章：上线后的评论与日志 ----
    late_rv = make_reviews(orders, shops, n=6000, start_id=500001, drift=True)
    late_rv[["review_id", "评论内容", "情感_参考"]].to_csv(OUT / "reviews_online.csv", index=False, encoding="utf-8-sig")
    logs = make_logs(reviews, late_rv)
    with open(OUT / "service_log.jsonl", "w", encoding="utf-8") as f:
        for r in logs.to_dict("records"):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("商家", len(shops), "用户", len(users), "订单", len(orders), "评论", len(reviews))
    print("情感分布", reviews["情感_参考"].value_counts().to_dict())
    print("脏订单", len(dirty), log)
    print("日志", len(logs))


if __name__ == "__main__":
    main()
