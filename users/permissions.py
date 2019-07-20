from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action == 'create' or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj


class BlogsPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action == 'list'

    def has_object_permission(self, request, view, obj):
        return False