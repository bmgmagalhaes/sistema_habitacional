from django.db import models
from simple_history.models import HistoricalRecords
from django.core.validators import RegexValidator
from gestao_municipio.opcoes import CampoBeneficiario


class Beneficiario(models.Model):

    # --- SEÇÃO DADOS PESSOAIS ---
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='CPF deve conter 11 dígitos.'
            )
        ],
        verbose_name='CPF')
    nome_completo = models.CharField(max_length=200)
    # nome_social = models.CharField(max_length=200, blank=True, null=True)
    nis = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='NIS deve conter 11 dígitos.'
            )
        ],
        verbose_name='NIS')

    # TIPO_DOC_CHOICES = [
    #     ('rg', 'RG'),
    #     ('cnh', 'CNH'),
    #     ('passaporte', 'Passaporte'),
    #     ('outro', 'Outro'),
    # ]
    # tipo_documento = models.CharField(max_length=20, choices=TIPO_DOC_CHOICES)
    # numero_documento = models.CharField(max_length=20)
    # data_emissao_documento = models.DateField(blank=True, null=True)
    # orgao_expedidor = models.CharField(max_length=50, blank=True, null=True)
    
    # UF_CHOICES = [
    #     ('AC', 'Acre'),
    #     ('AL', 'Alagoas'),
    #     ('AP', 'Amapá'),
    #     ('AM', 'Amazonas'),
    #     ('BA', 'Bahia'),
    #     ('CE', 'Ceará'),
    #     ('DF', 'Distrito Federal'),
    #     ('ES', 'Espírito Santo'),
    #     ('GO', 'Goiás'),
    #     ('MA', 'Maranhão'),
    #     ('MT', 'Mato Grosso'),
    #     ('MS', 'Mato Grosso do Sul'),
    #     ('MG', 'Minas Gerais'),
    #     ('PA', 'Pará'),
    #     ('PB', 'Paraíba'),
    #     ('PR', 'Paraná'),
    #     ('PE', 'Pernambuco'),
    #     ('PI', 'Piauí'),
    #     ('RJ', 'Rio de Janeiro'),
    #     ('RN', 'Rio Grande do Norte'),
    #     ('RS', 'Rio Grande do Sul'),
    #     ('RO', 'Rondônia'),
    #     ('RR', 'Roraima'),
    #     ('SC', 'Santa Catarina'),
    #     ('SP', 'São Paulo'),
    #     ('SE', 'Sergipe'),
    #     ('TO', 'Tocantins'),
    # ]

    # uf_emissao = models.CharField(max_length=2, choices=UF_CHOICES, blank=True, null=True)

    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento'
    )
    # NACIONALIDADE_CHOICES = [
    #     ('brasileira', 'Brasileira'),
    #     ('estrangeira', 'Estrangeira'),
    # ]
    # nacionalidade = models.CharField(max_length=20, choices=NACIONALIDADE_CHOICES)
    # naturalidade = models.CharField(max_length=100)

    ESTADO_CIVIL_CHOICES = [
        ('casado', 'Casado(a)'),
        ('separado', 'Separado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('uniao_estavel', 'Em união estável'),
        ('companheiro', 'Mora com companheiro(a)'),
        ('solteiro', 'Solteiro(a)'),
        ('viuvo', 'Viúvo(a)'),
    ]
    estado_civil = models.CharField(
        max_length=20, 
        choices=ESTADO_CIVIL_CHOICES,
        verbose_name='Estado Civil')

    # GRAU_INSTRUCAO_CHOICES = [
    #     ('fundamental', 'Ensino Fundamental'),
    #     ('medio', 'Ensino Médio'),
    #     ('superior', 'Ensino Superior'),
    #     ('pos', 'Pós-graduação'),
    # ]
    # grau_instrucao = models.CharField(max_length=20, choices=GRAU_INSTRUCAO_CHOICES)

    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        # ('outro', 'Outro'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)

    # GENERO_CHOICES = [
    #     ('cis', 'Cisgênero'),
    #     ('trans', 'Transgênero'),
    #     ('nao_binario', 'Não-binário'),
    #     ('outro', 'Outro'),
    # ]
    # genero = models.CharField(max_length=20, choices=GENERO_CHOICES, blank=True, null=True)

    # telefone1 = models.CharField(max_length=15)
    # telefone2 = models.CharField(max_length=15, blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    # profissao = models.CharField(max_length=100)
    # nome_mae = models.CharField(max_length=200)
    # nome_pai = models.CharField(max_length=200, blank=True, null=True)

    possui_deficiencia = models.BooleanField(default=False, verbose_name='Possui deficiência?')
    possui_doenca_rara = models.BooleanField(default=False, verbose_name='Possui doença rara?')
    mulher_responsavel_familia = models.BooleanField(default=False, verbose_name='Mulher responsável pela família?')

    # --- SEÇÃO RENDA ---
    renda_pessoal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    POSICAO_FAMILIAR_CHOICES = [
        ('chefe', 'Chefe de família'),
        ('conjuge', 'Cônjuge'),
        ('filho', 'Filho(a)'),
        ('outro', 'Outro'),
    ]
    
    posicao_familiar = models.CharField(
        max_length=20, 
        choices=POSICAO_FAMILIAR_CHOICES,
        verbose_name='Posição familiar')
    # fonte_pagadora = models.CharField(max_length=20, blank=True, null=True)
    # data_admissao = models.DateField(blank=True, null=True)

    # MES_REFERENCIA_CHOICES = [
    #     ('jan', 'Janeiro'),
    #     ('fev', 'Fevereiro'),
    #     ('mar', 'Março'),
    #     ('abr', 'Abril'),
    #     ('mai', 'Maio'),
    #     ('jun', 'Junho'),
    #     ('jul', 'Julho'),
    #     ('ago', 'Agosto'),
    #     ('set', 'Setembro'),
    #     ('out', 'Outubro'),
    #     ('nov', 'Novembro'),
    #     ('dez', 'Dezembro'),
    # ]
    # mes_referencia_renda = models.CharField(max_length=10, choices=MES_REFERENCIA_CHOICES, blank=True, null=True)
    # valor_renda_bruta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # valor_renda_liquida = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # data_inicio_renda = models.DateField(blank=True, null=True)
    # mes_referencia_renda_declarada = models.CharField(max_length=10, choices=MES_REFERENCIA_CHOICES, blank=True, null=True)
    # valor_renda_liquida_declarada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # --- SEÇÃO DADOS FAMILIARES ---
    numero_pessoas_familia = models.PositiveIntegerField(
        default=1,
        verbose_name='Número de pessoas na família')
    renda_familiar = models.DecimalField(max_digits=10, decimal_places=2)

    recebe_bolsa_familia = models.BooleanField(default=False, verbose_name='Recebe Bolsa Família?')
    deficiencia_na_familia = models.BooleanField(default=False, verbose_name='Há pessoa com deficiência na família?')
    doenca_rara_na_familia = models.BooleanField(default=False, verbose_name='Há pessoa com câncer ou doença rara crônica e degenerativa na família?')
    recebe_bpc = models.BooleanField(default=False, verbose_name='Recebe BPC?')
    pessoa_negra_na_familia = models.BooleanField(default=False, verbose_name='Há pessoa negra na família?')
    mulheres_violencia_domestica = models.BooleanField(default=False, verbose_name='Mulheres vítima de violência doméstica ou familiar?')
    povos_tradicionais_quilombolas = models.BooleanField(default=False, verbose_name='Há integrantes de povos tradicionais ou quilombolas na família?')
    idosos_na_familia = models.BooleanField(default=False, verbose_name='Há idosos na família?')
    beneficiario_contrato_rescindido = models.BooleanField(default=False, verbose_name='Beneficiário cujo contrato foi distrtado ou rescindido involuntariamente?')
    microcefalia_na_familia = models.BooleanField(default=False, verbose_name='Há pessoa com microcefalia na família?')

    filhos_0_6 = models.PositiveIntegerField(default=0, verbose_name='Filhos(a) de 0 a 6 anos')
    filhos_7_11 = models.PositiveIntegerField(default=0, verbose_name='Filhos(a) de 7 a 11 anos')
    filhos_12_18 = models.PositiveIntegerField(default=0, verbose_name='Filhos(a) de 12 a 18 anos')

    # cep = models.CharField(
    #     max_length=8,
    #     validators=[
    #         RegexValidator(
    #             regex=r'^\d{7}$',
    #             message='CEP deve conter 7 dígitos.'
    #         )
    #     ]
    #     )
    # nome_rua = models.CharField(max_length=200)
    # numero = models.CharField(max_length=10, blank=True, null=True)
    # bairro = models.CharField(max_length=100)
    # cidade = models.CharField(max_length=100)
    # estado = models.CharField(max_length=2, choices=UF_CHOICES, blank=True, null=True)
    # complemento = models.CharField(max_length=200, blank=True, null=True)

    residente_area_risco = models.BooleanField(default=False, verbose_name='Residente em área de risco?')
    situacao_rua = models.BooleanField(default=False, verbose_name='Pessoa em situação de rua?')

    # Campo para controle de registro

    SITUACAO_CADASTRAL_CHOICES = [
        ('em_analise', 'Em análise'),
        ('contemplado', 'Contemplado'), 
        ('indeferido', 'Indeferido'),
    ]
    situacao_cadastral = models.CharField(max_length=20, choices=SITUACAO_CADASTRAL_CHOICES, default='em_analise')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_ultima_alteracao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    history = HistoricalRecords()

    pontuacao = models.PositiveIntegerField(
        default=0,
        editable=False
    )

    def __str__(self):
        return f"{self.nome_completo} - CPF: {self.cpf} - NIS: {self.nis}"

    def calcular_pontuacao(self):
        """
        Recalcula a pontuação do beneficiário com base nos critérios de pontuação ativos.
        Usado para o caso de alterações cadastrais ou mudanças nos critérios de pontuação, garantindo que a pontuação do beneficiário esteja sempre atualizada e refletindo corretamente os critérios definidos.
        """

        # Importado aqui para evitar importação circular, já que o serviço de pontuação depende do modelo Beneficiário para acessar os campos necessários para o cálculo da pontuação.
        from gestao_municipio.servicos.pontuacao import PontuacaoServico

        nova_pontuacao = PontuacaoServico.calcular(self)

        if nova_pontuacao != self.pontuacao:
            
            self.pontuacao = nova_pontuacao
            self.save(update_fields=['pontuacao'])


    class Meta:
        ordering = ['nome_completo']
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'




class CriterioPontuacao(models.Model):

    descricao = models.CharField(
        max_length=255,
        verbose_name='Descrição')

    campo_beneficiario = models.CharField(
        max_length=100,
        # Campos carregados dinamicamentedo a partir do arquivo gestao_municipio/opcoes.py, 
        choices= CampoBeneficiario.choices,
        unique=True,
        verbose_name='Identificação do critério'
    )

    pontos = models.PositiveIntegerField(
        help_text='Quantidade de pontos atribuída ao critério',
        verbose_name='Valor da pontuação'
        )


    TIPO_CALCULO_CHOICES = [
        ('fixo', 'Fixo'),
        ('multiplicador', 'Multiplicador'),
    ]
    tipo_calculo = models.CharField(
        max_length=20,
        choices=TIPO_CALCULO_CHOICES,
        default='fixo',
        verbose_name='Forma de cálculo')

    fundamentacao_legal = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Fundamentação legal')

    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do cadastro'
    )

    history = HistoricalRecords()


    class Meta:
        ordering = ['descricao']
        verbose_name = 'Critério de Pontuação'
        verbose_name_plural = 'Critérios de Pontuação'

    def __str__(self):
        return f'{self.descricao} ({self.pontos} pts)'