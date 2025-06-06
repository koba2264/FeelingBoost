from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


# ログインのフォームクラス
class LoginForm(FlaskForm):
  username = StringField(
    "ユーザー名",
    validators=[
      DataRequired("ユーザー名は必須です。")
    ],
  )
  password = PasswordField(
    "パスワード",
    validators=[
      DataRequired("パスワードは必須です。")
    ]
  )
  submit = SubmitField("ログイン")