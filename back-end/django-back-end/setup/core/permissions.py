from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Permissões que somente o <admin> pode acessar ou ter acesso
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_type == 'admin')

class IsAluno(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_type == 'aluno')

class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_type == 'professor')

class IsEscola(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_type == 'escola')