"""drmvid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from django.contrib import admin
from django.urls import path, include

from vid import views as vid_views


router = routers.DefaultRouter()
router.register(r'vid', vid_views.DRMVideoView, 'vid')
router.register(r'format', vid_views.FormatVideoView, 'format')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    # following will allow to login using a simple html form
    path('drf-auth', include('rest_framework.urls')),
    path('django-rq/', include('django_rq.urls')),
]
