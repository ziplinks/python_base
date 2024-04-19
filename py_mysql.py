from pymysql import Connection
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
# print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")

# 执行sql 创建表和默认字段
# cursor.execute("create table test_py(id int, money int, address varchar(20))")

# 执行查询
cursor.execute("select * from student")

# 插入数据
cursor.execute("insert into student values(11,'李丽',32),(35,'王五一',21)")


# 获取查询结果(元组)
result: tuple = cursor.fetchall()
for item in result:
    print(item)

# (1, '周成', 34)
# (2, '达简', 23)
# (3, '刘欢', 26)

# 确认提交（插入数据使用）
# conn.commit()

# 关闭
conn.close()