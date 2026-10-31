"""“食客说”评论开放接口的本地模拟服务（实验 3-3 用）。只用 Python 标准库，不需要安装任何东西。

启动方法：在 labs/ch03 目录下执行  python mock_api.py          （模拟“第一天”：只有 2025-12-15 之前的评论）
          第二次采集前改用          python mock_api.py --day 2  （模拟“第二天”：多了之后的新评论）
看到“接口已启动”后不要关闭这个窗口，另开一个命令行窗口运行采集脚本。按 Ctrl + C 停止。

接口说明：
    地址      GET http://127.0.0.1:8800/api/reviews
    请求头    X-API-Key: shike-demo-key        （没有或不对返回 401）
    参数      page 第几页（从 1 开始）  page_size 每页条数（最多 100）  since 只要这个时间之后的评论（可选）
    限流      每秒最多 4 次请求，超过返回 429，并在 Retry-After 头里说明等几秒
    偶发错误  大约每 17 次请求有 1 次返回 500（模拟服务器临时故障），重试即可
"""
import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import csv

API_KEY = "shike-demo-key"
CUTOFF = "2025-12-15" if "--day" not in sys.argv or sys.argv[-1] != "2" else "9999"
with open("../data/ch03/api_reviews_all.csv", encoding="utf-8-sig") as f:
    ROWS = sorted((r for r in csv.DictReader(f) if r["评论时间"] < CUTOFF), key=lambda r: (r["评论时间"], r["review_id"]))
STATE = {"n": 0, "recent": []}


class Handler(BaseHTTPRequestHandler):
    def send(self, code, body, headers=None):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/api/reviews":
            return self.send(404, {"code": 404, "msg": "没有这个接口"})
        if self.headers.get("X-API-Key") != API_KEY:
            return self.send(401, {"code": 401, "msg": "API 密钥缺失或错误"})
        now = time.time()
        STATE["recent"] = [t for t in STATE["recent"] if now - t < 1] + [now]
        if len(STATE["recent"]) > 4:
            return self.send(429, {"code": 429, "msg": "请求太频繁"}, {"Retry-After": "1"})
        STATE["n"] += 1
        if STATE["n"] % 17 == 0:
            return self.send(500, {"code": 500, "msg": "服务器临时故障，请重试"})
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        page, size = int(q.get("page", 1)), min(int(q.get("page_size", 30)), 100)
        since = q.get("since", "").replace("T", " ")
        rows = [r for r in ROWS if r["评论时间"] > since] if since else ROWS
        items = [{"review_id": r["review_id"], "order_id": r["order_id"], "shop": {"shop_id": r["shop_id"]},
                  "user": {"user_id": r["user_id"]}, "rating": int(r["评分"]), "content": r["评论内容"],
                  "created_at": r["评论时间"].replace(" ", "T")} for r in rows[(page - 1) * size: page * size]]
        self.send(200, {"code": 0, "msg": "ok", "data": {"page": page, "page_size": size, "total": len(rows), "items": items}})

    def log_message(self, fmt, *args):                       # 每次请求在窗口里打印一行
        sys.stderr.write("  收到请求 %s -> %s\n" % (self.path, args[1] if len(args) > 1 else ""))


if __name__ == "__main__":
    day = "第二天" if CUTOFF == "9999" else "第一天"
    print(f"接口已启动（模拟{day}，共 {len(ROWS)} 条评论）：http://127.0.0.1:8800/api/reviews  按 Ctrl + C 停止")
    ThreadingHTTPServer(("127.0.0.1", 8800), Handler).serve_forever()
