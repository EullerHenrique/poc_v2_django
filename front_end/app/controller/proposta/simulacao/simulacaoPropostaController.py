import json
import logging
import requests
from django.http import HttpResponse
from app.service.internal.util.authentication import authenticationUtilInternalService
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

logger = logging.getLogger('app')

def realizar_simulacao_proposta(request):
    try:
        authenticationUtilInternalService.validar_expiracao_acess_token(request) 
        access_token = request.session.get('ACCESS_TOKEN')
        headers={'Authorization': f"Bearer {access_token}"}
        body={"dto": json.loads(request.body.decode())}
        response = requests.post('http://127.0.0.1:8000/proposta/simulacao/realizar', headers=headers, json=body)
        return HttpResponse(response, content_type=TypeHttpConstants.APPLICATION_JSON, status=response.status_code) 
    except UnauthorizedException:
        response_json = authenticationUtilInternalService.atualizar_acess_token(request)
        if response_json['status'] == CodeHttpConstants.OK:
            return realizar_simulacao_proposta(request)
        else:
            response_txt_json = json.dumps(response_json)
            return HttpResponse(response_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON, status=response_json['status'])
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e, content_type=TypeHttpConstants.APPLICATION_JSON, status=500)
        
def gerar_excel_simulacao_proposta(request):
    try:
        authenticationUtilInternalService.validar_expiracao_acess_token(request) 
        access_token = request.session.get('ACCESS_TOKEN')
        headers={'Authorization': f"Bearer {access_token}"}
        body={"dto": json.loads(request.body.decode())}
        response = requests.post('http://127.0.0.1:8000/proposta/simulacao/gerar/excel', headers=headers, json=body)
        if response.status_code == CodeHttpConstants.OK:
            response_excel = HttpResponse(response.content, content_type=TypeHttpConstants.APPLICATION_EXCEL)
            response_excel['Content-Disposition'] = 'attachment; filename=simulacaoProposta.xlsx'
            return response_excel
        elif response.status_code == CodeHttpConstants.UNAUTHORIZED:
            raise UnauthorizedException()
        else:
            return HttpResponse(response, content_type=TypeHttpConstants.APPLICATION_JSON, status=response.status_code)
    except UnauthorizedException:
        response_json = authenticationUtilInternalService.atualizar_acess_token(request)
        if response_json['status'] == CodeHttpConstants.OK:
            return gerar_excel_simulacao_proposta(request)
        else:
            response_txt_json = json.dumps(response_json)
            return HttpResponse(response_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON, status=response_json['status'])
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e, content_type=TypeHttpConstants.APPLICATION_JSON, status=500)