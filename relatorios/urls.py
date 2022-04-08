from django.db import router
from rest_framework import urlpatterns
from .views import *
from rest_framework.routers import DefaultRouter
from .views import ListRelatorios
from django.urls import path

router = DefaultRouter()
# router.register(r'relatorios', RelatoriosViewsets)
urlpatterns = [
    path('reservas/', ListRelatorios.as_view(), name='relatorios'),
]

urlpatterns += router.urls