from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from core.settings.base import MEDIA_ROOT, MEDIA_URL


schema_view = get_schema_view(
   openapi.Info(
      title="{{ files.1 }} API",
      default_version='v0',
      description="Description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include(('api.urls', 'api'), namespace='api')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
