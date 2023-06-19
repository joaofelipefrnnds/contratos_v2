from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from contrato.models import Empresa, Contrato
from django.contrib import messages
from .forms import *

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    return render(request, 'contrato/index.html')

def cadastro_contrato(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    if request.method == "GET":
        form = ContratoForm()
        context = {
            'form': form
        }
        return render(request, 'contrato/cadastro_contrato.html', context=context)
    else:
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save()
            form = ContratoForm()
        
        context = {
        'form': form
            }
        return render(request, 'contrato/cadastro_contrato.html', context=context)

def cadastro_empresa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    if request.method == "GET":
        form = EmpresaForm()
        context = {
            'form': form
        }
        return render(request, 'contrato/cadastro_empresa.html', context=context)
    else:
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save()
            form = EmpresaForm()
        
        context = {
        'form': form
            }
        return render(request, 'contrato/cadastro_empresa.html', context=context)

def cadastro_evento(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    if request.method == "GET":
        form = EventoForm()
        context = {
            'form': form
        }
        return render(request, 'contrato/cadastro_evento.html', context=context)
    else:
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save()
            form = EmpresaForm()
        
        context = {
        'form': form
            }
        return render(request, 'contrato/cadastro_empresa.html', context=context)


def listagem_contrato(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    contratos = Contrato.objects.all()
    dados = {
        'contratos' : contratos
    }
    return render(request, 'contrato/listagem_contrato.html', dados)

def listagem_empresa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    empresas = Empresa.objects.all()
    dados = {
        'empresas' : empresas
    }
    return render(request, 'contrato/listagem_empresa.html', dados)


def detalhes_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    empresa_detail = {
        'empresa' : empresa_id
    }
    return render(request,'contrato/detalhe_empresa.html', empresa_detail)

