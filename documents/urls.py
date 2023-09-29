from django.urls import path
from documents.views import documents, directory, download

app_name = 'documents'

urlpatterns = [
    path('category/<int:category_id>', documents, name='index'),
    path('category/directory/<int:directory_id>', directory, name='directory'),
    path('download/<int:index>', download, name='download')
]
