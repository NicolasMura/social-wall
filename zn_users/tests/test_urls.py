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
        self.user = Profile.objects.create_user(
            username='test', email='test@test.com', password='test')

        # Create a client
        self.client = Client()

    def test_public_urls(self):
        for url in public_urls:
            response = self.client.get(reverse(url['name']))
            self.assertEqual(
                response.status_code, url['status'], msg=url['name'])

    def test_private_urls(self):
        # Login
        self.client.login(
            username='test', password='test')
        for url in private_urls:
            response = self.client.get(
                reverse(url['name'], kwargs={'pk': self.user.pk}))
            self.assertEqual(
                response.status_code, url['status'], msg=url['name'])

public_urls = [
    {'name': 'zn_users:generic-login-view', 'status': 200},
    {'name': 'zn_users:user-profile-signup-view', 'status': 200},
    {'name': 'zn_users:generic-logout', 'status': 302},
]

private_urls = [
    {'name': 'zn_users:user-profile-update-view', 'status': 200},
]
