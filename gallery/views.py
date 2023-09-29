from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gallery.models import Image


@login_required
def gallery(request):
    images = Image.objects.all()
    context = {
        'title': 'Галерея',
        'images': images
    }
    return render(request, 'gallery/gallery.html', context)
