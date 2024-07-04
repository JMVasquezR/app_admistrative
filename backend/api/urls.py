from django.urls import path, include

from backend.api.views import ChargeInfractionView, ListInfractionForEmailView

app_name = 'backend'

urlpatterns = [
    path('cargar_infraccion/', ChargeInfractionView.as_view(), name='cargar_infraccion'),
    path('infracciones/<str:email>/', ListInfractionForEmailView.as_view(), name='listar_infracciones_por_correo'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
