from pathlib import os
from dotenv import load_dotenv
from app.service.external.util.http import httpUtilExternalService
from app.service.external.ms_moneyp_bmp.util.authentication import authenticationUtilExternalService

load_dotenv()

def obter_token():
    url = os.getenv('MS_MONEYP_BMP_URL_OBTER_TOKEN')
    headers = authenticationUtilExternalService.obter_headers()
    body = authenticationUtilExternalService.obter_body()
    response = httpUtilExternalService.realizar_request_post(url, headers, body, eh_json=False)
    response_json = authenticationUtilExternalService.obter_resposta(response)
    return response_json
