from rest_framework import serializers
from ..models import *

class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'cargo']
class ChaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chave
        fields = ['id', 'nome', 'numero']

class ReservaSerializers(serializers.ModelSerializer):
    chave = ChaveSerializers(many=True, read_only=True)
    class Meta:
        model = Reserva
        #fields = "__all__"
        fields = ['id', 'pessoas', 'chave', 'nome_pessoa', 'data_reserva_formatada',
         'data_devolucao_formatada', 'chaves', 'devolvido']

        