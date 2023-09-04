from django.shortcuts import render


def index(request):
    return render(request, 'snt/index.html')


def about_us(request):
    return render(request, 'snt/page_about_us.html')
