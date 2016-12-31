# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns(
    '',
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
)
