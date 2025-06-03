from flask import Blueprint, render_template, current_app, request, session
from apps.main.models import ChatHistory ,Task ,TaskHistory
from apps.app import db
# from flask_login import current_user, login_required
import google.generativeai as genai
import os

userid = 'test'

main = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/mane', methods=["GET","POST"])
def menu():
    # 設定をconfigから取得
    # gemini_pro = current_app.config["GEMINI"]
    GOOGLE_API_KEY=os.getenv("GeminiAPI")
    genai.configure(api_key=GOOGLE_API_KEY)

    gemini_pro = genai.GenerativeModel("gemini-1.5-flash")
    # 前回以前の履歴の取得
    # history = getHistory()
    history=[]
    # chatbotのスタート
    ai = gemini_pro.start_chat(history=history)

    # 直前のチャット履歴の取得
    if 'chat_his' in session:
        chat_his = session['chat_his']
    else:
        chat_his = []

    # POSTの時
    if request.method == 'POST':
        # 投稿の取得
        text = request.form['text']
        # レスポンスの生成
        # response = chat(text, ai)
        response = ai.send_message(text)
        print(response.text)
        # chatの履歴へ追加
        chat_his.append({'user':text,'model':response.text})
        
    # セッションにchatの履歴を保存
    session['chat_his'] = chat_his
    return render_template('main/index.html', chat_his=chat_his)

# chatの処理
def chat(text,ai):
    # 回答の生成
    response = ai.send_message(text)
    # 回答の保存
    return response

# chatの履歴をDBへ保存する関数
def saveHistory(text,response):
    # ユーザーが送信したテキスト
    user = ChatHistory(
        # 後でログイン中のユーザーIDへ変更する
        user_id = userid,
        role = 'user',
        text = text
    )
    # AIが生成した回答
    model = ChatHistory(
        # 後でログイン中のユーザーIDへ変更する
        userid = userid,
        role = 'model',
        text = response
    )
    db.session.add(user)
    db.session.add(model)
    db.session.commit()

# DBから現在ログイン中のユーザーのチャット履歴を取得する関数
def getHistory():
    history = []
    histories = (
        db.session.query(ChatHistory)
        # 後でログイン中のユーザーIDへ変更する
        .filter(ChatHistory.user_id == userid)
        .all()
    )
    for his in histories:
        history.append({"role":his.role, "parts":his.text})
    
    return history

    