from datetime import datetime
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = 'users/home.html'
    extra_context = {'today': datetime.today()}


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'


class LoginInterfaceView(LoginView):
    template_name = 'users/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'users/logout.html'
