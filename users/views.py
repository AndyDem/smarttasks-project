from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from users.forms import CustomAuthenicationForm, CustomUserCreationForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView


class HomeView(TemplateView):
    template_name = 'users/home.html'
    extra_context = {'today': datetime.today()}


class SignupView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['referer'] = self.request.META['HTTP_REFERER']
        except KeyError:
            context['referer'] = None
        return context


class LoginInterfaceView(BSModalLoginView):
    form_class = CustomAuthenicationForm
    template_name = 'users/login.html'
    success_message = 'Successfully logged in.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['referer'] = self.request.META['HTTP_REFERER']
        except KeyError:
            context['referer'] = None
        return context


class LogoutInterfaceView(LogoutView):
    # template_name = 'users/logout.html'
    success_message = 'Successfully logged out.'
