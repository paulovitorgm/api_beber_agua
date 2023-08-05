from django.contrib import admin
from agua.models import *


class AdminUsuario(admin.ModelAdmin):
    list_display = ['id', 'nome', 'peso']
    list_display_links = ['id', 'nome', 'peso']
    search_fields = ['nome']

class AdminConsumo(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'data', 'meta_diaria']
    list_display_links = ['id', 'usuario',]
    search_fields = ['usuario']




admin.site.register(Usuario, AdminUsuario)
admin.site.register(Consumo, AdminConsumo)
