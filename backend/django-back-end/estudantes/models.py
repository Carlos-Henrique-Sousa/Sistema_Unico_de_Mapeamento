from django.db import models
from core.models import User
from escola.models import Turma
from simple_history.models import HistoricalRecords

class Estudante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'aluno'})
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='estudantes')
    dificuldade_visao = models.CharField(max_length=50, choices=[('NENHUMA', 'Nenhuma'), ('BAIXA', 'Baixa'), ('MEDIA', 'Média'), ('ALTA', 'Alta')], default='NENHUMA')
    dificuldade_aprendizado = models.CharField(max_length=50, choices=[('NENHUMA', 'Nenhuma'), ('LEVE', 'Leve'), ('MODERADA', 'Moderada'), ('SEVERA', 'Severa')], default='NENHUMA')
    media_humanas = models.FloatField(default=0.0)
    media_linguagens = models.FloatField(default=0.0)
    media_exatas = models.FloatField(default=0.0)
    dots_pontos = models.IntegerField(default=0)
    dots_detalhes = models.JSONField(default=dict)
    history = HistoricalRecords()

    def __str__(self):
        return self.usuario.nome

    def atualizar_dots(self, categoria, valor):
        self.dots_detalhes[categoria] = self.dots_detalhes.get(categoria, 0) + valor
        self.dots_pontos += valor
        self.save()

class Nota(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='notas')
    materia = models.CharField(max_length=100)
    area = models.CharField(max_length=50, choices=[('HUMANAS', 'Humanas'), ('LINGUAGENS', 'Linguagens'), ('EXATAS', 'Exatas')])
    nota_global = models.FloatField()
    nota_parcial1 = models.FloatField(null=True, blank=True)
    nota_parcial2 = models.FloatField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.estudante} - {self.materia}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.estudante.atualizar_dots('notas', int(self.nota_global))
        self.atualizar_medias()

    def atualizar_medias(self):
        estudante = self.estudante
        if self.area == 'HUMANAS':
            notas_humanas = Nota.objects.filter(estudante=estudante, area='HUMANAS')
            estudante.media_humanas = sum(n.nota_global for n in notas_humanas) / len(notas_humanas) if notas_humanas else 0
        elif self.area == 'LINGUAGENS':
            notas_linguagens = Nota.objects.filter(estudante=estudante, area='LINGUAGENS')
            estudante.media_linguagens = sum(n.nota_global for n in notas_linguagens) / len(notas_linguagens) if notas_linguagens else 0
        elif self.area == 'EXATAS':
            notas_exatas = Nota.objects.filter(estudante=estudante, area='EXATAS')
            estudante.media_exatas = sum(n.nota_global for n in notas_exatas) / len(notas_exatas) if notas_exatas else 0
        estudante.save()

class Falta(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='faltas')
    data = models.DateField()
    aula = models.CharField(max_length=100)
    justificativa = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.estudante} - {self.data} - {self.aula}"