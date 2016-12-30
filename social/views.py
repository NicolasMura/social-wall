# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
import re

from .wall import get_wall_home, get_wall_profile
from zn_users.models import Profile


class AppView(View):
    """
    Base view for Social Wall's views
    """
    def __init__(self, *args, **kwargs):
        self.context = {}
        return super(AppView, self).__init__(*args, **kwargs)

    def get(self, request):
        return self.render(request)

    def render(self, request):
        return render(request, self.template_name, self.context)


class WallView(AppView):
    """
    This view call a WallHome Python object and returns it to context
    """
    template_name = "social/wall_home.html"

    def get(self, request):
        # TEMP ?
        wall_home = get_wall_home()

        self.context.update({
            'wall_home': wall_home,
        })
        return render(request, self.template_name, self.context)

    def post(self, request):
        # May be mutualised with WallProfileView's post method
        wall_home = get_wall_home()
        post_dict = self.request.POST

        # If a post has been posted
        if 'submit-user-post' in post_dict:
            wall_home.process_user_post(request=request)

        # If a comment has been posted
        reg_exp = r'^(submit-user-comment-\d+)'
        for key, value in post_dict.items():
            if re.search(reg_exp, key):
                wall_home.process_user_comment(request=request)
        self.context.update({
            'wall_home': wall_home,
        })
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class WallProfileView(AppView):
    """
    This view call a WallProfile Python object and returns it to context
    """
    template_name = "social/wall_profile.html"

    def get(self, request, username):
        profile = Profile.objects.get(username=username)
        wall_profile = get_wall_profile(
                profile=profile)
        self.context.update({
            'wall_profile': wall_profile
        })
        return render(request, self.template_name, self.context)

    def post(self, request, username):
        # May be mutualised with WallHomeView's post method
        profile = Profile.objects.get(username=username)
        wall_profile = get_wall_profile(
                profile=profile)
        post_dict = self.request.POST

        # If a post has been posted
        if 'submit-user-post' in post_dict:
            wall_profile.process_user_post(request=request)

        # If a comment has been posted
        reg_exp = r'^(submit-user-comment-\d+)'
        for key, value in post_dict.items():
            if re.search(reg_exp, key):
                wall_profile.process_user_comment(request=request)
        self.context.update({
            'wall_profile': wall_profile,
        })
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)
