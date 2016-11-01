# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

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
    # url(
    #     r'^/login$',
    #     'login_view',
    #     name='login_view',
    # ),
    url(
        r'^post-create/$',
        PostCreate.as_view(),
        name='generic-post-create',
    ),
    url(
        # TO DO sur cette vue :
        # - rediriger vers le wall-user-view
        # - ajouter un message "Bonjour <user> !"
        r'^login/$',
        auth_views.login,
        {'template_name': 'social/login.html'},
        name='generic-login-view',
        # To try in Django 1.10 :
        # redirect_authenticated_user=...
    ),
    # url(
    #     r'^/logout/$',
    #     auth_views.logout_then_login,
    #     name='generic_logout_then_login_view',
    # ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': '/'},
        name='generic-logout',
    ),
    # url(
    #     r'^/signup/$',
    #     views.ProfileCreateView.as_view(),
    #     name='signup_view',
    # ),
    url(
        r'^signup/$',
        UserProfileCreateView.as_view(),
        name='generic-signup-view',
    ),
    url(
        r'^profile/(?P<profile>.+)$',
        # r'^Nikouz/$',
        login_required(WallProfileView.as_view()),
        name='wall-profile-view',
    ),
)
