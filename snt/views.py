from django.shortcuts import render


def index(request):
    context = {'title': 'СНТ "Мичуринец-3"'}
    return render(request, 'snt/index.html', context)


def about_us(request):
    context = {'title': 'О нас'}
    return render(request, 'snt/page_about_us.html', context)
