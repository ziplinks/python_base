

# 6种数据类型 数字（Number）、字符串(String)、 列表（List）、元组（Tuple）、集合（Set）、字典(Dictionary)

name = "张三"
age = 30

# 单个字符串拼接  %s 字符串占位  %d整数占位  %f浮点数占位
print("姓名 %s" % name)

# 多个字符串拼接
print("姓名 %s,年龄 %s" % (name, age))

# 方式二：字符串拼接
print(f"来吧这里是新的格式化方法名字{name},年龄:{age}")

num0 = 11.367

# 输出结果  11.37  %7.2f 7代表字符宽度，不足宽度的用空格代替 宽度小于数字本身宽度不生效（比如%1f）
#  %.2f 代表保留两位是小数（四舍五入）
print("num0 = %7.2f" % num0)

# value = input("你是？？？？")
# print(f"我知道了，你是：{value}")

# 冒号  4个空格缩进
if age > 18:
    print("成年了")


# value = input("欢迎来到游乐园,\n请输入你的年龄：")
# if int(value) >= 18:
#     print("你已成年，需要补票10元")
# else:
#     print("你未成年，可以免费游玩")
# print("祝您游玩愉快！")

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

