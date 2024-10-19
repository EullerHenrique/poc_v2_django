import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.service.internal.dto.proposta.simulacao import simulacaoPropostaInternalDtoService
from app.service.internal.dto.authentication import authenticationInternalDtoService
from app.service.internal.util.http import httpUtilInternalService
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants

@csrf_exempt
def realizar_simulacao_proposta(request):
    try:
        authenticationInternalDtoService.realizar_autenticacao(request)
        data_json = simulacaoPropostaInternalDtoService.realizar_simulacao_proposta(request)
        data_txt_json = json.dumps(data_json)
        return HttpResponse(data_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON)
    except Exception as e:
        return httpUtilInternalService.obter_resposta_erro(e)
    
@csrf_exempt
def gerar_excel_colaboradores(request):
    try:
        authenticationInternalDtoService.realizar_autenticacao(request)
        byte = simulacaoPropostaInternalDtoService.gerar_excel_simulacao_proposta(request)  
        response = HttpResponse(byte, content_type=TypeHttpConstants.APPLICATION_EXCEL)
        response['Content-Disposition'] = 'attachment; filename=simulacaoProposta.xlsx'
        return response
    except Exception as e:
        return httpUtilInternalService.obter_resposta_erro(e)