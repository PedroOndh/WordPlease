from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users.permissions import UserPermission, BlogsPermission
from users.serializers import UserSerializer, UserListSerializer, WriteUserSerializer, BlogListSerializer


class UsersViewSet(GenericViewSet):

    permission_classes = [UserPermission]

    def get_serializer_class(self):
        return UserListSerializer if self.action == 'list' else UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def list(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WriteUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = WriteUserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogsViewSet(GenericViewSet):

    permission_classes = [BlogsPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['username']

    def get_serializer_class(self):
        return BlogListSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def list(self, request):
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append({
                'username': user.username,
                'blog_url': request.get_host() + '/' + str(user.username)
            })
        return Response(user_list)
