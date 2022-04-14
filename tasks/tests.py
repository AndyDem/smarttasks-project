from datetime import datetime
from django.test import TestCase

from tasks.forms import TaskForm
from tasks.models import Task


class UnitTestCase(TestCase):

    def test_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'users/home.html')

    def test_signup_template(self):
        response = self.client.get('/signup')
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_login_template(self):
        response = self.client.get('/login')
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_template(self):
        response = self.client.get('/logout')
        self.assertTemplateUsed(response, 'users/logout.html')

    def test_task_form(self):
        form = TaskForm(data={'text': 'Test'})
        self.assertFalse(form.is_valid())
        form = TaskForm(data={'text': 'Test', 'priority': 0})
        self.assertTrue(form.is_valid())
        form = TaskForm(
            data={'text': 'Test', 'priority': 0, 'deadline': datetime.now()}
        )
        self.assertTrue(form.is_valid())
