from django.contrib import admin
from gestao_municipio import models



@admin.register(models.Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    # Colunas a serem exibidas na lista de beneficiários
    list_display = ('cpf', 'nis', 'nome_completo', 'ativo', 'pontuacao', 'data_cadastro',)
    # Campos para busca e ordenação
    search_fields = ('nome_completo', 'cpf', 'nis',)
    # Ordenação padrão por data de cadastro (mais recente primeiro)
    ordering = ('-data_cadastro',)
    # Filtros para facilitar a navegação
    list_filter = ('ativo',)
    # Número de registros por página
    list_per_page = 30
    # Campos para edição rápida
    list_editable = ('nome_completo', 'ativo',)
    # Limite para exibir todos os registros sem paginação (cuidado com muitos registros)
    list_max_show_all = 100
    # Campos clicáveis para acessar detalhes do beneficiário
    list_display_links = ('cpf','nis',)  

@admin.register(models.CriterioPontuacao)
class CriterioPontuacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'campo_beneficiario', 'pontos', 'tipo_calculo', 'ativo', 'data_cadastro')
    search_fields = ('descricao',)
    ordering = ('-data_cadastro',)
    list_filter = ('ativo', 'tipo_calculo')
    list_per_page = 30
    list_editable = ('pontos', 'tipo_calculo', 'ativo')
    list_max_show_all = 100
    list_display_links = ('campo_beneficiario','descricao',)
    
