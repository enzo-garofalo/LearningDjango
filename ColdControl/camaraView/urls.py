# Esse código configura as rotas (URLs) de uma aplicação no Django.
from django.urls import path

from . import views

# Essa lista define as rotas específicas para a aplicação e mapeia cada URL para uma view.
app_name = "camaraView"
urlpatterns = [
    path("", views.home, name="home")
]
