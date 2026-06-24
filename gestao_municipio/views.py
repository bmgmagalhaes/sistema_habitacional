import csv
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from gestao_municipio.forms import (
    BeneficiarioAdminForm,
    BeneficiarioForm,
    CriterioPontuacaoForm,
)
from gestao_municipio.models import Beneficiario, CriterioPontuacao
from gestao_municipio.servicos.filtro import BeneficiarioFiltroServico
from gestao_municipio.servicos.pontuacao import PontuacaoServico

# from .models import Beneficiario

# Create your views here.


class BeneficiarioCreateView(CreateView):
    model = Beneficiario
    form_class = BeneficiarioForm

    # Especifica o template a ser usado para renderizar o formulário de criação do beneficiário.
    template_name = "gestao_municipio/portal_prefeitura/beneficiario_form.html"
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

        messages.success(self.request, "Cadastro realizado com sucesso.")
        # messages.MessageFailure(self.request, "Erro ao realizar cadastro.")
        # Redireciona para a URL de sucesso após salvar o beneficiário
        # return HttpResponseRedirect(self.get_success_url())
        return redirect("gestao_municipio:beneficiario_detalhe", pk=beneficiario.pk)


class BeneficiarioListView(LoginRequiredMixin, ListView):

    model = Beneficiario

    paginate_by = 30

    template_name = "gestao_municipio/administrativo/beneficiario_lista.html"

    context_object_name = "beneficiarios"

    def get_queryset(self):

        queryset = Beneficiario.objects.filter(ativo=True)

        return BeneficiarioFiltroServico.aplicar(queryset, self.request)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["pesquisa"] = self.request.GET.get("pesquisa", "")
        context["primeira_classificacao"] = (
            (context["page_obj"].number - 1) * self.paginate_by
        ) + 1

        return context


class BeneficiarioDetailView(DetailView):
    model = Beneficiario
    template_name = "gestao_municipio/portal_prefeitura/beneficiario_detalhe.html"
    context_object_name = "beneficiario"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Pega o valor do dicionário chave next. Se não houver, usa index_prefeitura
        context["next"] = self.request.GET.get("next", "index_prefeitura")

        return context


class BeneficiarioUpdateView(UpdateView):

    model = Beneficiario
    template_name = "gestao_municipio/portal_prefeitura/beneficiario_form.html"

    def get_form_class(self):

        next_url = self.request.GET.get("next")

        if next_url == "beneficiario_lista":
            return BeneficiarioAdminForm

        return BeneficiarioForm

    def form_valid(self, form):

        beneficiario = form.save(commit=False)
        beneficiario.pontuacao = PontuacaoServico.calcular(beneficiario)

        self.object = beneficiario
        self.object.save()

        messages.success(self.request, "Cadastro alterado com sucesso.")

        # Se não existir o parâmetro 'next', retorna index_prefeitura
        next_url = self.request.GET.get("next", "index_prefeitura")

        url = reverse(
            "gestao_municipio:beneficiario_detalhe", kwargs={"pk": self.object.pk}
        )

        return redirect(f"{url}?next={next_url}")


class ExportarBeneficiariosCSVView(LoginRequiredMixin, View):

    def get(self, request):

        # Obtém todos os beneficiários ativos,
        # ordenados pela pontuação.
        # beneficiarios = (
        #     Beneficiario.objects
        #     .filter(ativo=True)
        #     .order_by(
        #         '-pontuacao',
        #         'nome_completo'
        #     )
        # )
        beneficiarios = BeneficiarioFiltroServico.aplicar(
            Beneficiario.objects.filter(ativo=True), request
        )
        quantidade = request.GET.get("quantidade")

        if quantidade:
            try:
                quantidade = int(quantidade)
                if quantidade > 0:
                    beneficiarios = beneficiarios[:quantidade]

            except ValueError:
                pass
        # Nome do arquivo
        data = datetime.now().strftime("%d_%m_%Y")

        response = HttpResponse(content_type="text/csv; charset=utf-8")

        response["Content-Disposition"] = (
            f'attachment; filename="beneficiarios_{data}.csv"'
        )

        # Escreve o BOM para que o Excel reconheça UTF-8
        response.write("\ufeff")

        writer = csv.writer(response, delimiter=";")

        # Cabeçalho
        writer.writerow(
            [
                "Classificação",
                "Nome",
                "CPF",
                "Pontuação",
                "Data do cadastro",
            ]
        )

        classificacao = 1

        for beneficiario in beneficiarios:

            writer.writerow(
                [
                    classificacao,
                    beneficiario.nome_completo,
                    beneficiario.cpf,
                    beneficiario.pontuacao,
                    beneficiario.data_cadastro.strftime("%d/%m/%Y"),
                ]
            )

            classificacao += 1

        return response


