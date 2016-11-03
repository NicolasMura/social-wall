# -*- coding: utf-8 -*-
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages


def get_wall_profile(profile):
    return WallProfile(profile)


class WallProfile(object):

    def __init__(self, profile):
        self.profile = profile
        # Get post form
        self.user_post_form = PostForm()
        # Get comment forms
        self.user_comment_form = CommentForm()
        # Get all user's posts & associated comments
        self.profile_posts = Post.objects.filter(
            wall_profile=self.profile).order_by('-submit_date')

    def process_user_post(self, request):
        """
        Save user's post if valid, else return form with errors.
        """
        self.user_post_form = PostForm(request.POST)
        if self.user_post_form.is_valid():
            self.user_post_form.save()
            # post = self.user_post_form.save(commit=False)
            # post.user = 
            # Clean form and update context
            self.user_post_form = PostForm()
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre message a été publié !'
            )
        else:
            self.user_post_form = self.user_post_form

    def process_user_comment(self, request):
        """
        Save user's comment if valid, else return form with errors.
        """
        self.user_comment_form = CommentForm(request.POST)
        if self.user_comment_form.is_valid():
            self.user_comment_form.save()
            # Clean form and update context
            self.user_comment_form = CommentForm()
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre commentaire a été publié !'
            )
        else:
            self.user_comment_form = self.user_comment_form
