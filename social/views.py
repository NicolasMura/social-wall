# -*- coding: utf-8 -*-
from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import View, CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login
# from django.contrib import messages


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
        print(request.user)
        return self.render(request)

    def render(self, request):
        # self.context.update(self.build_context(request))
        return render(request, self.template_name, self.context)

    # print(request.user.username)
    # return render(request, 'social/wall.html', {})


class WallUserView(AppView, ListView):
    """
    A DOCUMENTER
    """
    # template_name = "social/wall_user.html"

    model = UserProfile
    template_name = "social/wall_user.html"
    context_object_name = 'avatar'
    queryset = UserProfile.objects.all()

    def get(self, request, username):
        print("request.user.avatar = ", request.user.avatar)
        print("request.user.avatar.url = ", request.user.avatar.url)

        return self.render(request)

    def render(self, request):
        return render(request, self.template_name, self.context)


# class LoginView(AppView):
#     """
#     A DOCUMENTER
#     """
#     template_name = "social/login.html"

#     # Essayer d'utiliser une vue générique !
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             messages.add_message(
#                 request, messages.INFO, 'Bonjour {} !'.format(user.username))
#             # return self.render(request)
#             return redirect('social:wall-user-view', user=user)
#         else:
#             # Return an 'invalid login' error message.
#             return self.render(request)

#     def get(self, request):
#         return self.render(request)

#     def render(self, request):
#         self.context.update(self.build_context(request))
#         return render(request, self.template_name, self.context)


class UserProfileCreateView(SuccessMessageMixin, CreateView):
    model = UserProfileForm
    template_name = 'social/signup.html'
    form_class = UserProfileForm
    success_url = reverse_lazy(
        'social:wall-user-view',
        kwargs={'username': '%(username)s'},
    )
    success_message = 'Vous êtes désormais inscrit(e) '
    'sur OpenFaceRoom, %(username)s !'

    # def get_success_url(self):
    #     return reverse('social:wall_view')

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         calculated_field=self.object.username,
    #     )

    # def get_success_url(self):
    #     return reverse(
    #         'social:wall_user_view',
    #         kwargs={'username': self.request.user.username}
    #     )

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


# def signup_view(request):
#     """
#     A DOCUMENTER
#     """

#     # Penser à utiliser request.FILES pour l'avatar !
#     # + pour le formatage des dates : https://simpleisbetterthancomplex.com/article/2016/08/10/exploring-django-utils-1.html
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)

#         if form.is_valid():
#             # On ne sauvegarde pas directement l'article
#             # dans la base de données avec un commit=False
#             article = form.save(commit=False)
#             article.slug = slugify(article.titre)
#             article.save()
#             return redirect('wall_view')  # A rediriger sur le wall_user_view

#     else:  # Si ce n'est pas du POST, c'est probablement une requête GET
#         form = ProfileForm()  # Nous créons un formulaire vide

#     return render(request, 'social/signup.html', {'profile_form': form})
