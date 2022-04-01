from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Chave)
class ChaveAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('chaves', 'pessoa', 'data_reserva', 'data_devolucao', 'devolvido')