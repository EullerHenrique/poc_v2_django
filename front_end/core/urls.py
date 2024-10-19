from django.urls import path, include

urlpatterns = [
    path("", include('app.config.urls.index.urls')),
    path("auth/", include('app.config.urls.authentication.urls')),
    path("proposta/simulacao/", include('app.config.urls.proposta.simulacao.urls')),
]