class BeneficiarioAdminUpdateView(LoginRequiredMixin, UpdateView):

    model = Beneficiario
    template_name = "gestao_municipio/administrativo/beneficiario_admin_form.html"

    def get_form_class(self):

        next_url = self.request.GET.get("next")

        if next_url == "beneficiario_lista":
            return BeneficiarioAdminForm

        return BeneficiarioForm

    def form_valid(self, form):

        beneficiario = form.save(commit=False)
        beneficiario.pontuacao = PontuacaoServico.calcular(beneficiario)

        self.object = beneficiario
        self.object.save()

        messages.success(self.request, "Cadastro alterado com sucesso.")

        # Se não existir o parâmetro 'next', retorna index_prefeitura
        next_url = self.request.GET.get("next", "index_prefeitura")

        url = reverse(
            "gestao_municipio:beneficiario_detalhe", kwargs={"pk": self.object.pk}
        )

        return redirect(f"{url}?next={next_url}")


def index_prefeitura(request):

    return render(
        request,
        "gestao_municipio/portal_prefeitura/index_prefeitura.html",
    )


def consultar_cadastro(request):

    if request.method == "POST":

        cpf = request.POST.get("cpf")
        nis = request.POST.get("nis")

        try:

            beneficiario = Beneficiario.objects.get(cpf=cpf, nis=nis, ativo=True)

            # Redireciona para a página de detalhes do beneficiário encontrado
            return redirect("gestao_municipio:beneficiario_detalhe", pk=beneficiario.pk)

        except Beneficiario.DoesNotExist:

            messages.error(request, "CPF ou NIS não encontrados.")

    return render(request, "gestao_municipio/portal_prefeitura/consultar_cadastro.html")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# VIEWS DO CRITÉRIO DE PONTUÇAO
class CriterioPontuacaoCreateView(LoginRequiredMixin, CreateView):
    model = CriterioPontuacao
    form_class = CriterioPontuacaoForm

    # Especifica o template a ser usado para renderizar o formulário de criação do beneficiário.
    template_name = "gestao_municipio/administrativo/criterio_pontuacao_form.html"

    # Método sobrescrito form_valid é chamado pelo Django quando o formulário é válido.
    def form_valid(self, form):

        # Salva o formulário sem enviar para o banco de dados ainda
        criterio_pontuacao = form.save()
        messages.success(self.request, "Cadastro realizado com sucesso.")
        messages.MessageFailure(self.request, "Erro ao realizar cadastro.")

        # Redireciona para a URL de sucesso após salvar o beneficiário
        return redirect(
            "gestao_municipio:criterio_pontuacao_lista",
        )


class CriterioPontuacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterioPontuacao
    form_class = CriterioPontuacaoForm
    template_name = "gestao_municipio/administrativo/criterio_pontuacao_form.html"

    def form_valid(self, form):

        criterio_pontuacao = form.save()

        messages.success(self.request, "Cadastro alterado com sucesso.")
        messages.MessageFailure(self.request, "Erro ao atualizar cadastro.")

        # return HttpResponseRedirect(self.get_success_url())
        return redirect(
            "gestao_municipio:criterio_pontuacao_lista",
        )


class CriterioPontuacaoListView(LoginRequiredMixin, ListView):

    model = CriterioPontuacao

    #
    template_name = "gestao_municipio/administrativo/criterio_pontuacao_lista.html"

    context_object_name = "criterios"

    ordering = ["descricao"]


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "gestao_municipio/administrativo/dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_beneficiarios"] = Beneficiario.objects.filter(ativo=True).count()

        # SITUACAO_CADASTRAL_CHOICES = [
        #     ('em_analise', 'Em análise'),
        #     ('contemplado', 'Contemplado'),
        #     ('indeferido', 'Indeferido'),
        # ]
        # situacao = Beneficiario.SITUACAO_CADASTRAL_CHOICES
        context["total_em_analise"] = Beneficiario.objects.filter(
            ativo=True, situacao_cadastral="em_analise"
        ).count()

        context["total_contemplados"] = Beneficiario.objects.filter(
            ativo=True, situacao_cadastral="contemplado"
        ).count()

        context["total_indeferido"] = Beneficiario.objects.filter(
            ativo=True, situacao_cadastral="indeferido"
        ).count()

        context["total_criterios"] = CriterioPontuacao.objects.filter(
            ativo=True
        ).count()

        return context


class ReprocessarPontuacaoView(LoginRequiredMixin, View):

    def post(self, request):

        total = PontuacaoServico.reprocessar()

        messages.success(
            request, f"Pontuação recalculada com sucesso para {total} beneficiários."
        )

        return redirect("gestao_municipio:dashboard")
