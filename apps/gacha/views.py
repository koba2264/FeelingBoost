from flask import Blueprint,jsonify, render_template, request
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

# ガチャ画面
@gacha.route('/gacha_page')
@login_required
def gacha_page():
    form = FlaskForm()
    return render_template('gacha/gacha_page.html', form=form)

# ガチャAPI
@gacha.route('/result', methods=['POST'])
@login_required
def gachaApi():
    # 取得済みの人格の一覧を取得
    obtained = (
        db.session.query(Prsnlty,GachaHistory).join(Prsnlty.user_prsnlty).filter(GachaHistory.user_id == current_user.id).all()
    )
    # idのみを抜き出す
    obtainedId = [1,2]
    for obt in obtained:
        obtainedId.append(obt.Prsnlty.prsnlty_id)
    
    # 今回抽選される人格の一覧を取得
    # 被りがないようにする場合
    # prizes = (
    #     db.session.query(Prsnlty).filter(~Prsnlty.prsnlty_id.in_(obtainedId)).all()
    # )
    # 被りありの場合(こっちを使用中)
    prizes = (
        db.session.query(Prsnlty).all()
    )
    # リストに移動
    prize_list = []
    for prize in prizes:
        prize_list.append({"id":prize.prsnlty_id, "name":prize.name})
    
    # ランダム取得
    result = random.choice(prize_list)
    
    overlapping = False

    # 被らなかった場合
    if (result in prize_list):
        # DBに保存
        gachaHis = GachaHistory(
            user_id = current_user.id,
            prsnlty_id = result["id"]
        )
        db.session.add(gachaHis)
        db.session.commit()

        # ポイントの減少(1回5ポイント)
        current_user.point -= 5
    # 被った場合(1ポイント変換)
    else:
        overlapping = True
        current_user.point += 1
    
    return render_template('gacha/result.html',result=result, overlapping=overlapping)