
from django.urls import path
from gestao_municipio import views

app_name = 'gestao_municipio'

urlpatterns = [
    path('', views.index, name='index'),
]
