from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from gestao_municipio.models import Beneficiario
from gestao_municipio.forms import BeneficiarioForm
from gestao_municipio.servicos.pontuacao import PontuacaoServico
from django.shortcuts import render
from django.contrib import messages

# Create your views here.

class BeneficiarioCreateView(CreateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    
    # Especifica o template a ser usado para renderizar o formulário de criação do beneficiário.
    template_name = 'gestao_municipio/portal_prefeitura/beneficiario_form.html'
    # Especifica a URL para redirecionar após a criação bem-sucedida do beneficiário. Neste caso, redireciona para a index da prefeitura.
    success_url = reverse_lazy('gestao_municipio:index_prefeitura')

    # Método sobrescrito form_valid é chamado pelo Django quando o formulário é válido. 
    def form_valid(self, form):
        
        # Antes de salvar o formulário, podemos realizar ações adicionais, como calcular a pontuação do beneficiário com base nos critérios de pontuação ativos.
        
        # Salva o formulário sem enviar para o banco de dados ainda
        beneficiario = form.save(commit=False)  

        # Recalcula a pontuação do beneficiário com base nos critérios de pontuação ativos
        beneficiario.pontuacao = PontuacaoServico.calcular(beneficiario)  
        
        # Agora salva o beneficiário no banco de dados com a pontuação calculada
        beneficiario.save()  
        self.object = beneficiario


        messages.success(
            self.request,
            'Cadastro realizado com sucesso.'
        )
        messages.MessageFailure(
            self.request,
            'Erro ao realizar cadastro.'
        )
        # Redireciona para a URL de sucesso após salvar o beneficiário
        return HttpResponseRedirect(self.get_success_url())  



class BeneficiarioListView(ListView):
    model = Beneficiario
    paginate_by = 30
    template_name = 'gestao_municipio/portal_prefeitura/beneficiario_lista.html'

    # Define o nome do contexto para a lista de beneficiários, permitindo que seja acessada no template usando esse nome.
    context_object_name = 'beneficiarios'

    def get_queryset(self):
        
        # Retorna um queryset de beneficiários ativos, ordenados por pontuação (do maior para o menor)
        # Em caso de empate na pontuação, ordenados por nome completo em ordem alfabética.

        queryset = (
            Beneficiario.objects
            .filter(ativo=True
            # .order_by('-pontuacao', 
            #           'nome_completo')
            )
        )
        
        return queryset

# class BeneficiarioDetailView(DetailView):
#     model = Beneficiario
#     template_name = 'gestao_municipio/portal_prefeitura/beneficiario_detalhe.html'
#     context_object_name = 'beneficiario'

# class BeneficiarioUpdateView(UpdateView):
#     model = Beneficiario
#     form_class = BeneficiarioForm
#     template_name = 'gestao_municipio/portal_prefeitura/beneficiario_form.html'
#     success_url = reverse_lazy('beneficiario_lista')

# class BeneficiarioDeleteView(DeleteView):
#     model = Beneficiario
#     template_name = 'gestao_municipio/portal_prefeitura/beneficiario_confirm_delete.html'
#     success_url = reverse_lazy('beneficiario_lista')


def index_prefeitura(request):

    return render(
        request, 
        'gestao_municipio\portal_prefeitura\index_prefeitura.html',
        )
