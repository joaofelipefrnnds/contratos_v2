from django import forms
from .models import *

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["cnpj_empresa", "nome_empresa", "email_empresa", "telefone_empresa"]

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ["numero_contrato", "numero_processo", "numero_empenho", "objeto", "fk_empresa", "fk_fiscal"]


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["cnpj_empresa", "nome_empresa", "email_empresa", "telefone_empresa", "estado"]

class EventoForm(forms.ModelForm):
    class Meta:
        model = NovoEvento
        fields = ["numero_aditivo", "valor_aditivo", "objeto_aditivo", "fk_contrato", "assinado_em"]

