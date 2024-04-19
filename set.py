# 定义集合
my_set = {"a", "b", "c", "d", "d"}
# 打印结果 {'b', 'c', 'a', 'd'}  无序的
my_set_empty = set()
print(my_set)

# 添加新元素
my_set.add("e")
print(my_set)

# 移除元素
my_set.remove("e")
print(my_set)

# 随机取出元素
print(my_set.pop(), my_set)

# 清空  None <class 'set'>
print(my_set.clear(), type(my_set))

# 取差集
my_set_1 = {1, 2, 3}
my_set_2 = {1, 4, 5}

# 打印结果 {2, 3}
print(my_set_1.difference(my_set_2), my_set_1)

# 取消差集
my_set_1 = {1, 2, 3}
my_set_2 = {1, 4, 5}
my_set_1.difference_update(my_set_2)
print(my_set_1, my_set_2)

# 合并集合
# 打印结果 {1, 2, 3, 4, 5} 合并后my_set_1、my_set_2两个集合不改变 会得到新的集合
print(my_set_1.union(my_set_2))

# 元素数量
my_set_1 = {1, 2, 3, 1}

# 3个（会去重的）
print(len(my_set_1))

# 遍历 只能使用for循环