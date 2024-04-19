# 异常捕获
try:
    print("name")
except Exception as e:
    print("异常出现了")
else:
    print("没有异常")
finally:
    print("不管有没有异常都会执行")


    try:
        print(name)
    except:
        print("异常出现了")
        