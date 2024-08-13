"""
URL configuration for RestFullAPI project.

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

from . import settings
from .views import welcome, login, logout, register, profile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path(settings.API_PREFIX_STRING + '/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(settings.API_PREFIX_STRING + '/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(settings.API_PREFIX_STRING + '/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path(settings.API_PREFIX_STRING + '/login/', login, name='login'),
    path(settings.API_PREFIX_STRING + '/logout/', logout, name='logout'),
    path(settings.API_PREFIX_STRING + '/register/', register, name='register'),
    path(settings.API_PREFIX_STRING + '/profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
]
