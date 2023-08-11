from django import forms
from .models import *
from django.forms import ClearableFileInput


class DateInput(forms.DateInput):
    input_type = 'date'


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["cnpj_empresa", "nome_empresa", "email_empresa", "telefone_empresa"]


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ["numero_contrato", "numero_processo", "numero_empenho", "objeto", "anx_contrato", "anx_empenho", "anx_portaria", "fk_empresa", "fk_fiscal"]
        #widgets = {
            #"anx_empenho": ClearableFileInput(attrs={'multiple': True}),
        #}


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["cnpj_empresa", "nome_empresa", "email_empresa", "telefone_empresa", "estado"]


class EventoForm(forms.ModelForm):
    class Meta:
        model = NovoEvento
        fields = ["numero_aditivo", "valor_aditivo", "objeto_aditivo", "descricao", "anx", "fk_contrato", "assinado_em"]
        widgets = {
            "assinado_em": DateInput()
        }

