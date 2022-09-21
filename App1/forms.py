from django import forms


class FormularioProductoApi(forms.Form):
    codigo=forms.IntegerField()
    marca=forms.CharField(max_length=50)
    tipo=forms.CharField(max_length=50)
    precio=forms.IntegerField()
    cantidad=forms.IntegerField()