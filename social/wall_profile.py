# -*- coding: utf-8 -*-
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages


def get_wall_home():
    return WallHome()


def get_wall_profile(profile):
    return WallProfile(profile)


class Wall(object):

    def process_user_post(self, request):
        """
        Save user's post if valid, else return form with errors.
        """
        self.user_post_form = PostForm(request.POST)
        print(self.user_post_form)
        if self.user_post_form.is_valid():
            print("form POST OK !")
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
            print("form POST NOK !")
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


class WallHome(Wall):

    def __init__(self):
        self.profile = None
        # Get post form
        self.user_post_form = PostForm()
        # Get comment forms
        self.user_comment_form = CommentForm()
        # Get all posts from all users associated comments
        self.posts = Post.objects.order_by('-submit_date')


class WallProfile(Wall):

    def __init__(self, profile):
        self.profile = profile
        # Get post form
        self.user_post_form = PostForm()
        # Get comment forms
        self.user_comment_form = CommentForm()
        # Get all user's posts & associated comments
        self.posts = Post.objects.filter(
            wall=self.profile).order_by('-submit_date')
