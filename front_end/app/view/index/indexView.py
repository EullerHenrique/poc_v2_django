import logging
from django.http import HttpResponse
from django.shortcuts import render
from app.service.internal.util.authentication import authenticationUtilInternalService
from app.view.authentication import authenticationView
from app.domain.exception.http.UnauthorizedException import UnauthorizedException

logger = logging.getLogger('app')

def exibir_pagina_index(request):
    try:        
        authenticationUtilInternalService.validar_expiracao_acess_token(request)
        return render(request, 'index.html') 
    except UnauthorizedException:
        return authenticationView.exibir_pagina_x_apos_atualizar_acess_token(request, exibir_pagina_index)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e)
	

