# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # utile ?

from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from django import forms
# from django.utils.html import strip_tags


class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['email', 'username', 'avatar']

    def save(self):
        user = super(ProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        user.avatar = self.cleaned_data['avatar']

        user = Profile.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        user.avatar = self.cleaned_data['avatar']

        user.save()

        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'author', 'wall']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'post-form-content-input',
            }),
        }

    # Overwrite clean method to strip HTML tags
    # def clean(self):

    #     cleaned_data = super(PostForm, self).clean()
    #     cleaned_data['content'] = strip_tags(cleaned_data.get('content'))
    #     return cleaned_data

    # def save(self):
    #     post = super(PostForm, self).save(commit=False)
    #     post.user = self.cleaned_data['user']

    #     post.save()

    #     return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'post-comment-content-input',
                'placeholder': 'Ajoutez un commentaire',
            }),
        }
