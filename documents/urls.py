from django.urls import path
from documents.views import documentation_main

app_name = 'documents'

urlpatterns = [
    path('', documentation_main, name='index')
]
