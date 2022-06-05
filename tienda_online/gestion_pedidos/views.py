from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from gestion_pedidos.models import Articulos
from django.core.mail import send_mail
from gestion_pedidos.forms import Formulario

# Create your views here.

def busqueda(request):

    return render(request, 'busqueda.html')

def buscar(request):
    
    if request.GET['prd']:
        #mensaje = 'Articulo buscado: %r' %request.GET['prd']
        producto = request.GET['prd']
        
        if len(producto) > 20:
            mensaje = 'texto de busqueda demasiado largo'
            
        else:
        
            articulos = Articulos.objects.filter(nombre__icontains=producto)
        
            return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
    else:
        mensaje = 'No introduciste nada'
    return HttpResponse(mensaje)

def contacto(request):
    
    if request.method=='POST':
        
        #asunto = request.POST['asunto']
        #mensaje = request.POST['mensaje'] + '' + request.POST['email']
        #email_from = settings.EMAIL_HOST_USER
        #recipiente = ['nefftep79@gmail.com']
        #send_mail(asunto, mensaje, email_from, recipiente)
        #return render(request, 'gracias.html')
    #return render(request, 'contacto.html')
        mi_formulario = Formulario(request.POST)
        
        if mi_formulario.is_valid():
            
            info = mi_formulario.cleaned_data
            send_mail(info['asunto'], info['mensaje'], info.get('email', ''),['cursos@pildorasinformaticas.es'],)
            
            return render(request, 'gracias.html')   
    else:
        mi_formulario = Formulario()
        
    return render(request, 'formulario.html', {'form':mi_formulario})