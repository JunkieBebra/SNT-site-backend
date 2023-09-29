from django.http.response import FileResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from documents.models import Directory, Category, Document
from MitschurinezSNT.settings import BASE_DIR


@login_required
def documents(request, category_id=1):
    category = Category.objects.filter(id=category_id).first()
    directories = Directory.objects.filter(document_type=category_id)
    context = {
        'title': 'Документация',
        'directories': directories,
        'category': category,
        'category_id_1': True if category_id == 1 else False,
        'category_id_2': True if category_id == 2 else False,
        'category_id_3': True if category_id == 3 else False,
        'category_id_4': True if category_id == 4 else False,
        'category_id_5': True if category_id == 5 else False
    }
    return render(request, 'documents/documentation.html', context)


@login_required
def directory(request, directory_id=None):
    directory_of_page = Directory.objects.filter(id=directory_id).first()
    documents_on_page = Document.objects.filter(directory=directory_id)
    context = {
        'base_dir': BASE_DIR,
        'title': 'Директория ' + directory_of_page.name,
        'documents': documents_on_page,
        'directory': directory_of_page,
        'category_id_1': True if directory_of_page.document_type.id == 1 else False,
        'category_id_2': True if directory_of_page.document_type.id == 2 else False,
        'category_id_3': True if directory_of_page.document_type.id == 3 else False,
        'category_id_4': True if directory_of_page.document_type.id == 4 else False,
        'category_id_5': True if directory_of_page.document_type.id == 5 else False
    }
    return render(request, 'documents/directory.html', context)


@login_required
def download(request, index):
    obj = Document.objects.get(id=index)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response
