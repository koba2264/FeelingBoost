from apps.app import db, login_manager
import uuid
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Userクラス
# UserMixinを継承することでflask_loginの機能を利用可能にする
class User(db.Model, UserMixin):
    # テーブル名
    __tablename__ = "users"
    # ユーザーID
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    # ユーザー名
    username = db.Column(db.String, index=True)
    # ハッシュ化したパスワード
    password_hash = db.Column(db.String)
    # べた褒めポイント
    point = db.Column(db.Integer, default=0)
    # 進行中のタスクを保存
    # タスクの内容
    task1_text = db.Column(db.String)
    task2_text = db.Column(db.String)
    task3_text = db.Column(db.String)
    # タスクの達成状況
    task1_judge = db.Column(db.Boolean)
    task2_judge = db.Column(db.Boolean)
    task3_judge = db.Column(db.Boolean)
    task_date = db.Column(db.Date)
    # プロフィール画像
    profile_image = db.Column(db.String, default="default.png")
    # ガチャポイント
    gacha_point = db.Column(db.Integer, default=0)

    # 関連する履歴
    user_chat_historys = db.relationship("ChatHistory",backref="user1",order_by="asc(ChatHistory.history_id)")
    # 関連するタスク(いったん削除変更)
    # user_task = db.relationship("Task",backref="user",order_by="asc(Task.task_id)")
    # 関連するタスクの完了履歴
    user_task_history = db.relationship("TaskHistory",backref="user",order_by="asc(TaskHistory.task_history_id)")

    @property
    def password(self):
        raise AttributeError("読み取り不可")

    # パスワードをハッシュ化してセットする
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # パスワードのチェック
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # usernameの重複チェック(重複している場合:true)
    def is_duplicate_username(self):
        return User.query.filter_by(username=self.username).first() is not None
    
# ログインしているユーザーの情報を取得する関数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)