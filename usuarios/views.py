from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroUsuarioForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.paginator import Paginator 
def login(request):
    form = LoginForms()
    if request.method == 'POST':
          form = LoginForms(request.POST) 
          if form.is_valid():  
              nome=form['nome_login'].value()
              senha=form['senha'].value() 
          usuario = auth.authenticate(
              request,
              username=nome,
              password=senha
          )
          if usuario is not None:
              auth.login(request, usuario)
              messages.success(request, f"{nome} Logado com Sucesso!")
              return redirect('index')
          else:
              messages.error(request, "Usuário ou Senha !")
              return redirect('login')
    return render(request, "usuarios/login.html", {"form": form})

def cadastro_usuario(request):
    form = CadastroUsuarioForms()
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')    
    if request.method == 'POST':
        form = CadastroUsuarioForms(request.POST)   
        if form.is_valid():  #verifica se o formulário está válido
            if form["senha_1"].value() != form["senha_2"].value(): #compara se as senhas são diferentes 
                messages.error(request, "As senhas não são iguais!")
                return redirect('cadastro_usuario')   # se forem DIFERENTES, é redirecionado para o cadastro novamente   
            nome = form["nome_usuario"].value() #caso NÃO, guarda os campos da tabela nas variáveis
            first = form["first_name"].value() #caso NÃO, guarda os campos da tabela nas variáveis
            last = form["last_name"].value() #caso NÃO, guarda os campos da tabela nas variáveis
            email = form["email"].value()#caso NÃO, guarda os campos da tabela nas variáveis
            senha = form["senha_1"].value()#caso NÃO, guarda os campos da tabela nas variáveis            
            if User.objects.filter(username=nome).exists(): #válida se já existe usuário com o mesmo nome
                 messages.error(request, "Já existe um usuário com esse NOME DE USUÁRIO na base de dados!")
                 return redirect('cadastro_usuario') #caso SIM, guarda os campos da tabela nas variáveis
            if User.objects.filter(email=email).exists(): #válida se já existe usuário com o mesmo email
                messages.error(request, "Já existe um usuário com esse EMAIL na base de dados!")
                return redirect('cadastro_usuario') #caso SIM, guarda os campos da tabela nas variáveis
            usuario = User.objects.create_user( #CRIA DE FATO OS USUÁRIO DE ACORDO COM AS VARIÁVEIS ANTERIOR
                username=nome,
                first_name=first,
                last_name=last,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('cadastro_usuario')
    return render(request, "usuarios/cadastro_usuario.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

def listagem_usuario(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    usuarios = User.objects.all()
    paginator = Paginator(usuarios, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'usuarios/listagem_usuario.html', context = {'usuarios' : usuarios,'page_obj': page_obj})
