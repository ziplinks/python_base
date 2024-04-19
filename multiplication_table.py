# 九九乘法表 while循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')  # end='' 控制打印不换行； \t制表符 控制对齐
        j += 1
    i += 1
    print()  # 控制换行


# 九九乘法表 for循环
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end='')  # end='' 控制打印不换行； \t制表符 控制对齐
    print()  # 控制换行
