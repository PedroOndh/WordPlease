import datetime

from rest_framework.permissions import BasePermission


class PostsPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action == 'list' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj, utc=None):
        return view.action == 'retrieve' or obj.owner == request.user or request.user.is_superuser
