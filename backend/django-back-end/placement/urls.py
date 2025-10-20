# placement/urls.py
from django.urls import path
from .views import (
    GerarMapeamentoView,
    MapeamentoAtualView,
    MoverAlunoView,
    HistoricoMapeamentosView,
    AlterarGrupoView
)

urlpatterns = [
    path("gerar/", GerarMapeamentoView.as_view(), name="gerar"),
    path("atual/<uuid:uuid>/", MapeamentoAtualView.as_view(), name="atual"),
    path("mover/", MoverAlunoView.as_view(), name="mover"),
    path("historico/<int:turma_id>/", HistoricoMapeamentosView.as_view(), name="historico"),
    path("grupo/alterar/", AlterarGrupoView.as_view(), name="alterar_grupo"),
]