# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django import forms
# from django.utils.html import strip_tags (TO DO)

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'author', 'wall']
        widgets = {
            'content': forms.Textarea(attrs={
                'id': 'post-form-content-input',
                'rows': '2',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'related_post']
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': _('Ajoutez un commentaire'),
            }),
        }
