from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users.permissions import UserPermission, BlogsPermission
from users.serializers import UserSerializer, UserListSerializer, BlogListSerializer


class UsersViewSet(ModelViewSet):

    permission_classes = [UserPermission]

    def get_serializer_class(self):

        if self.action == 'list':
            return UserListSerializer
        else:
            return UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class BlogsViewSet(ModelViewSet):

    permission_classes = [BlogsPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['username']

    def get_serializer_class(self):
        return BlogListSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset