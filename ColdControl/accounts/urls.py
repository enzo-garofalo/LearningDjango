# Esse código configura as rotas (URLs) de uma aplicação no Django.
from django.urls import path

from . import views

# Essa lista define as rotas específicas para a aplicação e mapeia cada URL para uma view.
app_name = "accounts"
urlpatterns = [
    path("", views.login, name="login"),
    path("signUP/", views.signUP, name="signUP"),
    path("validateUser/", views.validateUser, name="validateUser"),
    path("createNewUser/", views.createNewUser, name="createNewUser"),
]