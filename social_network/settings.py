# -*- coding: utf-8 -*-
"""
Django settings for social_network project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '80-9_*26o8$124q@cd6133t$cj0=26pwsoa#t^7p@h3+wa$^5p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'bootstrap3',
    'social',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'social_network.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
        ],
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

WSGI_APPLICATION = 'social_network.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # Production :
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'social_network',
    #     'USER': 'nmura',
    #     'PASSWORD': '4SVTGSwhGQj&74x2',
    #     'HOST': '127.0.0.1',  # Si bdd sur une autre machine
    #     'PORT': '',  # Si bdd utilise un autre port que celui par défaut
    # }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_ROOT = BASE_DIR  # Marche pas (doit être diff de MEDIA_ROOT)
STATIC_URL = '/s/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# RP-server
# PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
AUTH_USER_MODEL = 'social.Profile'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/m/'

# RP-server :
# MEDIA_URL = '/m/'
# STATIC_URL = '/s/'
