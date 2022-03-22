from django.db import models
from django.db.models.fields import DateTimeField


# Create your models here.
class Chave(models.Model):
    numero = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.numero


class Reserva(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    chaves = models.ForeignKey(Chave, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.CharField(max_length=100, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.primeiro_nome)

    def chave(self):
        content_chave = { 'numero': self.chaves.numero, 'nome': self.chaves.nome }
        return content_chave

    def data_reserva_formatada(self):
        return self.data_reserva.strftime('%d/%m/%Y - %H:%M')
    
    def reservado(self):
        if self.data_devolucao != None:
            self.ativo = False
            return self.ativo
        else:
            self.ativo = True
            return self.ativo
            