from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
