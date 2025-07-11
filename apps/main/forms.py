from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField

# 画像アップロード用のフォームクラス
class UploadImageForm(FlaskForm):
    # ファイルフィールド
    image = FileField(
        "画像",
        validators=[
            # 画像が選択されているか
            FileRequired("画像ファイルを指定してください"),
            # 拡張子がリストのものと合うかどうか
            FileAllowed(["png","jpg","jpeg"],"サポートされていない画像形式です。"),
        ]
    )
    submit = SubmitField("アップロード")