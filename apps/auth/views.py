from apps.app import db
from flask import Blueprint, render_template, url_for, redirect, flash,request
from apps.auth.forms import LoginForm, SignUpForm
from apps.auth.models import User
from apps.gacha.models import GachaHistory
from flask_login import login_user,logout_user
from datetime import date
from flask_login import current_user
import uuid

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@auth.route('/')
def index():
    return render_template('auth/index.html')


@auth.route("/signup", methods=["GET","POST"])
def signup():
    # SignUpFormをインスタンス化する
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            id = str(uuid.uuid4()),
            username=form.username.data,
            password=form.password.data,
            task_date=date.today(),
            point = 30,
        )

                # メールアドレスの重複チェック
        if user.is_duplicate_username():
            flash("指定のユーザー名は登録済みです")
            return redirect(url_for("auth.signup"))


        # ユーザー情報を登録する
        db.session.add(user)
        db.session.commit()
        # ユーザー情報をセッションに格納する
        login_user(user)

        # ずんだもんを初期追加
        gachaHis = GachaHistory(
            user_id = current_user.id,
            prsnlty_id = 59
        )
        db.session.add(gachaHis)
        db.session.commit()

        # GETパラメータにnextキーが存在し、値がない場合はログインページへリダイレクト
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("main.menu")
        return redirect(next_)
    return render_template("auth/signup.html", form=form)


@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    # idからユーザーを取得する
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # ユーザーが存在するときはログインの許可
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("main.menu"))
    
        # ログイン失敗時の処理
        flash("idかパスワードが違います")
    return render_template("auth/login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))