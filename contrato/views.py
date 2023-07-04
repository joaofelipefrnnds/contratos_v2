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
        form = ContratoForm(request.POST, request.FILES or None)
        files = request.FILES.getlist('anx_empenho')
        if form.is_valid():
            #for file in files:
             #   instance = Contrato(files=file)
              #  instance.save()
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
        form = EventoForm(request.POST, request.FILES or None)
        if form.is_valid():
            evento = form.save()
            form = EventoForm()
        
        context = {
        'form': form
            }
        return render(request, 'contrato/cadastro_evento.html', context=context)

def listagem_evento(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    eventos = NovoEvento.objects.all()
    dados = {
        'eventos' : eventos
    }
    return render(request, 'contrato/listagem_evento.html', dados)

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

def detalhes_contrato(request, contrato_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    contrato = get_object_or_404(Contrato, pk=contrato_id)
    eventos = NovoEvento.objects.filter(fk_contrato=contrato).all()
    return render(request,'contrato/detalhes_contrato.html', context={'contrato': contrato, 'eventos': eventos})

#def search_contrato(request):


def update_contrato(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    data = {}
    cadastro_contrato = Contrato.objects.get(pk=pk)
    form = ContratoForm(request.POST or None, request.FILES or None, instance=cadastro_contrato)
    if form.is_valid():
            form.save()
            messages.success(request,'Alteração realizada')
            return redirect('listagem_contrato')
    data['form'] = form
    data['cadastro_contrato'] = cadastro_contrato
    return render(request, 'contrato/cadastro_contrato.html', data)


