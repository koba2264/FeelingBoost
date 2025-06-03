from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

# chat履歴保存
class ChatHistory(db.Model):
  # テーブル名
  __tablename__ = "chat_histories"
  # カラム
  # chatid
  history_id = db.Column(db.Integer, primary_key=True)
  # ユーザーID
  user_id = db.Column(db.String, db.ForeignKey("users.id"), primary_key=True)
  # 発言者
  # ユーザーの発言:'user' モデルの返答:'model'
  role = db.Column(db.String)
  # chat内容
  text = db.Column(db.String)

# 現在のタスク
class Task(db.Model):
  # テーブル名
  __tablename__ = "task"
  # カラム
  # タスクID
  task_id = db.Column(db.String, primary_key=True)
  # ユーザーID
  user_id = db.Column(db.String, db.ForeignKey("users.id"), primary_key=True)
  task1_text = db.Column(db.String)
  task2_text = db.Column(db.String)
  task3_text = db.Column(db.String)
  task1_judge = db.Column(db.Boolean)
  task2_judge = db.Column(db.Boolean)
  task3_judge = db.Column(db.Boolean)
  date_judge = db.Column(db.Boolean)


class TaskHistory(db.Model):
  # テーブル名
  __tablename__ = "task_histories"
  # カラム
  task_history_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String,db.ForeignKey("users.id"), primary_key=True)
  task1 = db.Column(db.String)
  task2 = db.Column(db.String)
  task3 = db.Column(db.String)
  date = db.Column(db.DateTime, default=datetime.now)

