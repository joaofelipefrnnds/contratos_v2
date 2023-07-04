from django.contrib import admin
from contrato.models import Empresa, Contrato, NovoEvento

class ListandoEmpresas(admin.ModelAdmin):
    list_display = ("id", "nome_empresa", "cnpj_empresa", "email_empresa", "telefone_empresa", "estado")
    list_display_links = ("id","nome_empresa")
    search_fields = ("nome_empresa",)
    list_per_page = 10

admin.site.register(Empresa, ListandoEmpresas)

class ListandoContratos(admin.ModelAdmin):
    list_display = ("id", "numero_contrato", "numero_processo", "numero_empenho", "objeto", "fk_empresa", "fk_fiscal")
    list_display_links = ("id","numero_contrato")
    search_fields = ("numero_contrato",)
    list_per_page = 10
admin.site.register(Contrato, ListandoContratos)

class ListandoEventos(admin.ModelAdmin):
    list_display = ("id", "numero_aditivo", "valor_aditivo", "objeto_aditivo", "fk_contrato", "assinado_em", "cadastrado_em")
    list_display_links = ("id","numero_aditivo")
    search_fields = ("fk_contrato",)
    list_per_page = 10

admin.site.register(NovoEvento, ListandoEventos)