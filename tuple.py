# 元组 不可修改的list 可以看作只读的list
t1 = (True, 1, "123")
# 空元组定义
t2 = ()
t3 = tuple()

# 注意事项  单个元素需要使用 , 标注
t4 = ("hello")
t5 = ("hello",)

# t4类型为<class 'str'>，值为hello
print(f"t4类型为{type(t4)}，值为{t4}")
# t5类型为<class 'tuple'>，值为('hello',)
print(f"t5类型为{type(t5)}，值为{t5}")

# 嵌套
t6 = ((1, 2, 3), (4, 5, 6))
print(t6[1][2])  # 打印 6

# 由于不可修改 只有 index、count、len 操作方法


# 可进行while、for循环
