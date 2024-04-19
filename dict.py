# 定义空字典
my_dict1 = {}
my_dict2 = dict()

my_dict = {"张三": 99,"李四": 77,"王二麻子": "90"}

# 取值
print(my_dict["张三"])

# 新增、更新  key存在即更改  不存在就是新增

my_dict["张三"] = 78
# {'张三': 78, '李四': 77, '王二麻子': '90'}
print(my_dict)

my_dict["王五"] = 100
# {'张三': 78, '李四': 77, '王二麻子': '90', '王五': 100}
print(my_dict)

# 删除 pop
my_dict = {"张三": 99,"李四": 77,"王二麻子": "88"}
value = my_dict.pop("张三")
# 打印 99  {'李四': 77, '王二麻子': '88'}
print(value, my_dict)

# 清空
print(my_dict.clear())

# 获取字典全部key
my_dict = {"张三": 99,"李四": 77,"王二麻子": "88"}
keys = my_dict.keys()
# 打印 dict_keys(['张三', '李四', '王二麻子'])
print(keys)

# for循环遍历
# 方式一 先取出所有keys 对keys 进行遍历
for key in keys:
    print(key)
    print(my_dict[key])

# 方式二 直接对字典进行遍历
for key in my_dict:
    print(key)
    print(my_dict[key])

# 元素数量
print(len(my_dict))
