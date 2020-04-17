"""
Django settings for posapi project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from datetime import timedelta
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r^q2y!0skd=t!z$ig5^psljjdndswe)02b80f8im1kkra1br2)4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

AUTH_USER_MODEL = "accounts.user"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    )
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # < As per whitenoise documentation
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',

    'django_celery_beat',

    'accounts',
    'backtester',
]


# Celery settings
#CELERY_BROKER_URL = 'amqp://localhost'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

# for security reasons, mention the list of accepted content-types (in this case json)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Dhaka'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://localhost:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

# CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#    }
# }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware', # "CorsMiddleware" should be placed as high as possible before "CommonMiddleware"
    'django.middleware.locale.LocaleMiddleware', # for localization. Place before "CommonMiddleware"

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'posapi.urls'

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
                'django.template.context_processors.i18n', # for localization.
            ],
        },
    },
]

WSGI_APPLICATION = 'posapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'de1kmmsedpo7an',
#             'USER': 'tvdrivjlbtnlvk',
#             'PASSWORD': 'f7fdfaaf6dd3a2052683a2945835362d84e1aa02a281908dbb4a65d283f9ac23',
#             'HOST': 'ec2-52-71-85-210.compute-1.amazonaws.com',
#             'PORT': '5432',
#     },
#         'optional': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('bn', _('Bengali')),
]

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# this is directory name where collectstatic files command will put your app level static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

# this is directory paths where you have to put your project level static files
# you can put multiple folders here
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configure app for Heroku deployment
django_heroku.settings(locals())


# cors config
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}