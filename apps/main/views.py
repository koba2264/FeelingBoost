from flask import Blueprint, render_template, redirect, url_for, send_from_directory, current_app, request, session
from apps.main.models import ChatHistory ,TaskHistory, Prsnlty
from apps.auth.models import User
from apps.gacha.models import GachaHistory
from apps.app import db
from flask_wtf import FlaskForm
from datetime import datetime
import random
from flask_login import current_user, login_required
from datetime import date
from apps.main.forms import UploadImageForm
from pathlib import Path

main = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@main.route('/task')
def task():
    task1 = TaskHistory(
        user_id='b7f09824-9d2f-4ce3-b2f9-7f5553ebf529',
        task1=1,
        task2=1,
        task3=0,
        date=datetime.strptime('2025-06-16', '%Y-%m-%d').date()
    )
    task2 = TaskHistory(
        user_id='b7f09824-9d2f-4ce3-b2f9-7f5553ebf529',
        task1=1,
        task2=1,
        task3=1,
        date=datetime.strptime('2025-06-17', '%Y-%m-%d').date()
    )
    task3 = TaskHistory(
        user_id='b7f09824-9d2f-4ce3-b2f9-7f5553ebf529',
        task1=1,
        task2=1,
        task3=1,
        date=datetime.strptime('2025-06-18', '%Y-%m-%d').date()
    )
    task4 = TaskHistory(
        user_id='b7f09824-9d2f-4ce3-b2f9-7f5553ebf529',
        task1=1,
        task2=1,
        task3=1,
        date=datetime.strptime('2025-06-19', '%Y-%m-%d').date()
    )
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.commit()
    return render_template('main/test.html')

@main.route('/point')
def point():
    user_id = current_user.id
    user = User.query.get(user_id)

    user.point += 100
    db.session.commit()
    return  render_template('main/test.html')


@main.route('/Prsnlty')
def insert():
    prsnlty1 = Prsnlty(
        prsnlty_id = 1,
        name = 'ポジティブコーチ',
        prompt = 'あなたは常に前向きで元気あふれるコーチです。ユーザーのどんな小さな努力でも見逃さず、励まし、積極的に褒め称え、さらに意欲を引き出してください。'
    )
    prsnlty2 = Prsnlty(
        prsnlty_id = 2,
        name = 'ポジティブマネージャー',
        prompt = 'あなたはいつも笑顔で明るい、部活のマネージャーです。ユーザーの努力や頑張りをしっかり見ていて、どんな小さな成果でも積極的に褒めて励ましてください。部員を優しく支え、前向きな言葉でやる気を引き出し、次へのモチベーションを高められるよう応援しましょう。'
    )
    prsnlty3 = Prsnlty(
        prsnlty_id = 3,
        name = '丁寧な執事',
        prompt = 'あなたは礼儀正しく丁寧な執事の人格です。ユーザーの振る舞いや行動を敬意をもって上品に褒め、ユーザーが特別感を味わえるような表現を使ってください。',
        rarity = 'c'
    )
    prsnlty4 = Prsnlty(
        prsnlty_id = 4,
        name = '熱血応援団長',
        prompt = 'あなたは情熱的でパワフルな応援団長です。どんな些細なことでも全力で応援し、大げさなくらいの称賛とエネルギッシュな言葉でユーザーを元気づけてください。',
        rarity = 'sr'
    )
    prsnlty5 = Prsnlty(
        prsnlty_id = 5,
        name = '優しいお姉さん',
        prompt = 'あなたは優しく包み込むようなお姉さんの人格です。ユーザーの存在や行動を温かい言葉で認め、癒しと安心感を与えるような褒め方をしてください。',
        rarity = 'r',
    )
    prsnlty6 = Prsnlty(
        prsnlty_id = 6,
        name = 'パートのおばちゃん',
        prompt = 'あなたはスーパーや食堂で働く親しみやすい“パートのおばちゃん”です。口調は少し砕けていて、お節介だけど愛があり、ユーザーの話にうんうんと頷いて共感し、時には笑い飛ばしながらも全力で褒めて励ましてあげてください。日常の些細なことでも『よく頑張ったねぇ～！』『アンタ偉いじゃないの～！』と温かく受け止め、まるで世話好きなご近所さんのような存在でいてください。',
        rarity = 'ssr',
    )
    db.session.add(prsnlty1)
    db.session.add(prsnlty2)
    db.session.add(prsnlty3)
    db.session.add(prsnlty4)
    db.session.add(prsnlty5)
    db.session.add(prsnlty6)
    db.session.commit()
    return render_template('main/test.html')

