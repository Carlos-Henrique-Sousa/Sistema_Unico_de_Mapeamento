from core.permissions import IsProfessor, IsAluno, IsPDT, IsEscola, IsPDT, IsEscola, IsEscola, IsEscola
# atividades/views.py
from rest_framework import viewsets, filters, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Atividade, RespostaAtividade, QuestaoBanco
from .serializers import AtividadeSerializer, RespostaAtividadeSerializer, QuestaoBancoSerializer
from core.permissions import IsProfessor, IsAluno, IsPDT, IsEscola, IsPDT, IsEscola, IsEscola, IsEscola
from placement.ia import gerar_atividade

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all().order_by('data_inicio')
    serializer_class = AtividadeSerializer
    permission_classes = [permissions.IsAuthenticated, IsProfessor | IsAluno | IsPDT | IsEscola]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descricao']
    ordering_fields = ['data_inicio', 'data_fim']

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'professor':
            return Atividade.objects.filter(professor__usuario=user)
        elif user.tipo == 'aluno':
            estudante = Estudante.objects.get(usuario=user)
            return Atividade.objects.filter(turma=estudante.turma)
        elif user.tipo == 'pdt':
            pdt = PDT.objects.get(usuario=user)
            return Atividade.objects.filter(turma=pdt.turma)
        return Atividade.objects.none()

    def perform_create(self, serializer):
        professor = Professor.objects.get(usuario=self.request.user)
        serializer.save(professor=professor)

class RespostaAtividadeViewSet(viewsets.ModelViewSet):
    serializer_class = RespostaAtividadeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAluno | IsProfessor | IsPDT]

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'aluno':
            estudante = Estudante.objects.get(usuario=user)
            return RespostaAtividade.objects.filter(estudante=estudante)
        elif user.tipo in ('professor', 'pdt'):
            return RespostaAtividade.objects.all()
        return RespostaAtividade.objects.none()

    def perform_create(self, serializer):
        estudante = Estudante.objects.get(usuario=self.request.user)
        serializer.save(estudante=estudante)

class GerarAtividadeIAView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsProfessor | IsPDT]

    def post(self, request):
        descricao = request.data['descricao']
        tipo = request.data['tipo']
        turma_id = request.data['turma_id']
        conteudo_ia = gerar_atividade(descricao, tipo)
        professor = Professor.objects.get(usuario=request.user) if request.user.tipo == 'professor' else PDT.objects.get(usuario=request.user)
        atividade = Atividade.objects.create(
            titulo=f"Atividade IA: {descricao[:50]}",
            descricao=conteudo_ia,
            data_inicio=timezone.now(),
            data_fim=timezone.now() + timezone.timedelta(days=7),
            tipo=tipo,
            professor=professor if request.user.tipo == 'professor' else None,
            turma_id=turma_id,
            gerada_por_ia=True
        )
        questoes = QuestaoBanco.objects.filter(area__icontains=descricao)[:10]
        atividade.questoes.add(*questoes)
        serializer = AtividadeSerializer(atividade)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class QuestaoBancoViewSet(viewsets.ModelViewSet):
    queryset = QuestaoBanco.objects.all()
    serializer_class = QuestaoBancoSerializer
    permission_classes = [permissions.IsAuthenticated, IsProfessor | IsPDT | IsEscola]