from django import forms
from .models import Beneficiario, CriterioPontuacao

class BeneficiarioForm(forms.ModelForm):
        
    class Meta:

        model = Beneficiario
        
        # Usar '__all__' para incluir todos os campos do modelo, exceto os que estão listados em 'exclude'. 
        # Isso é útil para garantir que todos os campos sejam incluídos automaticamente, 
        # mesmo que novos campos sejam adicionados ao modelo no futuro, sem a necessidade de atualizar manualmente a lista de campos.
        fields = '__all__'
        exclude = (
            'pontuacao',
            'ativo',
            'situacao_cadastral',
            'data_cadastro',
            'data_ultima_alteracao',
        )
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for nome, field in self.fields.items():

            if isinstance(field, forms.BooleanField):

                field.widget.attrs.update({
                    'class': 'form-check-input'
                })

            else:

                field.widget.attrs.update({
                    'class': 'form-control'
                })


class BeneficiarioAdminForm(forms.ModelForm):

    class Meta:

        model = Beneficiario

        exclude = (
            'pontuacao',
            'data_cadastro',
            'data_ultima_alteracao',
            'history',
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for nome, field in self.fields.items():

            if isinstance(field, forms.BooleanField):

                field.widget.attrs.update({
                    'class': 'form-check-input'
                })

            else:

                field.widget.attrs.update({
                    'class': 'form-control'
                })



class CriterioPontuacaoForm(forms.ModelForm):
        
    class Meta:

        model = CriterioPontuacao
        
        fields = '__all__'
        exclude = (
            'data_cadastro',
            'history',
        )
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for nome, field in self.fields.items():

            if isinstance(field, forms.BooleanField):

                field.widget.attrs.update({
                    'class': 'form-check-input'
                })

            else:

                field.widget.attrs.update({
                    'class': 'form-control'
                })