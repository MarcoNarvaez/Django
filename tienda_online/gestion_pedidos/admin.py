from django.contrib import admin
from gestion_pedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class clientes_admin(admin.ModelAdmin):
    list_display = ('nombre','direccion','telefono')
    search_fields = ('nombre', 'telefono')
    
class articulos_admin(admin.ModelAdmin):
    list_filter = ('seccion',)

class pedidos_admin(admin.ModelAdmin):
    list_display = ('numero', 'fecha')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'

admin.site.register(Clientes, clientes_admin)
admin.site.register(Articulos, articulos_admin)
admin.site.register(Pedidos, pedidos_admin)