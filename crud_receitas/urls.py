from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar/', views.editar, name='editar'),
    path('criar_receita/', views.criar_receita, name='criar_receita'),
]