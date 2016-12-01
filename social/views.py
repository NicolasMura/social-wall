# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View, CreateView, UpdateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from .models import Profile
from .forms import ProfileCreationForm, ProfileChangeForm
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import re

from .wall import get_wall_home, get_wall_profile


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


class LoginView(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'social/login.html'
    success_message = _('Heureux de vous revoir, %(username)s !')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        asked_page = self.request.POST['next']
        if asked_page != '':
            return asked_page
        else:
            return reverse_lazy(
                'social:wall-profile-view',
                kwargs={'username': self.request.user.username}
            )


class UserProfileCreateView(SuccessMessageMixin, CreateView):
    """
    Signup class based on generic CreateView class.
    Needs to overwrite form_valid method to login after create.
    """

    # model = Profile
    # fields = ['email', 'username', 'avatar', 'password']
    form_class = ProfileCreationForm
    template_name = 'social/signup.html'
    # Redirection to user's wall doesn't work - To correct :
    # success_url = reverse_lazy(
    #     'social:wall-profile-view',
    #     kwargs={'profile': '%(username)s'},
    # )
    success_url = reverse_lazy(
        'social:wall-view',
    )
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

    # def get_success_url(self, **kwargs):
    #     print("*****", self.request.user.username, "*****")
    #     print("*****", self.kwargs, "*****")
    #     print("*****", kwargs, "*****")
    #     return reverse_lazy(
    #         'social:wall-profile-view',
    #         kwargs={'username': self.request.user.username}
    #     )


class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    """
    Update class based on generic UpdateView class.
    """

    # model = Profile  # Needs to declare model (or queryset or queryset)
    # fields = ['email', 'username', 'avatar']
    form_class = ProfileChangeForm
    template_name = 'social/update-profile.html'

    # UserProfileUpdateView needs a QuerySet
    def get_object(self, queryset=None):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return profile

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'social:user-profile-update-view',
            kwargs={'pk': self.kwargs['pk']}
        )
