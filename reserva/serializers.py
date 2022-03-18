from rest_framework import serializers
from .models import Reserva, Chave

class ReservaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"

class ChaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chave
        fields = "__all__"