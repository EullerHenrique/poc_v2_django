import requests
import logging
import json
from django.http import HttpResponse
from app.domain.constant.http.type.TypeHttpConstants import TypeHttpConstants
from app.domain.constant.http.code.CodeHttpConstants import CodeHttpConstants

logger = logging.getLogger('app')
   
def realizar_login(request):
    try:
        response = requests.post('http://127.0.0.1:8000/auth/get/token', json=json.loads(request.body.decode())) 
        status_code = response.status_code
        if status_code == CodeHttpConstants.OK:
            response_json = response.json()
            request.session['ACCESS_TOKEN'] = response_json['access']
            request.session['REFRESH_TOKEN'] = response_json['refresh']
        return HttpResponse(response, content_type=TypeHttpConstants.APPLICATION_JSON, status=status_code)
    except Exception as e:
        logger.exception(e)
        return HttpResponse(e, content_type=TypeHttpConstants.APPLICATION_JSON, status=CodeHttpConstants.INTERNAL_SERVER_ERROR)