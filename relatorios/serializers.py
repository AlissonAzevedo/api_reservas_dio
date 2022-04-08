from rest_framework import serializers
from reserva.models import Reserva, Chave, Pessoa

class RelatoriosSerializers(serializers.ModelSerializer):
    chaves = serializers.PrimaryKeyRelatedField(many=False, queryset=Chave.objects.all())
    pessoas = serializers.PrimaryKeyRelatedField(many=False, queryset=Pessoa.objects.all())
    #chaves = ChaveSerializers(many=False, read_only=True)
    class Meta:
        model = Reserva
        #fields = "__all__"
        fields = ['id', 'pessoas', 'pessoa','data_reserva_formatada',
         'data_devolucao_formatada', 'chaves', 'chave', 'devolvido']

        