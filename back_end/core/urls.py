from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include('app.config.urls.authentication.urls')),
    path("proposta/simulacao/", include('app.config.urls.proposta.simulacao.urls')),
]
