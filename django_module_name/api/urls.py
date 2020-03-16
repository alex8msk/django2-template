from django.urls import path, include


urlpatterns = [
    path('v0/', include(('api.v0.urls', 'api-v0'), namespace='api_v0')),
]