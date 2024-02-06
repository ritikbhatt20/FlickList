from django.test import TestCase
from django.contrib import auth
from .models import *

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = Movie.objects.create_user('test@dom.com', 'iamtest', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')
# Create your tests here.
