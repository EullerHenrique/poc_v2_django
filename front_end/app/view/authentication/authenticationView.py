import logging
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import RedirectView
from app.service.internal.util.authentication import authenticationUtilInternalService
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants
from app.domain.exception.http.UnauthorizedException import UnauthorizedException

logger = logging.getLogger('app')

def exibir_pagina_login(request):
    try:  
        acess_token =  request.session.get('ACCESS_TOKEN') 
        if acess_token is None:
            return render(request, "authentication/login.html")             
        authenticationUtilInternalService.validar_expiracao_acess_token(request)
        return RedirectView.as_view(url='/')(request)
    except UnauthorizedException:
        return exibir_pagina_x_apos_atualizar_acess_token(request, '/')
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)

def exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_x):
    response_json = authenticationUtilInternalService.atualizar_acess_token(request)
    if response_json['status'] == CodeHttpConstants.OK:
        if exibir_pagina_x == '/':
            return RedirectView.as_view(url='/')(request)
        return exibir_pagina_x(request)
    elif response_json['status'] == CodeHttpConstants.BAD_REQUEST or response_json['status'] == CodeHttpConstants.UNAUTHORIZED:
        request.session.flush()
        return RedirectView.as_view(url='/auth/login')(request)
    else:
        data_txt_json = json.dumps(response_json)
        return HttpResponse(data_txt_json, content_type=TypeHttpConstants.APPLICATION_JSON, status=response_json['status'])