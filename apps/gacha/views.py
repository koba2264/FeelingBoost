from flask import Blueprint,jsonify, render_template, request
import random

gacha = Blueprint(
    "gacha",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# ガチャ画面
@gacha.route('/gacha_page')
def gacha_page():
    return render_template('gacha/gacha_page.html')

# ガチャAPI
@gacha.route('/result', methods=['POST'])
def result():
    # ダミー抽選ロジック
    items = ['★1 Sword', '★2 Shield', '★3 Magic Wand', '★5 Legendary Sword']    
    result = random.choice(items)
    return jsonify({'result': result})