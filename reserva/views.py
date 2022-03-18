from django.http import response
from rest_framework.exceptions import NotFound
from .models import Reserva, Chave
from .serializers import ReservaSerializers, ChaveSerializers

from rest_framework import status
from rest_framework import viewsets

from rest_framework.exceptions import NotFound
from rest_framework.response import Response



class ReservaViewsets(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializers

class ChaveViewsets(viewsets.ModelViewSet):
    queryset = Chave.objects.all()
    serializer_class = ChaveSerializers