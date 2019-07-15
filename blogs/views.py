from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blogs.forms import PostForm
from blogs.models import Blog


def blogs_index(request):

    # Recoger los blogs existentes
    blogs = Blog.objects.all().order_by('-modification_date')

    # Creamos el contexto

    context = {'latest_blogs': blogs[:9]}

    # Crear una respuesta HTML
    html = render(request, 'blogs/blogs_index.html', context)

    #Devolver la respuesta HTML
    return HttpResponse(html)

def blog_page(request, pk):

    # Recoger los blogs existentes
    blog = get_object_or_404(Blog, pk=pk)

    # Creamos el contexto

    context = {'latest_blogs': blog}

    # Crear una respuesta HTML
    html = render(request, 'blogs/blogs_index.html', context)

    #Devolver la respuesta HTML
    return HttpResponse(html)

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post creado correctamente con ID {0}'.format(new_post.pk))
            form = PostForm()
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'blogs/new.html', context)