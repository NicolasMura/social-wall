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
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '80-9_*26o8$124q@cd6133t$cj0=26pwsoa#t^7p@h3+wa$^5p'

ALLOWED_HOSTS = ['192.168.1.2']


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
# See https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Internationalization
# See https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# See https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/s/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
AUTH_USER_MODEL = 'social.Profile'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/m/'


# Choose right settings additionnal configuration (dev or prod)
HOST = socket.gethostname()
if HOST != 'vps121400.ovh.net':
    SITE_ID = 1
    DEBUG = True
    TEMPLATE_DEBUG = True
    SECRET_KEY = 'development_settings_secret_key'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    from .production import *