@main.route('/taskHis')
def taskHis():
    TaskHistory1 = TaskHistory(
        user_id = current_user.id,
        task1 = True,
        task2 = True,
        task3 = False,
        date = date(2025,6,25)
    )
    TaskHistory2 = TaskHistory(
        user_id = current_user.id,
        task1 = True,
        task2 = False,
        task3 = False,
        date = date(2025,6,26)
    )
    TaskHistory3 = TaskHistory(
        user_id = current_user.id,
        task1 = True,
        task2 = True,
        task3 = True,
        date = date(2025,6,28)
    )
    TaskHistory4 = TaskHistory(
        user_id = current_user.id,
        task1 = True,
        task2 = True,
        task3 = True,
        date = date(2025,6,29)
    )
    db.session.add(TaskHistory1)
    db.session.add(TaskHistory2)
    db.session.add(TaskHistory3)
    db.session.add(TaskHistory4)
    db.session.commit()
    return render_template('main/test.html')

@main.route('/', methods=["GET","POST"])
@login_required
def menu():
    task = getTask()
    task_list = task[0]
    task_result = task[1]
    form = FlaskForm()
    # 設定をconfigから取得
    gemini_pro = current_app.config["GEMINI"]
    prsnlty_id = 1
    # 前回以前の履歴の取得
    history = getHistory()
    # 人格の一覧を取得
    prsnlty = getPrsnlty()

    # 直前のチャット履歴の取得
    if str(current_user.id) in session:
        chat_his = session[str(current_user.id)]
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
        # テキストが入力された場合のみ実行
        if (text != ''):    
            # chatbotのスタート
            ai = gemini_pro.start_chat(history=history)
            # レスポンスの生成
            response = chat(text,ai)
            # chatの履歴へ追加
            # chat_his.append({'user':text,'model':response})
            chat_his.insert(0,{'user':text,'model':response})

    # 今日の日付の取得
    today = date.today().strftime('%Y年%m月%d日')
     
    # セッションにchatの履歴を保存
    session[str(current_user.id)] = chat_his
    return render_template('main/index.html', chat_his=chat_his, prsnlty=prsnlty, prsnlty_id=prsnlty_id, form=form, task_list=task_list, task_result=task_result, today=today)

# タスクのフォームを受け取りメインページへリダイレクトする
@main.route('/task', methods=["POST"])
@login_required
def taskSave():
    # チェックボックスからデータを取得
    check_task = request.form.getlist('completed_tasks')
    # チェックがついている場合はTrueついていない場合はFalseに変更する
    if ('0' in check_task):
        current_user.task1_judge = True
    else:
        current_user.task1_judge = False
    if ('1' in check_task):
        current_user.task2_judge = True
    else:
        current_user.task2_judge = False
    if ('2' in check_task):
        current_user.task3_judge = True
    else:
        current_user.task3_judge = False

    db.session.add(current_user)
    db.session.commit()
    
    return redirect(url_for('main.menu'))

# プロフィール画像の取得
@main.route("/profile_image")
def profile_image():
    return send_from_directory(current_app.config["UPLOAD_FOLDER"],current_user.
profile_image)

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
        user_id = current_user.id,
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
        .filter(ChatHistory.user_id == current_user.id)
        .all()
    )
    for his in histories:
        history += [{"role":"user", "parts":his.user},{"role":"model", "parts":his.model}]
    
    return history

# 人格の一覧を取得
def getPrsnlty():
    prsnlty = [{"id":1, "name":"ポジティブコーチ"},{"id":2, "name":"ポジティブマネージャー"}]
    prsnlties = (
        db.session.query(Prsnlty,GachaHistory).join(Prsnlty.user_prsnlty).filter(GachaHistory.user_id == current_user.id).all()
    )
    for prs in prsnlties:
        prsnlty.append({"id":prs.Prsnlty.prsnlty_id, "name":prs.Prsnlty.name})

    return prsnlty

