# 需要用到的包引入
from pymysql import Connection
from flask import Flask
from flask_cors import CORS

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")

# 后端服务启动 新建Flask实例
app = Flask(__name__)
# 为所有路径启用CORS
CORS(app)

# 导入视图模块来注册路由，. 符号用来表示当前包的目录；注意需要在app创建之后导入
from . import login
from . import student
