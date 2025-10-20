# atividades/models.py
from django.db import models
from django.utils import timezone
from estudantes.models import Estudante
from professores.models import Professor
from escola.models import Turma
from simple_history.models import HistoricalRecords

class QuestaoBanco(models.Model):
    conteudo = models.TextField()
    area = models.CharField(max_length=50)
    dificuldade = models.CharField(max_length=20)
    resposta_correta = models.TextField()
    opcoes = models.JSONField(default=list)
    history = HistoricalRecords()

class Atividade(models.Model):
    QUIZ = 'quiz'
    UPLOAD = 'upload'
    FORUM = 'forum'
    VIDEO = 'video'
    ANOTACAO = 'anotacao'
    PROVA = 'prova'

    TIPOS = [
        (QUIZ, 'Quiz'),
        (UPLOAD, 'Upload de Arquivo'),
        (FORUM, 'Fórum de Discussão'),
        (VIDEO, 'Vídeo Interativo'),
        (ANOTACAO, 'Anotação'),
        (PROVA, 'Prova Opcional'),
    ]

    ATIVA = 'ativa'
    INATIVA = 'inativa'
    FINALIZADA = 'finalizada'

    STATUS = [
        (ATIVA, 'Ativa'),
        (INATIVA, 'Inativa'),
        (FINALIZADA, 'Finalizada'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    status = models.CharField(max_length=20, choices=STATUS, default=ATIVA)
    criado_em = models.DateTimeField(auto_now_add=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='atividades')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='atividades')
    gerada_por_ia = models.BooleanField(default=False)
    questoes = models.ManyToManyField(QuestaoBanco, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.titulo

    def is_aberto(self):
        agora = timezone.now()
        return self.data_inicio <= agora <= self.data_fim

class RespostaAtividade(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='respostas')
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='respostas_atividades')
    resposta = models.TextField()
    nota = models.FloatField(null=True, blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        unique_together = ('atividade', 'estudante')

    def __str__(self):
        return f"{self.estudante.usuario.nome} → {self.atividade.titulo}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.nota is not None:
            self.estudante.atualizar_dots('atividades_concluidas', int(self.nota))