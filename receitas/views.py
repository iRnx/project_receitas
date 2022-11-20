from django.shortcuts import redirect, render, get_object_or_404
from .models import Receita



def index(request):

    receitas = Receita.objects.filter(publicada=True).order_by('-data_receita')

    return render(request, 'index.html', {'receitas': receitas})


def receita(request, id):

    receita = get_object_or_404(Receita, id=id)

    return render(request, 'receita.html', {'receita': receita})


def buscar(request):

    search = request.GET.get('search')

    if search:
        receitas = Receita.objects.filter(nome__icontains=search, pessoa=request.user)
    else:
        receitas = Receita.objects.filter(pessoa=request.user)
        
    
    return render(request, 'buscar.html', {'receitas': receitas, 'search': search })
        

    