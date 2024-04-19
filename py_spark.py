from pyspark import SparkConf, SparkContext
import os

# 如果使用相关算子，则需要配置环境变量告诉pyspark python解释器位置

# 注意： python3.12.2 与 pyspark3.5.1 不兼容  所以降级使用了Python3.10
# os.environ['PYSPARK_PYTHON'] = "C:/software/Python/python3.12.2/python.exe"

os.environ['PYSPARK_PYTHON'] = "C:/Users/bin.zhang1/AppData/Local/Programs/Python/Python310/python.exe"

# 新建 SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("my_pyspark_app")
# 新建 SparkContext对象
sc = SparkContext(conf=conf)

# 方式一  读取list 字符串等待

rdd0 = sc.parallelize("abcdefg")
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(rdd0.collect())

rdd = sc.parallelize([1, 2, 3, 4, 5, 6])


def add(data):
    return data + 10


# [11, 12, 13, 14, 15, 16]
print(rdd.map(add).collect())

# 支持链式语法
rdd4 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
# [15, 25, 35, 45, 55, 65]
print(rdd4.collect())

# 方式二  读取文件内容

rdd3 = sc.textFile("E:/Python/pythonTest/data/data.txt")
# ['1223 6456345 安徽省', '123 34773 河北省', '2088 2374782 江西省', '983 25334 淮北市', '52153 8345983894 上海市', '2341 89999 杭州']
# 一行一行读取 转字符串放入list内
print(rdd3.collect())


sc.stop()

"""
PySpark中常用的算子可以分为两大类：Transformation（转换）算子和Action（动作）算子。

Transformation算子主要用于在RDD（弹性分布式数据集）上进行各种转换操作，产生新的RDD。以下是一些常用的Transformation算子：

    map：对RDD中的每个元素应用一个函数，返回新的RDD。
    flatMap：类似于map，但每个输入项可以映射到0或多个输出项。
    filter：返回一个新RDD，它包含通过给定函数的RDD的所有元素。
    union：对两个RDD进行并集操作。
    distinct：返回一个新的RDD，包含原RDD中所有唯一的元素。
    groupBy：根据键对RDD中的元素进行分组。
    groupByKey：将具有相同键的值组合在一起。
    sortBy：根据指定的键或函数对RDD进行排序。
    reduceByKey：使用指定的函数对具有相同键的值进行归约操作。
    join：在两个键类型相同的RDD上执行内连接操作。

Action算子用于触发实际的计算，并将结果返回到驱动程序。以下是一些常用的Action算子：

    foreach：对RDD中的每个元素应用一个函数。
    saveAsTextFile：将RDD的内容保存为文本文件。
    collect：将RDD的所有元素作为数组返回给驱动程序。
    count：返回RDD中的元素数量。
"""
