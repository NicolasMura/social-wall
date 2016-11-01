# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import View, CreateView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from .models import Post
from .forms import UserProfileForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .wall_user import get_wall_user


class AppView(View):
    """
    A DOCUMENTER
    """
    template_name = "social/base.html"

    def __init__(self, *args, **kwargs):
        self.context = {}
        return super(AppView, self).__init__(*args, **kwargs)

    def get(self, request):
        return self.render(request)

    def render(self, request):
        return render(request, self.template_name, self.context)


class WallView(AppView):
    """
    A DOCUMENTER
    """
    template_name = "social/wall.html"

    # Essayer d'utiliser une vue générique !
    def get(self, request):
        return self.render(request)

    def render(self, request):
        # self.context.update(self.build_context(request))
        return render(request, self.template_name, self.context)


# class WallUserView(CreateView, AppView):
#     """
#     A DOCUMENTER
#     """

#     form_class = PostForm
#     template_name = "social/wall_user.html"
#     success_url = reverse_lazy(
#         'social:wall-user-view',
#         kwargs={'username': '%(username)s'},
#     )
#     # context_object_name = 'post_form'  # Marche pas...

#     # queryset = Post.objects.filter(user=request.user)
#     # paginate_by = 25

#     # def get_queryset(self):
#     #     print("user : ", self.request.user)
#     #     queryset = Post.objects.filter(user=self.request.user)
#     #     print("queryset : ", queryset)
#     #     return queryset

#     # Overwrite get_context_data method to get user's posts
#     def get_context_data(self, **kwargs):
#         context = super(WallUserView, self).get_context_data(**kwargs)
#         # post_form = PostForm()
#         # print(dir(context.items.__getattribute__))
#         posts = Post.objects.filter(user=self.request.user)
#         context.update({
#             # 'post_form': post_form
#             'posts': posts
#             })
#         return context

#     # Overwrite post method to save PostForm
#     # def post(self, request, username):
#     #     form = PostForm()
#     #     if form.is_valid():
#     #         print("form.cleaned_data['content'] : ", form.cleaned_data["content"])
#     #         return render(request, self.template_name, self.context)

#     #     return render(request, self.template_name, self.context)


#     # def render(self, request):
#     #     return render(request, self.template_name, self.context)


class WallUserView(AppView):
    """
    A DOCUMENTER
    """
    template_name = "social/wall_user.html"

    def get(self, request, username):
        # Get post form
        post_form = PostForm()

        # Get comment forms
        comment_form = CommentForm()

        # Get all user's posts & associated comments
        user_posts = []
        # post_dict = {}
        user_posts = Post.objects.filter(
            user=request.user.id).order_by('-submit_date')

        # for post in user_posts_list:
        #     post_dict['content'] = post
        #     comments = post.comments.all()
        #     post_dict['comments'] = comments
        #     user_posts.append(post_dict)
        #     print(user_posts)

        # Update context
        self.context.update({
            'post_form': post_form,
            'comment_form': comment_form,
            # 'user_posts': user_posts,
            'user_posts': user_posts,
        })
        return render(request, self.template_name, self.context)

    def post(self, request, username):
        # Get all user's posts
        user_posts = Post.objects.filter(
            user=request.user.id).order_by('-submit_date')

        # Update context
        self.context.update({
            'user_posts': user_posts,
        })
        # Save user's post if valid
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            # Clean form and update context
            post_form = PostForm()
            self.context.update({
                'post_form': post_form,
            })
            # Add success message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Votre message a été publié !'
            )
        else:
            self.context.update({
                'post_form': post_form,
            })

        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class PostCreate(CreateView, AppView):
    """
    A DOCUMENTER
    """

    model = Post
    fields = ['content']
    # extra_context = {'post_form': PostForm()}
    # queryset = Post.objects.filter(user=request.user)
    # paginate_by = 25

    # def get_queryset(self):
    #     print("user : ", self.request.user)
    #     queryset = Post.objects.filter(user=self.request.user)
    #     print("queryset : ", queryset)
    #     return queryset

    # Overwrite get_context_data method to get PostForm
    # def get_context_data(self, **kwargs):
    #     context = super(WallUserView, self).get_context_data(**kwargs)
    #     post_form = PostForm()
    #     context.update({
    #         'post_form': post_form
    #         })
    #     return context

    # # Overwrite post method to save PostForm
    # def post(self, request, username):
    #     form = PostForm()
    #     if form.is_valid():
    #         print("form.cleaned_data['content'] : ", form.cleaned_data["content"])
    #         return render(request, self.template_name, self.context)

    #     return render(request, self.template_name, self.context)


    # def render(self, request):
    #     return render(request, self.template_name, self.context)


class UserProfileCreateView(SuccessMessageMixin, CreateView):
    """
    Signup class based on generic CreateView class.
    Needs to overwrite form_valid method to save avatar.
    """

    model = UserProfileForm
    template_name = 'social/signup.html'
    form_class = UserProfileForm
    success_url = reverse_lazy(
        'social:wall-user-view',
        kwargs={'username': '%(username)s'},
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
