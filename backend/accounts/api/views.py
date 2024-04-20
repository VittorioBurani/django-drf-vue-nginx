from django.contrib.auth import login
from rest_framework import views
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from drf_spectacular.utils import extend_schema
from accounts.utils.rest_knox_openapi_schema import KnoxTokenScheme # For DRF Knox Token Auth Schema Creation (import-only need: https://github.com/tfranzel/drf-spectacular/issues/264)
from .serializers import UserDisplaySerializer


##################
### User Views ###
##################

class CurrentUserAPIView(views.APIView):
    '''Get current logged user info'''
    authentication_classes = (TokenAuthentication, JWTAuthentication, JWTStatelessUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        responses={200: UserDisplaySerializer},
    )
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class LoginAPIView(KnoxLoginView):
    '''Login API view using Knox Authentication'''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @extend_schema(
        request=AuthTokenSerializer,
        responses={
            200: AuthTokenSerializer
        }
    )
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)
