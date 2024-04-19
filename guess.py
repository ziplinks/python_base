import random

flag = True
number = random.randint(1,100)
count = 0
while flag:
    inputValue = int(input("请输入你猜测的数字："))
    count += 1
    if inputValue == number:
        print("恭喜你，猜对了")
        flag = False
    elif inputValue > number:
        print("你猜大了")
    else:
        print("你猜小了")
print(f"总共猜了{count}次")