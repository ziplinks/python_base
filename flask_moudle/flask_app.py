from flask_moudle.route import app, conn

if __name__ == "__main__":
    app.run("0.0.0.0", port=9090, debug=True)
    # 关闭 数据库
    conn.close()
