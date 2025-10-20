from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import health_check

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),

    # Página base ou landing page
    path('', TemplateView.as_view(template_name='base.html'), name='base'),

    # Endpoints de API (agrupados sob /api/)
    path('api/health/', health_check, name='api_health_check'),
    path('api/ping/', health_check, name='api_ping'),

    # Apps principais (pode adicionar prefixo /api/ se quiser APIs versionadas)
    path('api/escola/', include(('escola.urls', 'escola'), namespace='escola')),
    path('api/estudantes/', include(('estudantes.urls', 'estudantes'), namespace='estudantes')),
    path('api/professores/', include(('professores.urls', 'professores'), namespace='professores')),
    path('api/atividades/', include(('atividades.urls', 'atividades'), namespace='atividades')),
    path('api/eventos/', include(('eventos.urls', 'eventos'), namespace='eventos')),
    path('api/mapeamento/', include(('placement.urls', 'placement'), namespace='placement')),
]
