from django.urls import path

from snt.views import about_us

app_name = 'snt'

urlpatterns = [
    path('', about_us, name='index')
]
