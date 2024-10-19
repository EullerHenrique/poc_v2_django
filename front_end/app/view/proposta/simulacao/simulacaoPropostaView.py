import logging
from django.shortcuts import render
from django.http import HttpResponse
from app.service.internal.util.authentication import authenticationUtilInternalService
from app.view.authentication import authenticationView
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants

logger = logging.getLogger('app')
  
def exibir_pagina_simulacao_proposta(request):
    try:   
        authenticationUtilInternalService.validar_expiracao_acess_token(request) 
        return render(request, 'proposta/simulacao/simulacaoProposta.html')
    except UnauthorizedException:
        return authenticationView.exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_simulacao_proposta)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e, content_type=TypeHttpConstants.APPLICATION_JSON, status=500)