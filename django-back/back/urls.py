"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="测试工程API",
      default_version='v1.0',
      description="测试工程接口文档",
      terms_of_service="https://www.cnblogs.com/jinjiangongzuoshi/",
      contact=openapi.Contact(email="狂师"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    # django自带的 == 不用管
    # path("admin/", admin.site.urls),
    # django-rest-framework == 不用管
    path('api-auth/', include('rest_framework.urls')),

    # 系统鉴权用的 url
    path("", include("apps.users.urls")),

    # 配置drf-yasg路由
    path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
