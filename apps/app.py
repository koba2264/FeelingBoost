from flask import Flask
from pathlib import Path
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

from apps.config import config

def create_app():
    app = Flask(__name__)
    config_key = 'local'
    app.config.from_object(config[config_key])
    from apps.main import views as main_views

    app.register_blueprint(main_views.main, url_prefix="/main")

    return app