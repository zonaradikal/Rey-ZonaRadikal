import os
from datetime import timedelta
from dotenv import load_dotenv

# === LOAD ENVIRONMENT === #
load_dotenv()

# === KONFIGURASI APLIKASI === #
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "zona-radikal-secret-key")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/zona_radikal"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # === KONFIGURASI SESSION === #
    PERMANENT_SESSION_LIFETIME = timedelta(hours=3)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get(
        "SESSION_COOKIE_SECURE",
        "False"
    ).lower() == "true"