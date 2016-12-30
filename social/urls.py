# -*- coding: utf-8 -*-
# from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
# from django.contrib.auth import views as auth_views
from django.conf.urls import include

from .views import *

# app_name = 'social'

urlpatterns = patterns(
    # '',
    'social.views',
    url(
        r'^$',
        WallView.as_view(),
        name='wall-view',
    ),
    url(
        r'^wall/(?P<username>.+)$',
        # r'^profile/(?P<username>[\w.@+-]+)/$',
        WallProfileView.as_view(),
        name='wall-profile-view',
    ),
    url(
        r'^i18n/',
        include('django.conf.urls.i18n'),
    ),
)
