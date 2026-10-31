"""实验 5-3 第 4 步：把 Label Studio 导出的 COCO 和 YOLO 标注框画回图片，核对框得准不准、两种格式是否一致。
运行方法：在 labs/ch05 目录下执行  python lab5_3_draw_boxes.py
"""
import json
import os
from PIL import Image, ImageDraw

COCO = "示例导出/coco/result.json"
YOLO_DIR = "示例导出/yolo/labels/"
IMG_DIR = "../data/images/"
os.makedirs("核对图", exist_ok=True)
coco = json.load(open(COCO, encoding="utf-8"))
names = {c["id"]: c["name"] for c in coco["categories"]}            # 类别编号 → 类别名
print("类别：", names, " 图片：", len(coco["images"]), " 框：", len(coco["annotations"]))

def short(path):
    """Label Studio 会在文件名前加一段随机前缀，如 a6922596-table_01.jpg，去掉它"""
    return os.path.basename(path).split("-", 1)[-1]

COLORS = {"碗": "blue", "盘子": "green", "杯子": "red"}
for img in coco["images"]:
    name = short(img["file_name"])
    im = Image.open(IMG_DIR + name).convert("RGB")
    draw = ImageDraw.Draw(im)
    for a in coco["annotations"]:
        if a["image_id"] == img["id"]:
            x, y, w, h = a["bbox"]                                  # COCO：左上角 x、y，宽，高（像素）
            draw.rectangle([x, y, x + w, y + h], outline=COLORS[names[a["category_id"]]], width=3)
    im.save("核对图/" + name)

# 用第一张图对比两种格式：YOLO 每行是“类别编号 中心x 中心y 宽 高”，都是相对图片宽高的比例
first = coco["images"][0]
yolo_file = [f for f in os.listdir(YOLO_DIR) if short(f) == short(first["file_name"]).replace(".jpg", ".txt")][0]
classes = open("示例导出/yolo/classes.txt", encoding="utf-8").read().split()
print("图片", short(first["file_name"]), "的标注：")
for line in open(YOLO_DIR + yolo_file):
    c, cx, cy, w, h = line.split()
    W, H = first["width"], first["height"]
    x = (float(cx) - float(w) / 2) * W                              # 中心点换算回左上角，比例换算回像素
    y = (float(cy) - float(h) / 2) * H
    print(f"  YOLO: {classes[int(c)]} {line.strip()}  →  像素框 x={x:.0f} y={y:.0f} 宽={float(w) * W:.0f} 高={float(h) * H:.0f}")
for a in coco["annotations"]:
    if a["image_id"] == first["id"]:
        print(f"  COCO: {names[a['category_id']]} bbox={[round(v) for v in a['bbox']]}")
print("已把框画回 20 张图片，保存在 核对图/ 文件夹")
