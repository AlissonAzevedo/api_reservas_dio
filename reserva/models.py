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
    cargo = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.nome


class Reserva(models.Model):

    chaves = models.ManyToManyField(Chave, null=False)
    pessoas = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=None)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(auto_now=True, null=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.pessoas

    # def chave(self):
    #     content_chave = { 'numero': self.chaves.numero, 'nome': self.chaves.nome }
    #     return content_chave
    def chave(self):
        return self.chaves.all()
        #return self.chaves.numero
    
    def nome_pessoa(self):
        return self.pessoas.nome

    # def pessoa(self):
    #     content_pessoa = { 'nome': self.pessoas.nome, 'cargo': self.pessoas.cargo }
    #     return content_pessoa

    def data_reserva_formatada(self):
        return self.data_reserva.strftime('%d/%m/%Y - %H:%M')
    
    def data_devolucao_formatada(self):
        return self.data_devolucao.strftime('%d/%m/%Y - %H:%M')

    def Chaves(self):
        if self.chaves.all():
            return list(self.chaves.all().values_list('numero', flat=True))
        else:
            return 'NA'
            