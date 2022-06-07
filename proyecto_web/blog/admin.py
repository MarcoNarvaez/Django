from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class categoria_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class post_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Categoria, categoria_admin)
admin.site.register(Post, post_admin)