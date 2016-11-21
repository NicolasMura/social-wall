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
        Saves user's post if valid, else returns form with errors.
        """
        self.author_post_form = PostForm(request.POST)
        if self.author_post_form.is_valid():
            print("form POST OK !")
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
        else:
            print("author_post_form POST NOK !")

    def process_user_comment(self, request):
        """
        Saves user's comment if valid, else returns form with errors.
        """
        related_post_pk = request.POST['related_post']
        related_post = Post.objects.get(pk=related_post_pk)

        # TO BE SIMPLIFIED
        for post_object in self.post_objects_list:
            if post_object['post_object']['post'] == related_post:
                index_post_object_in_list = self.post_objects_list.index(post_object)
                self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'] = CommentForm(request.POST)
        if self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'].is_valid():
            print("author_comment_form POST OK !")
            self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'].save()
            # Clean form
            self.post_objects_list[index_post_object_in_list]['post_object']['author_comment_form'] = CommentForm()
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre commentaire a été publié !'
            )
        else:
            print("author_comment_form POST NOK !")

    def update_wall(self):
        """
        Update posts & post_objects_list's wall after processing user's
        post or comment
        """

        # Get all posts from all users associated comments
        if self.profile:
            self.posts = Post.objects.filter(
                wall=self.profile,
                is_public=True,
                is_removed=False).order_by('-submit_date')
        else:
            self.posts = Post.objects.filter(
                is_public=True,
                is_removed=False).order_by('-submit_date')
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