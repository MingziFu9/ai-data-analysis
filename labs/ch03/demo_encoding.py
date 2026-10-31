"""3.2 节演示：同一段中文在 UTF-8 和 GBK 下的字节，以及“用错编码”时出现的乱码。"""
text = "食客说"
print("UTF-8 字节：", text.encode("utf-8"))        # 每个汉字 3 个字节
print("GBK   字节：", text.encode("gbk"))          # 每个汉字 2 个字节
print("GBK 存、UTF-8 读：", text.encode("gbk").decode("utf-8", errors="replace"))
print("UTF-8 存、GBK 读：", text.encode("utf-8").decode("gbk", errors="replace"))
