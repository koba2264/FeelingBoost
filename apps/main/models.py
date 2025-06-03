from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

# chat履歴保存
class ChatHistory(db.Model):
  # テーブル名
  __tablename__ = "chat_histories"
  # カラム
  # chatid
  history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  # ユーザーID
  user_id = db.Column(db.String, db.ForeignKey("users.id"))
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
  # タスクの内容
  task1_text = db.Column(db.String)
  task2_text = db.Column(db.String)
  task3_text = db.Column(db.String)
  # タスクの達成状況
  task1_judge = db.Column(db.Boolean)
  task2_judge = db.Column(db.Boolean)
  task3_judge = db.Column(db.Boolean)
  date_judge = db.Column(db.Boolean)

# タスクの達成状況
class TaskHistory(db.Model):
  # テーブル名
  __tablename__ = "task_histories"
  # ID
  task_history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  # ユーザーID
  user_id = db.Column(db.String,db.ForeignKey("users.id"))
  # タスクの達成状況
  task1 = db.Column(db.Boolean)
  task2 = db.Column(db.Boolean)
  task3 = db.Column(db.Boolean)
  # タスクの日付
  date = db.Column(db.DateTime, default=datetime.now)

# 人格テーブル
class Prsnlty(db.Model):
  __tablename__ = "personality"
  # ID
  prsnlty_id = db.Column(db.Integer, primary_key=True)
  # 人格名
  name = db.Column(db.String)
  # プロンプト
  prompt = db.Column(db.String)