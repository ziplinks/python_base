from time import sleep
import threading


def sing(msg):
    while True:
        print(msg)
        sleep(1)


def dance(msg):
    while True:
        print(msg)
        sleep(1)


# 以元组形式传参 只有一个元素注意用逗号隔开
sing_thread = threading.Thread(target=sing, args=("我是在唱歌，哈哈哈哈",))
# 以字典形式传参
dance_thread = threading.Thread(target=dance, kwargs={"msg": "我现在在跳舞咯  呵呵呵呵"})
sing_thread.start()
dance_thread.start()
