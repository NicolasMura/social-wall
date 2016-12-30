# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Profile


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['email', 'username', 'avatar']

    # Needs to overwrite save method to save avatar.
    def save(self):
        user = super(ProfileCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.avatar = self.cleaned_data['avatar']

        user = Profile.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        user.avatar = self.cleaned_data['avatar']
        user.save()

        return user

    # Needs to overwrite clean method to check if email already exists
    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.exclude(pk=self.instance.pk).filter(
                email=email).exists():
            raise forms.ValidationError(_(
                'Un utilisateur avec cette adresse électronique existe déjà.'))
        return email


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['email', 'username', 'avatar', 'password']

    # Override __init__ method to get user's pk (sse views.py)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('pk', None)
        super(ProfileChangeForm, self).__init__(*args, **kwargs)

    # Needs to overwrite save method to save avatar.
    def save(self):
        user = super(ProfileChangeForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.avatar = self.cleaned_data['avatar']

        if user.avatar:
            user.avatar = self.cleaned_data['avatar']
        # If user wants to delete his avatar
        else:
            user.avatar = 'default/avatars/default-avatar.png'
        user.save()

        return user

    # Needs to overwrite clean method to check if email already exists
    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.exclude(pk=self.instance.pk).filter(
                email=email).exists():
            raise forms.ValidationError(_(
                'Un utilisateur avec cette adresse électronique existe déjà.'))
        return email
