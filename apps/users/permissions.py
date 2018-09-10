from rest_framework import permissions

from .models import User


class IsLibrarianUser(permissions.BasePermission):
    """Check if user is librarian"""

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS):
            return True

        user = User.objects.get(username=request.user)
        profile = user.is_librarian()
        return profile


class IsVisitorUser(permissions.BasePermission):
    """ Checks if the user is a Visitor """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = User.objects.get(username=request.user)
        return user.is_librarian()


class IsStudentUser(permissions.BasePermission):
    """ Checks if user is registered as student """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = User.objects.get(username=request.user)
        return user.is_student()
