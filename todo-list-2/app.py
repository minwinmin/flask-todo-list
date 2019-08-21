#参考
#https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html
#https://www.atmarkit.co.jp/ait/articles/1807/24/news024_3.html

from flask import Flask, render_template, redirect, request
from todo import ToDoList, init_db

app = Flask(__name__)
todolist = ToDoList()

#appモジュールでFlaskアプリを構築してから、
#それをinit_db関数経由でtodoモジュールに引き渡して初期化を行う
init_db(app)

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

@app.route("/updatedone", methods=["POST"])
def update_done():
  keys = request.form.keys()
  items = [int(x) for x in keys]
  todolist.update_done(items)
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