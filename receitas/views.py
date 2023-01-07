from django.shortcuts import redirect, render, get_object_or_404
from .models import Receita, Categoria
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):

    receitas = Receita.objects.filter(publicada=True).order_by('-data_receita')
    categorias = Categoria.objects.all()

    paginator = Paginator(receitas, 2)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    return render(request, 'receitas/index.html', {'receitas': receitas_por_pagina, 'categorias': categorias})


def receita(request, slug):

    receita = get_object_or_404(Receita, slug=slug)
    categorias = Categoria.objects.all()

    return render(request, 'receitas/receita.html', {'receita': receita, 'categorias': categorias})


@login_required(login_url='index')
def buscar(request):

    if request.user.is_anonymous:
        return render(request, 'receitas/buscar.html', {'receitas': receitas})

    
    if request.user.is_authenticated:

        search = request.GET.get('search')

        if search:
            receitas = Receita.objects.filter(nome__icontains=search, pessoa=request.user)
        else:
            receitas = Receita.objects.filter(pessoa=request.user)
            
        
        return render(request, 'receitas/buscar.html', {'receitas': receitas, 'search': search })
        

# para ver as categorias, e cada categoria com sua respectiva receita #
def categoria(request, slug):

    categorias = Categoria.objects.all()
    receitas = Receita.objects.filter(categoria__slug=slug)
    
    return render(request, 'receitas/index.html', {'categorias': categorias, 'receitas': receitas})
