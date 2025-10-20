# eventos/views.py
from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from .models import Evento, InscricaoEvento
from .serializers import EventoSerializer, InscricaoEventoSerializer
from core.permissions import IsEscola, IsAluno, IsProfessor, IsPDT, IsProfessor, IsPDT

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated, IsEscola | IsAluno | IsProfessor | IsPDT]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descricao', 'escola__nome']
    ordering_fields = ['data_inicio', 'data_fim']

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'escola':
            return Evento.objects.filter(escola=user)
        elif user.tipo == 'aluno':
            return Evento.objects.filter(inscricoes__estudante=user)
        elif user.tipo in ('professor', 'pdt'):
            return Evento.objects.all()
        return Evento.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.tipo != 'escola':
            raise permissions.PermissionDenied("Apenas escolas podem criar eventos.")
        serializer.save(escola=user)

class InscricaoEventoViewSet(viewsets.ModelViewSet):
    serializer_class = InscricaoEventoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'aluno':
            return InscricaoEvento.objects.filter(estudante=user)
        elif user.tipo == 'escola':
            return InscricaoEvento.objects.filter(evento__escola=user)
        return InscricaoEvento.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.tipo != 'aluno':
            raise permissions.PermissionDenied("Apenas estudantes podem se inscrever em eventos.")
        serializer.save(estudante=user)

    def perform_update(self, serializer):
        instance = serializer.instance
        if self.request.user.tipo == 'escola' and instance.evento.escola == self.request.user:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Apenas a escola criadora pode atualizar inscrições.")