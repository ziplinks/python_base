# r模式 打开文件为只读模式
# f = open("E:/个人.txt", "r", encoding="UTF-8")
import time

# w模式 文件不存在 会自动创建,文件存在会自动覆盖（血的教训）
# f = open("E:/个人.txt", "w", encoding="UTF-8")
# f.write("hello world")
# f.flush()

# a模式 文件不存在会自动创建,文件存在会在尾部追加内容
f = open("E:/个人.txt", "w", encoding="UTF-8")
f.write("\n这是一行测试python写入文字")

# print(f"读取前10个字节：{f.read(10)}")

# 需要注意的是f.read()是接着上次打印的f.read(10)之后开始读取

# print(f"读取全部内容：{f.read()}")

# print(f"读取全部行，并以list形式打印：{f.readlines()}")

# readline 调用一次读取一行，依次进行读取
# print(f"读取全部行，并以list形式打印：{f.readline()}")
# print(f"读取全部行，并以list形式打印：{f.readline()}")
# print(f"读取全部行，并以list形式打印：{f.readline()}")
# print(f"读取全部行，并以list形式打印：{f.readline()}")

# for循环读取文件

# for line in f:
#     print(f"读取的每一行文字是：{line}")

# 关闭(解除文件占用)

f.close()

# with open 这种方式会自动调用f.close()
# with open("E:/个人.txt", "r", encoding="UTF-8") as f:
#     f.readlines()
