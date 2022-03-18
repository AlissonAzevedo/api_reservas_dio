from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Chave)
class ChaveAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('chave', 'primeiro_nome', 'data_reserva', 'data_devolucao')