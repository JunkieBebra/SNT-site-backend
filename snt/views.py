from django.shortcuts import render
from snt.models import ProminentOnes, ImportantMessage


def index(request):
    model = ImportantMessage.objects.last()
    context = {
        'title': 'СНТ "Мичуринец-3"',
        'message': model
    }
    return render(request, 'snt/index.html', context)


def about_us(request):
    model = ProminentOnes.objects.all()
    context = {
        'title': 'О нас',
        'prominent_cr': model.filter(type='CR'),
        'prominent_gv': model.filter(type='GV'),
        'prominent_gp': model.filter(type='GP'),
        'prominent_ob': model.filter(type='OB')

    }
    return render(request, 'snt/page_about_us.html', context)
