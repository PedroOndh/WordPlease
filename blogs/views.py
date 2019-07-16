from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blogs.forms import PostForm
from blogs.models import Post


def posts_index(request):
    # Recoger los blogs existentes
    posts = Post.objects.all().order_by('-modification_date')

    # Creamos el contexto

    context = {'latest_posts': posts[:9]}

    # Crear una respuesta HTML
    html = render(request, 'blogs/blogs_index.html', context)

    # Devolver la respuesta HTML
    return HttpResponse(html)


def blog_page(request, username):
    # Recoger los blogs existentes
    posts = Post.objects.all().filter(owner=username)

    # Creamos el contexto

    context = {'latest_posts': posts}

    # Crear una respuesta HTML
    html = render(request, 'blogs/blogs_index.html', context)

    # Devolver la respuesta HTML
    return HttpResponse(html)


@login_required
def new_post(request):
    if request.method == 'POST':
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post creado correctamente con ID {0}'.format(new_post.pk))
            form = PostForm()
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)
