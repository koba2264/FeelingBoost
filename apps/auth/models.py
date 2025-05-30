from flask import Blueprint, render_template

main = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@main.route('/')
def index():
    return render_template('main/index.html')