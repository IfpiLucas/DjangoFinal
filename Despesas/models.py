from django.db import models
import datetime


tupla = (
    ('roupa', 'Roupa'), ('remedio', 'Remedio'), ('Alimentaçao', 'Alimentaçao'), ('1', 'Educaçao'), ('2', 'Transporte'))
tupla_pagamento = (('1', 'Dinheiro'), ('2', 'Cartao de Credito'), ('3', 'Cartao de debito'))


class Despesa(models.Model):
    data_criaçao = models.CharField(max_length=100)
    tipo_despesa = models.CharField(max_length=40, choices=tupla)
    descriçao = models.CharField(max_length=100)
    forma_pagamento = models.CharField(max_length=100, choices=tupla_pagamento)
    vencimento = models.DateField()
    quitado = models.BooleanField()
    campo_temp = datetime.timedelta(days=2)


    def __srt__(self):
        return self.data_criaçao