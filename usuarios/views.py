from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages
from django.contrib import auth
from receitas.models import Receita


def cadastro(request):

    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')


    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('/accounts/cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('/accounts/cadastro')

        if senhas_nao_sao_iguais(password, password2):
            messages.error(request, 'as senhas não são iguais')
            return redirect('/accounts/cadastro')

        if Usuarios.objects.filter(email=email).exists():
            messages.error(request, 'Email ja cadastrado')
            return redirect('/accounts/cadastro')

        if Usuarios.objects.filter(username=nome).exists():
            messages.error(request, 'Nome ja cadastrado')
            return redirect('/accounts/cadastro')
        
        user = Usuarios.objects.create_user(username=nome, email=email, password=password)
        user.save()
        return redirect('/accounts/login')
    

def login(request):

    if request.method == 'GET':
        return render(request, 'usuarios/login.html')

    if request.method == 'POST':

        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Nenhum campo pode ficar em branco.')
            return redirect('/accounts/login')
        
        
        if Usuarios.objects.filter(email=email).exists():

            nome = Usuarios.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('/minhas_receitas/dashboard')

            else:
                messages.error(request, 'Usuário não encontrado')
                return redirect('/accounts/login')
        else:
            messages.error(request, 'Email ou senha inválido')
            return redirect('/accounts/login')


def logout(request):
    auth.logout(request)
    return redirect('index')




def campo_vazio(campo):
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
