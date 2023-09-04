from django.urls import path
from news.views import news

app_name = 'news'

urlpatterns = [
    path('', news, name='index')
]
