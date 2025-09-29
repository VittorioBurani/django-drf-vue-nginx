from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser


#####################
# Utility Functions #
#####################

def is_blocked(user:CustomUser) -> bool:
    return (not user.is_active)


def is_admin(user:CustomUser) -> bool:
    return user.is_superuser and user.is_staff


#############################
# Custom Permission Classes #
#############################

class IsAuthenticatedAndNotBlocked(IsAuthenticated):
    '''Custom permission class that allows user access if not blocked.'''

    def has_permission(self, request, view):
        # Check if user is authenticated:
        if not super().has_permission(request, view):
            return False
        # Check if user is not blocked:
        if is_blocked(request.user):
            return False
        # User is authenticated and not blocked:
        return True


class IsAdmin(IsAuthenticatedAndNotBlocked):
    '''Custom permission class that allows only Superusers access.'''

    def has_object_permission(self, request, view, obj):
        return is_admin(request.user)


####################################################
# Permission Function for custom APIViews/Viewsets #
####################################################

def check_IsAuthenticated(request:Request) -> Response|None:
    # Check if user is authenticated:
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


def check_IsAuthenticatedAndNotBlocked(request:Request) -> Response|None:
    # Check if user is authenticated:
    if check:=check_IsAuthenticated(request):
        return check
    # Check if user is blocked:
    if is_blocked(request.user):
        return Response(status=status.HTTP_403_FORBIDDEN)


def check_IsAdmin(request:Request) -> Response|None:
    # Check if user is authenticated:
    if check:=check_IsAuthenticated(request):
        return check
    # Check if user is blocked:
    if is_blocked(request.user) or not is_admin(request.user):
        return Response(status=status.HTTP_403_FORBIDDEN)
