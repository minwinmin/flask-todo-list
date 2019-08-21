#参考
#https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html
#https://www.atmarkit.co.jp/ait/articles/1807/24/news024_3.html

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/todoitems.db"
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
CORS(app)

class ToDoItem(db.Model):
  __tablename__ = "todoitems"
  item_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  done = db.Column(db.Boolean, nullable=False, default=False)

manager.create_api(ToDoItem,
  methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])


