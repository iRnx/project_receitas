from django.contrib import admin
from .models import Receita, Categoria

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'data_receita', 'publicada', 'slug')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 3

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'slug')