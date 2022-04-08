from collections import _OrderedDictItemsView
from typing import OrderedDict
from django.http import response
from rest_framework.exceptions import NotFound
from reserva.models import Reserva
from .serializers import RelatoriosSerializers

from rest_framework import status
from rest_framework import viewsets

from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from rest_framework.views import APIView


# class RelatoriosViewsets(viewsets.ModelViewSet):
#     queryset = Reserva.objects.filter(devolvido=False).order_by('-data_reserva')
#     serializer_class = RelatoriosSerializers
    
class ListRelatorios(APIView):
    def get(self, request):
        reservas = Reserva.objects.filter(devolvido=False).order_by('-data_reserva')
        serializer = RelatoriosSerializers(reservas, many=True)
        return Response(serializer.data)
