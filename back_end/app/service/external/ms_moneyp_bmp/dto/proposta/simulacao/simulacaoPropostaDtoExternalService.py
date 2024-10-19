from pathlib import os
from dotenv import load_dotenv
from app.service.external.util.http import httpUtilExternalService
from app.service.external.ms_moneyp_bmp.util.proposta.simulacao import simulacaoPropostaUtilExternalService

load_dotenv()

def realizar_simulacao_proposta(request):
    url = os.getenv('MS_MONEYP_BMP_URL_SIMULACAO_PROPOSTA')
    headers = simulacaoPropostaUtilExternalService.obter_headers()
    body = simulacaoPropostaUtilExternalService.obter_body(request)
    response = httpUtilExternalService.realizar_request_post(url, headers, body, eh_json=True)
    return simulacaoPropostaUtilExternalService.obter_resposta(response)
