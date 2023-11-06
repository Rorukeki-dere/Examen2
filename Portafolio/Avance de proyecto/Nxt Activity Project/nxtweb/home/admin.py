from django.contrib import admin

# Register your models here.
from  .models import *

admin.site.register(user)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Equipo)
admin.site.register(Compra)
admin.site.register(Fabricante)
