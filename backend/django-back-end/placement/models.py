# placement/models.py
from django.db import models
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords
from estudantes.models import Estudante
from escola.models import Turma, Escola
from typing import List, Dict
import uuid

class MapeamentoSala(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=255)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    # Configurações da sala
    linhas = models.PositiveIntegerField(default=4)
    colunas = models.PositiveIntegerField(default=5)
    
    # Configurações de agrupamento
    TIPO_AGRUPAMENTO_CHOICES = [
        ('SOLO', 'Individual (Solo)'),
        ('DUPLA', 'Dupla'),
        ('TRIO', 'Trio'),
        ('QUARTETO', 'Quarteto'),
        ('CUSTOMIZADO', 'Número Customizado')
    ]
    tipo_agrupamento = models.CharField(max_length=20, choices=TIPO_AGRUPAMENTO_CHOICES, default='SOLO')
    numero_pessoas_grupo = models.PositiveIntegerField(default=1, help_text="Número de pessoas por grupo (usado quando tipo_agrupamento = CUSTOMIZADO)")
    
    # Configurações da sala física
    tem_armarios = models.BooleanField(default=False)
    posicao_armarios = models.JSONField(default=dict, blank=True)  # {x: 0, y: 0, width: 2, height: 1}
    posicao_mesa_professor = models.JSONField(default=dict, blank=True)  # {x: 0, y: 0}
    posicao_quadro = models.JSONField(default=dict, blank=True)  # {x: 0, y: 0, width: 4, height: 2}
    
    # Novos campos para objetos adicionais
    objetos_adicionais = models.JSONField(default=list, blank=True, help_text="Lista de objetos adicionais: [{'tipo': 'estante', 'posicao': {...}}]")
    
    # Configurações de sistema de líderes
    usar_sistema_lideres = models.BooleanField(default=True, help_text="Se True, permite posicionar líderes em locais estratégicos")
    posicionamento_lideres = models.JSONField(default=dict, blank=True, help_text="Configuração de onde líderes devem ficar na sala")
    
    # Configurações de IA
    usar_ia_automatica = models.BooleanField(default=False)
    criterios_ia = models.JSONField(default=dict, blank=True, help_text="Critérios para IA: {'considerar_dificuldades': True, 'considerar_notas': True, etc}")
    
    # Modo de edição (drag-and-drop manual ou automático)
    modo_edicao = models.CharField(
        max_length=20,
        choices=[
            ('MANUAL', 'Manual (Drag and Drop)'),
            ('AUTOMATICO', 'Automático (IA)'),
            ('HIBRIDO', 'Híbrido')
        ],
        default='MANUAL'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
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
        if self.linhas * self.colunas < self.posicoes.count():
            raise ValidationError("A capacidade da sala é menor que o número de alunos alocados.")
    
    @property
    def capacidade_total(self):
        return self.linhas * self.colunas
    
    @property
    def numero_grupos(self):
        if self.tipo_agrupamento == 'CUSTOMIZADO':
            return self.numero_pessoas_grupo
        elif self.tipo_agrupamento == 'DUPLA':
            return 2
        elif self.tipo_agrupamento == 'TRIO':
            return 3
        elif self.tipo_agrupamento == 'QUARTETO':
            return 4
        else:  # SOLO
            return 1
    
    # ========== MÉTODOS DE IA E ANÁLISE ==========
    
    def organizar_com_ia(self):
        """
        Organiza o mapeamento usando IA
        """
        from placement.services import IAMapeamentoSala
        
        ia = IAMapeamentoSala(self)
        posicoes = ia.organizar_automaticamente()
        
        # Salvar posições
        for pos_data in posicoes:
            PosicaoAluno.objects.update_or_create(
                mapeamento=self,
                estudante=pos_data['estudante'],
                defaults={
                    'linha': pos_data['linha'],
                    'coluna': pos_data['coluna'],
                    'grupo': pos_data.get('grupo', 0),
                    'eh_lider': pos_data.get('eh_lider', False)
                }
            )
        
        return posicoes
    
    def analisar_layout(self):
        """
        Analisa o layout atual e sugere melhorias
        """
        from placement.services import IAMapeamentoSala, ValidacaoMapeamento
        
        ia = IAMapeamentoSala(self)
        analise = ia.analisar_layout_otimo()
        
        validador = ValidacaoMapeamento()
        validacao = validador.validar_layout(self)
        
        analise['validacao'] = validacao
        
        return analise
    
    def otimizar_layout(self, iteracoes: int = 100):
        """
        Otimiza o layout atual usando algoritmos genéticos
        """
        from placement.services import OtimizadorMapeamento
        
        otimizador = OtimizadorMapeamento()
        melhores_posicoes = otimizador.otimizar_posicionamento(self, iteracoes)
        
        # Aplicar melhorias
        for pos in melhores_posicoes:
            PosicaoAluno.objects.filter(
                mapeamento=self,
                estudante=pos.estudante
            ).update(
                linha=pos.linha,
                coluna=pos.coluna
            )
        
        return melhores_posicoes
    
    def obter_estatisticas(self):
        """
        Retorna estatísticas detalhadas do mapeamento
        """
        from placement.services import EstatisticasMapeamento
        
        stats = EstatisticasMapeamento.gerar_estatisticas(self)
        return stats
    
    def validar_configuracao(self):
        """
        Valida a configuração do mapeamento
        """
        problemas = []
        
        # Validar dimensões
        if self.linhas < 2 or self.colunas < 2:
            problemas.append("Dimensões muito pequenas (mínimo 2x2)")
        
        if self.linhas > 10 or self.colunas > 10:
            problemas.append("Dimensões muito grandes (máximo 10x10)")
        
        # Validar agrupamento
        total_alunos = self.turma.estudantes.count()
        capacidade = self.capacidade_total
        
        if total_alunos > capacidade:
            problemas.append(f"Muitos alunos ({total_alunos}) para capacidade ({capacidade})")
        
        # Validar objetos físicos
        if self.objetos_adicionais:
            for obj in self.objetos_adicionais:
                if 'tipo' not in obj or 'posicao' not in obj:
                    problemas.append("Objeto adicional sem tipo ou posição")
        
        return {
            'valido': len(problemas) == 0,
            'problemas': problemas
        }
    
    def aplicar_template_layout(self, template: str):
        """
        Aplica um template pré-definido de layout
        Templates: 'retangular', 'em_ferradura', 'laboratorio', 'auditorio'
        """
        templates = {
            'retangular': {'linhas': 4, 'colunas': 5},
            'em_ferradura': {'linhas': 3, 'colunas': 6, 'tipo_agrupamento': 'DUPLA'},
            'laboratorio': {'linhas': 5, 'colunas': 6, 'tipo_agrupamento': 'TRIO'},
            'auditorio': {'linhas': 6, 'colunas': 8, 'tipo_agrupamento': 'SOLO'}
        }
        
        if template not in templates:
            raise ValueError(f"Template '{template}' não existe")
        
        config = templates[template]
        self.linhas = config.get('linhas', self.linhas)
        self.colunas = config.get('colunas', self.colunas)
        
        if 'tipo_agrupamento' in config:
            self.tipo_agrupamento = config['tipo_agrupamento']
        
        self.save()
    
    def duplicar_layout(self, novo_nome: str):
        """
        Cria uma cópia do mapeamento atual com novo nome
        """
        from copy import deepcopy
        
        novo_mapeamento = MapeamentoSala.objects.create(
            nome=novo_nome,
            escola=self.escola,
            turma=self.turma,
            linhas=self.linhas,
            colunas=self.colunas,
            tipo_agrupamento=self.tipo_agrupamento,
            numero_pessoas_grupo=self.numero_pessoas_grupo,
            tem_armarios=self.tem_armarios,
            posicao_armarios=deepcopy(self.posicao_armarios),
            posicao_mesa_professor=deepcopy(self.posicao_mesa_professor),
            posicao_quadro=deepcopy(self.posicao_quadro),
            objetos_adicionais=deepcopy(self.objetos_adicionais),
            usar_sistema_lideres=self.usar_sistema_lideres,
            posicionamento_lideres=deepcopy(self.posicionamento_lideres),
            usar_ia_automatica=self.usar_ia_automatica,
            criterios_ia=deepcopy(self.criterios_ia),
            modo_edicao=self.modo_edicao
        )
        
        # Copiar posições
        for pos in self.posicoes.all():
            PosicaoAluno.objects.create(
                mapeamento=novo_mapeamento,
                estudante=pos.estudante,
                linha=pos.linha,
                coluna=pos.coluna,
                grupo=pos.grupo,
                fixo=pos.fixo,
                eh_lider=pos.eh_lider,
                observacoes=pos.observacoes
            )
        
        return novo_mapeamento

class PosicaoAluno(models.Model):
    mapeamento = models.ForeignKey(MapeamentoSala, on_delete=models.CASCADE, related_name='posicoes')
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    linha = models.PositiveIntegerField()
    coluna = models.PositiveIntegerField()
    grupo = models.IntegerField(default=0)
    
    # Campos adicionais para controle
    fixo = models.BooleanField(default=False, help_text="Se True, não pode ser movido (mesa de aluno especial)")
    eh_lider = models.BooleanField(default=False, help_text="Se True, é um líder posicionado estrategicamente")
    observacoes = models.TextField(blank=True, help_text="Observações sobre esta posição")
    
    # Timestamps
    posicionado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            ('mapeamento', 'estudante'),
            ('mapeamento', 'linha', 'coluna'),
        ]
        indexes = [
            models.Index(fields=['mapeamento']),
        ]
        verbose_name = "Posição do Aluno"
        verbose_name_plural = "Posições dos Alunos"
    
    def __str__(self):
        return f"{self.estudante.usuario.nome} - Linha {self.linha}, Coluna {self.coluna}"
    
    # ========== MÉTODOS ÚTEIS ==========
    
    def mover_para(self, nova_linha: int, nova_coluna: int, forcar: bool = False):
        """
        Move o aluno para uma nova posição
        """
        if not forcar:
            # Verificar se a posição está ocupada
            conflito = PosicaoAluno.objects.filter(
                mapeamento=self.mapeamento,
                linha=nova_linha,
                coluna=nova_coluna
            ).exclude(id=self.id)
            
            if conflito.exists():
                raise ValidationError(f"Posição {nova_linha},{nova_coluna} já está ocupada")
            
            # Verificar se não está fixo
            if self.fixo:
                raise ValidationError("Esta posição está fixa e não pode ser movida")
            
            # Validar limites
            if nova_linha >= self.mapeamento.linhas or nova_coluna >= self.mapeamento.colunas:
                raise ValidationError("Posição fora dos limites da sala")
        
        self.linha = nova_linha
        self.coluna = nova_coluna
        self.save()
    
    def trocar_com(self, outra_posicao: 'PosicaoAluno'):
        """
        Troca de posição com outro aluno
        """
        if self.fixo or outra_posicao.fixo:
            raise ValidationError("Não é possível trocar posições fixas")
        
        self.linha, outra_posicao.linha = outra_posicao.linha, self.linha
        self.coluna, outra_posicao.coluna = outra_posicao.coluna, self.coluna
        
        self.save()
        outra_posicao.save()
    
    def calcular_distancia_quadro(self) -> float:
        """
        Calcula a distância até o quadro (assumindo que o quadro está na linha 0)
        """
        return self.linha  # Quanto maior o número da linha, mais longe do quadro
    
    def calcular_distancia_professor(self) -> float:
        """
        Calcula a distância até a mesa do professor
        """
        if not self.mapeamento.posicao_mesa_professor:
            return 0
        
        prof_linha = self.mapeamento.posicao_mesa_professor.get('y', 0)
        prof_coluna = self.mapeamento.posicao_mesa_professor.get('x', 0)
        
        distancia = ((self.linha - prof_linha) ** 2 + (self.coluna - prof_coluna) ** 2) ** 0.5
        return distancia
    
    def is_posicao_ideal_para_aluno(self) -> bool:
        """
        Verifica se a posição atual é ideal para este aluno específico
        """
        estudante = self.estudante
        
        # Alunos com dificuldade visual devem ficar perto do quadro
        if estudante.dificuldade_visao in ['MEDIA', 'ALTA']:
            if self.linha > 2:
                return False
        
        # Alunos baixos devem ficar na frente
        if estudante.altura == 'BAIXA':
            if self.linha > 2:
                return False
        
        # Líderes devem estar em posições estratégicas (lados da sala)
        if estudante.eh_lider:
            if self.coluna not in [0, self.mapeamento.colunas - 1]:
                return False
        
        return True
    
    def obter_posicoes_adjacentes(self) -> List[Dict[str, int]]:
        """
        Retorna posições adjacentes vazias
        """
        adjacentes = []
        
        direcoes = [
            (-1, 0),  # cima
            (1, 0),   # baixo
            (0, -1),  # esquerda
            (0, 1)    # direita
        ]
        
        for dl, dc in direcoes:
            nova_linha = self.linha + dl
            nova_coluna = self.coluna + dc
            
            if 0 <= nova_linha < self.mapeamento.linhas and 0 <= nova_coluna < self.mapeamento.colunas:
                ocupada = PosicaoAluno.objects.filter(
                    mapeamento=self.mapeamento,
                    linha=nova_linha,
                    coluna=nova_coluna
                ).exists()
                
                if not ocupada:
                    adjacentes.append({
                        'linha': nova_linha,
                        'coluna': nova_coluna
                    })
        
        return adjacentes
    
    def obter_companheiros_grupo(self) -> List['PosicaoAluno']:
        """
        Retorna companheiros do mesmo grupo
        """
        return PosicaoAluno.objects.filter(
            mapeamento=self.mapeamento,
            grupo=self.grupo
        ).exclude(id=self.id).select_related('estudante')