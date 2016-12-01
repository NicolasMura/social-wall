# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
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
        r'^login/$',
        LoginView.as_view(),
        name='generic-login-view',
        # To try in Django 1.10 :
        # redirect_authenticated_user=...
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        # auth_views.logout_then_login,
        {'next_page': '/'},
        name='generic-logout',
        # name='generic_logout_then_login_view',
    ),
    url(
        r'^signup/$',
        UserProfileCreateView.as_view(),
        name='user-profile-signup-view',
    ),
    url(
        r'^profile/edit/(?P<pk>\d+)$',
        login_required(UserProfileUpdateView.as_view()),
        name='user-profile-update-view',
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
