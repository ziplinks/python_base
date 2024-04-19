# 封装
class Animal:
    type = "还不确定"
    # 私有成员变量 __lovely
    __lovely = "非常可爱"

    # 私有方法 __what_animal
    def __what_animal(self):
        print("你调用了内部方法")

    # 调用内部私有变量和方法
    def test(self):
        self.__what_animal()
        print(f"该动物是很巨大，但是非常的{self.__lovely}")

    def like_doing(self):
        print("那该动物的喜好又是什么呢？")


animal = Animal()
print(animal.type)
animal.test()
animal.like_doing()


# 继承（单继承）
class CatCategory(Animal):
    category = "猫科动物"

    def cat_method(self):
        print(f"虽然我是继承动物，但是仅仅是{self.category}")
        # 调用父类方法和成员变量 方式一
        # Animal.like_doing(self)
        # print(f"测试一下调用父类type = {Animal.type}")

        # 调用父类方法和成员变量 方式二
        super().like_doing()
        print(f"测试一下调用父类type = {super().type}")

    def like_doing(self):
        print("这里重写了父类 like_doing方法")


cat = CatCategory()
cat.cat_method()
cat.like_doing()


# 多态
# 含有抽象方法的类 叫抽象类
class A:
    # 定义抽象方法
    def test_method(self):
        pass


class A_1:
    def test_method(self):
        print("A_1 打印啦")

class A_2:
    def test_method(self):
        print("A_2 打印啦")

def test_find(type: A):
    type.test_method()

a1 = A_1()
a2 = A_2()
test_find(a1) # A_1 打印啦
test_find(a2) # A_2 打印啦



