from django.contrib import admin
from .models import Turma, Professor

class AdminTurma(admin.ModelAdmin):
    model = Turma
    extra = 1

class AdminProfessor(admin.ModelAdmin):
    inlines = AdminTurma