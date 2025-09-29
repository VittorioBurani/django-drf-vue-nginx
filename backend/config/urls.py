"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# For MEDIA
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    # For MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# For OpenAPI file generation during development:
if settings.DEPLOYMENT_STAGE != 'PRODUCTION':
    from drf_spectacular.views import SpectacularAPIView
    from custom.rest_knox_openapi_schema import KnoxTokenScheme # For DRF Knox Token Auth Schema Creation (import-only need: https://github.com/tfranzel/drf-spectacular/issues/264)
    urlpatterns += [
        # path('api/schema/', include('drf_spectacular.urls')),
        path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    ]
