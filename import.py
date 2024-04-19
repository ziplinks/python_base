
# 方式一 引入time全部功能
# import time
# time.sleep(5000)

# 方式二 只引入sleep
# from time import sleep
# sleep(5000)

# 方式三
# from time import *

# 方式四  改成别名
import time as t
from time import sleep as sl
t.sleep(500)
sl(500)
