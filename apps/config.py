from pathlib import Path

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