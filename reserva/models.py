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
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.chave)