from django.urls import path
from app.controller.authentication import authenticationController
from app.view.authentication import authenticationView

urlpatterns = [
    path("login", authenticationView.exibir_pagina_login, name="login"),
    path("realizar/login", authenticationController.realizar_login, name="realizarLogin"),
]
