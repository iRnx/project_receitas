from django.contrib.auth import forms
from .models import Usuarios

class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):
        model = Usuarios

class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = Usuarios