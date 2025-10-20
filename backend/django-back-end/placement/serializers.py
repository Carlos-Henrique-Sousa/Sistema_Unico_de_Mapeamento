# placement/serializers.py
from rest_framework import serializers
from .models import MapeamentoSala, PosicaoAluno
from estudantes.serializers import EstudanteSerializer

class PosicaoAlunoSerializer(serializers.ModelSerializer):
    estudante = EstudanteSerializer(read_only=True)

    class Meta:
        model = PosicaoAluno
        fields = ['id', 'estudante', 'linha', 'coluna', 'grupo']

class MoverAlunoSerializer(serializers.Serializer):
    estudante_id = serializers.IntegerField()
    nova_linha = serializers.IntegerField(min_value=1)
    nova_coluna = serializers.IntegerField(min_value=1)
    novo_grupo = serializers.IntegerField(min_value=0, required=False)

class MapeamentoSerializer(serializers.ModelSerializer):
    posicoes = PosicaoAlunoSerializer(many=True, read_only=True)
    linhas = serializers.IntegerField(min_value=1)
    colunas = serializers.IntegerField(min_value=1)

    class Meta:
        model = MapeamentoSala
        fields = ['uuid', 'nome', 'turma', 'linhas', 'colunas', 'posicoes', 'criado_em']

    def validate(self, data):
        if self.instance:
            total = data.get('linhas', self.instance.linhas) * data.get('colunas', self.instance.colunas)
            count = self.instance.posicoes.count()
            if count > total:
                raise serializers.ValidationError("Capacidade insuficiente para alunos já alocados.")
        return data