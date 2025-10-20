# placement/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MapeamentoSala, PosicaoAluno
from .serializers import MapeamentoSerializer, MoverAlunoSerializer
from .services import gerar_novo_mapeamento
from .permissions import IsProfessorOrPDTOrAdmin
from django.shortcuts import get_object_or_404
from escola.models import Turma

class GerarMapeamentoView(APIView):
    permission_classes = [IsProfessorOrPDTOrAdmin]

    def post(self, request):
        try:
            turma_id = request.data.get("turma_id")
            nome = request.data.get("nome", "Mapeamento Automático")
            linhas = int(request.data.get("linhas", 4))
            colunas = int(request.data.get("colunas", 5))
            turma = get_object_or_404(Turma, id=turma_id)
            mapeamento = gerar_novo_mapeamento(turma, turma.escola, nome, linhas, colunas)
            return Response(MapeamentoSerializer(mapeamento).data)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MapeamentoAtualView(APIView):
    permission_classes = [IsProfessorOrPDTOrAdmin]

    def get(self, request, uuid):
        mapeamento = get_object_or_404(MapeamentoSala, uuid=uuid)
        return Response(MapeamentoSerializer(mapeamento).data)

class MoverAlunoView(APIView):
    permission_classes = [IsProfessorOrPDTOrAdmin]

    def patch(self, request):
        serializer = MoverAlunoSerializer(data=request.data)
        if serializer.is_valid():
            estudante_id = serializer.validated_data["estudante_id"]
            nova_linha = serializer.validated_data["nova_linha"]
            nova_coluna = serializer.validated_data["nova_coluna"]
            posicao = get_object_or_404(PosicaoAluno, estudante_id=estudante_id)
            posicao.linha = nova_linha
            posicao.coluna = nova_coluna
            if 'novo_grupo' in serializer.validated_data:
                posicao.grupo = serializer.validated_data["novo_grupo"]
            posicao.save()
            return Response({"mensagem": "Posição atualizada com sucesso"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoricoMapeamentosView(APIView):
    permission_classes = [IsProfessorOrPDTOrAdmin]

    def get(self, request, turma_id):
        historico = MapeamentoSala.objects.filter(turma_id=turma_id).order_by("-criado_em")
        return Response(MapeamentoSerializer(historico, many=True).data)

class AlterarGrupoView(APIView):
    permission_classes = [IsProfessorOrPDTOrAdmin]

    def patch(self, request):
        estudante_id = request.data.get('estudante_id')
        novo_grupo = request.data.get('novo_grupo')
        posicao = get_object_or_404(PosicaoAluno, estudante_id=estudante_id)
        posicao.grupo = novo_grupo
        posicao.save()
        return Response({"mensagem": "Grupo atualizado com sucesso"})