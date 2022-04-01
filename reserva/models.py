from django.db import models
from django.db.models.fields import DateTimeField


# Create your models here.
class Chave(models.Model):
    numero = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.numero

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False)
    chapa = models.CharField(max_length=10)
    def __str__(self):
        return self.nome


class Reserva(models.Model):

    chaves = models.ForeignKey(Chave, on_delete=models.CASCADE)
    pessoas = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=None)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.CharField(max_length=100, null=True, blank=True)

    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.primeiro_nome)

    def chave(self):
        content_chave = { 'numero': self.chaves.numero, 'nome': self.chaves.nome }
        return content_chave

    def pessoa(self):
        content_pessoa = { 'nome': self.pessoas.nome, 'chapa': self.pessoas.chapa }
        return content_pessoa

    def data_reserva_formatada(self):
        return self.data_reserva.strftime('%d/%m/%Y - %H:%M')
    
    def reservado(self):
        if self.data_devolucao is None:
            self.data_devolucao = 'Não devolvido'
            