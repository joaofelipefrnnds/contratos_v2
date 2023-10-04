from django import forms
from django.forms import ValidationError, widgets
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
          widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg"
            }
        )
    )

class CadastroUsuarioForms(forms.Form):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, *kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Que legal'

        nome_usuario = forms.CharField(
            label="Nome de usuário",
            required=True,
            max_length=100,
              widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg"
                }
            ),
            help_text=(
                'Insira um nome de usuário'
            )
        )
        first_name = forms.CharField(
            label="Primeiro Nome",
            required=True,
            max_length=100,
              widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg"
                }
            )
        )
        help_text = {
            'first_name': 'Digite o nome'
        }
        last_name = forms.CharField(
            label="Último Nome",
            required=True,
            max_length=100,
              widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg"
                }
            )
        )
        email = forms.EmailField(
            label="Email",
            required=True,
            max_length=100,
              widget=forms.EmailInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder":"Ex: fulano@defensoria.ap.def.br"
                }
            )
        )
        senha_1 = forms.CharField(
            label="Digite sua senha",
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder":"Confirme sua senha"
                }
            )
        )  
        senha_2 = forms.CharField(
            label="Digite sua senha novamente",
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder":"Confirme sua senha"
                }
            )
        )

def clean_email(self):
    email = self.clean_field('email', '')
    exists = User.objects.filter(email=email).exists()
    if exists:
        raise ValidationError('Já existe um usuário o email informado',code='invalid',)    
    return email




