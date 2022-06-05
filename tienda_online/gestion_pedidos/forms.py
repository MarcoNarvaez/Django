from django import forms

class Formulario(forms.Form):
    
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()