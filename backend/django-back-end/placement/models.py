# placement/models.py
from django.db import models
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords
from estudantes.models import Estudante
from escola.models import Turma, Escola
import uuid

class MapeamentoSala(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=255)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    linhas = models.PositiveIntegerField(default=4)
    colunas = models.PositiveIntegerField(default=5)
    criado_em = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['-criado_em']
        indexes = [
            models.Index(fields=['turma']),
            models.Index(fields=['escola']),
        ]
        unique_together = ('turma', 'nome')

    def __str__(self):
        return f"{self.nome} - {self.turma}"

    def clean(self):
        if self.linhas * self.colunas < self.posicaoaluno_set.count():
            raise ValidationError("A capacidade da sala é menor que o número de alunos alocados.")

class PosicaoAluno(models.Model):
    mapeamento = models.ForeignKey(MapeamentoSala, on_delete=models.CASCADE, related_name='posicoes')
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    linha = models.PositiveIntegerField()
    coluna = models.PositiveIntegerField()
    grupo = models.IntegerField(default=0)

    class Meta:
        unique_together = [
            ('mapeamento', 'estudante'),
            ('mapeamento', 'linha', 'coluna'),
        ]
        indexes = [
            models.Index(fields=['mapeamento']),
        ]