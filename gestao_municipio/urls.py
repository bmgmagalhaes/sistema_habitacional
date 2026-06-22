
from django.urls import path
from gestao_municipio import views

app_name = 'gestao_municipio'

# .../portal_prefeitura/...

urlpatterns = [

    # URL para acessar a página inicial do portal da prefeitura, onde o usuário pode escolher entre fazer o cadastro ou consultar os dados
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # ÁREA PÚBLICA - Acessível a todos os usuários, incluindo cidadãos e visitantes do site
    path('portal_prefeitura/', views.index_prefeitura, name='index_prefeitura'),
    path('portal_prefeitura/beneficiario/novo/', views.BeneficiarioCreateView.as_view(), name='beneficiario_novo'),
    path('portal_prefeitura/consultar_cadastro/', views.consultar_cadastro, name='consultar_cadastro'),
    # TODO: Alterar url pra não usar <int:pk>, usar um slug (UUID) ou outro identificador mais seguro e menos previsível
    path('portal_prefeitura/beneficiario/<int:pk>/', views.BeneficiarioDetailView.as_view(), name='beneficiario_detalhe'), 
    path('portal_prefeitura/beneficiario/<int:pk>/editar/', views.BeneficiarioUpdateView.as_view(), name='beneficiario_editar'),


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # AREA RESTRITA - Somente para usuários autenticados (funcionários da prefeitura)
    path('administrativo/',views.DashboardView.as_view(),name='dashboard'),
    path('administrativo/criterios-pontuacao/',views.CriterioPontuacaoListView.as_view(),name='criterio_pontuacao_lista'),
    path('administrativo/criterios-pontuacao/novo/',views.CriterioPontuacaoCreateView.as_view(),name='criterio_pontuacao_novo'),
    path('administrativo/criterios-pontuacao/<int:pk>/editar/',views.CriterioPontuacaoUpdateView.as_view(),name='criterio_pontuacao_editar'),
    path('administrativo/beneficiarios/',views.BeneficiarioListView.as_view(),name='beneficiario_lista'),
    path('administrativo/beneficiario/<int:pk>/editar/', views.BeneficiarioAdminUpdateView.as_view(), name='beneficiario_admin_editar'),
    path('administrativo/beneficiarios/exportar/',views.ExportarBeneficiariosCSVView.as_view(),name='beneficiario_exportar_csv'),
]
