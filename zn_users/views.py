# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView, FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .models import Profile
from .forms import ProfileCreationForm, ProfileChangeForm


class LoginView(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'zn_users/login.html'
    success_message = _('Heureux de vous revoir, %(username)s !')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        next_page = self.request.POST['next']
        if next_page != '':
            return next_page
        else:
            return reverse_lazy(
                'social:wall-profile-view',
                kwargs={'username': self.request.user.username}
            )

    def get(self, request):
        next_page = request.GET.get('next')
        if next_page:
            messages.add_message(
                self.request,
                messages.ERROR,
                'Vous devez vous connecter pour accéder à cette page.'
            )
        if request.user.is_authenticated():
            messages.add_message(
                self.request,
                messages.INFO,
                'Vous êtes déjà connecté !'
            )
        return super(LoginView, self).get(request)


class UserProfileCreateView(SuccessMessageMixin, CreateView):
    """
    Signup class based on generic CreateView class.
    Needs to overwrite form_valid method to login after create.
    """

    # model = Profile
    # fields = ['email', 'username', 'avatar', 'password']
    form_class = ProfileCreationForm
    template_name = 'zn_users/signup.html'
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
    #     return reverse_lazy(
    #         'social:wall-profile-view',
    #         kwargs={'username': self.request.user.username}
    #     )

    def get(self, request):
        if request.user.is_authenticated():
            messages.add_message(
                self.request,
                messages.INFO,
                'Vous êtes déjà inscrit !'
            )
        return super(UserProfileCreateView, self).get(request)


class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    """
    Update class based on generic UpdateView class.
    """

    # model = Profile  # Needs to declare model (or queryset or queryset)
    # fields = ['email', 'username', 'avatar']
    form_class = ProfileChangeForm
    template_name = 'zn_users/update-profile.html'

    # UserProfileUpdateView needs a QuerySet
    def get_object(self, queryset=None):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return profile

    def get_success_url(self, **kwargs):
        messages.add_message(
                self.request,
                messages.SUCCESS,
                'Vos informations ont bien été mises à jour.'
            )
        return reverse_lazy(
            'social:user-profile-update-view',
            kwargs={'pk': self.kwargs['pk']}
        )
