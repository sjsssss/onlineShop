import os
import pymysql
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-kwd$xwxf8m0to7x^69wg+s00uw#7=dw1r*sj)k@8ra1ofzccc='
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'qiaoqiaowu.shop', 'www.qiaoqiaowu.shop']

# 应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_extensions',

    'online_shop_backend',
    'online_shop_homepage',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'online_shop_web.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'online_shop_backend', 'static')],  # Vue 构建后 HTML 目录
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

WSGI_APPLICATION = 'online_shop_web.wsgi.application'

# 数据库设置（根据实际选择启用一项）
# -- 开发环境 homepage
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'hp_site',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': 3306,
#     }
# }

# -- 开发环境 shopping_site
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'shopping_site',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': 3306,
#     }
# }

# 密码验证器
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# REST Framework + JWT 配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASS': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=90),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGN_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# 语言与时区
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# 静态资源设置
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'online_shop_backend', 'static'),
]

# 默认主键类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 跨域设置（生产环境建议关闭 CORS_ORIGIN_ALLOW_ALL）
CORS_ALLOWED_ORIGINS = [
    "https://qiaoqiaowu.shop",
    "https://www.qiaoqiaowu.shop",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True  # 开发阶段使用，生产建议关闭
CORS_ALLOW_METHODS = ["GET", "POST", "OPTIONS", "PUT", "DELETE", "PATCH"]
CORS_ALLOW_HEADERS = ["content-type", "authorization", "x-requested-with"]

# CSRF 安全设置
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://qiaoqiaowu.shop',
    'https://www.qiaoqiaowu.shop'
]

# 日志（可选）
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'level': 'ERROR', 'class': 'logging.StreamHandler'},
    },
    'loggers': {
        'django': {'handlers': ['console'], 'level': 'ERROR', 'propagate': True},
        'my_logger': {'handlers': ['console'], 'level': 'ERROR'},
    },
}

APPEND_SLASH = False
INTERNAL_IPS = ['127.0.0.1']
