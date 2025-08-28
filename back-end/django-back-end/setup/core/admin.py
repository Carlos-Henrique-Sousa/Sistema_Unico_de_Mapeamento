from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from simple_history.admin import SimpleHistoryAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(DjangoUserAdmin, SimpleHistoryAdmin):
    list_display = ('identificador', 'nome', 'tipo', 'is_active', 'is_staff', 'created_at')
    list_filter = ('tipo', 'is_active', 'is_staff')
    search_fields = ('identificador', 'nome', 'email')
    ordering = ('created_at',)

    fieldsets = (
        (None, {'fields': ('identificador', 'senha')}),
        ('Informações Pessoais', {'fields': ('nome', 'email', 'tipo', 'metadata')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')

    actions = ['ativar_usuarios', 'desativar_usuarios']

    def ativar_usuarios(self, queryset):
        queryset.update(is_active=True)

    ativar_usuarios.short_description = "Ativar usuários selecionados"

    def desativar_usuarios(self, queryset):
        queryset.update(is_active=False)
        
    desativar_usuarios.short_description = "Desativar usuários selecionados"