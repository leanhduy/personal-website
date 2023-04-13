"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import mimetypes

# Load environment variables from .env file
load_dotenv()


# Add SVG to the list of known mimetypes for loading svg file in Vue templates
mimetypes.add_type("image/svg+xml", ".svg")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# FOR MONITORING ONLY - PRINT THE PATH OF BASE_DIR
print("base dir path", BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: Removed this secret key for SECURITY reason. When deploying to production, generate a new secret key and store it in an environment variable, using this command
# python manage.py shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "leanhduy.pythonanywhere.com",
    "personal-website-git-main-leanhduy.vercel.app",
    "personal-website-leanhduy.vercel.app",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # ! FOR PASSING CI TESTS ON GITHUB - UNCOMMENT THIS SECTION AND COMMENT OUT THE NEXT SECTION WHEN COMMITTING TO GITHUB
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # ! FOR DEVELOPING LOCALLY - UNCOMMENT THIS SECTION AND COMMENT OUT THE PREVIOUS SECTION WHEN DEVELOPING LOCALLY
    # ? POSTGRES
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "personal_website_dev_db",
    #     "USER": "postgres",
    #     "PASSWORD": os.getenv("DB_PASSWORD"),
    # },
    # ? MYSQL
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "personal_website_dev_db",
    #     "USER": "root",
    #     "PASSWORD": os.getenv("MYSQL_ROOT_PW"),
    #     "HOST": "127.0.0.1",
    #     "PORT": "3306",
    #     "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    "https://personal-website-git-main-leanhduy.vercel.app",
    "https://personal-website-leanhduy.vercel.app",
]

CORS_ALLOW_ALL_ORIGINS = True
