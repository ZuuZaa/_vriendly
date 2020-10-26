"""
Django settings for Vriendly project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'x!=_=g)3kz4w*pt&+*h=32ku0=wnopu^=-&y@6w6amln-sr@me'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'x!=_=g)3kz4w*pt&+*h=32ku0=wnopu^=-&y@6w6amln-sr@me') 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATABASES = { 'default' : dj_database_url.config()}
DATABASES['default'] = dj_database_url.parse('postgres://ombcknsqbvvxgv:d0ae70a9af0a8ad4e0442e705f935e57eed0e991a48c87d72c5591d40835f1b1@ec2-54-157-234-29.compute-1.amazonaws.com:5432/d278ja54gd83aj', conn_max_age=600)


ALLOWED_HOSTS = ['*']

LOCALE_PATHS = [ os.path.join(BASE_DIR, 'locale')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'rest_framework',
    'rest_framework.authtoken',

    'core.apps.CoreConfig',
    'account.apps.AccountConfig',
    'app.apps.AppConfig',
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

ROOT_URLCONF = 'Vriendly.urls'

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

WSGI_APPLICATION = 'Vriendly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'vriendly',
#         'USER': 'vriendly_user',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# DATABASES = {
#     'default': {
#         'DATABASE_URL':'postgres://ombcknsqbvvxgv:d0ae70a9af0a8ad4e0442e705f935e57eed0e991a48c87d72c5591d40835f1b1@ec2-54-157-234-29.compute-1.amazonaws.com:5432/d278ja54gd83aj',
#         'HEROKU_POSTGRESQL_BLUE_URL': 'postgres://ombcknsqbvvxgv:d0ae70a9af0a8ad4e0442e705f935e57eed0e991a48c87d72c5591d40835f1b1@ec2-54-157-234-29.compute-1.amazonaws.com:5432/d278ja54gd83aj',
#         'HEROKU_POSTGRESQL_COBALT_URL': 'postgres://tnkbjxcfngpzwc:afb55bf086dbac79676b9603ec2a5187027452105cb043b8d5dbedfb5399b3f2@ec2-52-21-247-176.compute-1.amazonaws.com:5432/ddt4pvssqluu8k',
#         'DISABLE_COLLECTSTATIC': '1',
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'vriendly',
#         'USER': 'tnkbjxcfngpzwc',
#         'PASSWORD': 'afb55bf086dbac79676b9603ec2a5187027452105cb043b8d5dbedfb5399b3f2',
#         'HOST': 'ec2-52-21-247-176.compute-1.amazonaws.com',
#         'PORT': '5432',
#         'Heroku CLI': 'heroku pg:psql postgresql-clean-47158 --app vriendly',
#         'URI': 'postgres://tnkbjxcfngpzwc:afb55bf086dbac79676b9603ec2a5187027452105cb043b8d5dbedfb5399b3f2@ec2-52-21-247-176.compute-1.amazonaws.com:5432/ddt4pvssqluu8k'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'account.Account'

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


# Email Confirmation
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND  
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'zumbaghirova@gmail.com'
# EMAIL_HOST_PASSWORD = '' 
# EMAIL_USE_SSL = True  
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'zumbaghirova@gmail.com'
# EMAIL_HOST_PASSWORD = 'meamoreme1'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'