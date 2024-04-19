# 该文件主要是关于接口调用相关内容

# 需要用到的包引入
from pymysql import Connection
from flask import Flask, request, jsonify
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

# 后端服务启动
app = Flask(__name__)
# 为所有路径启用CORS
CORS(app)


# 获取列表数据
@app.route("/student/list", methods=['GET'])
def student_list():
    # 获取某个参数，例如 'name'
    name = request.args.get('name')
    # 构造查询语句
    if name:
        # 使用LIKE操作符和通配符%来查询包含name的记录
        query = "select * from student where name like %s"
        # 使用%%作为通配符%的转义，因为%在SQL中是特殊字符
        cursor.execute(query, ('%' + name + '%',))
    else:
        # 如果没有name参数，查询所有记录
        query = "select * from student"
        cursor.execute(query)

    try:
        # 获取查询结果
        data = cursor.fetchall()
    except Exception as e:
        # 处理数据库查询异常
        print(f"查询异常: {e}")
        return jsonify([]), 500

    # 将结果转换为字典列表
    # 这段代码使用了Python的列表推导式（list comprehension）来将一个数据库查询结果列表转换为包含字典的列表
    result = [
        {
            "id": row[0],
            "name": row[1],
            "age": row[2]
        } for row in data
    ]

    # 返回JSON响应
    return jsonify(result)


# 增加一条数据
@app.route("/student", methods=['POST'])
def create_student():
    name = request.form.get("name")
    age = request.form.get("age")
    ids = request.form.get("id")

    if not name or not age or not ids:
        return jsonify({"message": "缺少必填参数"}), 400

    query = "insert into student (name, age, id) values (%s, %s, %s)"
    try:
        cursor.execute(query, (name, age, ids))
        return jsonify({"message": f"学生{name}新增成功"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# 删除某条数据
@app.route("/student/<int:student_id>", methods=['DELETE'])
def delete_student(student_id):
    query = "delete from student where id=%s"
    try:
        cursor.execute(query, (student_id,))
        return jsonify({"message": f"学生 {student_id} 删除成功"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# 修改某条数据
@app.route("/student/<int:student_id>", methods=['PUT'])
def update_student(student_id):
    name = request.form.get("name")
    age = request.form.get("age")

    if not name and not age:
        return jsonify({"message": "缺少必要参数"}), 400

    update_query = "update student set "
    update_params = []

    if name:
        update_query += "name=%s, "
        update_params.append(name)
    if age:
        update_query += "age=%s, "
        update_params.append(age)

    update_query = update_query.rstrip(', ')

    query = f"{update_query} where id=%s"
    update_params.append(student_id)
    # print(query)
    # print(update_params)
    try:
        cursor.execute(query, tuple(update_params))
        return jsonify({"message": f"学生{name}信息更新成功"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run("0.0.0.0", port=9090, debug=True)
    conn.close()
