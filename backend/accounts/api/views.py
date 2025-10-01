from django.contrib.auth import login
from django.contrib.auth.models import Group
from rest_framework import status, views, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from custom.std_openapi_response import OK_EMPTY_BODY, BAD_REQUEST, UNAUTHORIZED, FORBIDDEN
from accounts.models import CustomUser
from accounts.permissions import (
    is_blocked,
    is_admin,
    IsAuthenticatedAndNotBlocked,
    IsAdmin,
    check_IsAuthenticatedAndNotBlocked,
    check_IsAdmin,
)
from .serializers import (
    UserDisplaySerializer,
    PasswordResetSerializer,
)


##################
### Auth Views ###
##################

class LoginAPIView(KnoxLoginView):
    '''Login API view using Knox Authentication'''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @extend_schema(
        request=AuthTokenSerializer,
        responses={
            200: AuthTokenSerializer,
            **UNAUTHORIZED,
            **FORBIDDEN,
        }
    )
    def post(self, request:Request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if not user.is_active:
            return Response({"error": "Deleted user"}, status=403)
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)


##################
### User Views ###
##################

class CurrentUserAPIView(views.APIView):
    '''Get current logged user info'''
    authentication_classes = (TokenAuthentication, JWTAuthentication, JWTStatelessUserAuthentication,)

    @extend_schema(
        responses={
            200: UserDisplaySerializer,
            **UNAUTHORIZED,
        },
    )
    def get(self, request:Request):
        # Check if user is authenticated and not blocked:
        if check:=check_IsAuthenticatedAndNotBlocked(request):
            return check
        # Get User:
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class UserPasswordResetAPIView(views.APIView):
    '''User Password Reset'''
    authentication_classes = (TokenAuthentication, JWTAuthentication, JWTStatelessUserAuthentication,)

    @extend_schema(
        request=PasswordResetSerializer,
        responses={
            **OK_EMPTY_BODY,
            **BAD_REQUEST,
            **UNAUTHORIZED,
        },
    )
    def post(self, request:Request):
        # Check if user is authenticated and not blocked:
        if check:=check_IsAuthenticatedAndNotBlocked(request):
            return check
        # Get User:
        user = get_object_or_404(CustomUser, pk=request.user.id)
        # Validate Password:
        serializer = PasswordResetSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        new_password = serializer.validated_data['new_password']
        confirm_password = serializer.validated_data['confirm_password']
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        # Update Password:
        user.set_password(new_password)
        user.password_must_be_reset = False
        user.save()
        return Response(status=200)
