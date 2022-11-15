from django.contrib import admin
from .models import Pessoas
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as admin_auth_django

@admin.register(Pessoas)
class PessoasAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ("Informações residenciais", {"fields": ("rua", "cep", "numero")}),
        )