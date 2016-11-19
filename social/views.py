# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import authenticate, login
import re

from .wall_profile import get_wall_home, get_wall_profile


class AppView(View):
    """
    A DOCUMENTER
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
    A DOCUMENTER
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
        wall_home = get_wall_home()
        post_dict = self.request.POST
        # print(post_dict)

        # If a post has been posted
        if 'submit-user-post' in post_dict:
            print("POST submit-user-post")
            wall_home.process_user_post(request=request)

        # If a comment has been posted
        reg_exp = r'^(submit-user-comment-\d+)'
        for key, value in post_dict.items():
            if re.search(reg_exp, key):
                post_pk = re.sub('submit-user-comment-', '', key)
                print("POST submit-user-comment-"+post_pk)
                wall_home.process_user_comment(request=request)
        self.context.update({
            'wall_home': wall_home,
        })
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class WallProfileView(AppView):
    """
    A DOCUMENTER
    """
    template_name = "social/wall_profile.html"

    def get(self, request, profile):
        profile = Profile.objects.get(username=profile)
        wall_profile = get_wall_profile(
                profile=profile)
        self.context.update({
            'wall_profile': wall_profile
        })
        return render(request, self.template_name, self.context)

    def post(self, request, profile):
        profile = Profile.objects.get(username=profile)
        wall_profile = get_wall_profile(
                profile=profile)

        if 'submit-user-post' in self.request.POST:
            print("POST submit-user-post")
            wall_profile.process_user_post(request=request)
        if 'submit-user-comment' in self.request.POST:
            print("POST submit-user-comment")
            wall_profile.process_user_comment(request=request)
        self.context.update({
            'wall_profile': wall_profile,
        })
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class UserProfileCreateView(SuccessMessageMixin, CreateView):
    """
    Signup class based on generic CreateView class.
    Needs to overwrite form_valid method to save avatar.
    """

    model = ProfileForm
    template_name = 'social/signup.html'
    form_class = ProfileForm
    # Redirection to user's wall doesn't work - To correct :
    # success_url = reverse_lazy(
    #     'social:wall-profile-view',
    #     kwargs={'profile': '%(username)s'},
    # )
    success_url = reverse_lazy(
        'social:wall-view',
    )
    # print(success_url)
    success_message = _(
        'Vous êtes désormais inscrit(e) '
        'sur OpenFaceRoom, %(username)s !')

    def form_valid(self, form):
        valid = super(UserProfileCreateView, self).form_valid(form)
        username = form.cleaned_data.get(
            'username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(
            username=username,
            password=password
        )
        login(self.request, new_user)
        return valid
