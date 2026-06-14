from django import forms
from .models import Beneficiario

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