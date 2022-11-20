from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('criar_receita/', views.criar_receita, name='criar_receita'),
    path('editar/<slug:slug>', views.editar, name='editar'),
    path('deletar/<slug:slug>', views.deletar, name='deletar'),
    path('publicar/<int:id>', views.publicar, name='publicar'),
    path('remover/<int:id>', views.remover, name='remover')
    
]