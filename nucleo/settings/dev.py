from .base import *
from decouple import config

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

CORS_ALLOW_ALL_ORIGINS = True

if config("DB_HOST", default=""):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT", default=5432, cast=int),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / config("DB_NAME", default="db.sqlite3"),
        }
    }