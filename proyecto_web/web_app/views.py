from django.shortcuts import redirect, render, HttpResponse
from servicios.models import Servicio
from blog.models import Categoria, Post
from contacto.forms import Formulario_contacto

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def servicios(request):
    
    servicios = Servicio.objects.all()
    
    return render(request, 'servicios.html', {'servicios': servicios})

def tienda(request):
    
    return render(request, 'tienda.html')

def blog(request):
    
    posts = Post.objects.all()
    
    return render(request, 'blog.html', {'posts': posts})

def contacto(request):
    formulario_contacto = Formulario_contacto()
    
    if request.method == "POST":
        formulario_contacto = Formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            return redirect("/contacto/?valido")
    
    return render(request, 'contacto.html', {'mi_formulario': formulario_contacto})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    
    return render(request, 'categorias.html', {'categoria': categoria, 'posts': posts})