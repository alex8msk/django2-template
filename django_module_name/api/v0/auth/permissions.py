from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_anonymous
