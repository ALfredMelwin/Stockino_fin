import os
from decimal import Decimal
from datetime import datetime
from Config import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Discord News
#DISCORD_NEWS_BOT_URL = os.environ.get('DISCORD_NEWS_URL')
#DISCORD_NEWS_BOT_AVATAR = os.environ.get('DISCORD_NEWS_BOT_AVATAR', "https://media1.tenor.com/images/ccf584b7ebafc83beb1b929ae93421ec/tenor.gif?itemid=5753267")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = Config['SECRET_KEY']

ALLOWED_HOSTS = ['stockino.me', 'www.stockino.me', '139.59.33.123']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = Config['EMAIL_USER']
EMAIL_HOST_PASSWORD = Config['EMAIL_PASS']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
BASE_URL = 'stockino.me'

DEFAULT_ACTIVATION_DAYS = 2

# This allows sendgrid to send emails to the specified id whenever server error occurs.
DEFAULT_FROM_EMAIL = 'E-Club  Stockino'
MANAGERS = (
)
ADMINS = MANAGERS

# Bank Data
DEFAULT_CASH = Decimal(100000.00)
DEFAULT_LOAN_AMOUNT = Decimal(25000.00)
MAX_LOAN_ISSUE = 3
RATE_OF_INTEREST = Decimal(0.01)  # 15%
TAX_RATE = Decimal(0.15)  # 40%

# Global settings
START_TIME = datetime.strptime(Config["START_TIME"], "%Y/%m/%d:%H:%M:%S")
STOP_TIME = datetime.strptime(Config["STOP_TIME"], "%Y/%m/%d:%H:%M:%S")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # 3rd party
    'rest_framework',
    'storages',
    'crispy_forms',
    # custom apps
    'accounts',
    'market',
    # 'chat'
]


# Replace the built-in values
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stockino.urls'
LOGOUT_REDIRECT_URL = '/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stockino.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_files")
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')

#from stockino.aws.conf import *


# SSL/TLS settings for https security
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True