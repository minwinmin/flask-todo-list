#参考
#https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html
#https://www.atmarkit.co.jp/ait/articles/1807/24/news024_3.html

from flask import Flask, render_template, redirect, request
from todo import ToDoList
from flask_sqlalchemy import SQLAlchemy

# @app.route("/")
# def hello_world():
#     return "Hello World"

# @app.route("/about")
# def about():
#     return "<h1>About</h1>"

# @app.route("/hello/<whom>")
# def hello(whom):
#   return f"<h1>Hello {whom}</h1>"

# @app.route("/100_plus/<int:n>")
# def adder(n):
#     return f"100+{n}={100+n}"

# @app.route("/welcome/<whom>")
# def welcome(whom):
#   return render_template("main.html", whom=whom)

# #todoリスト
# todolist = ToDoList()

# #redirectメソッド：指定したパスにリダイレクトする
# #requestオブジェクト：ユーザーからのリクエストに関する情報を含んだオブジェクト
# #requestオブジェクトには、リクエストに関する情報が含まれる
# #Webページではフォームを利用して、ToDo項目を送信しているが、その情報（キー／値）はrequest.formというディクショナリから取得できる
# @app.route("/")
# def show_todolist():
#     return render_template("todo.html", todolist = todolist.get_all())

# #「/additemというURLにPOSTメソッドでリクエストが送られた場合」に処理を行うことを意味
# @app.route("/additem", methods=["POST"])
# def add_item():
#     title = request.form["title"]
#     if not title:
#         return redirect("/")
    
#     todolist.add(title)
#     return redirect("/")

# @app.route("/deleteitem/<int:item_id>")
# def delete_todoitem(item_id):
#     todolist.delete(item_id)
#     return redirect("")

# @app.route("/updatedone/<int:item_id>")
# def update_todoitemdone(item_id):
#     todolist.update(item_id)
#     return redirect("/")

# @app.route("/deletealldoneitems")
# def delete_alldoneitems():
#     todolist.delete_doneitem()
#     return redirect("/")

app = Flask(__name__)
#https://teratail.com/questions/190825
#データベースのエラーについて、下記はURLみたいな感じ
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/sample.db"
db = SQLAlchemy(app)

todolist = ToDoList()


class ToDoItem2(db.Model):
  __tablename__ = "todoitems"
  item_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  done = db.Column(db.Boolean, nullable=False, default=False)
  

@app.route("/")
def show_todolist():
  return render_template("todo.html", todolist=todolist.get_all())

@app.route("/additem", methods=["POST"])
def add_item():
  title = request.form["title"]
  if not title:
    return redirect("/")

  todolist.add(title)
  return redirect("/")

@app.route("/deleteitem/<int:item_id>")
def delete_todoitem(item_id):
  todolist.delete(item_id)
  return redirect("/")

@app.route("/updatedone/<int:item_id>")
def update_todoitemdone(item_id):
  todolist.update(item_id)
  return redirect("/")

@app.route("/deletealldoneitems")
def delete_alldoneitems():
  todolist.delete_doneitem()
  return redirect("/")




# from app import db
# db.create_all()
# from app import ToDoItem2
# item1 = ToDoItem2(title="buy milk")
# item2 = ToDoItem2(title="play game!")
# db.session.add(item1)
# db.session.add(item2)
# db.session.commit()
# db.session.query(ToDoItem2).all()
# ToDoItem2.query.all()