#参考
#https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html
#https://www.atmarkit.co.jp/ait/articles/1807/24/news024_3.html

from flask import Flask, render_template, redirect, request
from todo import ToDoItem, init_db, init_schema
from todo import item_schema, items_schema

app = Flask(__name__)
#todolist = ToDoList()

#appモジュールでFlaskアプリを構築してから、
#それをinit_db関数経由でtodoモジュールに引き渡して初期化を行う
db = init_db(app)
init_schema(app)

@app.route("/api/todoitems", methods=["GET"])
def get_todoitems():
  items = ToDoItem.query.all()
  return items_schema.jsonify(items)

@app.route("/api/todoitems/<int:item_id>", methods=["GET"])
def get_todoitem(item_id):
  item = ToDoItem.query.filter_by(item_id=item_id).first_or_404()
  return item_schema.jsonify(item)

@app.route("/api/todoitems", methods=["POST"])
def add_todoitem():
  if not "title" in request.json:
    return "error"
  item = ToDoItem(title=request.json["title"], done=False)
  db.session.add(item)
  db.session.commit()
  return item_schema.jsonify(item)

@app.route("/api/todoitems/<int:item_id>", methods=["DELETE"])
def delete_todoitem(item_id):
  item = ToDoItem.query.filter_by(item_id=item_id).first_or_404()
  db.session.delete(item)
  db.session.commit()
  return jsonify({"result": True})

@app.route("/api/todoitems/<int:item_id>", methods=["PUT"])
def update_todoitem(item_id):
  item = ToDoItem.query.filter_by(item_id=item_id).first_or_404()
  item.done = not item.done
  db.session.commit()
  return item_schema.jsonify(item)

#curlコマンドとはサーバから、もしくはサーバへデータ転送を行うコマンド

# @app.route("/")
# def show_todolist():
#   return render_template("todo.html", todolist=todolist.get_all())

# @app.route("/additem", methods=["POST"])
# def add_item():
#   title = request.form["title"]
#   if not title:
#     return redirect("/")

#   todolist.add(title)
#   return redirect("/")

# @app.route("/deleteitem/<int:item_id>")
# def delete_todoitem(item_id):
#   todolist.delete(item_id)
#   return redirect("/")

# @app.route("/updatedone", methods=["POST"])
# def update_done():
#   keys = request.form.keys()
#   items = [int(x) for x in keys]
#   todolist.update_done(items)
#   return redirect("/")

# @app.route("/deletealldoneitems")
# def delete_alldoneitems():
#   todolist.delete_doneitem()
#   return redirect("/")

# from app import db
# db.create_all()
# from app import ToDoItem2
# item1 = ToDoItem2(title="buy milk")
# item2 = ToDoItem2(title="play game!")
# db.session.add(item1)
# db.session.add(item2)
# db.session.commit()


