str = "hello world"
# 从下标2位置开始截取到下标为4的地方
result1 = str[2:4]
# 从下标0位置开始截取到下标为4的地方
result2 = str[:4]
# 每隔2个字符截取字符串
result3 = str[::2]
# 打印结果 ll hell hlowrd
print(result1, result2, result3)

# 定义一个字符串
my_string = "Hello, World!"

# 使用负数索引提取最后两位字符
last_two_chars = my_string[-2:]
print(last_two_chars)  # 输出: d!

