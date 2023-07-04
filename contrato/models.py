from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os

def directory_path(instance, filename):
    return os.path.join('arquivos/'+instance.__class__.__name__+"/", filename)

class Empresa(models.Model):
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("ES", "Espiríto Santo"),
        ("GO", "Góias"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),             
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
        ("DF", "Distrito Federal"),
    )

    cnpj_empresa = models.CharField(max_length=14, null=False, blank=False)
    nome_empresa = models.CharField(max_length=255,null=False, blank=False)
    email_empresa = models.EmailField(null=False, blank=False)
    telefone_empresa = models.CharField(max_length=11, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, null=True)
    cadastrado_em = models.DateField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.nome_empresa

class Contrato(models.Model):
    numero_contrato = models.CharField(max_length=11, null=False, blank=False)
    numero_processo = models.CharField(max_length=11, null=False, blank=False)
    numero_empenho = models.CharField(max_length=11, null=False, blank=False)
    objeto = models.CharField(max_length=255, null=False, blank=False)
    fk_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fk_fiscal = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cadastrado_em = models.DateField(default=datetime.now, blank=True, null=True)
    #anx_empenho = models.FileField(upload_to=directory_path, null=True)
    def __str__(self):
        return self.numero_processo
    

class NovoEvento(models.Model):
    numero_aditivo = models.CharField(max_length=11, null=False, blank=False)
    valor_aditivo = models.CharField(max_length=255, null=False, blank=False)
    objeto_aditivo = models.CharField(max_length=255, null=False, blank=False)
    fk_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    #anexo=models.FileField(upload_to=directory_path, null=True, blank=True)
    assinado_em = models.DateField()
    cadastrado_em = models.DateField(default=datetime.now, blank=True, null=True)
    anx_empenho = models.FileField(upload_to=directory_path, null=True)
    def __str__(self):
        return self.numero_aditivo

class Anexo(models.Model):
    titulo = models.FileField(upload_to=directory_path, null=True)
    fk_contrato = models.ForeignKey(NovoEvento, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.titulo