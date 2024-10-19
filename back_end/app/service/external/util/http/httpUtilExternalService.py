import requests
from app.domain.exception.http.InternalServerErrorException import InternalServerErrorException

def realizar_request_get(url, headers):
    try:
        return requests.get(url, headers=headers)
    except Exception as e:
        raise InternalServerErrorException(message=e)
    
def realizar_request_post(url, headers, body, eh_json=True):
    try:
        if eh_json:
            return requests.post(url, headers=headers, json=body)
        return requests.post(url, headers=headers, data=body)
    except Exception as e:
        raise InternalServerErrorException(message=e)
        