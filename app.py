from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# 用列表临时保存待办事项。
# 这是最小可运行版本，所以先不接数据库。
todos = []


@app.route("/", methods=["GET"])
def index():
    """显示待办清单首页。"""
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add_todo():
    """接收表单内容，并添加到待办列表。"""
    content = request.form.get("content", "").strip()

    # 只有输入了内容时才添加，避免空白项。
    if content:
        todos.append(content)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
