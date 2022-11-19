from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('receita/<int:id>', views.receita, name='receita'),
    path('buscar/', views.buscar, name='buscar'),
]
