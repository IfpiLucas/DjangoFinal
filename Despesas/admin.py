from django.contrib import admin

from .models import Despesa


class AdminDespesas(admin.ModelAdmin):
    list_display = ('data_criaçao', 'tipo_despesa', 'forma_pagamento', 'descriçao', 'vencimento', 'quitado','campo_temp')
    list_filter = ('quitado', 'vencimento')

admin.site.register(Despesa, AdminDespesas)
