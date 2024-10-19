from django.urls import path
from app.view.proposta.simulacao import simulacaoPropostaView
from app.controller.proposta.simulacao import simulacaoPropostaController

urlpatterns = [
    path("", simulacaoPropostaView.exibir_pagina_simulacao_proposta, name="simulacaoProposta"),
    path("realizar", simulacaoPropostaController.realizar_simulacao_proposta, name="simulacaoPropostaRealizar"),
    path("gerar/excel", simulacaoPropostaController.gerar_excel_simulacao_proposta, name="gerarExcelSimulacaoProposta")
]
