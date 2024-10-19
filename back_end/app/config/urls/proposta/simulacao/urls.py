from django.urls import path
from app.controller.proposta.simulacao import simulacaoPropostaController

urlpatterns = [
    path("realizar", simulacaoPropostaController.realizar_simulacao_proposta),
    path("gerar/excel", simulacaoPropostaController.gerar_excel_colaboradores),
]
