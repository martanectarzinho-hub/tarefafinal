from django.contrib import admin
from .models import Categoria, Prato, Mesa, Pedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome']

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'capacidade']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'mesa', 'data', 'estado']
    list_filter = ['estado']