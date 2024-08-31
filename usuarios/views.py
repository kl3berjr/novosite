from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django
from .models import Nota

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login_django(request, user)
            #return HttpResponse('Acesso liberado!')
            return render(request, 'usuarios/home.html')
        else:
            return HttpResponse('Credenciais invalida!')
        

def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        first_name = request.POST.get('nome')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Usuário já cadastrado")
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()

            #return HttpResponse("Usuário cadastrado com sucesso!")
            return render(request, 'usuarios/login.html')

def logout(request):
    if request.user.is_authenticated:
        logout_django(request)
        return render(request, 'usuarios/login.html')
    else:
        return HttpResponse("É preciso logar no sistema antes!")

def home(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/home.html')
    else:
         return HttpResponse("Erro!")

def lancar(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return render(request, 'usuarios/lancar.html')
        else:
            return HttpResponse("Erro!")
    else:
        nota=Nota()
        nota.nome_aluno=request.user.first_name
        nota.disciplina=request.POST.get('disciplina')
        nota.nota_atividades=request.POST.get('nota_atividades')
        nota.nota_trabalho=request.POST.get('nota_trabalho')
        nota.nota_prova=request.POST.get('nota_prova')
        nota.media=int(nota.nota_atividades + nota.nota_trabalho + nota.nota_prova)

        nota_verificada=Nota.objects.filter(disciplina=nota.disciplina).first()

        if nota_verificada:
            return HttpResponse("A disciplina já possui nota cadastrada!")
        else:
            nota.save()
            return render(request, 'usuarios/home.html')
        


def alterar(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/alterar.html')
    else:
         return HttpResponse("Erro!")

def visualizar(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/visualizar.html')
    else:
         return HttpResponse("Erro!")