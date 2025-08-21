from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Permissões que somente o <admin> pode acessar ou ter acesso
    """
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.identificador.startswith('<admin')

class IsAluno(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.identificador.startswith('#')

class IsProfessor(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.identificador.startswith('@')

class IsPDT(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.identificador.startswith('_') and request.user.tipo == 'pdt'

class IsEscola(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.identificador.startswith('_') and request.user.tipo == 'escola'