from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FormularioProductoApi(forms.Form):
    codigo=forms.IntegerField()
    marca=forms.CharField(max_length=50)
    tipo=forms.CharField(max_length=50)
    precio=forms.IntegerField()
    cantidad=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar Email')
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}