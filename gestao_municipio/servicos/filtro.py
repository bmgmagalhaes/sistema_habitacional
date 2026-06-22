from django.db.models import Q

class BeneficiarioFiltroServico:

    @staticmethod
    def aplicar(queryset, request):

        pesquisa = request.GET.get('pesquisa')

        if pesquisa:

            queryset = queryset.filter(
                Q(nome_completo__icontains=pesquisa) |
                Q(cpf__icontains=pesquisa) |
                Q(nis__icontains=pesquisa)
            )

        
        return queryset.order_by(
            '-pontuacao',
            'nome_completo'
        )