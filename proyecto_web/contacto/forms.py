import email
from django import forms

class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)