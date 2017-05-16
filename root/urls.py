"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view as get_swagger_schema_view
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)

from users.views import UserViewSet
from things.views import ThingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'things', ThingViewSet)

swagger_schema_view = get_swagger_schema_view(title=settings.PROJECT_NAME)

urlpatterns = [
    url(r'^$', swagger_schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', obtain_jwt_token),
    url(r'^api/token/refresh/', refresh_jwt_token),
    url(r'^api/token/verify/', verify_jwt_token),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
