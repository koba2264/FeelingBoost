from pathlib import Path
import os
from dotenv import load_dotenv
import google.generativeai as genai

# config.pyの親フォルダ(apps)の親フォルダ(flaskbook)をベースフォルダに設定
basedir = Path(__file__).parent.parent

# 共通の設定
class BaseConfig:
    # セッションを使用するのに必要
    SECRET_KEY = "2AZSMss3p5QPbcY2hBs"
    # CSRF対策をする際に必要(defaultではSECRET_KEYが使われるらしい)
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"
    # 画像のアップロード先をapps/imagesに設定する
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))
    # ボイス保存先をapps/voiceに設定する
    VOICE_FOLDER = str(Path(basedir, "apps", "voice"))
    # アップロードできる画像の最大サイズを16MBに制限
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000

    # .envファイルの読み込み
    load_dotenv()
    # APIキー
    # GOOGLE_API_KEY=os.getenv("GeminiAPI")
    GOOGLE_API_KEY="AIzaSyDdj7xGZLMlls7LizCoUepOdtpfVtktLmw"
    genai.configure(api_key=GOOGLE_API_KEY)

    # GEMINI = genai.GenerativeModel("gemini-1.5-flash")
    GEMINI = genai.GenerativeModel("models/gemini-2.5-flash-lite-preview-06-17")


# 個別の設定
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = F"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = F"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CSRF対策のON/OFF
    WTF_CSRF_ENABLED = False

# 辞書にマッピング
config = {
    "testing" : TestingConfig,
    "local" : LocalConfig,
}