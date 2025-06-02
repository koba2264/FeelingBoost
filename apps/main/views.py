from flask import Blueprint, render_template, current_app
from apps.main.chat import main as chat

main = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/mane')
def menu():
    gemini_pro = current_app.config["GEMINI"]
    # chat(gemini_pro)

