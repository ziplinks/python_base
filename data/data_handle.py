import json
from pymysql import Connection

f = open("data.txt","r",encoding="UTF-8")
# 解析数据并转换为字典列表
data = []
for line in f:
    fields = line.strip().split()  # 使用空格作为分隔符
    if len(fields) == 3:
        data.append({
            "ID": fields[0],
            "Number": fields[1],
            "Location": fields[2]
        })
    else:
        print(f"警告：数据行 '{line}' 格式不正确，已跳过。")

    # 将字典列表转换为JSON格式的字符串   ensure_ascii=False 识别汉字  indent控制缩进，打印出来更直观
json_data = json.dumps(data, indent=4, ensure_ascii=False)

# 输出JSON数据
print(json_data)
print("------------------分割符--------------------")
f.close()


# 读取json 数据  并用对象接收
from file_read import ReadJsonFile

jf = ReadJsonFile("data_json")
list = jf.read_file()
for line in list:
    print(line)


# 将数据写入mysql数据库

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

# 选择数据库
conn.select_db("test")

# 获取游标对象
cursor = conn.cursor()

# 遍历数据将一个个Record对象 写入test_py表内
for line in list:
    sql = f"insert into test_py(id, money, address) values({line.id},{line.money},'{line.address}')"

    # 执行sql
    cursor.execute(sql)

# 关闭链接
conn.close()
