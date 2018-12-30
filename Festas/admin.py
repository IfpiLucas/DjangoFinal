from django.contrib import admin
from .models import Tema, ItemTema, Cliente, Endereco, Aluguel

class AdminTema(admin.ModelAdmin):
    list_display = ('nome', 'cor_toalha')

class AdminAluguel(admin.ModelAdmin):
    list_display = ('cliente','data_festa','hora_inicio','hora_termino', 'tema', 'endereco')
    list_filter = ('data_festa', 'endereco','tema', 'cliente')

class AdminCliente(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

class AdminItemTema(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'tema')
    list_filter = ('tema', 'nome')

class AdminEndereco(admin.ModelAdmin):
    list_display = ('logradouro', 'numero','bairro','cidade', 'uf', 'cep')
    list_filter = ('bairro', 'uf', 'cidade')

admin.site.register(Tema, AdminTema)
admin.site.register(Cliente, AdminCliente)
admin.site.register(ItemTema, AdminItemTema)
admin.site.register(Endereco, AdminEndereco)
admin.site.register(Aluguel, AdminAluguel)

