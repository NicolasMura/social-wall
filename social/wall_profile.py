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
            user=self.profile).order_by('-submit_date')

    def save_user_post(self, request):
        # Get all user's posts
        # profile_posts = Post.objects.filter(
        #     user=self.user).order_by('-submit_date')

        # # Update context
        # self.context.update({
        #     'profile_posts': profile_posts,
        # })
        # Save user's post if valid
        self.post_form = PostForm(request.POST)
        if self.post_form.is_valid():
            self.post_form.save()
            # Clean form and update context
            self.post_form = PostForm()
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre message a été publié !'
            )
        else:
            self.post_form = self.post_form
