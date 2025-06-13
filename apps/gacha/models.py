
from apps.app import db

# ガチャの履歴
class GachaHistory(db.Model):
    # テーブル名
    __tablename__ = "gacha_histories"
    # 取得したユーザーのID
    user_id = db.Column(db.String, db.ForeignKey("users.id"),primary_key=True)
    # 取得した称号のID
    prsnlty_id = db.Column(db.Integer, db.ForeignKey("personality.prsnlty_id"),primary_key=True)