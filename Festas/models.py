from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=256)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.bairro

    class Meta:
        verbose_name_plural = 'Endereços'
        verbose_name = 'Endereço'


class Tema(models.Model):
    nome = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField(max_digits=5, decimal_places=2)
    cor_toalha = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class ItemTema(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField()
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Itens Tema'


class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_festa = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    valor_cobrado = models.DecimalField(max_digits=8, decimal_places=2)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, primary_key=True)


    class Meta:
        verbose_name_plural = 'Alugeis'
