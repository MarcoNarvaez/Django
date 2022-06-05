from datetime import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
import datetime

class Persona(object):
    
    def __init__(self, nombre, apellido):
        
        self.nombre = nombre
        
        self.apellido = apellido

def saludo(request): #primera vista
    
    p1 = Persona('Marco', 'Narvaez')
    
    #nombre = 'juan'
    
    #apellido = 'Diaz'
    
    temas = ['plantillas', 'modelos', 'formularios', 'vistas', 'despliegue']
    
    ahora = datetime.datetime.now()
    
    #doc_externo = open('/home/marco/django/Proyecto/Proyecto/plantillas/index.html')
    
    #plt = Template(doc_externo.read())
    
    #doc_externo.close()
    
    #doc_externo = get_template('index.html')
    
    #ctx = Context({'nombre_persona': p1.nombre, 'apellido_persona': p1.apellido , 'momento_actual': ahora, 'temas': temas})
    
    #documento = doc_externo.render({'nombre_persona': p1.nombre, 'apellido_persona': p1.apellido , 'momento_actual': ahora, 'temas': temas})
    
    return render(request, 'index.html', {'nombre_persona': p1.nombre, 'apellido_persona': p1.apellido , 'momento_actual': ahora, 'temas': temas})

def curso_c(request):
    
    fecha_actual = datetime.datetime.now()
    
    return render(request, 'CursoC.html', {'fecha': fecha_actual})

def curso_css(request):
    
    fecha_actual = datetime.datetime.now()
    
    return render(request, 'css.html', {'fecha': fecha_actual})

def despedida(request):
    
    return HttpResponse('Adios mundo')

def fecha(request):
    
    fecha_actual = datetime.datetime.now()
    
    documento = """
    <html>
    <body>
    <h3>
    fecha y hora actuales %s
    </h3>
    </body>
    </html> """ % fecha_actual
    
    return HttpResponse(documento)

def calcula_edad(request, edad, año):
    
    #edadActual = 24
    periodo = año - 2022
    edadFutura = edad + periodo
    documento = '<html><body><h2>En el año %s tendras %s años'%(año, edadFutura)
    
    return HttpResponse(documento)