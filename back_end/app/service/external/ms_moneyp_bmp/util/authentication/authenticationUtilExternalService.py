from pathlib import os
from dotenv import load_dotenv
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants
from app.domain.exception.http.UnknownException import UnknownException
from app.service.external.ms_moneyp_bmp.model.authentication import authenticationModelExternalService
from app.service.external.ms_moneyp_bmp.dto.authentication import authenticationDtoExternalService
from datetime import datetime, timezone, timedelta

load_dotenv()

def obter_token():
    response_token_obj = authenticationModelExternalService.buscar_token()
    datetime_now = datetime.now().replace(tzinfo=timezone.utc)
    if response_token_obj is not None:
        access_token = response_token_obj.access_token
        expires_at = response_token_obj.expires_at
        if datetime_now <= expires_at:
            return access_token    
    
    response_token_json = authenticationDtoExternalService.obter_token()
    expires_in = response_token_json['expires_in']
    expires_at = datetime_now + timedelta(seconds=expires_in)
    response_token_json['expires_at'] = expires_at
    authenticationModelExternalService.deletar_tokens()
    authenticationModelExternalService.salvar_token(response_token_json)
    return response_token_json['access_token']
    
def obter_headers():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
    }
    return headers

def obter_body():
    form = {
        'grant_type': os.getenv('MS_MONEYP_BMP_GRANT_TYPE'),
        'client_id': os.getenv('MS_MONEYP_BMP_CLIENT_ID'),
        'scope': os.getenv('MS_MONEYP_BMP_SCOPE'),
        'client_assertion': os.getenv('MS_MONEYP_BMP_CLIENT_ASSERTION'),
        'client_assertion_type': os.getenv('MS_MONEYP_BMP_CLIENT_ASSERTION_TYPE')
    }
    return form 

def obter_resposta(response):
    status_response = response.status_code
    if status_response != CodeHttpConstants.OK:      
        if response.text == '':
            raise UnknownException(status=status_response)
        json_response = response.json()
        msg_error = json_response.get('error')
        raise UnknownException(status=status_response, message=msg_error)
    return response.json() 


