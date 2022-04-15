from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'placeholder': 'Enter password'}),
        strip=False,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'placeholder': 'Confirm password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'your@email.com'
            })
        }


class CustomAuthenicationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
    )
