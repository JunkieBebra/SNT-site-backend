from django.shortcuts import render


def documentation_main(request):

    context = {'title': 'Документация'}

    return render(request, 'documents/documentation.html', context)
