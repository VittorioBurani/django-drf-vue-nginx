from django.urls import path
from knox import views as knox_views
from .views import (
    CurrentUserAPIView,
    LoginAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Generic user views:
    path('get-user/', CurrentUserAPIView.as_view(), name='get-user'),
    # Django-Rest-Knox + Auth:
    path('login/', LoginAPIView.as_view(), name="knox-login"),
    path('logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name="knox-logoutall"),
    # Simple JWT:
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
