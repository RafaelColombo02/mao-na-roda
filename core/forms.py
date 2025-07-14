from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    tipo = forms.ChoiceField(choices=Usuario.TIPO_USUARIO)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'tipo', 'password1', 'password2']
