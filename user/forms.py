from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': 'email@example.ru',
        'name': 'email',
        'type': 'email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': '••••••••',
        'name': 'password',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
