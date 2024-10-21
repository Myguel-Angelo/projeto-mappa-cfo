from django import forms
from anotacao.models import Anotacao

class LoginForm(forms.Form):
    nome_ou_numerica = forms.CharField(max_length=100, label='Nome ou Numérica')
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')

from django import forms
from .models import UserMilitar

class AlterarSenhaForm(forms.Form):
    nova_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua nova senha'}),
        label="Nova Senha",
        max_length=255,
        required=True
    )
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua nova senha'}),
        label="Confirmar Senha",
        max_length=255,
        required=True
    )

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)

    # Validação do formulário como um todo
    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get("nova_senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        # Verificar se as senhas coincidem
        if nova_senha and confirmar_senha:
            if nova_senha != confirmar_senha:
                raise forms.ValidationError("As senhas não coincidem.")
        
        # Verificar se a nova senha é a mesma que a antiga
        if self.usuario and nova_senha and self.usuario.senha == nova_senha:
            raise forms.ValidationError("A nova senha não pode ser a mesma que a senha antiga.")

        return cleaned_data

class AnotacaoForm(forms.ModelForm):
    class Meta:
        model = Anotacao
        fields = ['tipo_anotacao', 'motivo']
        labels = {
            'tipo_anotacao': 'Tipo de Anotação',
            'motivo': 'Motivo'
        }
        widgets = {
            'tipo_anotacao': forms.Select(
                choices=[('positivo', 'Positivo'), ('negativo', 'Negativo')],
                attrs={'class': 'form-control'}  # Adiciona a classe form-control
            ),
            'motivo': forms.Textarea(attrs={'class': 'form-control','rows': 4}),
        }