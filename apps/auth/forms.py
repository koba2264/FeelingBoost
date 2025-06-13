from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
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
  submit = SubmitField("新規登録")


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