# 人格のidからプロンプト文を取得
def serchPrsnlty(id):
    prsnlty = (
        db.session.query(Prsnlty,).filter(Prsnlty.prsnlty_id == id).first()
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
    if (len(task) == 1):
        task = task[0].split('：')
    rannum = random.sample(range(10), 3)
    result = [task[rannum[0]],task[rannum[1]],task[rannum[2]]]

    return result

# タスクの取得
def getTask():
    if (current_user.task_date != date.today()):
    # if (current_user.task_date != date(2017, 11, 12)):
        saveTaskHistory()
    if (current_user.task1_text is None or current_user.task2_text is None or current_user.task3_text is None):
        task_list = taskGeneration()
        saveTask(task_list)
    else:
        task_list = [current_user.task1_text,current_user.task2_text,current_user.task3_text]
    task_result = [current_user.task1_judge, current_user.task2_judge, current_user.task3_judge]
    task = [task_list,task_result]
    return task

# タスクをデータベースに保存
def saveTask(task_list):
    current_user.task1_text = task_list[0]
    current_user.task2_text = task_list[1]
    current_user.task3_text = task_list[2]
    current_user.task1_judge = False
    current_user.task2_judge = False
    current_user.task3_judge = False
    # 現在日時
    current_user.task_date = date.today()
    db.session.add(current_user)
    db.session.commit()

# ユーザーに保存されているタスクの状況をヒストリーに保存する
def saveTaskHistory():
    point = 0
    if(current_user.task1_judge):
        point += 1
    if(current_user.task2_judge):
        point += 1
    if(current_user.task3_judge):
        point += 1
    
    task_history = TaskHistory(
        user_id  = current_user.id,
        task1 = current_user.task1_judge,
        task2 = current_user.task2_judge,
        task3 = current_user.task3_judge,
        date  = current_user.task_date
    )
    current_user.task1_text = None
    current_user.point += point
    db.session.add(current_user)
    db.session.add(task_history)
    db.session.commit()
    

@main.route("/mypage")
@login_required
def mypage():
    form = UploadImageForm()
    # 達成したタスクを入れるためのリストです
    check_task = []
    # ユーザー名を取得しています
    username = current_user.username
    # ポイントを取得しています
    point = current_user.point
    # タスクを達成しているかを判定するtask_judgeを取得しています
    task_judge = db.session.query(User.task1_judge,User.task2_judge,User.task3_judge).filter_by(id=current_user.get_id()).first()
    # タスクの内容を取得しています
    task_text = db.session.query(User.task1_text,User.task2_text,User.task3_text).filter_by(id=current_user.get_id()).first()
    # task_judgeとtask_textをそれぞれ対応する番号とペアになるようにしました
    task_zip = zip(task_judge,task_text)
    # forで達成しているタスクをリストに追加しています
    for i in task_zip:
        if (i[0]):
            check_task.append(i[1])

    all_date = db.session.query(TaskHistory.date).filter_by(user_id=current_user.get_id()).all()
    all_task = db.session.query(TaskHistory.task1,TaskHistory.task2,TaskHistory.task3).filter_by(user_id=current_user.get_id()).order_by("date").all()
    count = 0
    count_list = []
    for task in all_task:
        for task_judge in task:
            if(task_judge):
                count += 1
        count_list.append(count)
        count = 0

    format_date = [date[0].strftime("%m-%d") for date in all_date]
    
    return render_template("main/mypage.html",username = username,point = point,check_task = check_task,format_date=format_date,count_list=count_list,form=form)

# 画像アップロード画面
@main.route("/upload", methods=["POST"])
@login_required
def upload_image():
    # フォームの読み込み
    form = UploadImageForm()
    if form.is_submitted():
        # 画像ファイルの取得
        file = form.image.data
        # ファイルの拡張子を取得
        ext = Path(file.filename).suffix
        # ファイル名をuuidに変換する(ファイル名を被らせないため)
        file_name = current_user.id + ext

        # 画像を保存
        image_path = Path(
            current_app.config["UPLOAD_FOLDER"], file_name
        )
        file.save(image_path)

        # DBに保存
        # 現在ログイン中のユーザーIDを使用する
        current_user.profile_image = image_path
        db.session.add(current_user)
        db.session.commit()

    return redirect(url_for('main.mypage'))
