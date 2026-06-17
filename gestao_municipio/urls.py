
from django.urls import path
from gestao_municipio import views

app_name = 'gestao_municipio'

# .../portal_prefeitura/...

urlpatterns = [

    # URL para acessar a página inicial do portal da prefeitura, onde o usuário pode escolher entre fazer o cadastro ou consultar os dados
    # ÁREA PÚBLICA - Acessível a todos os usuários, incluindo cidadãos e visitantes do site
    path('portal_prefeitura/', views.index_prefeitura, name='index_prefeitura'),
    path('portal_prefeitura/beneficiario/novo/', views.BeneficiarioCreateView.as_view(), name='beneficiario_novo'),
    path('portal_prefeitura/consultar_cadastro/', views.consultar_cadastro, name='consultar_cadastro'),


    # TODO: Alterar url pra não usar <int:pk>, usar um slug (UUID) ou outro identificador mais seguro e menos previsível
    path('portal_prefeitura/beneficiario/<int:pk>/', views.BeneficiarioDetailView.as_view(), name='beneficiario_detalhe'), 
    path('portal_prefeitura/beneficiario/<int:pk>/editar/', views.BeneficiarioUpdateView.as_view(), name='beneficiario_editar'),
    
    # AREA RESTRITA - Somente para usuários autenticados (funcionários da prefeitura)
    # path('beneficiarios/', views.BeneficiarioListView.as_view(), name='beneficiario_lista'),

    
    # path('portal_prefeitura/cadastro_beneficiario/', views.cadastro_beneficiario, name='cadastro_beneficiario'),
    # path('portal_prefeitura/consulta_beneficiario/', views.consulta_beneficiario, name='consulta_beneficiario'),


]
