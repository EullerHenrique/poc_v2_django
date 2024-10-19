from app.domain.model.external.ms_moneyp_bmp.authentication.Token import Token

def deletar_tokens():
    Token.objects.all().delete()

def salvar_token(response_token):
    token = Token(
        access_token=response_token['access_token'],
        expires_at=response_token['expires_at'],
        expires_in=response_token['expires_in']
    )
    token.save()

def buscar_token():
    return Token.objects.all().first()