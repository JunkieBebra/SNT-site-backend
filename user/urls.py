from django.urls import path
from user.views import login, register
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
