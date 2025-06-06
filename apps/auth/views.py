from flask import Blueprint, render_template, url_for, redirect, flash
from apps.auth.forms import LoginForm
from apps.auth.models import User
from flask_login import login_user

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@auth.route('/')
def index():
    return render_template('auth/index.html')

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    # idからユーザーを取得する
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # ユーザーが存在するときはログインの許可
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("main.index"))
    
        # ログイン失敗時の処理
        flash("idかパスワードが違います")
    return render_template("auth/login.html", form=form)
