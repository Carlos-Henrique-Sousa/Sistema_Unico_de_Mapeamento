from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

app_name = 'core'

urlpatterns = [
    # Autenticação JWT padrão
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Autenticação customizada
    path('login/', views.LoginView.as_view(), name='custom-login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Usuário atual
    path('me/', views.CurrentUserView.as_view(), name='current-user'),
    
    # CRUD de Usuários
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
]