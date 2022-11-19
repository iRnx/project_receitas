from django import template

register = template.Library()


# Deixando a primeira letra do nome maiúsculo #
@register.filter(name='title')
def letra_maiuscula(nome):
    return f'{nome.title()}'