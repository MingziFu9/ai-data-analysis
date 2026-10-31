"""实验 3-3 调用接口分页采集评论：带重试、写采集日志、支持增量采集。
运行方法：先在一个窗口运行 python mock_api.py，再在另一个窗口（labs/ch03 目录）运行 python lab3_3_fetch_reviews.py
"""
import os
import time
from datetime import datetime

import pandas as pd
import requests

URL = "http://127.0.0.1:8800/api/reviews"
HEADERS = {"X-API-Key": os.environ.get("SHIKE_API_KEY", "shike-demo-key")}  # 密钥优先从环境变量读
OUT, LOG = "reviews_api.csv", "采集日志.txt"


def log(text):
    """同时打印到屏幕和写进采集日志"""
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} {text}"
    print(line)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def get_page(page, since, max_try=5):
    """取一页；遇到 429（太频繁）或 500（服务器故障）就等一会儿再试，最多试 max_try 次"""
    for i in range(1, max_try + 1):
        r = requests.get(URL, headers=HEADERS, timeout=10,
                         params={"page": page, "page_size": 100, "since": since})
        if r.status_code == 200:
            return r.json()["data"]
        wait = int(r.headers.get("Retry-After", 2))
        log(f"第 {page} 页第 {i} 次请求失败，状态码 {r.status_code}，{wait} 秒后重试")
        time.sleep(wait)
    raise RuntimeError(f"第 {page} 页连续 {max_try} 次失败，停止采集")


# 增量采集：如果以前采过，只要上次最新一条评论之后的数据
old = pd.read_csv(OUT) if os.path.exists(OUT) else None
since = old["created_at"].max() if old is not None else ""
log(f"开始采集，since = {since or '（全量）'}")

items, page = [], 1
while True:
    data = get_page(page, since)
    items += data["items"]
    if page * data["page_size"] >= data["total"]:          # 已经取到最后一页
        break
    page += 1
    time.sleep(0.3)                                          # 每页之间稍等，对接口友好（限流是每秒 4 次）

new = pd.json_normalize(items)
log(f"本次共 {page} 页，新增 {len(new)} 条")
all_rows = pd.concat([old, new]) if old is not None else new
all_rows = all_rows.drop_duplicates("review_id")             # 防止重复采集同一条
all_rows.to_csv(OUT, index=False, encoding="utf-8-sig")
log(f"已保存 {OUT}，累计 {len(all_rows)} 条")
