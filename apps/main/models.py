from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

class History(db.Model):
  # テーブル名
  __tablename__ = "history"
  # カラム
  history_id = db.Column(db.String, primary_key=True)
  user_id = db.Column(db.String, primary_key=True)
  role = db.Column(db.String)
  text = db.Column(db.String)

class Task(db.Model):
  # テーブル名
  __tablename__ = "task"
  # カラム
  task_id = db.Column(db.String, primary_key=True)
  user_id = db.Column(db.String, primary_key=True)
  task1_text = db.Column(db.String)
  task2_text = db.Column(db.String)
  task3_text = db.Column(db.String)
  task1_judge = db.Column(db.Boolean)
  task2_judge = db.Column(db.Boolean)
  task3_judge = db.Column(db.Boolean)
  date_judge = db.Column(db.Boolean)


class TaskHistory(db.Model):
  # テーブル名
  __tablename__ = "task_history"
  # カラム
  task_history_id = db.Column(db.String, primary_key=True)
  user_id = db.Column(db.String, primary_key=True)
  task1 = db.Column(db.String)
  task2 = db.Column(db.String)
  task3 = db.Column(db.String)
  date = db.Column(db.Datetime, default=datetime.now)

