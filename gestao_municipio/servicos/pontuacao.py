from gestao_municipio.models import CriterioPontuacao


class PontuacaoServico:
    """
    Serviço para calcular a pontuação de um beneficiário com base nos critérios definidos.
    A pontuação é calculada iterando sobre os critérios ativos e aplicando a lógica de cálculo definida para cada um deles. 
    O resultado é a pontuação total do beneficiário, que pode ser utilizada para fins de classificação ou priorização em programas sociais.
    """

    @staticmethod
    def calcular(beneficiario):

        total = 0

        # Recupera os critérios de pontuação ativos
        criterios = CriterioPontuacao.objects.filter(
            ativo=True
        )

        # Itera sobre os critérios e calcula a pontuação com base no valor do campo correspondente do beneficiário
        for criterio in criterios:

            # Obtém o valor do campo correspondente do beneficiário usando getattr, passando o nome do campo definido no critério
            valor = getattr(
                beneficiario,
                criterio.campo_beneficiario,
                None
            )

            # Aplica a lógica de cálculo definida para o critério, verificando o tipo de cálculo (fixo ou multiplicador) e somando a pontuação total
            if criterio.tipo_calculo == 'fixo':

                # Para critérios de cálculo fixo, a pontuação é adicionada ao total se o valor do campo for verdadeiro (para campos booleanos) ou maior que zero (para campos numéricos)
                if valor:
                    total += criterio.pontos
            # Para critérios de cálculo multiplicador, a pontuação é calculada multiplicando o valor do campo pelo número de pontos definido no critério e somando ao total
            elif criterio.tipo_calculo == 'multiplicador':

                total += (valor or 0) * criterio.pontos

        return total