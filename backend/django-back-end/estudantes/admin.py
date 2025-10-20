# estudantes/admin.py
from django.contrib import admin
from .models import Estudante, Nota, Falta
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Estudante)
class EstudanteAdmin(SimpleHistoryAdmin):
    list_display = ('usuario', 'turma', 'dificuldade_visao', 'dificuldade_aprendizado')
    search_fields = ('usuario__nome',)

@admin.register(Nota)
class NotaAdmin(SimpleHistoryAdmin):
    list_display = ('estudante', 'materia', 'nota_global')
    list_filter = ('area',)

@admin.register(Falta)
class FaltaAdmin(SimpleHistoryAdmin):
    list_display = ('estudante', 'data', 'aula')
    list_filter = ('data',)