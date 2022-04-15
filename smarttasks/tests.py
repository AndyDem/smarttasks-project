from datetime import datetime
from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

    def create_user(self):
        user = User()
        user.username = 'testuser'
        user.password = '123test'
        user.save()
        return user

    def test_user_object(self):
        user = self.create_user()
        pulled_user = User.objects.get(username=user.username)
        self.assertEqual(user, pulled_user)

    def test_task_form(self):
        form = TaskForm(data={'text': 'Test'})
        self.assertFalse(form.is_valid())
        form = TaskForm(data={'text': 'Test', 'priority': 0})
        self.assertTrue(form.is_valid())
        form = TaskForm(
            data={'text': 'Test', 'priority': 0, 'deadline': datetime.now()}
        )
        self.assertTrue(form.is_valid())

    def create_task(self):
        task = Task()
        task.user = self.create_user()
        task.text = 'Test'
        task.priority = 0
        task.deadline = datetime.now()
        task.save()
        return task

    def test_task_object(self):
        task = self.create_task()
        pulled_task = Task.objects.get(text='Test')
        self.assertEqual(task, pulled_task)
