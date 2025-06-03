from flask import Blueprint, render_template, current_app
# from apps.main.models import History

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

# chatの処理
def chat(text,chat):
    # 回答の生成
    response = chat.send_message(text)
    # 回答の保存
    return response

# def saveHistory(text,response):

