from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blogs.models import Blog


def blogs_index(request):

    # Recoger los blogs existentes
    blogs = Blog.objects.all()

    # Creamos el contexto

    context = {'latest_blogs': blogs}

    # Crear una respuesta HTML
    html = render(request, 'blogs/index.html', context)

    #Devolver la respuesta HTML
    return HttpResponse(html)