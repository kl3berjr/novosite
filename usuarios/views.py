from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def login(request):
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)

        if user:
            login_django(request, user)
            return HttpResponse('Acesso liberado!')
        else:
            return HttpResponse('Credenciais invalida!')