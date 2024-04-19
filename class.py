class Student:
    name = None
    age = None
    grade = None
    gender = None

    def say_hi(self):
        print(f"大家好，我是{self.name},我今年{self.age}岁,我在{self.grade}年级,我是{self.gender}。")

    def say_hi_custom(self, msg):
        print(f"大家好呀，都知道我的，我是{msg}")


student1 = Student()
student1.name = "John"
student1.age = 18
student1.grade = 9
student1.gender = "男生"
student1.say_hi()
student1.say_hi_custom("大将军")


# 构造方法

class Animal:
    # 可以省略
    # height = None
    # weight = None
    # like = None
    def __init__(self, height, weight, like):
        self.height = height
        self.weight = weight
        self.like = like

        # 转字符串
    def __str__(self):
        return  f"{self.height}"

    # 大小比较
    def __lt__(self, other):
        return self.height < other.height

    def __le__(self, other):
        return self.height <= other.height

animal = Animal(40, 50, "吃饭")
print(f"这只小动物喜欢{animal.like},身高：{animal.height},体重：{animal.weight}")
print(animal)
animal2 = Animal(400, 500, "睡觉")

# True
print(animal < animal2)

