"""WordPlease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from blogs.views import PostsIndexView, BlogPageView, NewPostView, PostDetailView, BlogIndexView
from blogs.api import PostsViewSet
from users.api import UsersViewSet, BlogsViewSet
from users.views import LogoutView, LoginView, NewUserView

router = SimpleRouter()
router.register('api/users', UsersViewSet, basename='users_api')
router.register('api/blogs', BlogsViewSet, basename='blogs_api')
router.register('api/posts', PostsViewSet, basename='posts_api')



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('blogs/', BlogIndexView.as_view(), name='blogs'),
    path('blogs/<username>/', BlogPageView.as_view(), name='blog_page'),
    path('blogs/<username>/<post_id>', PostDetailView.as_view(), name='post_page'),
    path('new-post/', NewPostView.as_view(), name='new_post'),
    path('signup/', NewUserView.as_view(), name='new_user'),
    path('', PostsIndexView.as_view(), name='home')
] + router.urls