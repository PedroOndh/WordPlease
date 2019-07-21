import datetime

from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from blogs.models import Post
from blogs.permissions import PostsPermission
from blogs.serializers import PostsListSerializer, PostsSerializer


class PostsViewSet(ModelViewSet):

    permission_classes = [PostsPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content_introduction', 'content_body']
    ordering_fields = ['title', 'publishing_date']

    def get_user_id(self, username):
        user = get_object_or_404(User.objects, username=username)
        return user

    def get_queryset(self):
        date = datetime.datetime.now()
        if self.request.query_params.get('blog'):
            queryset = Post.objects.select_related('owner').order_by('-modification_date')\
                .filter(owner=self.get_user_id(self.request.query_params.get('blog')))
        else:
            queryset = Post.objects.select_related('owner').order_by('-modification_date')
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(publishing_date__lte=date)
        elif not self.request.user.is_superuser:
            queryset = queryset.filter(Q(publishing_date__lte=date) | Q(owner=self.request.user))
        return queryset

    def get_serializer_class(self):
        return PostsListSerializer if self.action == 'list' else PostsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
