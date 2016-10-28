# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # utile ?

# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
# from django import forms
# from django.core.files.images import get_image_dimensions


class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'avatar']

    def save(self):
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        user.avatar = self.cleaned_data['avatar']

        user = UserProfile.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        user.avatar = self.cleaned_data['avatar']

        user.save()

        return user

    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']

    #     try:
    #         w, h = get_image_dimensions(avatar)

    #         # validate dimensions
    #         max_width = max_height = 512
    #         if w > max_width or h > max_height:
    #             raise forms.ValidationError(
    #                 u'Please use an image that is '
    #                 '%s x %s pixels or smaller.' % (max_width, max_height))

    #         # validate content type
    #         main, sub = avatar.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise forms.ValidationError(
    #                 u'Please use a JPEG, GIF or PNG image.')

    #         # validate file size
    #         if len(avatar) > (20 * 1024):
    #             raise forms.ValidationError(
    #                 u'Avatar file size may not exceed 20k.')

    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass

    #     return avatar


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['email', 'username', 'avatar']

#     # user_email = forms.EmailField(label="Votre nom d'utilisateur")
#     # user_name = forms.CharField(label="Votre email", max_length=254)
#     # avatar = forms.ImageField(label="Votre avatar")
