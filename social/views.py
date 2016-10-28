# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import View, CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login
# from django.contrib import messages


class AppView(View):
    """
    A DOCUMENTER
    """
    template_name = "social/base.html"

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
    template_name = "social/wall.html"

    # Essayer d'utiliser une vue générique !
    def get(self, request):
        print(request.user)
        return self.render(request)

    def render(self, request):
        # self.context.update(self.build_context(request))
        return render(request, self.template_name, self.context)

    # print(request.user.username)
    # return render(request, 'social/wall.html', {})


class WallUserView(AppView, ListView):
    """
    A DOCUMENTER
    """
    # template_name = "social/wall_user.html"

    model = UserProfile
    template_name = "social/wall_user.html"
    context_object_name = 'avatar'
    queryset = UserProfile.objects.all()

    def get(self, request, username):
        print("request.user.avatar = ", request.user.avatar)
        print("request.user.avatar.url = ", request.user.avatar.url)

        return self.render(request)

    def render(self, request):
        return render(request, self.template_name, self.context)


class UserProfileCreateView(SuccessMessageMixin, CreateView):
    model = UserProfileForm
    template_name = 'social/signup.html'
    form_class = UserProfileForm
    success_url = reverse_lazy(
        'social:wall-user-view',
        kwargs={'username': '%(username)s'},
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
