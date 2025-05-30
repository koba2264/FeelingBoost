from flask import Flask

def create_app():
    app = Flask(__name__)

    from apps.main import views as main_views

    app.register_blueprint(main_views.main)

    return app