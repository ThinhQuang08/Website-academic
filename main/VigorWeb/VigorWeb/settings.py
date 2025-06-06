'''
Django settings for VigorWeb project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
'''

from pathlib import Path
import os
from .AES_GCM import decrypt_data


with open('key.txt', 'r') as file:
    # Đọc dòng đầu tiên và lưu vào biến first_line
    first_line = file.readline().strip()

key = first_line.encode('utf-8')
sec_key = decrypt_data(
    key, 'dWl0QHZudSNoY20lt1fgJlmRbEddbcXjWy1cj-_q2m3tNrkEA7M8XMHe0zbuBRwP').decode('utf-8')
access_key = decrypt_data(
    key, 'dWl0QHZudSNoY20lsS6eFi6FZiBBb_fVP1B56_jN02YcyBw6Th-Y_HzyQ77eeWJ6WT6eZxjgshN0lfdLvHubxJHOTII=').decode('utf-8')
OAUTH2_KEY = decrypt_data(
    key, 'dWl0QHZudSNoY20lziiYVlj2GU1cF6mQIVBup9zPvwccxR4kD1OwuRvJad7QfmNsDU7PQvD2MjT3LLzNDyZRiec7POet5t0MbCi-8x0XoFyzKak35foaDblgl2dmyOt37WOLow==').decode('utf-8')
OAUTH2_SECRET = decrypt_data(
    key, 'dWl0QHZudSNoY20lsVPqNDucAhpbEtXxe1FEucz382Io7hUaEAqV4RieOLaOZRCrW4SpBleCgt58FcxP3q7K').decode('utf-8')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xiqh7w^d%g^(5yo8zc+58t6ry9)=)4nq!xk-$dgsjriy&j=d=#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'site1',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'VigorWeb.urls'

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
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'VigorWeb.wsgi.application'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vigorwebsite@gmail.com'
EMAIL_HOST_PASSWORD = 'byzanesrojydokzm'  # 4chu
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vigor_website',
        'USER': 'admin',
        'PASSWORD': 'Thienlai241203',
        'HOST': 'viggor-website.clce6ae44hhz.ap-southeast-2.rds.amazonaws.com',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/site1')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# social app
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '841132686664-2agbn63nemst4l54nd79c0o23aj607mh.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '841132686664-2agbn63nemst4l54nd79c0o23aj607mh.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = OAUTH2_SECRET


LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


AWS_ACCESS_KEY_ID = sec_key
AWS_SECRET_ACCESS_KEY = access_key
AWS_STORAGE_BUCKET_NAME = 'vigorweb-storages'
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = 'ap-southeast-1'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
