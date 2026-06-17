# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from gestao_municipio.models import Beneficiario, CriterioPontuacao
from gestao_municipio.forms import BeneficiarioForm, CriterioPontuacaoForm
from gestao_municipio.servicos.pontuacao import PontuacaoServico
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.       

class BeneficiarioCreateView(CreateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    
    # Especifica o template a ser usado para renderizar o formulário de criação do beneficiário.
    template_name = 'gestao_municipio/portal_prefeitura/beneficiario_form.html'
    # Especifica a URL para redirecionar após a criação bem-sucedida do beneficiário. Neste caso, redireciona para a index da prefeitura.
    # success_url = reverse_lazy('gestao_municipio:index_prefeitura')

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
        # return HttpResponseRedirect(self.get_success_url())  
        return redirect(
                'gestao_municipio:beneficiario_detalhe',
                pk=beneficiario.pk
            )
    




# class BeneficiarioListView(ListView):
#     model = Beneficiario
#     paginate_by = 30
#     template_name = 'gestao_municipio/portal_prefeitura/beneficiario_lista.html'

#     # Define o nome do contexto para a lista de beneficiários, permitindo que seja acessada no template usando esse nome.
#     context_object_name = 'beneficiarios'

#     def get_queryset(self):
        
#         # Retorna um queryset de beneficiários ativos, ordenados por pontuação (do maior para o menor)
#         # Em caso de empate na pontuação, ordenados por nome completo em ordem alfabética.

#         queryset = (
#             Beneficiario.objects
#             .filter(ativo=True
#             # .order_by('-pontuacao', 
#             #           'nome_completo')
#             )
#         )
        
#         return queryset

class BeneficiarioDetailView(DetailView):
    model = Beneficiario
    template_name = 'gestao_municipio/portal_prefeitura/beneficiario_detalhe.html'
    context_object_name = 'beneficiario'

class BeneficiarioUpdateView(UpdateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    template_name = 'gestao_municipio/portal_prefeitura/beneficiario_form.html'
    # success_url = reverse_lazy('gestao_municipio:index_prefeitura')

    def form_valid(self, form):
        
        beneficiario = form.save(commit=False)  
        beneficiario.pontuacao = PontuacaoServico.calcular(beneficiario)  
        
        beneficiario.save()  
        self.object = beneficiario


        messages.success(
            self.request,
            'Cadastro alterado com sucesso.'
        )
        messages.MessageFailure(
            self.request,
            'Erro ao atualizar cadastro.'
        )
        
        # return HttpResponseRedirect(self.get_success_url())  
        return redirect(
                'gestao_municipio:beneficiario_detalhe',
                pk=beneficiario.pk
            )


def index_prefeitura(request):

    return render(
        request, 
        'gestao_municipio\portal_prefeitura\index_prefeitura.html',
        )

def consultar_cadastro(request):

    if request.method == 'POST':

        cpf = request.POST.get('cpf')
        nis = request.POST.get('nis')

        try:

            beneficiario = Beneficiario.objects.get(
                cpf=cpf,
                nis=nis,
                ativo=True
            )

            # Redireciona para a página de detalhes do beneficiário encontrado
            return redirect(
                'gestao_municipio:beneficiario_detalhe',
                pk=beneficiario.pk
            )

        except Beneficiario.DoesNotExist:

            messages.error(
                request,
                'CPF ou NIS não encontrados.'
            )

    return render(
        request,
        'gestao_municipio/portal_prefeitura/consultar_cadastro.html'
    )


@login_required
def dashboard_admin(request):

    return render(
        request,
        'gestao_municipio/administrativo/dashboard.html'
    )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# VIEWS DO CRITÉRIO DE PONTUÇAO
class CriterioPontuacaoCreateView(LoginRequiredMixin, CreateView):
    model = CriterioPontuacao
    form_class = CriterioPontuacaoForm
    
    # Especifica o template a ser usado para renderizar o formulário de criação do beneficiário.
    template_name = 'gestao_municipio/administrativo/criterio_pontuacao_form.html'
    
    # Método sobrescrito form_valid é chamado pelo Django quando o formulário é válido. 
    def form_valid(self, form):
        
        # Salva o formulário sem enviar para o banco de dados ainda
        criterio_pontuacao = form.save()  
        messages.success(
            self.request,
            'Cadastro realizado com sucesso.'
        )
        messages.MessageFailure(
            self.request,
            'Erro ao realizar cadastro.'
        )

        # Redireciona para a URL de sucesso após salvar o beneficiário
        return redirect(
                'gestao_municipio:criterio_pontuacao_lista',
            )

class CriterioPontuacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterioPontuacao
    form_class = CriterioPontuacaoForm
    template_name = 'gestao_municipio/administrativo/criterio_pontuacao_form.html'

    def form_valid(self, form):
        
        criterio_pontuacao = form.save()  
        
        messages.success(
            self.request,
            'Cadastro alterado com sucesso.'
        )
        messages.MessageFailure(
            self.request,
            'Erro ao atualizar cadastro.'
        )
        
        # return HttpResponseRedirect(self.get_success_url())  
        return redirect(
                'gestao_municipio:criterio_pontuacao_lista',
                
            )

class CriterioPontuacaoListView(LoginRequiredMixin, ListView):
    model = CriterioPontuacao

    # 
    template_name = ('gestao_municipio/administrativo/criterio_pontuacao_lista.html')

    context_object_name = 'criterios'

    ordering = ['descricao']