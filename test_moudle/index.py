
import my_moudle

sum = my_moudle.add(10, 80)
print(sum)

# 从自定义模块包(my_package)内导入


# # 方式1
# import my_package.my_moudle2
# import my_package.my_moudle3
#
# my_package.my_moudle2.info2()
# my_package.my_moudle3.info3()


# # 方式2
# from my_package import my_moudle2
# from my_package import my_moudle3
# my_moudle2.info2()
# my_moudle3.info3()


# 方式3
from my_package import *
my_moudle3.info3()


# 下载插件速度提升方式
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple + 包名称
