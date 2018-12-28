from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length=100)
    valor = models.FloatField()

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    valor_hora_aula = models.FloatField()

class Turma(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    chave = models.ForeignKey(Curso, on_delete=models.CASCADE)
    chave1 = models.ForeignKey(Professor, on_delete=models.CASCADE)

