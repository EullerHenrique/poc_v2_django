import json
import random
from app.domain.exception.http.UnknownException import UnknownException
from app.domain.exception.http.ForbiddenException import ForbiddenException
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants
from app.service.external.ms_moneyp_bmp.util.authentication import authenticationUtilExternalService

def obter_headers():
    idempotency_key = str(random.randint(0, 99999999))
    acess_token = authenticationUtilExternalService.obter_token()
    headers = {
        'Authorization' : f"Bearer {acess_token}",
        'IdempotencyKey' : idempotency_key,
        'Content-Type': 'application/json'
    }
    return headers

def obter_body(request):
    return json.loads(request.body.decode())

def obter_resposta(response):
    status_response = response.status_code
    if status_response != CodeHttpConstants.OK:
        if status_response == CodeHttpConstants.UNAUTHORIZED:
            status_response = CodeHttpConstants.FORBIDDEN
            
        if response.text == '':
            if status_response == CodeHttpConstants.FORBIDDEN:
                raise ForbiddenException(status=status_response)
            raise UnknownException(status=status_response)
        
        json_response = response.json()
        has_error_json = json_response.get('hasError')
        msg_json = json_response.get('msg')
        messages_json = json_response.get('messages')
        if has_error_json:
            raise UnknownException(status=status_response, error=msg_json, message=messages_json)
        raise UnknownException(status=status_response, message=json_response)
    return response.json() 

