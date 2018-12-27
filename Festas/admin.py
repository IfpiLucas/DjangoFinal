from django.contrib import admin
from .models import Tema, ItemTema, Cliente, Endereco, Aluguel

admin.site.register(Tema)
admin.site.register(Cliente)
admin.site.register(ItemTema)
admin.site.register(Endereco)
admin.site.register(Aluguel)

