# placement/services.py
import logging
from .models import MapeamentoSala, PosicaoAluno
from .ia import gerar_mapeamento_inteligente
from estudantes.models import Estudante

logger = logging.getLogger(__name__)

def gerar_novo_mapeamento(turma, escola, nome, linhas, colunas):
    mapeamento = MapeamentoSala.objects.create(
        turma=turma, escola=escola, nome=nome,
        linhas=linhas, colunas=colunas
    )

    resposta = gerar_mapeamento_inteligente(turma.id, linhas, colunas)
    posicoes = [
        PosicaoAluno(
            mapeamento=mapeamento,
            estudante=Estudante.objects.get(id=aluno_id),
            linha=info['linha'],
            coluna=info['coluna'],
            grupo=info.get('grupo', 0)
        ) for aluno_id, info in resposta.items()
    ]
    PosicaoAluno.objects.bulk_create(posicoes)
    return mapeamento