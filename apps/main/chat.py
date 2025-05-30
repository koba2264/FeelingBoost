import os
from dotenv import load_dotenv
import google.generativeai as genai
from  flask import current_app

history = [
    {"role": "user", "parts": "おすすめの本を教えて"},
    {"role": "model", "parts": "ふむ、どんな本がお好みかね？  最近の若い者は、電子書籍ばかりで活字離れが激しいようだが…  爺さんの時代は、紙の感触、インクの匂い…それが読書の醍醐味だったのじゃ。さて、君に合う本…  まずは君の興味は何だ？  歴史が好きか？  それともミステリー？  それとも…美しい女性が登場する物語？（笑）  教えてくれれば、爺さんの蔵書の中から、君に相応しい一冊を選んでやろう。  …ただし、つまらない本は薦めないぞ。  人生は短い。  読む価値のある本を読むべきだ。"},
    ]


def main():

    # gemini_pro = current_app.config[""]

    history = []

    setting = '宇宙人風に返答してくれ'
    # chat = gemini_pro.start_chat(history=history)
    # chat.send_message(setting)

# 履歴を保存
def saveHistory(text,chat):
    history

# チャット機能
def chat(text,chat):
    response = chat.send_message(text)
    return response


main()