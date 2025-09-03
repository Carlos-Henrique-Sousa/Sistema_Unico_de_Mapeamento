from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

app_name = 'core'

urlpatterns = [
    # Health Check
    path('api/health/', views.health_check, name='health-check'),
    
    # Autenticação JWT padrão
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Autenticação customizada
    path('api/login/', views.LoginView.as_view(), name='custom-login'),
    path('api/logout/', views.logout_view, name='logout'),
    
    # Usuário atual
    path('api/me/', views.CurrentUserView.as_view(), name='current-user'),
    
    # CRUD de Usuários
    path('api/users/', views.UserListView.as_view(), name='user-list'),
    path('api/users/create/', views.UserCreateView.as_view(), name='user-create'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('api/users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('api/users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
    
]