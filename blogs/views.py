import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from blogs.forms import PostForm
from blogs.models import Post


class PostsIndexView(View):

    def get(self, request):
        # Recoger los blogs existentes
        date = datetime.datetime.now()
        posts = Post.objects.all().order_by('-modification_date').filter(publishing_date__lte=date)

        # Creamos el contexto

        context = {'latest_posts': posts[:9]}

        # Crear una respuesta HTML
        html = render(request, 'blogs/posts_index.html', context)

        # Devolver la respuesta HTML
        return HttpResponse(html)


class BlogPageView(View):

    def get_user_id(self, username):
        user = get_object_or_404(User.objects, username=username)
        return user

    def get(self, request, **kwargs):
        # Recoger los blogs existentes
        username = kwargs.get('username')
        date = datetime.datetime.now()
        posts = Post.objects.filter(owner=self.get_user_id(username)).order_by('-modification_date').filter(publishing_date__lte=date)

        # Creamos el contexto

        context = {'latest_posts': posts}

        # Crear una respuesta HTML
        html = render(request, 'blogs/blog_page.html', context)

        # Devolver la respuesta HTML
        return HttpResponse(html)


class BlogIndexView(View):

    def get(self, request):
        # Recoger los blogs existentes
        blogs = User.objects.all()

        # Creamos el contexto

        context = {'blogs': blogs}

        # Crear una respuesta HTML
        html = render(request, 'blogs/blogs_index.html', context)

        # Devolver la respuesta HTML
        return HttpResponse(html)


class NewPostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'blogs/new_post.html', context)

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post creado correctamente con ID {0}'.format(new_post.pk))
            form = PostForm()
        context = {'form': form}
        return render(request, 'blogs/new_post.html', context)


class PostDetailView(View):

    def get_user_id(self, username):
        user = get_object_or_404(User.objects, username=username)
        return user

    def get(self, request, **kwargs):
        post_id = kwargs.get('post_id')
        user_id = self.get_user_id(kwargs.get('username'))
        post = get_object_or_404(Post.objects, id=post_id, owner=user_id)

        # Creamos el contexto

        context = {'post': post}

        # Crear una respuesta HTML
        html = render(request, 'blogs/post_page.html', context)

        # Devolver la respuesta HTML
        return HttpResponse(html)
