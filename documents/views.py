from django.shortcuts import render

def documentation_main(request):
    return render(request, 'documents/documentation.html')
