from flask import Blueprint,jsonify, render_template, request, send_from_directory, current_app
import random
from flask_wtf import FlaskForm
from apps.app import db
from flask_login import current_user, login_required
from apps.gacha.models import GachaHistory
from apps.main.models import Prsnlty

gacha = Blueprint(
    "gacha",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# ガチャホーム画面
@gacha.route('/home')
@login_required
def home():
    form = FlaskForm()
    return render_template('gacha/home.html', form=form)

# ガチャ結果
@gacha.route('/result', methods=['POST'])
@login_required
def gachaApi():
    # 取得済みの人格の一覧を取得
    obtained = (
        db.session.query(Prsnlty,GachaHistory).join(Prsnlty.user_prsnlty).filter(GachaHistory.user_id == current_user.id).all()
    )
    # idのみを抜き出す
    obtainedId = []
    for obt in obtained:
        obtainedId.append(obt.Prsnlty.prsnlty_id)
    
    # レアリティの抽選
    tmp = random.random()
    # 1%
    if (tmp < 0.01):
    # if (True):
        rarity = 'ssr'
        count = 4
    # 10%
    elif (tmp < 0.11):
        rarity = 'sr'
        count = 3
    # 30%
    elif (tmp < 0.41):
        rarity = 'r'
        count = 2
    # 59%
    else:
        rarity = 'c'
        count = 1
    # 今回抽選される人格の一覧を取得
    # 被りがないようにする場合
    # prizes = (
    #     db.session.query(Prsnlty).filter(~Prsnlty.prsnlty_id.in_(obtainedId)).all()
    # )
    # 被りありの場合(こっちを使用中)
    prizes = (
        db.session.query(Prsnlty).filter(Prsnlty.rarity == rarity).all()
    )
    # リストに移動
    prize_list = []
    for prize in prizes:
        prize_list.append({"id":prize.prsnlty_id, "name":prize.name})
    
    # ランダム取得
    result = random.choice(prize_list)
    
    # 結果が取得済みかどうか確認
    overlapping = result["id"] in obtainedId

    # 被った場合(1ポイント加算)
    if (overlapping):
        current_user.point += 1
        db.session.add(current_user)
        db.session.commit()
    # 被らなかった場合(5ポイント減少,人格追加)
    else:
        # DBに保存
        gachaHis = GachaHistory(
            user_id = current_user.id,
            prsnlty_id = result["id"]
        )
        db.session.add(gachaHis)
        db.session.commit()

        # ポイントの減少(1回5ポイント)
        current_user.point -= 5
    
    return render_template('gacha/gacha_page.html',result=result, overlapping=overlapping, rarity=count )
