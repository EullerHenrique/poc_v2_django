from app.service.external.ms_moneyp_bmp.dto.proposta.simulacao import simulacaoPropostaDtoExternalService
from app.service.internal.util.relatorio import relatorioUtilService

def realizar_simulacao_proposta(request):
    return simulacaoPropostaDtoExternalService.realizar_simulacao_proposta(request)

def gerar_excel_simulacao_proposta(request):
   parcelas = realizar_simulacao_proposta(request)['parcelas']
   return relatorioUtilService.gerar_excel(parcelas, ['valorSolicitado', 'prazo', 'vlrParcela', 'vlrTAC', 'vlrBoleto', 'vlrSeguro', 'vlrIOF', 'percIOF', 'vlrTotalCredito', 'vlrTotalDivida', 'percCETMensal', 'percCETAnual', 'percJurosMensal', 'percJurosAnual'])
   