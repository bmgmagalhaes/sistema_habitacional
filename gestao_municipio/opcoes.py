from django.db import models

class CampoBeneficiario(models.TextChoices):
    POSSUI_DEFICIENCIA = 'possui_deficiencia', 'Possui deficiência'
    POSSUI_DOENCA_RARA = 'possui_doenca_rara', 'Possui doença rara'
    MULHER_RESPONSAVEL = 'mulher_responsavel_familia', 'Mulher responsável pela família'

    RECEBE_BOLSA_FAMILIA = 'recebe_bolsa_familia', 'Recebe Bolsa Família'
    DEFICIENCIA_NA_FAMILIA = 'deficiencia_na_familia', 'Deficiência na família'
    DOENCA_RARA_NA_FAMILIA = 'doenca_rara_na_familia', 'Doença rara na família'
    RECEBE_BPC = 'recebe_bpc', 'Recebe BPC'
    PESSOA_NEGRA = 'pessoa_negra_na_familia', 'Pessoa negra na família'

    MULHER_VIOLENCIA = 'mulheres_violencia_domestica', 'Mulheres vítimas de violência doméstica'
    POVOS_TRADICIONAIS = 'povos_tradicionais_quilombolas', 'Povos tradicionais e quilombolas'
    IDOSOS = 'idosos_na_familia', 'Idosos na família'
    CONTRATO_RESCINDIDO = 'beneficiario_contrato_rescindido', 'Contrato rescindido'
    MICROCEFALIA = 'microcefalia_na_familia', 'Microcefalia na família'

    FILHOS_0_6 = 'filhos_0_6', 'Filhos de 0 a 6 anos'
    FILHOS_7_11 = 'filhos_7_11', 'Filhos de 7 a 11 anos'
    FILHOS_12_18 = 'filhos_12_18', 'Filhos de 12 a 18 anos'

    AREA_RISCO = 'residente_area_risco', 'Residente em área de risco'
    SITUACAO_RUA = 'situacao_rua', 'Situação de rua'