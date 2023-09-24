from django.shortcuts import render


def gallery(request):
    context = {'title': 'Галерея'}
    return render(request, 'gallery/gallery.html', context)
