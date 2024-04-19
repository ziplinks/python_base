from flask import request, jsonify
from flask_moudle.route import app, cursor


# 登录接口
@app.route("/login", methods=['POST'])
def login_student():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"message": "缺少必填参数"}), 400

    query = "select * from user where username=%s and password=%s"
    try:
        cursor.execute(query, (username, password))
        user_data = cursor.fetchone()  # 获取查询结果的第一行
        if user_data:
            # 处理用户数据
            return jsonify({"message": f"学生{username}登录成功"}), 200
        else:
            return jsonify({"message": "用户名或密码错误"}), 401

    except Exception as e:
        return jsonify({"message": str(e)}), 500
