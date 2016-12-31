# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
# from django.contrib.auth.models import AnonymousUser, User
# from django.test import TestCase, RequestFactory

from zn_users.models import *


class StatusTest(TestCase):
    def setUp(self):
        # Create a test user
        # self.user = Profile.objects.create_user(
        #     username='test', email='test@test.com', password='test')

        # Create a client
        self.client = Client()

    def test_profile_signup(self):
        response = self.client.post(
            reverse('zn_users:user-profile-signup-view'),
            {
                'username': 'Nikouz',
                'password1': 'test',
                'password2': 'test',
                # Updload photo ? (with Factory)
            },
            follow=True
        )
        # Redirection à faire dans zn_users
        # self.assertEqual(response.template.name, 'social/wall_home.html')
        # Test user is connected
        self.assertEqual(response.context['user'].is_authenticated(), True)

        # Autres tests à écrire :
        # - erreurs de saisie sur les formulaire

    def test_login(self):
        self.test_profile_signup()
        response = self.client.post(
            reverse('zn_users:generic-login-view'),
            {
                'username': 'Nikouz',
                'password': 'test',
                'next': '',
            },
            follow=True
        )
        # Redirection à faire dans zn_users
        # self.assertEqual(response.template.name, 'social/wall_profile.html')
        # Test user is connected
        self.assertEqual(response.context['user'].is_authenticated(), True)

        # Autres tests à écrire :
        # - login avec next != ''
        # - erreurs de saisie sur les formulaire

    def test_profile_update(self):
        # TODO
        pass
