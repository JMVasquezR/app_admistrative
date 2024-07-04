from django.urls import path, include

app_name = 'backend'

urlpatterns = [
    path('api/', include('backend.api.urls', namespace='api')),
]
