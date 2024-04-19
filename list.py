my_list = ["js", "python", "java", "kotlin"]
# 查询下标索引
index = my_list.index("java")
print(f"index={index}")

# 修改指定下标的值
my_list[0] = "node.js"
print(f"my_list={my_list}")

# 指定位置插入值
my_list.insert(1, "swift")
print(f"插入后的my_list={my_list}")

# 追加元素到尾部
my_list.append("oc")
print(f"追加后的my_list={my_list}")

# 依次追加到尾部
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
# 运行结果 ['node.js', 'swift', 'python', 'java', 'kotlin', 'oc', 1, 2, 3]
print(f"追加一个新列表的my_list={my_list}")

# 元素删除
my_list = ["js", "python", "java", "kotlin"]
# 方式一
del my_list[0]
print(f"删除了第一个元素的 my_list={my_list}")
# 方式二
ele = my_list.pop(2)
print(f"删除的值是{ele},删除后数组值为：{my_list}")

# 方式三 移除指定元素(只删除第一个匹配到的)
my_list = ["js", "python", "java", "kotlin"]
my_list.remove("java")
print(f"remove my_list={my_list}")

# 清空list
my_list.clear()
print(f"clear my_list={my_list}")

# 统计某一个元素出现几次
my_list = ["js", "js", "js", "kotlin"]
count = my_list.count("js")
print(f"count my_list.count = {count}")

# 统计list元素个数（数组长度）
my_list = ["js", "python", "java", "kotlin"]
length = len(my_list)
print(f"my_list的len = {length}")

# 练习
list_all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = []
for item in list_all:
    if item % 2 == 0:
        arr.append(item)
print(f"结果集： {arr}")

# sort 排序
sort_list = [{"count": 163}, {"count": 15}, {"count": 13}, {"count": 130}, {"count": 2}]


def rules(element):
    return element["count"]


# 调用方式一
sort_list.sort(key=rules, reverse=False)

# 调用方式二 lambda函数
# sort_list.sort(key=lambda e: e["count"], reverse=True)

# sort_list = [{'count': 2}, {'count': 13}, {'count': 15}, {'count': 130}, {'count': 163}]
print(f"sort_list = {sort_list}")



