from flask import Blueprint, render_template, url_for

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@auth.route('/')
def index():
    return render_template('auth/index.html')