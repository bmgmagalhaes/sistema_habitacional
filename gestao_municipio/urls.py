
from django.urls import path
from gestao_municipio import views

app_name = 'gestao_municipio'

# .../portal_prefeitura/...

urlpatterns = [

    # URL para acessar a página inicial do portal da prefeitura, onde o usuário pode escolher entre fazer o cadastro ou consultar os dados
    path('portal_prefeitura/', views.index_prefeitura, name='index_prefeitura'),
    path('portal_prefeitura/cadastro_beneficiario/', views.cadastro_beneficiario, name='cadastro_beneficiario'),
    path('portal_prefeitura/consulta_beneficiario/', views.consulta_beneficiario, name='consulta_beneficiario'),


]
