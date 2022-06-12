from django.shortcuts import render, HttpResponse
from servicios.models import Servicio
from blog.models import Categoria, Post

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
    
    return render(request, 'contacto.html')

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    
    return render(request, 'categorias.html', {'categoria': categoria, 'posts': posts})