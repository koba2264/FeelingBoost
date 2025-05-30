from flask import Flask

from apps.config import config

def create_app(config_key):
    app = Flask(__name__)
    from apps.main import views as main_views

    app.register_blueprint(main_views.main, url_prefix="/main")

    return app