from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.db.models import JSONField

class User(models.Model):
  Types = [
    ('admin', 'Admin'),
    ('escola', 'Escola'),
    ('professor', 'Professor'),
    ('aluno', 'Aluno'),
    ('respnsavel', 'Responsavel'),
  ]

  id = models.UUIDField(
    primary_key=True,
    editable=False,
    auto_created=True,
    unique=True,
    default=uuid.uuid4
  )

  identifier = models.CharField(
    max_length= 20,
    unique=True,
    validators=[
      RegexValidator(
        regex=r'^[#@_-]+$',
        message=_('O identificador deve conter apenas caracteres alfanuméricos, #, @, _ ou -, seguidos da sequencia numérica.'),
        code='invalid_identifier'
      )
    ]
  )

  email = models.EmailField(
    max_lenght = 255,
    unique=True,
    blank = True,
    null = True
  )
  
  nome = models.CharField(
    max_length=255,
    blank=True,
  )

  type = models.CharField(
    max_length=60,
    db_collation='utf8mb4_unicode_ci',
    choices=Types,
    db_index=True,
  )

  is_acitive = models.BooleanField(
    default=True,
    verbose_name=_('ativo'),
    help_text=_('indica se o usuário está ativo ou não. Se não setiver desmarque a caixa de seleção')
  )

  is_staff = models.BooleanField(
    default=False,
  )
    
  metadata = JSONField(
    blank=True,
    null=True,
    verbose_name=_('metadados'),
    help_text=_('informações adicionais sobre o usuário')
  )

  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('criado em'),
    help_text=_('data e hora de criação do usuário')
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_('atualizado em'),
    help_text=_('data e hora da última atualização do usuário')
  )

  history = HistoricalRecords(
    verbose_name=_('histórico'),
    help_text=_('registros de histórico de alterações do usuário')
  )

  group = models.ForeignKey(
    'auth.Group',
    on_delete=models.CASCADE,
    blank=True,
    null=True,
    verbose_name=_('grupo'),
    help_text=_('grupo ao qual o usuário pertence')
  )

  user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_usuario_set_permissions',
        blank=True,
        help_text=_('Permissões específicas do usuário.'),
        verbose_name=_('permissões de usuário'),
    )
