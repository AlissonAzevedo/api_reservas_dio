from rest_framework import serializers
from .models import Reserva, Chave

class ChaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chave
        fields = "__all__"

class ReservaSerializers(serializers.ModelSerializer):
    chaves = serializers.PrimaryKeyRelatedField(many=False, queryset=Chave.objects.all())
    #chaves = ChaveSerializers(many=False, read_only=True)
    class Meta:
        model = Reserva
        #fields = "__all__"
        fields = ['id', 'primeiro_nome', 'ultimo_nome', 'reservado', 
        'data_reserva_formatada', 'data_devolucao', 'chaves', 'chave']
        