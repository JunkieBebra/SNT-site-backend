import os
import mimetypes
from django.http.response import HttpResponse, HttpResponseRedirect, Http404, FileResponse
from django.conf import settings
from django.shortcuts import render

from documents.models import Directory, Category, Document
from MitschurinezSNT.settings import BASE_DIR


def documents(request, category_id=1):
    category = Category.objects.filter(id=category_id).first()
    directories = Directory.objects.filter(document_type=category_id)
    context = {
        'title': 'Документация',
        'directories': directories,
        'category': category
    }
    return render(request, 'documents/documentation.html', context)


def directory(request, directory_id=None):
    directory_of_page = Directory.objects.filter(id=directory_id).first()
    documents_on_page = Document.objects.filter(directory=directory_id)
    context = {
        'base_dir': BASE_DIR,
        'title': 'Директория ' + directory_of_page.name,
        'documents': documents_on_page,
        'directory': directory_of_page
    }
    return render(request, 'documents/directory.html', context)


def download(request, index):
    obj = Document.objects.get(id=index)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response
