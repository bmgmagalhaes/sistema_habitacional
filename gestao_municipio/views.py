from django.shortcuts import render

# Create your views here.
def cadastro_beneficiario(request):

    return render(
        request, 
        'gestao_municipio/portal_prefeitura/cadastro_beneficiario.html',
        )

def consulta_beneficiario(request):

    return render(
        request, 
        'gestao_municipio/portal_prefeitura/consulta_beneficiario.html',
        )

def index_prefeitura(request):

    return render(
        request, 
        'gestao_municipio/portal_prefeitura/index_prefeitura.html',
        )