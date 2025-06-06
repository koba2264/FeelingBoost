from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()
# CSRFProtectをインスタンス化する
csrf = CSRFProtect()
# LoginManagerをインスタンス化
login_manager = LoginManager()
# 未ログイン時のリダイレクト先
login_manager.login_view = "auth.signup"
# ログイン後に表示するメッセージの設定
login_manager.login_message = ""

from apps.config import config

def create_app():
    app = Flask(__name__)
    config_key = 'local'
    app.config.from_object(config[config_key])

    # アプリと連携
    csrf.init_app(app)
    # SQLAlchemyとアプリを連携させる
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app,db)
    # login_managerをアプリケーションと連携する
    login_manager.init_app(app)

    from apps.main import views as main_views
    from apps.auth import views as auth_views

    app.register_blueprint(main_views.main)
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app