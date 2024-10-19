import requests
import datetime
import jwt
from app.domain.exception.http.UnauthorizedException import UnauthorizedException
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

def validar_expiracao_acess_token(request):
    acess_token = request.session.get('ACCESS_TOKEN')
    if acess_token is None:
        raise UnauthorizedException()   
    payload = jwt.decode(acess_token, algorithms=['RS256'], options={"verify_signature": False}) 
    if datetime.datetime.now() > datetime.datetime.fromtimestamp(payload['exp']):
        raise UnauthorizedException()
    
def atualizar_acess_token(request):
    response = requests.post('http://127.0.0.1:8000/auth/get/token/refresh', json={'refresh':  request.session.get('REFRESH_TOKEN')})
    status_code = response.status_code
    response_json = response.json()
    if response.status_code == CodeHttpConstants.OK:
        request.session['ACCESS_TOKEN'] = response_json['access']
        return {'status': status_code}
    else:
        return response_json
