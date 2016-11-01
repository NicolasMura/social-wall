# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import View, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from .models import Profile, Post
from .forms import ProfileForm
from django.contrib.auth import authenticate, login

from .wall_profile import get_wall_profile


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
#     template_name = "social/wall_profile.html"
#     success_url = reverse_lazy(
#         'social:wall-profile-view',
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


class WallProfileView(AppView):
    """
    A DOCUMENTER
    """
    template_name = "social/wall_profile.html"

    def get(self, request, profile):
        profile = Profile.objects.get(username=profile)

        wall_profile = get_wall_profile(
                profile=profile)
        self.context.update({
            'wall_profile': wall_profile
        })
        return render(request, self.template_name, self.context)

    def post(self, request, profile):
        # # Save user's post if valid
        # post_form = PostForm(request.POST)
        # if post_form.is_valid():
        #     post_form.save()
        #     # Clean form and update context
        #     post_form = PostForm()
        #     self.context.update({
        #         'post_form': post_form,
        #     })
        #     # Add success message
        #     messages.add_message(
        #         request,
        #         messages.SUCCESS,
        #         'Votre message a été publié !'
        #     )
        # else:
        #     self.context.update({
        #         'post_form': post_form,
        #     })

        profile = Profile.objects.get(username=profile)

        wall_profile = get_wall_profile(
                profile=profile)

        if 'submit-user-post' in self.request.POST:
            print("POST submit-user-post")
            wall_profile.process_user_post(request=request)
        if 'submit-user-comment' in self.request.POST:
            print("POST submit-user-comment")
            wall_profile.process_user_comment(request=request)
        self.context.update({
            'wall_profile': wall_profile,
        })
        print("Erreurs : ", wall_profile.user_comment_form.errors)

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

    model = ProfileForm
    template_name = 'social/signup.html'
    form_class = ProfileForm
    success_url = reverse_lazy(
        'social:wall-profile-view',
        kwargs={'profile': '%(username)s'},
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
