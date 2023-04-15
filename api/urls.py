"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from apiapp import views
from apiapp.serializers import *


schema_view = get_schema_view(
    openapi.Info(
        title="GIGHUB BACKEND API",
        default_version='v4',
        description="API Documentation for gighub",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # swaggerview as home
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('users/', ListAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),

    #loan
    path('loans/', views.loan_list, name='loan-list'),
    path('loans/<int:pk>/', views.loan_detail, name='loan-detail'),
    path('loans/<int:pk>/update/', views.loan_update, name='loan-apply'),

    # auth
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

]   

