from datetime import datetime

from apps.app import db

# chat履歴保存
class ChatHistory(db.Model):
  # テーブル名
  __tablename__ = "chat_histories"
  # カラム
  # chatid
  history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  # ユーザーID
  user_id = db.Column(db.String, db.ForeignKey("users.id"))
  # ユーザーの発言
  user = db.Column(db.String)
  # AIからの回答
  model = db.Column(db.String)

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
  # レアリティ
  rarity = db.Column(db.String)
  # クレジット
  credit = db.Column(db.String, default="")
  # voiceID
  voice_id = db.Column(db.Integer)
  # 抽選済みのテーブルとの関連
  user_prsnlty = db.relationship("GachaHistory",backref="gacha")