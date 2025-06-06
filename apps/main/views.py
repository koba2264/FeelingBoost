from flask import Blueprint, render_template, current_app, request, session
from apps.main.models import ChatHistory ,Task ,TaskHistory, Prsnlty
from apps.auth.models import User
from apps.app import db
from flask_wtf import FlaskForm
from flask_login import login_required
from datetime import datetime
import random
# from flask_login import current_user, login_required

# 仮のユーザーのID
userid = 123

main = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@main.route('/Prsnlty')
def insert():
    # 仮でユーザーを追加
    user1 = User(
        id = '123',
        username = 'test',
        password_hash = 'test'
    )
    prsnlty1 = Prsnlty(
        prsnlty_id = 1,
        name = 'ポジティブコーチ',
        prompt = 'あなたは常に前向きで元気あふれるコーチです。ユーザーのどんな小さな努力でも見逃さず、励まし、積極的に褒め称え、さらに意欲を引き出してください。'
    )
    prsnlty2 = Prsnlty(
        prsnlty_id = 2,
        name = '優しいお姉さん',
        prompt = 'あなたは優しく包み込むようなお姉さんの人格です。ユーザーの存在や行動を温かい言葉で認め、癒しと安心感を与えるような褒め方をしてください。'
    )
    prsnlty3 = Prsnlty(
        prsnlty_id = 3,
        name = '丁寧な執事',
        prompt = 'あなたは礼儀正しく丁寧な執事の人格です。ユーザーの振る舞いや行動を敬意をもって上品に褒め、ユーザーが特別感を味わえるような表現を使ってください。'
    )
    prsnlty4 = Prsnlty(
        prsnlty_id = 4,
        name = '熱血応援団長',
        prompt = 'あなたは情熱的でパワフルな応援団長です。どんな些細なことでも全力で応援し、大げさなくらいの称賛とエネルギッシュな言葉でユーザーを元気づけてください。'
    )
    db.session.add(prsnlty1)
    db.session.add(prsnlty2)
    db.session.add(prsnlty3)
    db.session.add(prsnlty4)
    db.session.add(user1)
    db.session.commit()
    return render_template('main/index.html')

@main.route('/', methods=["GET","POST"])
@login_required
def menu():
    task_list = taskGeneration()
    form = FlaskForm()
    # 設定をconfigから取得
    gemini_pro = current_app.config["GEMINI"]
    prsnlty_id = 1
    # 前回以前の履歴の取得
    history = getHistory()
    # 人格の一覧を取得
    prsnlty = getPrsnlty()

    # 直前のチャット履歴の取得
    if 'chat_his' in session:
        chat_his = session['chat_his']
    else:
        chat_his = []

    # POSTの時
    if request.method == 'POST':
        # 人格idの取得
        prsnlty_id = int(request.form['prsnlty_id'])
        # 人格のプロンプト文を取得
        prsnlty_plompt = serchPrsnlty(prsnlty_id)
        # 人格プロンプト文を設定
        history.append({"role":"user", "parts":prsnlty_plompt})
        # 共通のプロンプト文を設定
        history.append({"role":"user", "parts":"これ以降の文章は100文字以内で収めて、できうる限りほめてあげてください。過去の褒め方とできるだけ違う褒め方にしてください"})
        
        # 投稿の取得
        text = request.form['text']
        # chatbotのスタート
        ai = gemini_pro.start_chat(history=history)
        # レスポンスの生成
        response = chat(text,ai)
        # chatの履歴へ追加
        # chat_his.append({'user':text,'model':response})
        chat_his.insert(0,{'user':text,'model':response})
     
    # セッションにchatの履歴を保存
    session['chat_his'] = chat_his
    return render_template('main/index.html', chat_his=chat_his, prsnlty=prsnlty, prsnlty_id=prsnlty_id, form=form, task_list=task_list)


# chatの処理
def chat(text,ai):
    # 回答の生成
    response = ai.send_message(text).text
    # 回答の保存
    saveHistory(text,response)
    return response

# chatの履歴をDBへ保存する関数
def saveHistory(text,response):
    # chatの履歴を格納
    chat_his = ChatHistory(
        user_id = userid,
        user = text,
        model = response
    )
    db.session.add(chat_his)
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
        history += [{"role":"user", "parts":his.user},{"role":"model", "parts":his.model}]
    
    return history

# 人格の一覧を取得
def getPrsnlty():
    prsnlty = []
    prsnlties = (
        db.session.query(Prsnlty).all()
    )
    for prs in prsnlties:
        prsnlty.append({"id":prs.prsnlty_id, "name":prs.name})
    
    return prsnlty

# 人格のidからプロンプト文を取得
def serchPrsnlty(id):
    prsnlty = (
        db.session.query(Prsnlty).filter(Prsnlty.prsnlty_id == id).first()
    )
    return prsnlty.prompt

# タスクをランダムで3つ生成してリストで返す
def taskGeneration():
    today = datetime.today().strftime("%Y年%m月%d日")
    prompt = f"あなたはポジティブで人を褒めるのが得意なコーチです。今日は{today}です。毎日達成できる、シンプルで簡単な日常タスクを3つ考えてください。それぞれのタスクは1文で、短く、わかりやすくしてください。難しいことではなく、実行しやすい前向きな内容にしてください。タスクは10個生成して下さい。出力形式は「今日〇〇してみましょう」のようにして一文でタスクどうしは「:」でつなげてください。"
    gemini_pro = current_app.config["GEMINI"].start_chat()
    # ランダム性を持たせるようにした
    task = gemini_pro.model.generate_content(
        prompt,
        generation_config={
            "temperature": 1.2,
            "top_p": 0.9,
            "top_k": 40
        }
    ).text.split(':')

    rannum = random.sample(range(10), 3)
    result = [task[rannum(0)],task[rannum[1]],task[rannum[2]]]

    return result

# def getTask():
    

    

    