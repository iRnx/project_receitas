from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'data_receita')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_per_page = 3