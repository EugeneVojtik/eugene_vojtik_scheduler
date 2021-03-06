"""
Django settings for event_book project.
Generated by 'django-admin startproject' using Django 3.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
from decouple import config
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "rtb*w^093ygy%(2n_px8r!ky!dh^evcub7*3s+_%kc@7n2q=k^"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = ['scheduler-reminder-app.herokuapp.com/', '127.0.0.1']
# ALLOWED_HOSTS = ['127.0.0.1:6379', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'event_manager',
    'authentication_app',
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    'django_celery_results',
    'django_redis',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scheduler_APP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'scheduler_APP.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://cache://127.0.0.1:6379/1'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Extra places for collectstatic to find static files.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'event_manager.SchedulerUser'

REMIND_OPTIONS = [
    ((timedelta(hours=1)), 'in 1h'),
    ((timedelta(hours=2)), 'in 2h'),
    ((timedelta(hours=4)), 'in 4h'),
    ((timedelta(days=1)), 'day before'),
    ((timedelta(weeks=1)), 'week before'),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'evtestingemail@gmail.com'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_PASSWORD = "testtest1234567"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# REDIS_HOST = '0.0.0.0'
# REDIS_PORT = '6379'

CELERY_BROKER_URL = 'redis://:pdb2d30accd4ded711da61b429422c41f96cc719e0b20fd711c04fcbb473061bb@ec2-52-48-196-4.eu-west-1.compute.amazonaws.com:8529'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "UTC"
CELERY_BEAT_SCHEDULE = {
    "task_one": {
        "task": "event_manager.tasks.to_remind",
        "schedule": 180.0,
    },

}

# Activate Django-Heroku
django_heroku.settings(locals())
