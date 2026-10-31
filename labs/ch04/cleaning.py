"""实验 4-3 用到的清洗函数。把实验 4-2 的步骤写成函数，以后新到一批数据，调用一次就能按同样的规范清洗。"""
import re

import pandas as pd


def clean_orders(df, shops):
    """按《订单数据清洗规范》清洗原始订单表，返回清洗后的新表（不改动传入的原表）"""
    df = df.drop_duplicates().copy()
    t = df["下单时间"].str.replace("/", "-").str.replace("年", "-").str.replace("月", "-").str.replace("日", "")
    df["下单时间"] = pd.to_datetime(t, format="mixed")
    df["城区"] = df["城区"].str.removesuffix("区").fillna(df["shop_id"].map(shops.set_index("shop_id")["城区"]))
    df["配送距离"] = pd.to_numeric(df["配送距离"].str.replace("km", ""))
    for col in ["就餐人数", "订单金额", "优惠金额", "实付金额", "送达时长"]:
        df[col] = pd.to_numeric(df[col])
    fen = ((df["实付金额"] / 100 - (df["订单金额"] - df["优惠金额"])).abs() < 0.05) & (df["实付金额"] > 0)
    df.loc[fen, "实付金额"] = (df.loc[fen, "实付金额"] / 100).round(1)
    bad = df["优惠金额"] > df["订单金额"]
    df.loc[bad, "优惠金额"] = (df.loc[bad, "订单金额"] - df.loc[bad, "实付金额"]).round(1)
    df["送达时长"] = df["送达时长"].abs()
    df.loc[df["送达时长"] > 180, "送达时长"] = None
    df["距离为填充值"] = df["配送距离"].isna()
    df["配送距离"] = df["配送距离"].fillna(df.groupby("城区")["配送距离"].transform("median"))
    return df


AD = re.compile(r"(加微信|代写好评|关注公众号).*$")              # 广告：从关键词开始到结尾
HTML = re.compile(r"&nbsp;|<[^>]+>")                         # 网页残留：&nbsp; 和 <br> 这类标签
PHONE = re.compile(r"1[3-9]\d{9}")                           # 手机号：1 开头、第二位 3–9、共 11 位
PUNCT = re.compile(r"([！!？?。，])\1+")                       # 连续重复的标点


def clean_review(text):
    """清洗一条评论：去广告、去网页残留、手机号打码、重复标点只留一个、去首尾空格"""
    text = AD.sub("", text)
    text = HTML.sub("，", text)
    text = PHONE.sub("[手机号]", text)
    text = PUNCT.sub(r"\1", text)
    return text.strip(" ，")
