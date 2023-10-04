from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from contrato.models import Empresa, Contrato
from django.contrib import messages
from .forms import *
from django.core.paginator import Paginator 

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
        if form.is_valid():
            contrato = form.save()
            form = ContratoForm()
            messages.success(request,'Cadastro realizado')
            return redirect('/detalhes_contrato/'+str(contrato.id))
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
            return redirect('/listagem_empresa/')
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
            return redirect('/detalhes_contrato/'+str(evento.fk_contrato.id))
        context = {
        'form': form
            }
        return render(request, 'contrato/cadastro_evento.html', context=context)

def listagem_evento(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    eventos = NovoEvento.objects.filter(
        ativo=True
    )
    context = {
        'eventos' : eventos
    }
    return render(request, 'contrato/listagem_evento.html', context)

def listagem_contrato(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    contratos = Contrato.objects.filter(
        ativo=True,
        fk_fiscal=request.user
        #author=request.user,
        
    )
    search_query = request.GET.get('search')  # Obtém o valor do campo de pesquisa
    if search_query:
        contratos = contratos.filter(numero_contrato__icontains=search_query)
    context = {
        'contratos' : contratos
    }
    return render(request, 'contrato/listagem_contrato.html', context)

def listagem_empresa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    empresas = Empresa.objects.filter(
       # ativo=True
    )
    paginator = Paginator(empresas, 4) #mostra 3 empresas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    search_query = request.GET.get('search')  # Obtém o valor do campo de pesquisa
    if search_query:
        empresas = empresas.filter(nome_empresa__icontains=search_query)
    return render(request, 'contrato/listagem_empresa.html', context = {'empresas': empresas, 'page_obj':page_obj} )


def detalhes_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    context = {
        'empresa' : empresa
    }
    return render(request,'contrato/detalhes_empresa.html', context)


def detalhes_contrato(request, contrato_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    contrato = get_object_or_404(Contrato, pk=contrato_id)
    eventos = NovoEvento.objects.filter(fk_contrato=contrato).all()
    return render(request,'contrato/detalhes_contrato.html', context={'contrato': contrato, 'eventos': eventos})


def detalhes_evento(request, evento_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    evento = get_object_or_404(NovoEvento, pk=evento_id)
    evento_detail = {
        'evento' : evento
    }
    return render(request,'contrato/detalhes_evento.html', evento_detail)


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

def update_empresa(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    data = {}
    cadastro_empresa = Empresa.objects.get(pk=pk)
    form = EmpresaForm(request.POST or None, request.FILES or None, instance=cadastro_empresa)
    if form.is_valid():
            form.save()
            messages.success(request,'Alteração realizada')
            return redirect('listagem_empresa')
    data['form'] = form
    data['cadastro_empresa'] = cadastro_empresa
    return render(request, 'contrato/update_empresa.html', data)

def update_evento(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    data = {}
    evento = get_object_or_404(NovoEvento, pk=pk)
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)
    if form.is_valid():
            form.save()
            messages.success(request,'Alteração realizada')
            return redirect('/detalhes_contrato/'+str(evento.fk_contrato.id))
    data['form'] = form
    data['evento'] = evento
    return render(request, 'contrato/cadastro_evento.html', data)