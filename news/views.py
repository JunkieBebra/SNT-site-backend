from django.shortcuts import render
from news.models import News


def news(request):
    model = News.objects.all()
    context = {
        'title': 'Новости',
        'news': model
    }
    return render(request, 'news/news.html', context)
