from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita, Categoria
from usuarios.models import Usuarios
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

@login_required(login_url='index')
def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas_usuario = Receita.objects.all().filter(pessoa=id).order_by('-data_receita')
        categorias = Categoria.objects.all()
        return render(request, 'crud_receitas/dashboard.html', {'receitas': receitas_usuario, 'categorias': categorias})
    else:
        return redirect('index')


@login_required(login_url='index')
def criar_receita(request):

    categorias = Categoria.objects.all()

    
    if request.method == 'GET':
        
        return render(request, 'crud_receitas/criar_receita.html', {'categorias': categorias})

    if request.method == 'POST':


        nome_receita = request.POST.get('nome_receita')
        ingredientes = request.POST.get('ingredientes')
        descricao = request.POST.get('descricao')
        modo_preparo = request.POST.get('modo_preparo')
        tempo_preparo = request.POST.get('tempo_preparo')
        rendimento = request.POST.get('rendimento')
        categoria = request.POST.get('categorias', None)
        foto_receita = request.FILES.get('foto_receita')

        for cat in categoria:
            categoria = Categoria.objects.filter(id=cat)[0]

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
def editar(request, slug):

    receita = get_object_or_404(Receita, slug=slug)

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
def deletar(request, slug):
    receita = get_object_or_404(Receita, slug=slug)
    receita.delete()
    messages.success(request, 'Receita deletada com sucesso!!')
    return redirect('/minhas_receitas/dashboard')
    

@login_required(login_url='index')
def publicar(request, slug):

    receita = get_object_or_404(Receita, slug=slug)

    if receita.publicada == False:
        receita.publicada=True
        receita.save()
        messages.success(request, 'Receita Publicada com sucesso!!')
        return redirect('/minhas_receitas/dashboard')
    else:
        messages.warning(request, 'Est?? receita ja foi publicada')
        return redirect('/minhas_receitas/dashboard')


@login_required(login_url='index')
def remover(request, slug):
        
    receita = get_object_or_404(Receita, slug=slug)

    if receita.publicada == True:
        receita.publicada=False
        receita.save()
        messages.success(request, 'Receita removida com sucesso')
        return redirect('index')
    else:
        return redirect('/minhas_receitas/dashboard')
