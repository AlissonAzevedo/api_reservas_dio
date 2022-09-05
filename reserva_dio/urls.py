from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relatorios/', include('relatorios.urls')),
    path('api/v1/', include('reserva.urls')),
    path('auth/', include('rest_framework.urls'))
]
