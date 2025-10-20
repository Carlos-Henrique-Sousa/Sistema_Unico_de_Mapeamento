# placement/admin.py
from django.contrib import admin
from .models import MapeamentoSala, PosicaoAluno
from simple_history.admin import SimpleHistoryAdmin

@admin.register(MapeamentoSala)
class MapeamentoSalaAdmin(SimpleHistoryAdmin):
    list_display = ('nome', 'turma', 'linhas', 'colunas', 'criado_em')
    list_filter = ('turma', 'escola')

@admin.register(PosicaoAluno)
class PosicaoAlunoAdmin(admin.ModelAdmin):
    list_display = ('mapeamento', 'estudante', 'linha', 'coluna', 'grupo')
    list_filter = ('mapeamento',)