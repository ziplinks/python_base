"""
函数的定义中
1. def关键字，可以定义带有名称的函数
2. lambda关键字，可以定义匿名函数。 注意函数体只能写一行

有名称的函数，可以基于名称重复使用
无名称的匿名函数，只可以临时使用一次
"""


def add(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    sum = x + y
    print(f"和为{sum}")


add(1, 3)


# return多个值
def return_test():
    return 1, 3, 5


x, y, z = return_test()
# 1 3 5
print(x, y, z)


# 传参方式
def params_fun(name, age, sex="女"):
    print(f"name = {name} age = {age} sex = {sex}")


# 传参可以乱序
params_fun("Tom", "66", )
params_fun("kdsk", "666", "男")
params_fun(age=12, name="Jim", sex=1)


# 位置不定长 *号
def params_fun(*args):
    print(f"args类型 {type(args)} args值为 {args}")


# args类型 <class 'tuple'> args值为 (1, 2, 'hi')
params_fun(1, 2, "hi")


# 关键字不定长 **号
def params_fun(**kwargs):
    print(f"kwargs类型 {type(kwargs)} kwargs值为 {kwargs}")


# kwargs类型 <class 'dict'> kwargs值为 {'age': 1, 'name': 2, 'say': 'hi'}
params_fun(age=1, name=2, say="hi")


# 函数作为参数传递
def test_fun_def(compute):
    sum = compute(1, 2)
    print(f"def sum={sum}")


def compute(x, y):
    return x + y


test_fun_def(compute)


# 使用 lambda 函数进行优化
def test_fun_lambda(compute):
    sum = compute(2, 2)
    print(f"lambda sum={sum}")


test_fun_lambda(lambda x, y: x + y)
