"""
Django settings for hack project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e@8eoyx0g=o%^wnj5#kk68$$yt)5%q6(o06o0m0zl6u^sp2toh'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'jlemyp.ru']


INSTALLED_APPS = [
    'main.apps.SuitConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_extensions',
    'django_q',
    'reversion',

    'main.apps.MainConfig',
    'questionnaire.apps.QuestionnaireConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hack.urls'

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

WSGI_APPLICATION = 'hack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'hack',
        # 'USER': 'postgres',
        # 'PASSWORD': 'postgres',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTH_USER_MODEL = 'main.CustomUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'main.auth_backend.CustomAuthBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'static'


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = 'http://127.0.0.1:8000/_storage/'
MEDIA_URL = '/media/'

email = os.environ.get('EMAIL')
DEFAULT_FROM_EMAIL = email
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = email
EMAIL_HOST_PASSWORD = os.environ.get('PASSWORD')
# EMAIL_PORT = 587
EMAIL_PORT = 465


# -------- rest --------

REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'non_field_errors',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'main.renderers.JsonUnicodeRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}


# -------- rest jwt --------

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(weeks=4),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=4),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# -------- django-q --------

Q_CLUSTER = {
    'workers': 1,
    'recycle': 50,
    'catch_up': False,
    'timeout': 120,
    'compress': False,
    'save_limit': 250,
    'queue_limit': 2,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'bulk': 10,
    'orm': 'default',
}

# -------- own --------

RAPIDAPI_KEY = '04f156dee2mshcf09f640b7d94c6p19aae5jsnc108a262d259'
