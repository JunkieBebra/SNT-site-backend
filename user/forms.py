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


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': 'email@example.ru',
        'name': 'email',
        'type': 'email',
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': 'Иван',
        'name': 'first_name',
        'type': 'text',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': 'Иванов',
        'name': 'last_name',
        'type': 'text',
    }))

    patronym = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': 'Иванович',
        'name': 'patronym_name',
        'type': 'text',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': '••••••••',
        'name': 'password1',
        'type': 'password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5',
        'placeholder': '••••••••',
        'name': 'password2',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronym', 'username', 'password1', 'password2')
