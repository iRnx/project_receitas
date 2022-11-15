from django.shortcuts import render, get_object_or_404
from .models import Receita


def index(request):

    receitas = Receita.objects.all().order_by('-data_receita')

    return render(request, 'index.html', {'receitas': receitas})


def receita(request, id):

    receita = get_object_or_404(Receita, id=id)

    return render(request, 'receita.html', {'receita': receita})

