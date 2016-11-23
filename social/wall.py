# -*- coding: utf-8 -*-
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.db.models import Q
import operator
from functools import reduce


def get_wall_home():
    return WallHome()


def get_wall_profile(profile):
    return WallProfile(profile)


class Wall(object):

    def process_user_post(self, request):
        """
        Saves user's post if valid, else returns form with errors.
        """
        self.author_post_form = PostForm(request.POST)
        if self.author_post_form.is_valid():
            self.author_post_form.save()
            # Clean form
            self.author_post_form = PostForm()
            # Update posts & post_objects_list's wall
            self.update_wall()
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre message a été publié !'
            )

    def process_user_comment(self, request):
        """
        Saves user's comment if valid, else returns form with errors.
        """
        related_post_pk = request.POST['related_post']
        related_post = Post.objects.get(pk=related_post_pk)

        # TO BE SIMPLIFIED
        for post_object in self.post_objects_list:
            if post_object['post_object']['post'] == related_post:
                index_post_object_in_list = self.post_objects_list.index(
                    post_object)
                self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'] = CommentForm(request.POST)
        if self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'].is_valid():
            self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'].save()
            # Clean form
            self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'] = CommentForm()
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre commentaire a été publié !'
            )

    def update_wall(self):
        """
        Update posts & post_objects_list's wall :
        - at wall init
        or
        - after processing user's post or comment
        """

        # Get all posts from all users associated comments
        if self.profile:
            conditions = [
                ('wall', self.profile),
                ('is_public', True),
                ('is_removed', False)
            ]
            objects_Q = [Q(x) for x in conditions]
            self.posts = Post.objects.filter(
                reduce(operator.and_, objects_Q)).order_by('-submit_date')
        else:
            conditions = [
                ('is_public', True),
                ('is_removed', False)
            ]
            objects_Q = [Q(x) for x in conditions]
            self.posts = Post.objects.filter(
                reduce(operator.and_, objects_Q)).order_by('-submit_date')
        self.post_objects_list = []

        # Get all post objects
        for post in self.posts:
            self.post_objects_list.append({'post_object': {
                'post': post,
                'author_comment_form': CommentForm(),
                }
            })


class WallHome(Wall):

    def __init__(self):
        # No profile to get
        self.profile = None
        # Get post form
        self.author_post_form = PostForm()
        # Update wall with all posts and post objects
        self.update_wall()


class WallProfile(Wall):

    def __init__(self, profile):
        # Get wall profile
        self.profile = profile
        # Get post form
        self.author_post_form = PostForm()
        # Update wall with all posts and post objects
        self.update_wall()
