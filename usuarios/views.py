from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages

def cadastro(request):

    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')


    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('/accounts/cadastro')

        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('/accounts/cadastro')

        if password != password2:
            messages.error(request, 'as senhas não são iguais')
            return redirect('/accounts/cadastro')

        if Usuarios.objects.filter(email=email).exists():
            messages.error(request, 'Email ja cadastrado')
            return redirect('/accounts/cadastro')
        
        user = Usuarios.objects.create_user(username=nome, email=email, password=password)
        user.save()
        return redirect('/accounts/login')
    



def login(request):
    return render(request, 'usuarios/login.html')


def logout(request):
    pass


def dashboard(request):
    pass

