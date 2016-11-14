# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import View, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from .models import Profile, Post
from .forms import ProfileForm
from django.contrib.auth import authenticate, login

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
        # TEMP
        wall_home = get_wall_home()
        self.context.update({
            'wall_home': wall_home
        })
        return render(request, self.template_name, self.context)

    def post(self, request):
        wall_home = get_wall_home()

        if 'submit-user-post' in self.request.POST:
            print("POST submit-user-post")
            wall_home.process_user_post(request=request)
        if 'submit-user-comment' in self.request.POST:
            print("POST submit-user-comment")
            wall_home.process_user_comment(request=request)
        self.context.update({
            'wall_home': wall_home,
        })
        print("Erreurs : ", wall_home.user_comment_form.errors)

        return render(request, self.template_name, self.context)

    def render(self, request):
        # self.context.update(self.build_context(request))
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
        print("Erreurs : ", wall_profile.user_comment_form.errors)

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
