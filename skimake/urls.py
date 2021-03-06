# skimate/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
# for swagger and redoc
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# simple jwt module
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.api.views import home

schema_view = get_schema_view(
   openapi.Info(
      title="Skimake Api Documentation",
      default_version='v1',
      description="Skimake project backend api documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path('', home),
   path('admin/', admin.site.urls),
   path('api/v1/', include('users.api.urls')),  #api endpoint
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]