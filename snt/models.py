from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Модель пользователя в рамках сайта. Наследует логику абстрактного пользователя Django. Добавленные поля: patronym - 
отчество, address - номер участка пользователя.
"""


class User(AbstractUser):
    patronym = models.CharField(null=True, blank=True, max_length=150)

