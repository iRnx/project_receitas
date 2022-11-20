from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita
from usuarios.models import Usuarios
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='index')
def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas_usuario = Receita.objects.all().filter(pessoa=id).order_by('-data_receita')
        return render(request, 'crud_receitas/dashboard.html', {'receitas': receitas_usuario})
    else:
        return redirect('index')


@login_required(login_url='index')
def criar_receita(request):

    if request.method == 'GET':
        return render(request, 'crud_receitas/criar_receita.html')

    if request.method == 'POST':

        nome_receita = request.POST.get('nome_receita')
        ingredientes = request.POST.get('ingredientes')
        descricao = request.POST.get('descricao')
        modo_preparo = request.POST.get('modo_preparo')
        tempo_preparo = request.POST.get('tempo_preparo')
        rendimento = request.POST.get('rendimento')
        categoria = request.POST.get('categoria')
        foto_receita = request.FILES.get('foto_receita')

        user = get_object_or_404(Usuarios, pk=request.user.id)

        receita = Receita.objects.create(pessoa=user,
                                         nome=nome_receita, 
                                         ingredientes=ingredientes,
                                         descricao=descricao,
                                         preparo=modo_preparo,
                                         tempo_preparo=tempo_preparo,
                                         rendimento=rendimento,
                                         categoria=categoria,
                                         foto=foto_receita)
        receita.save()

        return redirect('/minhas_receitas/dashboard')


@login_required(login_url='index')
def editar(request, id):

    receita = get_object_or_404(Receita, id=id)

    if request.method == 'GET':
        return render(request, 'crud_receitas/editar.html', {'receita': receita})


    if request.method == 'POST':
        receita.nome = request.POST.get('nome')
        receita.descricao = request.POST.get('descricao')
        receita.ingredientes = request.POST.get('ingredientes')
        receita.preparo = request.POST.get('preparo')
        receita.tempo_preparo = request.POST.get('tempo_preparo')
        receita.rendimento = request.POST.get('rendimento')
        receita.categoria = request.POST.get('categoria')

        if 'foto' in request.FILES:
            receita.foto = request.FILES.get('foto')

        receita.save()
        return redirect('/minhas_receitas/dashboard')
    
    


@login_required(login_url='index')
def deletar(request, id):
    receita = get_object_or_404(Receita, id=id)
    receita.delete()
    messages.success(request, 'Receita deletada com sucesso!!')
    return redirect('/minhas_receitas/dashboard')
    


