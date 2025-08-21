from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.db.models import JSONField

class UsuarioQuerySet(models.QuerySet):
    def ativos(self):
        return self.filter(is_active=True)

    def por_tipo(self, tipo):
        return self.ativos().filter(tipo=tipo)
    

class User(AbstractUser):
    TYPES = [
        ('admin', 'Admin'),
        ('escola', 'Escola'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
        ('responsavel', 'Responsavel'),
    ]

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    identifier = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9#@_-]+$',
                message=_('O identificador deve conter apenas caracteres alfanuméricos, #, @, _ ou -.'),
                code='invalid_identifier'
            )
        ]
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    
    nome = models.CharField(
        max_length=255,
        blank=True,
    )

    type = models.CharField(
        max_length=60,
        choices=TYPES,
        db_index=True,
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('ativo')
    )

    is_staff = models.BooleanField(
        default=False,
    )
    
    metadata = JSONField(
        blank=True,
        null=True,
        verbose_name=_('metadados'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('criado em'),
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('atualizado em'),
    )

    history = HistoricalRecords(
        verbose_name=_('histórico')
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('grupo'),
        related_name='core_usuario_set_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        verbose_name=_('permissões de usuário'),
        related_name='core_usuario_set_permissions',
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name="core_user_set",
        related_query_name="core_user",
    )

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.get_tipo_display()} | {self.identifier}"

    def tipo_display(self):
        return dict(self.TIPOS).get(self.tipo, 'Desconhecido')

    def get_prefix(self):
        return self.identifier[0] if self.identifier else None
    
class ManageUser(BaseUserManager.from_queryset(UsuarioQuerySet)):
    def create_user(self, identifier, password=None, **extra_fields):
        if not identifier:
            raise ValueError('o identificador deve ser4 definido')
        user_model = self.model(UsuarioQuerySet, identificador=identifier, **extra_fields)
        user_model.set_password(password)
        user_model.save(using=self._db)
        return user_model
    
    def config_user(self, identifier, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(identifier, password, **extra_fields)
    
    def create_superuser(self, identifier, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(identifier, password, **extra_fields)

