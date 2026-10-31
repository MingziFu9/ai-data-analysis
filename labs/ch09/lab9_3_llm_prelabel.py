"""实验 9-3 第 2 部分（待实测）：调用大模型 API 给评论做情感分类和信息抽取
用法：
    1. 在大模型平台（如 DeepSeek、通义千问、文心、智谱等）注册并获取 API 密钥；
    2. 在命令行设置三个环境变量（Windows 用 set，macOS / Linux 用 export）：
         LLM_API_KEY=你的密钥
         LLM_BASE_URL=平台的“OpenAI 兼容”接口地址，如 https://api.deepseek.com
         LLM_MODEL=模型名，如 deepseek-chat
    3. 先不加参数运行，只打印提示词，不花钱：python labs/ch09/lab9_3_llm_prelabel.py
       确认无误后加 --run 真正调用：python labs/ch09/lab9_3_llm_prelabel.py --run
"""
import json, os, sys, time
from pathlib import Path
import pandas as pd
import requests

DATA = Path(__file__).resolve().parents[1] / "data"
todo = pd.read_csv(DATA / "annotation" / "to_label_100.csv")

PROMPT = """你是外卖平台的评论标注员。请按下面的规范标注这条评论，只输出 JSON，不要输出别的内容。
规范：
1. 情感：正面 / 中性 / 负面。好坏都有时看结尾的总结性表态（如“推荐”“五星好评”“不会再来”）；没有总结表态、好坏各半的标中性。
2. 方面：从 口味、服务、环境、价格、配送 中选出评论提到的（可多选，可以不选）。
3. 菜品：评论中出现的具体菜名，没有就输出空列表。
输出格式：{{"情感": "正面", "方面": ["口味"], "菜品": ["白切鸡"]}}
评论：{text}"""


def ask(text):
    """调用 OpenAI 兼容接口，返回解析后的字典"""
    resp = requests.post(
        os.environ["LLM_BASE_URL"].rstrip("/") + "/chat/completions",
        headers={"Authorization": "Bearer " + os.environ["LLM_API_KEY"]},
        json={"model": os.environ["LLM_MODEL"], "temperature": 0,
              "messages": [{"role": "user", "content": PROMPT.format(text=text)}]},
        timeout=60)
    resp.raise_for_status()
    answer = resp.json()["choices"][0]["message"]["content"]
    answer = answer.strip().removeprefix("```json").removesuffix("```")   # 有的模型会加代码块标记
    return json.loads(answer)


if "--run" not in sys.argv:
    print("【演示模式，不调用接口】第 1 条评论的提示词：\n")
    print(PROMPT.format(text=todo.loc[0, "text"]))
    sys.exit()

rows, start = [], time.time()
for _, r in todo.iterrows():
    try:
        out = ask(r["text"])
        rows.append({"review_id": r["review_id"], "大模型_情感": out.get("情感"),
                     "大模型_方面": "|".join(out.get("方面", [])), "大模型_菜品": "|".join(out.get("菜品", []))})
    except Exception as e:                       # 网络错误、返回的不是 JSON 等，记下来人工处理
        rows.append({"review_id": r["review_id"], "大模型_情感": "出错：" + str(e)[:30]})
    time.sleep(0.5)                              # 放慢速度，避免触发限流（3.5 节）
res = pd.DataFrame(rows)
ref = pd.read_csv(DATA / "reviews_参考答案.csv")
res = res.merge(ref, on="review_id")
print(f"用时 {time.time() - start:.0f} 秒")
print(f"情感准确率：{(res['大模型_情感'] == res['情感_参考']).mean():.1%}")
res.to_csv(Path(__file__).with_name("大模型预标注结果.csv"), index=False, encoding="utf-8-sig")
