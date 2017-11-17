from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.test import Client
from django.core.urlresolvers import reverse
import unittest

from .views import *

class TestViews(unittest.TestCase):

    def login_user(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login = client.login(username='testuser', password='12345')

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_redirect_to_login(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 302)

    def test_index_user_ok(self):
        request = self.factory.get('/')
        request.user = User()
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_add_viagem(self):
        client,user,login = self.login_user()
        request = client.get(reverse('add_viagem'))
        html = str(request.content)
        tag_html = '<h1>Cadastrar Viagem</h1>'
        self.assertRegexpMatches(html, tag_html)

    def test_add_motorista(self):
        client,user,login = self.login_user()
        request = client.get(reverse('add_motorista'))
        html = str(request.content)
        tag_html = '<h1>Cadastrar Motorista</h1>'
        self.assertRegexpMatches(html, tag_html)
