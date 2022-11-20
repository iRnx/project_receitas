from django.shortcuts import redirect, render, get_object_or_404
from .models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):

    receitas = Receita.objects.filter(publicada=True).order_by('-data_receita')

    paginator = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    return render(request, 'receitas/index.html', {'receitas': receitas_por_pagina})


def receita(request, slug):

    receita = get_object_or_404(Receita, slug=slug)

    return render(request, 'receitas/receita.html', {'receita': receita})


def buscar(request):

    search = request.GET.get('search')

    if search:
        receitas = Receita.objects.filter(nome__icontains=search, pessoa=request.user)
    else:
        receitas = Receita.objects.filter(pessoa=request.user)
        
    
    return render(request, 'receitas/buscar.html', {'receitas': receitas, 'search': search })
        

    