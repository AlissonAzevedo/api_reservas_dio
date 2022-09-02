from collections import _OrderedDictItemsView
from typing import OrderedDict
from django.http import response
from rest_framework.exceptions import NotFound
from ..models import *
from reserva.api.serializers import *

from rest_framework import status
from rest_framework import viewsets

from rest_framework.exceptions import NotFound
from rest_framework.response import Response


class ReservaViewsets(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('-data_reserva')
    serializer_class = ReservaSerializers
    

class ChaveViewsets(viewsets.ModelViewSet):
    queryset = Chave.objects.all()
    serializer_class = ChaveSerializers

class PessoaViewsets(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('nome')
    serializer_class = PessoaSerializers

